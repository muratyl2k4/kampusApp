from django.db import models

def intern_place_image_path(instance,filename):
    return f"intern/places/images/{instance}-{filename}"
class InternPlace(models.Model):
    place_name = models.CharField(unique=True , blank=False)
    place_text= models.TextField(blank=True)
    place_image = models.ImageField(blank=True , upload_to=intern_place_image_path)
    place_contact = models.TextField(blank=True)

    def __str__(self):
        return self.place_name

internship_time_choices = (('Full-Time' , 'Full-Time'),
                           ('Part-Time' , 'Part-Time'))


def intern_announcement_image_path(instance , filename):
    return f"intern/images/{instance}-{filename}"
class InternCategory(models.Model):
    category_name = models.CharField(max_length=120)

    def __str__(self):
        return self.category_name
class InternAnnouncement(models.Model):
    intern_category = models.ForeignKey(InternCategory , on_delete=models.CASCADE , blank=True , null=True , related_name='intern_announcements')
    intern_place = models.ForeignKey(InternPlace , on_delete=models.CASCADE , blank=False , related_name='intern_announcements')
    intern_title = models.CharField(max_length=150 , blank=False)
    intern_image = models.ImageField(upload_to=intern_announcement_image_path , blank=True)
    intern_text = models.TextField(blank=False)
    intern_contact = models.TextField(blank=False)
    intern_date = models.DateTimeField(auto_now=True , blank=False)
    intern_time = models.CharField(blank=False , choices=internship_time_choices)
    intern_remote = models.BooleanField(default=False , blank=False)
    intern_end = models.BooleanField(default=False)

    def __str__(self):
        return self.intern_title

