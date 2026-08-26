from django import forms


class InvoiceUploadForm(forms.Form):
    invoice_image = forms.ImageField(
        label="Upload Invoice",
        required=True,
        widget=forms.ClearableFileInput(attrs={
            "id": "invoice-image-input",
            "class": "file-input",
            "accept": "image/png, image/jpeg",
        }),
    )