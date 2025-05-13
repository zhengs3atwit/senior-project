from django.db import models
import uuid

# Create your models here.
class BaseRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    email = models.EmailField(max_length=255)
    firstName = models.CharField(max_length=255, blank=True, null=True)
    lastName = models.CharField(max_length=255, blank=True, null=True)
    clicked = models.BooleanField(default=False)
    email_sent_time = models.DateTimeField(blank=True, null=True)
    email_click_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract=True
        db_table = "user_record"
    
class Campaign(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

class UserRecord(BaseRecord):
    campaign = models.ManyToManyField(Campaign)
    template = models.IntegerField(default=0)
    latest_campaign = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        if self.pk:  
            campaign_names = ', '.join(c.name for c in self.campaign.all())
        else:
            campaign_names = '[Not saved yet]'
        return f'First Name: {self.firstName} Second Name: {self.lastName} Email: {self.email} Clicked: {self.clicked} Campaigns: {campaign_names} Template: {self.template}'
