from django.db import models
from accounts.models import KampusUser
# Create your models here.
def community_logo_path(instance, filename):
    
    return f"communities/logos/{instance.community_name}/{filename}"
class Community(models.Model):
    community_name = models.CharField(max_length=150, blank=False)
    community_logo = models.ImageField(upload_to=community_logo_path , blank=False)
    community_agent = models.OneToOneField(KampusUser , on_delete=models.CASCADE , primary_key=True , blank=True)
    community_about_text = models.TextField(blank=False)



    def __str__(self):
        return self.community_name
    
def announcement_image_path(instance, filename):
    
    return f"communities/announcements/images/{instance.annonuncement_community.community_name}/{filename}"

related_name = 'announcements'
class CommunityAnnouncement(models.Model):
    announcement_community = models.ForeignKey(Community, on_delete=models.CASCADE , 
                                               related_name=related_name ,blank=False)
    announcement_title = models.CharField(max_length=100, blank=False)
    announcement_shorttext = models.CharField(max_length=120 , blank=True)
    announcement_text = models.TextField(blank=False)
    announcement_date = models.DateTimeField(auto_now=False , blank=False)
    announcement_image = models.ImageField()

    def __str__(self):
        return self.announcement_community.community_name
