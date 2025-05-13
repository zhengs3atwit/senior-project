from django.contrib import admin
from .models import CustomUser
from dashboard.models import UserRecord, Campaign  


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'last_login', 'date_joined', 'campaigns_display']
    list_filter = ['is_staff', 'is_active', 'date_joined']
    search_fields = ['email', 'first_name', 'last_name']

    def campaigns_display(self, obj):
        try:
            user_record = UserRecord.objects.get(email=obj.email)
            campaigns = user_record.campaign.all()
            return ", ".join([campaign.name for campaign in campaigns])
        except UserRecord.DoesNotExist:
            return "No Record"  
        except Exception as e:
            return f"Error: {e}" 

    campaigns_display.short_description = 'Campaigns'

# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)