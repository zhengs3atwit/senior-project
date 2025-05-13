from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from .models import CustomUser
from dashboard.models import UserRecord, Campaign  

CAMPAIGN_CHOICES = [
    ("Credential Harvest", "Credential Harvest"),
    ("Malware Attachment", "Malware Attachment"),
    ("Spear Phishing", "Spear Phishing"),
    ("Fake Login Page", "Fake Login Page"),
]

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=150, label="Last Name")
    
    campaigns = forms.MultipleChoiceField(
        choices=CAMPAIGN_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Which phishing simulations do you want to receive?"
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("email", "first_name", "last_name")

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Email already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

        user_record = UserRecord.objects.create(
            email=user.email,
            firstName=user.first_name,
            lastName=user.last_name,
            template=0
        )

        selected_campaign_names = self.cleaned_data['campaigns']
        for name in selected_campaign_names:
            campaign, created = Campaign.objects.get_or_create(name=name)
            user_record.campaign.add(campaign)

        user_record.save()
        return user

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label=("Email"))