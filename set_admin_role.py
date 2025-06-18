import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'franchise_system.settings')  # <-- update this if your settings path is different
django.setup()

from django.contrib.auth.models import User
from onboarding.models import UserProfile

user = User.objects.get(username='admin')
profile, created = UserProfile.objects.get_or_create(user=user)
profile.role = 'admin'
profile.save()

print("Franchisee role assigned!")
user = User.objects.get(username='franchisee')
profile, created = UserProfile.objects.get_or_create(user=user)
profile.role = 'franchisee'
profile.save()

print("Admin role assigned!")
