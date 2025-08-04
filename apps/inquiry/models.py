from django.db import models
from django.conf import settings
from django.utils import timezone
import uuid

def inquiry_image_path(instance, filename):
    return f"inquiries/{instance.inquiry.id}/{filename}"

class Inquiry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='inquiries')
    phone = models.CharField(max_length=15)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Auto generate offer number using UUID short
    offer_number = models.CharField(max_length=20, unique=True, editable=False)
    contact_person = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='contact_offers',
        limit_choices_to={'is_staff': True}
    )

    def save(self, *args, **kwargs):
        if not self.offer_number:
            self.offer_number = str(uuid.uuid4().int)[:6]  # 6 digit offer number
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Offer {self.offer_number} - {self.user.company_name}"


class InquiryImage(models.Model):
    inquiry = models.ForeignKey(Inquiry, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=inquiry_image_path)

    def __str__(self):
        return f"Image for {self.inquiry.offer_number}"
