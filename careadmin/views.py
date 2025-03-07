from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages
from careapp.models import StaffDetails

# Create your views here.

class AdminLoginView(View):
    template_name = "carecenter/adminlogin.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        return redirect('dashboard-page')
        # ig

class DashboardView(View):
    template_name = 'carecenter/dashboard_admin.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('custom_admin_login')  
       
        return render(request, self.template_name)
    

class RecruitmentView(View):
    template_name = 'carecenter/candidate_details.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('custom_admin_login') 
        else:
            details = StaffDetails.objects.all()
            context ={
                'details':details
                } 
        return render(request, self.template_name,context)

class ProfileDetailsView(View):
    template_name = 'carecenter/profile_details.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('custom_admin_login') 
            # user_data = StaffDetails.objects.get(id=id)
            # context ={
            #     'user_data':user_data,
            #     } 
        return render(request, self.template_name,)
    