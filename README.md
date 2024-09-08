# Apple 2.0

Welcome to the Apple 2.0 project! This Django-based web application showcases Apple products, allowing users to view and purchase them.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Project Structure](#project-structure)
5. [Configuration](#configuration)
6. [Testing](#testing)
7. [Contributing](#contributing)
8. [License](#license)

## Project Overview

The Apple 2.0 project is a Django web application that provides a platform for users to browse and buy Apple products. It includes features such as product listing, order creation, and user authentication.

## Installation

To get started with the Apple 2.0 project, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/apple-2.0.git
    cd apple-2.0
    ```

2. **Set up a virtual environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:

    ```bash
    python manage.py migrate
    ```

5. **Collect static files**:

    ```bash
    python manage.py collectstatic
    ```

6. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

   The application will be available at `http://127.0.0.1:8000/`.

## Usage

- **Homepage**: Displays featured products and provides navigation to other parts of the site.
- **Product Pages**: Allows users to view product details and make purchases.
- **User Authentication**: Includes login and signup functionality for users to create accounts and manage their orders.
- **Admin Interface**: Manage products, users, and orders through Django's admin interface.

## Project Structure

Here is an overview of the project structure:

### **AppleStore** (Django Project Directory)
- `__init__.py` - Marks the directory as a Python package.
- `asgi.py` - ASGI configuration for the project.
- `settings.py` - Project settings and configuration.
- `urls.py` - URL declarations for routing.
- `wsgi.py` - WSGI configuration for serving the project.

### **Products** (Django App for Product Management)
- `__init__.py` - Marks the directory as a Python package.
- `admin.py` - Admin interface configuration.
- `apps.py` - Application-specific configuration.
- `models.py` - Models for product-related data.
- `tests.py` - Unit tests for the products app.
- `views.py` - Views handling product-related requests.
- **Templates**
  - `buyitem.html` - Template for item purchase.
  - `confirmed.html` - Order confirmation template.
  - `createorder.html` - Template for creating new orders.
  - `orderdetails.html` - Order details template.
  - `vieworders.html` - Template for viewing orders.

### **Storefront** (Django App for Storefront Management)
- `__init__.py` - Marks the directory as a Python package.
- `admin.py` - Admin interface configuration.
- `apps.py` - Application-specific configuration.
- `models.py` - Models for storefront data.
- `tests.py` - Unit tests for the storefront app.
- `views.py` - Views handling storefront-related requests.
- **Templates**
  - `base.html` - Base template for consistent layout.
  - `buypage.html` - Template for the buy page.
  - `home.html` - Home page template.
  - `login.html` - Login page template.
  - `signup.html` - Signup page template.

### **Media** (Directory for Media Files)
- **Products**
  - **Images**
    - `14296939_apple-vision-pro-getty-img.jpg`
    - `ipad.jpg`
    - `iphone.jpg`
    - `watch.jpg`

### **Static** (Directory for Static Files)
- **Media**
  - **Products**
    - **Images**
      - `ipadp.jpg`
      - `iphone.jpg`
      - `watch.jpg`
- **Base**
  - `applelogo.png`
  - `basestyle.css`
- **Buy Page**
  - `choosepage.css`
  - `finish.css`
  - `style.css`
- **Products**
  - `detail.css`
  - `productstyle.css`
  - `vieworders.css`

### **Configuration Files**
- `Pipfile` - Pipenv configuration file.
- `Pipfile.lock` - Pipenv lock file.
- `requirements.txt` - List of dependencies.
- `manage.py` - Command-line utility for managing the project.
- `db.sqlite3` - SQLite database file.

## Configuration

Update the `settings.py` file with any necessary configurations specific to your environment, including database settings and secret keys.

## Testing

Run tests using Django's testing framework:

```bash
python manage.py test
