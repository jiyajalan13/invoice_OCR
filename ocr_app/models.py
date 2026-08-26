from django.db import models

# Create your models here.



class InvoiceOCRResult(models.Model):
    image = models.ImageField(upload_to="invoices/")
    extracted_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice {self.id} - {self.created_at:%Y-%m-%d %H:%M}"