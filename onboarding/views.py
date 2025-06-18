from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Franchise, DigitalPresence, DigitalStatusMaster
from .forms import DigitalPresenceForm  
# Create your views here.
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User

from datetime import date
from .models import User, MailLog, Task  


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username, password=password, is_active=True, is_deleted=False)
            
            # If user is admin
            if user.role.role_name.lower() == 'admin':
                request.session['user_id'] = user.id
                return render(request, 'onboarding/admin_dashboard.html')  # 👈 THIS RENDERS YOUR HTML FILE

            # If user is not admin b 
            else:
                request.session['user_id'] = user.id
                return render(request, 'onboarding/user_dashboard.html')
        
        except User.DoesNotExist:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'onboarding/login.html')




def dashboard_view(request):
    return render(request, 'onboarding/dashboard.html')

from django.utils.timezone import localdate

def admin_dashboard(request):
    mail_logs = MailLog.objects.order_by('-sent_at')[:10]
    today = localdate()
    todays_work = Task.objects.filter(assigned_on=today)

    context = {
        'mail_logs': mail_logs,
        'todays_work': todays_work,
    }
    return render(request, 'onboarding/admin_dashboard.html', context)
# onboarding/views.py

from django.shortcuts import render

def user_dashboard(request):
    return render(request, 'onboarding/user_dashboard.html')


@login_required
def franchisee_dashboard(request):
    return render(request, 'onboarding/franchisee_dashboard.html')

@login_required
def manager_dashboard(request):
    return render(request, 'onboarding/manager_dashboard.html')
def logout_view(request):
    request.session.flush()  # Clears the session
    return redirect('login')
from .models import FranchiseApplication

from django.shortcuts import render, redirect
from .models import FranchiseApplication, FranchiseDetails
from django.views.decorators.csrf import csrf_exempt

def franchise_applications_list(request):
    applications = FranchiseApplication.objects.all()
    selected_application = None

    if request.method == 'POST':
        app_number = request.POST.get('application_number')
        franchise_id = request.POST.get('franchise_id')

        try:
            app = FranchiseApplication.objects.get(application_number=app_number)
        except FranchiseApplication.DoesNotExist:
            messages.error(request, "Application not found.")
            return redirect('franchise_applications')

        # Check if franchise already exists
        if FranchiseDetails.objects.filter(application=app).exists():
            messages.error(request, "Franchise already created for this application.")
        elif FranchiseDetails.objects.filter(franchise_id=franchise_id).exists():
            messages.error(request, "This Franchise ID is already used.")
        else:
            FranchiseDetails.objects.create(application=app, franchise_id=franchise_id)
            messages.success(request, "Franchise created successfully.")
            return redirect('franchise_applications')

    elif request.method == 'GET' and 'application_number' in request.GET:
        app_number = request.GET.get('application_number')
        selected_application = FranchiseApplication.objects.filter(application_number=app_number).first()

    return render(request, 'onboarding/franchise_applications.html', {
        'applications': applications,
        'selected_application': selected_application
    })
def franchise_list_view(request):
    franchises = FranchiseDetails.objects.select_related('application').all()
    return render(request, 'onboarding/franchise_list.html', {'franchises': franchises})
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest
from .models import Franchise, DigitalPresence, DigitalStatusMaster
from django.views.decorators.csrf import csrf_exempt

def franchise_phase1_view(request):
    if request.method == 'POST':
        form = DigitalPresenceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Franchise Phase 1 details submitted successfully.")
            return redirect('franchise_phase1')  # or redirect to 'user_dashboard' or 'franchise_phase2' as needed
        else:
            messages.error(request, "⚠️ Please correct the errors below.")
    else:
        form = DigitalPresenceForm()

    return render(request, 'onboarding/franchise_phase1.html', {'form': form})
from .forms import BrandingAssetForm

def franchise_phase2_view(request):
    if request.method == 'POST':
        form = BrandingAssetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Branding assets submitted successfully.")
            return redirect(request.path)  # Reloads the same form page
        else:
            messages.error(request, "⚠️ Please correct the errors below.")
    else:
        form = BrandingAssetForm()

    return render(request, 'onboarding/franchise_phase2.html', {'form': form})


# -------------------------------------------------------------------------------------------
from .forms import Phase3Form

def franchise_phase3_view(request):
    # Automatically fetch the first available Franchise
    franchise = Franchise.objects.first()

    if request.method == 'POST':
        form = Phase3Form(request.POST)
        if form.is_valid():
            phase_progress = form.save(commit=False)
            phase_progress.franchise = franchise
            phase_progress.save()
            messages.success(request, "✅ Phase 3: Promotion & Ad Setup submitted successfully.")
            return redirect(request.path)  # Stay on the same page
        else:
            messages.error(request, "⚠️ Please correct the errors below.")
    else:
        form = Phase3Form()

    return render(request, 'onboarding/franchise_phase3.html', {'form': form})
from django.http import JsonResponse
from django.db import connection


def get_franchise_applicants(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT f.franchise_id, a.applicant_name
            FROM onboarding_franchisedetails f
            JOIN onboarding_franchiseapplication a ON f.application_id = a.id
        """)
        rows = cursor.fetchall()

    # Convert to list of dicts
    data = [{"franchise_id": row[0], "applicant_name": row[1]} for row in rows]
    return JsonResponse(data, safe=False)
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import UserPrivilege

@csrf_exempt
def assign_user_privilege(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        franchise_id = data.get('franchiseId')
        role = data.get('role')

        if username and franchise_id and role:
            privilege = UserPrivilege.objects.create(
                username=username,
                franchise_id=franchise_id,
                role=role
            )
            return JsonResponse({'success': True, 'message': 'Privilege assigned successfully.'})
        else:
            return JsonResponse({'success': False, 'message': 'Missing fields.'}, status=400)
    
    return JsonResponse({'error': 'Invalid method'}, status=405)




def get_user_privileges(user_id):
    try:
        user = User.objects.get(id=user_id)
        role = user.role
        if role:
            return role.permissions  # this is a list from JSONField
        return []
    except User.DoesNotExist:
        return []
def get_user_franchise_details():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT u.username, f.branch_name, f.branch_code
            FROM yourapp_user u
            JOIN yourapp_franchise f ON u.id = f.created_by_id
        """)
        rows = cursor.fetchall()
    return rows
