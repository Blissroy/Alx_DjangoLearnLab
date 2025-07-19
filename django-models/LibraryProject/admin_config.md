# Django Admin Configuration for Book Model

## 1. Model Registration
python
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Configuration options


## 2. Admin Features Implemented
- *List Display*: Shows title, author, publication year, and creation date
- *Filters*: By author and publication year
- *Search*: By title and author
- *Ordering*: Newest books first
- *Fieldsets*: Grouped fields with collapsible sections

## 3. Accessing the Admin
1. Run development server:
bash
python manage.py runserver

2. Visit http://127.0.0.1:8000/admin
3. Login with superuser credentials
4. Find "Books" section in admin dashboard

## 4. Expected Admin Interface
![Book Admin Interface](book_admin_screenshot.png)
