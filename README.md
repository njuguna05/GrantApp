# GrantApp
# Grant Management System

## Overview

The Grant Management System (GMS) is a web-based application designed to streamline the management of grants, applications, beneficiaries, disbursements, and documents. The system allows grant administrators to manage the entire lifecycle of a grant, from application submission to disbursement, ensuring transparency and efficiency in the process.

## Features

- **Grant Types**: Manage different types of grants available for application.
- **Applications**: Track applications submitted by beneficiaries for specific grants.
- **Beneficiaries**: Manage beneficiary details, including their status and associated grants.
- **Disbursements**: Track disbursements made to beneficiaries and the status of each disbursement.
- **Documents**: Upload and manage documents related to applications and grants.
- **Admin Interface**: Django admin interface for managing all models, with search, filter, and display options.

## Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Django
- PostgreSQL (or any other database backend you prefer)
- Virtualenv (optional, but recommended)

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/grant-management.git
cd grant-management

Step 2: Create a Virtual Environment

If you're using a virtual environment (recommended), create one and activate it:

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Step 3: Install Dependencies
sudo apt-get install libpq-dev python3-dev
pip install psycopg2-binary
sudo apt update
sudo apt install postgresql postgresql-contrib
Install the required dependencies using pip:

pip install -r requirements.txt

Step 4: Set Up the Database

    Ensure your PostgreSQL (or another database) is set up.
    Update the DATABASES settings in settings.py to match your database configuration.
    Run the migrations to set up the database schema:

python manage.py migrate

Step 5: Create a Superuser

To access the Django admin interface, create a superuser:

python manage.py createsuperuser

Follow the prompts to set up the superuser credentials.
Step 6: Run the Development Server

Start the Django development server:

python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser. To access the admin interface, go to http://127.0.0.1:8000/admin/
Folder Structure

grant_management/
│
├── grants/                 # App for managing grants, applications, beneficiaries, etc.
│   ├── migrations/         # Database migrations for grants app
│   ├── models.py           # Model definitions
│   ├── admin.py            # Django admin interface registration
│   ├── views.py            # Views for the app
│   ├── serializers.py      # Serializers for API endpoints
│   ├── urls.py             # URLs for the grants app
│   └── ...
│
├── grant_app/              # Project settings and configuration
│   ├── settings.py         # Project settings
│   ├── urls.py             # Project-level URL configuration
│   ├── wsgi.py             # WSGI entry point for deployment
│   └── ...
│
├── manage.py              # Django management command script
├── requirements.txt       # List of dependencies
└── README.md              # Project documentation (this file)

Models Overview
1. GrantType

The GrantType model stores information about different types of grants available for application.
2. Beneficiary

The Beneficiary model tracks individuals or organizations who apply for grants.
3. Application

The Application model stores information about the applications submitted by beneficiaries for specific grants.
4. Disbursement

The Disbursement model records the financial disbursements made to beneficiaries upon approval of their application.
5. Document

The Document model allows the uploading and management of documents related to the application and grant process.
API Endpoints

The application may expose RESTful APIs to interact with the system. Some basic endpoints may include:

    GET /api/granttypes/: List all grant types.
    POST /api/applications/: Submit an application for a grant.
    GET /api/beneficiaries/: List all beneficiaries.
    GET /api/disbursements/: List disbursements made to beneficiaries.

You can extend this based on your application's needs.
Running Tests

To run the tests for the application, use the following command:

python manage.py test

Deployment

For deploying to production, you can use popular platforms like Heroku, DigitalOcean, or AWS. Ensure that you have configured the environment settings (e.g., database, static files) accordingly.
Contributing

We welcome contributions to this project! To contribute:

    Fork the repository.
    Create a new branch (git checkout -b feature-name).
    Make your changes.
    Commit your changes (git commit -am 'Add new feature').
    Push to the branch (git push origin feature-name).
    Create a new Pull Request.

License

This project is licensed under the MIT License - see the LICENSE file for details.

### Key Sections Explained:
- **Overview**: Describes the purpose of the project.
- **Installation**: Step-by-step guide to setting up the project on your local machine.
- **Folder Structure**: Describes the folder layout and important files.
- **Models Overview**: Brief explanation of the models used in the application.
- **API Endpoints**: Example API endpoints if you're planning to expose them.
- **Running Tests**: How to run tests for the application.
- **Deployment**: Basic instructions for deploying the project to production.
- **Contributing**: How others can contribute to the project.
- **License**: Licensing information for the project.

You can adjust the content as per your specific requirements.

