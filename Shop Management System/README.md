# Shop Management System

A modern shop management ERP website built with Django for backend and HTML/CSS/JavaScript for frontend.

## Setup

1. Create and activate a Python virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Run database migrations:
   ```powershell
   python manage.py migrate
   ```
4. Create a superuser for admin access:
   ```powershell
   python manage.py createsuperuser
   ```
5. Start the development server:
   ```powershell
   python manage.py runserver
   ```

## Features

- Admin panel for product, customer, supplier, sale, and purchase management
- Modern responsive dashboard with sales, stock, and activity summaries
- Customer, supplier, inventory, purchase, and sales pages
- Built-in authentication and role-aware access
- Frontend interactivity using JavaScript
