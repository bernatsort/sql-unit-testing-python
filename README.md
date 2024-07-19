# SQL Unit Testing in Python

This project demonstrates how to perform unit testing for SQL queries using Python. The goal is to ensure the accuracy and reliability of SQL logic used in data processing and analytics. The project leverages pytest for testing, SQLAlchemy for database interaction, and GitHub Actions for CI/CD.


## Prerequisites

- Python 3.12
- pip

## Setup

1. **Clone the repository**
    ```sh
    git clone https://github.com/bernatsort/sql-unit-testing-python.git
    cd sql-unit-testing-python
    ```

2. **Create a virtual environment**
    ```sh
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**
    ```sh
    pip install --upgrade pip
    pip install pytest sqlalchemy pandas openpyxl
    ```

## Running the Tests

-  **Run all tests**
    ```sh
    pytest
    ```

## CI/CD Pipeline

The project uses GitHub Actions for continuous integration. The CI pipeline is configured to:

1. **Checkout the repository**
2. **Set up Python 3.12**
3. **Install dependencies**

