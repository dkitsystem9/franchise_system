from django.db import models
from django.contrib.auth.models import User

# Master Tables
class State(models.Model):
    state_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class City(models.Model):
    city_name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Franchise Status Master
class FranchiseStatusMaster(models.Model):
    status_name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Franchise Master Table
class Franchise(models.Model):
    application_no = models.CharField(max_length=50)
    branch_name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    branch_code = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(FranchiseStatusMaster, on_delete=models.SET_NULL, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
from django.contrib.auth.models import User

class FranchiseApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # add this line
    application_number = models.CharField(max_length=20, unique=True)
    applicant_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

class Franchise(models.Model):

    created_by = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True)

class FranchiseDetails(models.Model):
    application = models.OneToOneField(FranchiseApplication, on_delete=models.CASCADE)
    franchise_id = models.CharField(max_length=100)

    def __str__(self):
        return f"Franchise ID {self.franchise_id} for Application {self.application.application_number}"

# Franchisee Contact Info
class FranchiseeDetail(models.Model):
    franchise = models.ForeignKey(Franchise, on_delete=models.CASCADE)
    franchisee_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    lead_form_status = models.CharField(max_length=20, choices=[('registered', 'Registered'), ('not_registered', 'Not Registered')])
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Digital Presence Phase
class DigitalStatusMaster(models.Model):
    status_name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# models.py
class DigitalPresence(models.Model):
    franchise = models.ForeignKey(Franchise, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(
    max_length=50, 
    choices=[('pending', 'Pending'), ('done', 'Done')],
    default='pending'   # <-- Add default here
)
    gmail = models.EmailField(max_length=255, null=True, blank=True)
    mobile_number = models.CharField(max_length=15,null=True, blank=True)
    google_business_url = models.URLField(max_length=255, blank=True)
    facebook_page_url = models.URLField(max_length=255, blank=True)
    instagram_account_url = models.URLField(max_length=255, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Branding Assets
class BrandingAssetStatusMaster(models.Model):
    status_name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BrandingAsset(models.Model):
    name_board_file = models.FileField(upload_to='branding_assets/', blank=True, null=True)
    name_board_gdrive_link = models.URLField(max_length=255, blank=True, null=True)

    side_wall_file = models.FileField(upload_to='branding_assets/', blank=True, null=True)
    side_wall_gdrive_link = models.URLField(max_length=255, blank=True, null=True)

    standee_file = models.FileField(upload_to='branding_assets/', blank=True, null=True)
    standee_gdrive_link = models.URLField(max_length=255, blank=True, null=True)

    reception_pov_file = models.FileField(upload_to='branding_assets/', blank=True, null=True)
    reception_pov_gdrive_link = models.URLField(max_length=255, blank=True, null=True)

    benefits_of_language_file = models.FileField(upload_to='branding_assets/', blank=True, null=True)
    benefits_of_language_gdrive_link = models.URLField(max_length=255, blank=True, null=True)

    centre_seal_file = models.FileField(upload_to='branding_assets/', blank=True, null=True)
    centre_seal_gdrive_link = models.URLField(max_length=255, blank=True, null=True)

    centre_letter_pad_file = models.FileField(upload_to='branding_assets/', blank=True, null=True)
    centre_letter_pad_gdrive_link = models.URLField(max_length=255, blank=True, null=True)

    centre_visiting_card_file = models.FileField(upload_to='branding_assets/', blank=True, null=True)
    centre_visiting_card_gdrive_link = models.URLField(max_length=255, blank=True, null=True)

    centre_profile_pic_file = models.FileField(upload_to='branding_assets/', blank=True, null=True)
    centre_profile_pic_gdrive_link = models.URLField(max_length=255, blank=True, null=True)

    stall_file = models.FileField(upload_to='branding_assets/', blank=True, null=True)
    stall_gdrive_link = models.URLField(max_length=255, blank=True, null=True)

    pamphlet_file = models.FileField(upload_to='branding_assets/', blank=True, null=True)
    pamphlet_gdrive_link = models.URLField(max_length=255, blank=True, null=True)

    brochure_institution_file = models.FileField(upload_to='branding_assets/', blank=True, null=True)
    brochure_institution_gdrive_link = models.URLField(max_length=255, blank=True, null=True)

    brochure_parents_file = models.FileField(upload_to='branding_assets/', blank=True, null=True)
    brochure_parents_gdrive_link = models.URLField(max_length=255, blank=True, null=True)

    isml_logo_file = models.FileField(upload_to='branding_assets/', blank=True, null=True)
    isml_logo_gdrive_link = models.URLField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Ad Campaigns
class CampaignStatusMaster(models.Model):
    status_name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class AdCampaign(models.Model):
    franchise = models.ForeignKey(Franchise, on_delete=models.CASCADE)
    campaign_type = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.IntegerField()
    target_audience = models.TextField()
    status = models.ForeignKey(CampaignStatusMaster, on_delete=models.SET_NULL, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Phase Progress
class PhaseMaster(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    display_order = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PhaseProgress(models.Model):
    phase = models.ForeignKey('PhaseMaster', on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ])

    # ✅ New Phase 3-specific fields
    ad_set = models.BooleanField(default=False)
    promotion_setup = models.BooleanField(default=False)
    ad_account_creation = models.BooleanField(default=False)
    based_on_page = models.CharField(
        max_length=100, choices=[('fb', 'Facebook'), ('insta', 'Instagram'), ('both', 'Facebook & Instagram')],
        blank=True, null=True
    )
    ad_campaign_setup = models.BooleanField(default=False)
    target_audience_creation = models.BooleanField(default=False)

    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Users and Roles
class UserRole(models.Model):
    role_name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    permissions = models.JSONField(default=list)  # ✅ Use default=[]
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=255)  # Hashed password
    role = models.ForeignKey(UserRole, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)
# Example models based on your template

class MailLog(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    sent_at = models.DateTimeField()

    class Meta:
        db_table = 'onboarding_maillog'  # explicitly map to your table

    def __str__(self):
        return f"{self.email} - {self.subject}"

from django.utils.timezone import now

class Task(models.Model):
    franchise = models.CharField(max_length=100)
    task = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    assigned_on = models.DateField(default=now)  # default today

    def __str__(self):
        return f"{self.franchise} - {self.task}"
class UserPrivilege(models.Model):
    username = models.CharField(max_length=100)
    franchise_id = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.franchise_id} - {self.role}"
