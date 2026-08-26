# Invoice OCR Project

A Django-based Invoice OCR application that allows users to upload invoice images, extract text using Tesseract OCR, display the extracted text, and store the uploaded invoice and OCR result in PostgreSQL.

## Features

- Upload invoice images in PNG or JPG/JPEG format.
- Validate uploaded images using Pillow.
- Extract text from invoices using Tesseract OCR through `pytesseract`.
- Display extracted OCR text in the browser.
- Save the uploaded invoice and extracted text in PostgreSQL using Django ORM.
- View saved OCR records through Django Admin and pgAdmin 4.

## Technology Stack

- **Backend:** Django 6.x
- **Programming Language:** Python 3.x
- **OCR Engine:** Tesseract OCR
- **Python OCR Library:** pytesseract
- **Image Processing:** Pillow
- **Database:** PostgreSQL
- **PostgreSQL Driver:** psycopg2-binary
- **Development Environment:** VS Code / PowerShell

## Project Structure

```text
invoice_ocr_project/
│
├── manage.py
├── requirements.txt
├── db.sqlite3                 # Previous/local SQLite database; PostgreSQL is the active DB
│
├── invoice_project/
│   ├── __init__.py
│   ├── settings.py            # Django configuration and PostgreSQL connection
│   ├── urls.py                # Main URL configuration
│   ├── asgi.py
│   └── wsgi.py
│
└── ocr_app/
    ├── __init__.py
    ├── admin.py               # Django Admin configuration
    ├── apps.py
    ├── forms.py               # Invoice upload form
    ├── models.py              # InvoiceOCRResult database model
    ├── ocr.py                 # Tesseract OCR logic
    ├── urls.py                # OCR application routes
    ├── views.py               # Upload, OCR, and database-save workflow
    ├── migrations/
    ├── templates/
    │   └── ocr_app/
    │       ├── upload.html
    │       └── result.html
    └── test_images/
```

## How the Application Works

```text
User uploads invoice image
          ↓
Django receives the image
          ↓
InvoiceUploadForm validates the image
          ↓
Pillow opens and validates the image
          ↓
pytesseract sends image to Tesseract OCR
          ↓
Extracted text is returned
          ↓
InvoiceOCRResult.objects.create(...)
          ↓
PostgreSQL stores the OCR record
          ↓
Extracted text is displayed to the user
```


## Prerequisites

Install the following before running the project:

1. Python 3.x
2. PostgreSQL
3. pgAdmin 4 (recommended for viewing database records)
4. Tesseract OCR
5. Git (optional)

Verify Python:

```powershell
python --version
```

Verify pip:

```powershell
pip --version
```

Verify Tesseract:

```powershell
tesseract --version
```

If `tesseract` is not recognized, configure the Tesseract executable path using the `TESSERACT_CMD` environment variable.

## 1. Clone or Open the Project

Open the project folder in VS Code and open a PowerShell terminal in the folder containing `manage.py`.

Example:

```text
C:\Users\<username>\Desktop\invoice_ocr_project
```

## 2. Create and Activate Virtual Environment

Create the virtual environment:

```powershell
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

The terminal should show:

```text
(venv) PS C:\...\invoice_ocr_project>
```

## 3. Install Python Dependencies

Run:

```powershell
pip install -r requirements.txt
```

The main dependencies are:

```text
Django>=5.0,<7.0
pytesseract>=0.3.10
Pillow>=10.0
psycopg2-binary>=2.9
```

You can verify the PostgreSQL Python driver with:

```powershell
python -c "import psycopg2; print(psycopg2.__version__)"
```

## 4. Configure Tesseract OCR

The OCR code checks the following environment variable:

```text
TESSERACT_CMD
```

On Windows, if Tesseract is installed at a location such as:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

set the environment variable in the current PowerShell session:

```powershell
$env:TESSERACT_CMD="C:\Program Files\Tesseract-OCR\tesseract.exe"
```

Then verify the connection from Python:

```powershell
python -c "import pytesseract; print(pytesseract.get_tesseract_version())"
```

If the Tesseract version is printed, Python, pytesseract, and Tesseract are connected correctly.

## 5. Configure PostgreSQL

Create a PostgreSQL database named:

```text
invoice_ocr_db
```





**Security note:** Do not commit your real PostgreSQL password or Django secret key to GitHub. For production, use environment variables.

## 6. Test the Django Database Connection

From the folder containing `manage.py`, run:

```powershell
python manage.py check
```

If the configuration is correct, Django should report:

```text
System check identified no issues (0 silenced).
```


## 7. Create Database Migrations

Create migrations from the Django model:

```powershell
python manage.py makemigrations
```

Then apply them to PostgreSQL:

```powershell
python manage.py migrate
```

This creates the Django tables, including the OCR result table.

## 8. Verify the Database in pgAdmin 4

Open pgAdmin 4 and register/connect to the PostgreSQL server


## 9. Optional: Configure Django Media Storage


Because the model uses an `ImageField`, it is recommended to define media settings in `invoice_project/settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

Then update `invoice_project/urls.py` during development:
```

Uploaded invoices will then be stored under a structure similar to:


PostgreSQL stores the corresponding file reference in the `image` column.

## 10. Run the Application

Start Django:

```powershell
python manage.py runserver
```


Upload a PNG or JPG/JPEG invoice.

The application will:

1. Validate the uploaded image.
2. Run Tesseract OCR.
3. Extract the invoice text.
4. Save the invoice and extracted text to PostgreSQL.
5. Display the extracted text in the browser.

## 11. Verify That OCR Data Was Saved

After uploading an invoice, open pgAdmin and navigate to:

```text
invoice_ocr_db
→ Schemas
→ public
→ Tables
→ ocr_app_invoiceocrresult
→ Right-click
→ View/Edit Data
→ All Rows
```

## Security Notes

This project is currently configured for local development (`DEBUG = True`). Before production deployment:

- Move the Django `SECRET_KEY` to an environment variable.
- Move PostgreSQL credentials to environment variables.
- Set `DEBUG = False`.
- Configure `ALLOWED_HOSTS`.
- Configure secure media/static file serving.
- Use a production-ready PostgreSQL setup and deployment server.
- Do not commit `.env`, passwords, `SECRET_KEY`, uploaded invoices, or the `venv` directory to Git.

## Future Improvements

Possible next features include:

- Extract structured invoice fields such as invoice number, date, vendor, subtotal, tax, and total amount.
- Add confidence scores for OCR output.
- Add invoice history/search.
- Add pagination for stored invoices.
- Add authentication and user-specific invoice records.
- Add REST APIs using Django REST Framework.
- Add PostgreSQL full-text search.
- Improve OCR accuracy with image preprocessing such as grayscale conversion, thresholding, resizing, and noise removal.
- Add automated tests for OCR, uploads, database storage, and invalid files.

## End-to-End Result

The completed application follows this workflow:

```text
Invoice Image
     ↓
Django Upload Form
     ↓
Pillow Validation
     ↓
Tesseract OCR / pytesseract
     ↓
Extracted Invoice Text
     ↓
Django ORM
     ↓
PostgreSQL: invoice_ocr_db
     ↓
ocr_app_invoiceocrresult
     ↓
View Results in pgAdmin 4 / Django Admin
```

---

**Project:** Invoice OCR Project  
**Framework:** Django  
**OCR:** Tesseract + pytesseract  
**Database:** PostgreSQL
