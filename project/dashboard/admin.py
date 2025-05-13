from django.contrib import admin
from .models import UserRecord, Campaign
from django.utils import timezone
import os, random
import brevo_python
from brevo_python.rest import ApiException


CAMPAIGN_TEMPLATES = {
    "Malware Attachment": [39847563],
    "Spear Phishing": [39954589],
    "Fake Login Page": [39846014],
    "Credential Harvest": [39847802]
}

@admin.action(description="Send")
def SendEmail(modeladmin, request, queryset):
    configuration = brevo_python.Configuration()
    configuration.api_key['api-key'] = 'NrFZtpcV3q8yfJkQ'
    api_instance = brevo_python.TransactionalEmailsApi(brevo_python.ApiClient(configuration))
    for user in queryset:
        print("aplpes sauce")
        user_campaigns = list(user.campaign.all())  

        if not user_campaigns:
            continue  

        selected_campaign = random.choice(user_campaigns)
        templates = CAMPAIGN_TEMPLATES.get(selected_campaign.name, [])

        if not templates:
            continue  

        selected_template = random.choice(templates)

        send_smtp_email = brevo_python.SendSmtpEmail(
        to=[{"email": user.email, "name": user.first_name}],
        sender={"name" : user.first_name , "email" : 'zhengs3@wit.edu'},
        template_id=1,
        params={
            "FIRSTNAME": user.first_name,
            "LASTNAME": user.last_name,
            "CAMPAIGN": selected_campaign.name,
            "YEAR": "2025",
            "COMPANY_NAME": "potatos",
        }
    )
        try:
            api_response = api_instance.send_transac_email(send_smtp_email)
            print(api_response)
        except ApiException as e:
            print("Exception when calling TransactionalEmailsApi->send_transac_email: %s\n" % e)


        user.template = selected_template
        user.latest_campaign = selected_campaign.name
        user.email_sent_time = timezone.now()
        user.save()


# Campaign admin
class CampaignAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']

# UserRecords admin
class UserRecordsAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'firstName', 'lastName', 'clicked', 'email_sent_time', 'email_click_time', 'campaigns_list', 'template', 'latest_campaign']
    def campaigns_list(self, obj):
        return ", ".join([campaign.name for campaign in obj.campaign.all()])
    campaigns_list.short_description = 'Campaigns'
    actions = [SendEmail]

# Register your models here.
admin.site.register(UserRecord, UserRecordsAdmin)
admin.site.register(Campaign, CampaignAdmin)
