# LibraryProject

A Django project for library management system.

## Project Structure

- `manage.py` - Command-line utility for Django interactions
- `LibraryProject/` - Main project package
  - `__init__.py` - Empty file that marks this as a Python package
  - `settings.py` - Configuration and settings for the project
  - `urls.py` - URL declarations and routing
  - `wsgi.py` - WSGI web server interface
  - `asgi.py` - ASGI web server interface

## Getting Started

1. Run the development server: `python manage.py runserver`
2. Visit: http://127.0.0.1:8000/

## Features

- Django welcome page
- Development server with auto-reload
- Ready for library management applications


# Bookshelf Permission System Documentation

## Overview
This application implements a custom permission system for the Book model using Django's built-in authentication system.

## Custom Permissions
The Book model has the following custom permissions defined:

- `can_view` - Permission to view books
- `can_create` - Permission to create books
- `can_edit` - Permission to edit books
- `can_delete` - Permission to delete books

## Groups Configuration
Three user groups are configured with the following permissions:

### Viewers Group
- **Permissions**: `can_view`
- **Access**: Can only view book list and book details

### Editors Group
- **Permissions**: `can_view`, `can_create`, `can_edit`
- **Access**: Can view, create, and edit books but cannot delete

### Admins Group
- **Permissions**: `can_view`, `can_create`, `can_edit`, `can_delete`
- **Access**: Full access to all book operations

## View Protection
All views are protected with permission decorators:

- `book_list` - Requires `can_view` permission
- `book_detail` - Requires `can_view` permission
- `book_create` - Requires `can_create` permission
- `book_edit` - Requires `can_edit` permission
- `book_delete` - Requires `can_delete` permission

## Setup Instructions
1. Run migrations to create permissions: `python manage.py migrate`
2. Create groups manually in Django Admin and assign permissions
3. Assign users to appropriate groups in Django Admin

## Testing
- Users in Viewers group can only access list and detail views
- Users in Editors group can access list, detail, create, and edit views
- Users in Admins group can access all views including delete
- Users without permissions get 403 Forbidden errors
