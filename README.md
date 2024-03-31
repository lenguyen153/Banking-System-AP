## Banking System

This project is a basic banking system built using Django. It provides APIs for managing branches, banks, accounts, and more.

### Features

- **Branch Management**: APIs for listing branches (`branches/`) and retrieving details of a specific branch (`branch/<branch_id>/`).
- **Bank Management**: APIs for listing banks (`banks/`) and retrieving details of a specific bank (`bank/<bank_id>/`).
- **Account Management**: APIs for creating accounts (`create_account/`) and listing accounts (`accounts/`).

### API Endpoints

- `branches/`: Lists all branches.
- `branch/<branch_id>/`: Retrieves details of a specific branch by its ID.
- `banks/`: Lists all banks.
- `bank/<bank_id>/`: Retrieves details of a specific bank by its ID.
- `create_account/`: Creates a new account.
- `accounts/`: Lists all accounts.

### Usage

To use the APIs, you can send HTTP requests to the corresponding endpoints using tools like Postman or directly from your frontend or backend applications.

### Installation

1. Clone the repository:

  ```bash
  git clone <repository_url>
 ```

Install the required dependencies:

  ```bash
  pip install -r requirements.txt
 ```

Run migrations to set up the database:

  ```bash
  python manage.py migrate
 ```


Start the development server:
  ```bash
  python manage.py runserver
 ```

Access the API endpoints using the base URL provided by the development server, e.g., http://localhost:8000/.
API Authentication
The API endpoints may require authentication depending on your project's settings. Make sure to authenticate appropriately before accessing protected endpoints.

Contributors
Vincent Trinh

License
This project is licensed under the MIT License.
