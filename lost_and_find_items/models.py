from django.db import models
from accounts.models import KampusUser
def found_item_image_path(instance, filename):
    return f"LFItems/images/{instance.id}-{filename}"
class Item(models.Model):
    item_user = models.ForeignKey(KampusUser , on_delete=models.CASCADE , blank=False , related_name='found_items')
    item_title = models.CharField(max_length=150)
    item_image = models.ImageField(blank=True , upload_to=found_item_image_path)
    item_text = models.TextField(blank=False)
    item_date = models.DateTimeField(auto_now=True , blank=False)
    item_found = models.BooleanField(default=True , blank=False)

    def __str__(self):
        return self.item_title
