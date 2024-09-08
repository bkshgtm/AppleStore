# AppleStore

Welcome to the AppleStore project! This Django-based web application showcases Apple products, allowing users to view and purchase them.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Project Structure](#project-structure)
5. [Configuration](#configuration)
6. [Testing](#testing)
7. [Contributing](#contributing)
8. [License](#license)
9. [Acknowledgements](#acknowledgements)
10. [ScreenShots](#screenshots)
    

## Project Overview

The Apple 2.0 project is a Django web application that provides a platform for users to browse and buy Apple products. It includes features such as product listing, order creation, and user authentication.

## Installation

To get started with the Apple 2.0 project, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/bkshgtm/AppleStore.git
    cd AppleStore
    ```

2. **Set up a virtual environment**:
   
    ### macOS and Linux

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    ### Windows

    ```bash
    python -m venv venv
    venv\Scripts\activate
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
```

## Contributing

We welcome any contributions to the Apple 2.0 project! To contribute:

1. **Fork the repo** on GitHub.
2. **Clone** your forked repo to your local machine.
3. **Create a new branch** for your changes.
4. **Make your changes** and commit them.
5. **Push** your changes to your fork.
6. **Open a pull request** on GitHub.

Thank you for your contributions!

---

## License

The Apple 2.0 project is licensed under the MIT License.

---

MIT License

Copyright (c) [2024] [Bikash Gautam]

Permission is granted to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, with the same conditions mentioned above. The software is provided "as is", without any warranty of any kind.

---

## Acknowledgements

The Apple 2.0 project uses the following technologies:

- **Python**: For the programming language.
- **Django**: For the web framework.
- **HTML**: For structuring the web pages.
- **CSS**: For styling the web pages.
- **JavaScript**: For interactive elements.
- **Bootstrap**: For UI components and styling.

## Screenshots
![landpage](https://github.com/user-attachments/assets/c541294b-9347-4e29-bf90-e2041624ad0b)
![signuppage](https://github.com/user-attachments/assets/94f5e59a-d282-4613-80f4-d88ed48964c3)
![loginpage](https://github.com/user-attachments/assets/dba337cc-11d3-4bc3-83fc-e5507008bfae)
![ipad](https://github.com/user-attachments/assets/eb3a1858-e8a3-42a8-9a18-39e045c9b115)
![products](https://github.com/user-attachments/assets/9693c2b3-6707-4114-abc4-df0b161a0fc5)
![buypage](https://github.com/user-attachments/assets/ee091b72-4504-46ff-8ef8-84652f59eb31)
![createorder](https://github.com/user-attachments/assets/ddead817-310d-4159-bf17-0ecb6bb8a407)
![specselect](https://github.com/user-attachments/assets/7b58dd70-34d3-4379-8e09-dfa4f98ca216)
![ordercomplete](https://github.com/user-attachments/assets/af8e5d9e-c9cf-409e-9e48-1076ddbad20e)
![orders](https://github.com/user-attachments/assets/c9e42222-fcf4-45c5-a3f7-c09f986c25b5)
![orderdetails](https://github.com/user-attachments/assets/07dbf1de-04d6-4206-b818-6e04f5348b64)
![ordercancellation](https://github.com/user-attachments/assets/97d967ec-e136-4c9f-9a82-da6528ee11b4)




