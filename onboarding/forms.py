from django import forms
from .models import BrandingAsset

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
from .models import DigitalPresence, DigitalStatusMaster, Franchise

# onboarding/forms.py

from django import forms
from .models import DigitalPresence
class DigitalPresenceForm(forms.ModelForm):
    class Meta:
        model = DigitalPresence
        fields = [
            'status',
            'gmail',
            'mobile_number',
            'google_business_url',
            'facebook_page_url',
            'instagram_account_url',
        ]
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'gmail': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Gmail'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile Number'}),
            'google_business_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Google Business URL'}),
            'facebook_page_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Facebook Page URL'}),
            'instagram_account_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Instagram Account URL'}),
            'franchise': forms.Select(attrs={'class': 'form-control'}),
        }
from django import forms
class BrandingAssetForm(forms.ModelForm):
    class Meta:
        model = BrandingAsset
        fields = [
            'name_board_file', 'name_board_gdrive_link',
            'side_wall_file', 'side_wall_gdrive_link',
            'standee_file', 'standee_gdrive_link',
            'reception_pov_file', 'reception_pov_gdrive_link',
            'benefits_of_language_file', 'benefits_of_language_gdrive_link',
            'centre_seal_file', 'centre_seal_gdrive_link',
            'centre_letter_pad_file', 'centre_letter_pad_gdrive_link',
            'centre_visiting_card_file', 'centre_visiting_card_gdrive_link',
            'centre_profile_pic_file', 'centre_profile_pic_gdrive_link',
            'stall_file', 'stall_gdrive_link',
            'pamphlet_file', 'pamphlet_gdrive_link',
            'brochure_institution_file', 'brochure_institution_gdrive_link',
            'brochure_parents_file', 'brochure_parents_gdrive_link',
            'isml_logo_file', 'isml_logo_gdrive_link',
        ]

        widgets = {
            field: forms.ClearableFileInput(attrs={'class': 'form-control'})
            for field in [
                'name_board_file', 'side_wall_file', 'standee_file', 'reception_pov_file',
                'benefits_of_language_file', 'centre_seal_file', 'centre_letter_pad_file',
                'centre_visiting_card_file', 'centre_profile_pic_file', 'stall_file',
                'pamphlet_file', 'brochure_institution_file', 'brochure_parents_file',
                'isml_logo_file',
            ]
        } | {
            field: forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Google Drive Link'})
            for field in [
                'name_board_gdrive_link', 'side_wall_gdrive_link', 'standee_gdrive_link',
                'reception_pov_gdrive_link', 'benefits_of_language_gdrive_link',
                'centre_seal_gdrive_link', 'centre_letter_pad_gdrive_link',
                'centre_visiting_card_gdrive_link', 'centre_profile_pic_gdrive_link',
                'stall_gdrive_link', 'pamphlet_gdrive_link',
                'brochure_institution_gdrive_link', 'brochure_parents_gdrive_link',
                'isml_logo_gdrive_link',
            ]
        }

from .models import PhaseProgress

class Phase3Form(forms.ModelForm):
    class Meta:
        model = PhaseProgress
        fields = [
           'start_date', 'end_date', 'status',
            'ad_set', 'promotion_setup', 'ad_account_creation',
            'based_on_page', 'ad_campaign_setup', 'target_audience_creation'
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'based_on_page': forms.Select(attrs={'class': 'form-control'}),
        }
