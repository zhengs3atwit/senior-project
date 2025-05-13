from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.db import connection

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'


@receiver(post_migrate)
def create_default_campaigns(sender, **kwargs):
    if sender.name != 'dashboard':
        return

    from django.apps import apps
    Campaign = apps.get_model('dashboard', 'Campaign')
    
    if not connection.introspection.table_names() or 'dashboard_campaign' not in connection.introspection.table_names():
        return

    defaults = [
        "Credential Phishing", "Malware Attachment", "Spear Phishing", "Link-Based"
    ]
    for name in defaults:
        Campaign.objects.get_or_create(name=name)