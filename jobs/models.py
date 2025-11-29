from django.db import models


def discount_announcement_image_path(instance, filename):
    return f"discounts/images/{instance.id}-{filename}"

class DiscountAnnouncement(models.Model):
    announcement_title = models.CharField(max_length=120 , blank=False)
    announcement_image = models.ImageField(upload_to=discount_announcement_image_path)
    announcement_text = models.TextField(blank=False)
    contact_number = models.CharField(max_length=100 , blank=True)
    place = models.CharField(max_length=200 , blank=False)
    announcement_date = models.DateTimeField(auto_now=False , blank=False)
    
    def __str__(self):
        return self.announcement_title
# Create your models here.
