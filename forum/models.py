from django.db import models
from accounts.models import KampusUser

class Topic(models.Model):
    topic_name = models.CharField(max_length=100 , unique=True)
    
def entry_image_path(instance, filename):
    
    return f"forum/entry_images/{filename}"
class Entry(models.Model):
    entry_user = models.ForeignKey(KampusUser , on_delete=models.CASCADE , blank=False , related_name='entries')
    entry_topic = models.ForeignKey(Topic , on_delete=models.CASCADE , blank=False , related_name='entries')
    entry_date = models.DateTimeField(auto_now=True,blank=False)
    entry_title = models.CharField(max_length=120 , blank=False)
    entry_text = models.TextField(blank=False)
    entry_image = models.ImageField(blank=True , upload_to=entry_image_path)
    

    def __str__(self):
        return self.entry_title
    
class EntryLike(models.Model):
    liked_user = models.ForeignKey(KampusUser , on_delete=models.CASCADE , blank=False , related_name='likes')
    liked_entry = models.ForeignKey(Entry , on_delete=models.CASCADE , blank=False , related_name='likes')
    liked_date = models.DateTimeField(auto_now=True ,blank=False)
    

class EntryComment(models.Model):
    comment_entry = models.ForeignKey(Entry , on_delete=models.CASCADE , blank=False , related_name='comments')
    comment_user = models.ForeignKey(KampusUser , on_delete=models.CASCADE , blank=False , related_name='comments')
    comment_text = models.TextField(max_length=1000)

    def __str__(self):
        return self.comment_user.Username + self.comment_entry.entry_title + self.id
    
