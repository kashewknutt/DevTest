# DevTest Django Application

## Overview

This is a Django-based web application that allows users to upload Excel/CSV files, processes the data, generates a summary report, and emails the report to the specified email address. The application is deployed on Render for easy access and scalability.

## Features

- **File Upload:** Users can upload Excel/CSV files.
- **Data Processing:** The application processes the uploaded data and generates a summary report.
- **Email Summary:** The summary report is sent to the user's email as the body of the email.
- **User-Friendly Interface:** A simple, clean, and responsive interface for ease of use.

## Technologies Used

- **Django:** The web framework used to build the application.
- **pandas:** For processing Excel/CSV files and generating the summary report.
- **Gunicorn:** WSGI HTTP server for serving the application in production.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/DevTest.git
cd DevTest
```
### 2. Install Dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

Install the required packages

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python manage.py runserver
```

### 4. Access the application

Open a web browser and navigate to `http://localhost:8000/`

## Deploying on Render

1. Pushed code to GitHub.
2. Connected GitHub repository to Render.
3. Configured the web service with the following settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn DevTest.wsgi`

## Usage

- **Website:** The application can be accessed at `https://devtest-qve5.onrender.com/`.
- **Upload File:** Visit the landing page to upload an Excel/CSV file.
- **View Summary:** After successful upload, a summary report will be displayed and emailed to you.

## Contact

For any inquiries or issues, please reach out to [kashewknutt@gmail.com](mailto:kashewknutt@gmail.com).