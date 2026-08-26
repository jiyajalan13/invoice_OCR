from django.shortcuts import render

from .forms import InvoiceUploadForm
from .ocr import extract_text_from_image, InvalidImageError
from .models import InvoiceOCRResult


def upload_invoice(request):

    if request.method == "POST":

        form = InvoiceUploadForm(request.POST, request.FILES)

        if form.is_valid():

            image = form.cleaned_data["invoice_image"]

            try:
                extracted_text = extract_text_from_image(image)
            except InvalidImageError:
                return render(
                    request,
                    "ocr_app/result.html",
                    {"error": "That file couldn't be read as a valid image. "
                              "Please upload a PNG or JPG invoice image."}
                )

            # Save to Postgres
            image.seek(0)  # rewind — OCR already read the file once
            InvoiceOCRResult.objects.create(
                image=image,
                extracted_text=extracted_text
            )

            return render(
                request,
                "ocr_app/result.html",
                {"extracted_text": extracted_text}
            )

    else:
        form = InvoiceUploadForm()

    return render(request, "ocr_app/upload.html", {"form": form})