from django.urls import path
from . import views
from .views import franchise_phase1_view, get_franchise_applicants,assign_user_privilege

urlpatterns = [
    # 🔐 Authentication
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # 🏠 Dashboard
    path('', views.dashboard_view, name='dashboard'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('franchisee-dashboard/', views.franchisee_dashboard, name='franchisee_dashboard'),
    path('manager-dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('user/dashboard/', views.user_dashboard, name='user_dashboard'),

    # 📄 Franchise Applications & List
    path('applications/', views.franchise_applications_list, name='franchise_applications'),
    path('franchise-list/', views.franchise_list_view, name='franchise_list'),

    # 🚀 Franchise Onboarding Phases
    path('franchise/phase1/', franchise_phase1_view, name='franchise_phase1'),
    path('franchise/phase2/', views.franchise_phase2_view, name='franchise_phase2'),
    path('franchise/phase3/', views.franchise_phase3_view, name='franchise_phase3'),

    # 🌐 API Endpoints
    path('api/franchise-applicants/', get_franchise_applicants, name='get_franchise_applicants'),
    path('api/assign-privilege/', assign_user_privilege, name='assign_user_privilege'),

]
