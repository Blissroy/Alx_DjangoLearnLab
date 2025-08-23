from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from .models import Book

User = get_user_model()

class BookAPITestCase(APITestCase):
    def setUp(self):
        # create a user for authenticated actions
        self.user = User.objects.create_user(username="testuser", password="testpass123")

        # create some books to test listing/filter/search/ordering
        Book.objects.create(title="The Alchemist", author="Paulo Coelho", publication_year=1988, description="A fable about following your dream")
        Book.objects.create(title="Harry Potter and the Philosopher's Stone", author="J.K. Rowling", publication_year=1997, description="A young wizard's beginning")
        Book.objects.create(title="A Brief History of Time", author="Stephen Hawking", publication_year=1988, description="Cosmology for the masses")
        Book.objects.create(title="The Hobbit", author="J.R.R. Tolkien", publication_year=1937, description="Bilbo's adventure")

        # endpoints (adjust names if you used different url names)
        self.list_url = reverse("book-list")
        # we will build detail/update/delete urls dynamically with pk

    def test_list_books_returns_all(self):
        """GET /api/books/ returns 200 and the correct number of items"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # expect 4 books from setUp
        self.assertEqual(len(response.data), 4)

    def test_filter_books_by_title(self):
        """Test exact filtering using query params: ?title=The Hobbit"""
        response = self.client.get(self.list_url, {"title": "The Hobbit"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "The Hobbit")

    def test_search_books(self):
        """Test search across search_fields (e.g. ?search=wizard should match Harry Potter)"""
        response = self.client.get(self.list_url, {"search": "wizard"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # at least Harry Potter should be present
        titles = [item["title"] for item in response.data]
        self.assertIn("Harry Potter and the Philosopher's Stone", titles)

    def test_ordering_books_by_publication_year(self):
        """Test ordering: newest first with ?ordering=-publication_year"""
        response = self.client.get(self.list_url, {"ordering": "-publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [item["publication_year"] for item in response.data]
        # years should be non-increasing
        self.assertEqual(years, sorted(years, reverse=True))

    def test_unauthenticated_user_cannot_create_book(self):
        """POST without auth should be rejected (IsAuthenticatedOrReadOnly)"""
        payload = {
            "title": "New Book",
            "author": "Author X",
            "publication_year": 2024,
            "description": "Test book"
        }
        response = self.client.post(self.list_url, payload, format="json")
        # depending on your authentication classes the API may return 401 or 403 for unauthenticated writes
        self.assertIn(response.status_code, (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))

    def test_authenticated_user_can_create_update_delete_book(self):
        """Authenticated user should be able to create, update and delete a Book"""
        self.client.login(username="testuser", password="testpass123")
        # alternatively: self.client.force_authenticate(user=self.user)

        # Create
        payload = {
            "title": "Created Book",
            "author": "Creator",
            "publication_year": 2025,
            "description": "Created by test"
        }
        create_resp = self.client.post(self.list_url, payload, format="json")
        self.assertEqual(create_resp.status_code, status.HTTP_201_CREATED)
        created_pk = create_resp.data.get("id") or create_resp.data.get("pk")
        self.assertIsNotNone(created_pk)

        # Update (PUT/PATCH)
        detail_url = reverse("book-detail", args=[created_pk])
        update_payload = {"title": "Updated Book Title"}
        # Using PATCH so we only send changed fields
        patch_resp = self.client.patch(detail_url, update_payload, format="json")
        self.assertIn(patch_resp.status_code, (status.HTTP_200_OK, status.HTTP_202_ACCEPTED))
        self.assertEqual(patch_resp.data.get("title"), "Updated Book Title")

        # Delete
        delete_url = reverse("book-delete", args=[created_pk]) if "book-delete" in [i.name for i in self.client.handler._urls] else detail_url
        # (If you used the same view for delete detail, the detail_url will work.)
        del_resp = self.client.delete(detail_url)
        self.assertIn(del_resp.status_code, (status.HTTP_204_NO_CONTENT, status.HTTP_200_OK))

        # ensure the object is gone
        exists = Book.objects.filter(pk=created_pk).exists()
        self.assertFalse(exists)

        self.client.logout()

    def test_permission_enforced_on_update_delete_for_unauthenticated(self):
        """Ensure unauthenticated users can't update/delete an existing book"""
        book = Book.objects.first()
        detail_url = reverse("book-detail", args=[book.pk])

        # Attempt patch
        patch_resp = self.client.patch(detail_url, {"title": "Malicious Change"}, format="json")
        self.assertIn(patch_resp.status_code, (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))

        # Attempt delete
        del_resp = self.client.delete(detail_url)
        self.assertIn(del_resp.status_code, (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))
