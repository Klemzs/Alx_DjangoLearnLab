from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

User = get_user_model()

# Create your models here.
class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'received_notifications')
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'sent_notifications')
    verb = models.CharField(max_length=255)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    target = GenericForeignKey()
    timestamp = models.DateTimeField(auto_now_add=True)
