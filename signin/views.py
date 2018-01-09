from .forms import AttendanceForm, ProfileForm
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from signin.models import *
from django.shortcuts import render
from django_tables2 import RequestConfig
from .tables import ProfileTable, HereTable
from datetime import date, timedelta
from django.db.models import Count


def sign_in(request):
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.date = timezone.now()
            username = attendance.phone_number
            attendance.save()

            user = User.objects.get(username=username)

            profile = Profile.objects.get(phone=username)
            profile.last_active = timezone.now()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
        return render(request, 'signin/sign_in.html', {'old_member': form})
    form = AttendanceForm()
    return render(request, 'signin/sign_in.html', {'old_member': form})


def staff_login(request):
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.date = timezone.now()
            username = attendance.phone_number

            user = User.objects.get(username=username)

            if user.profile.staff:
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
                return redirect('staff_dash')
            return render(request, 'signin/staff_login.html', {'not_staff': True})
        return render(request, 'signin/staff_login.html', {'old_member': form})
    form = AttendanceForm()
    return render(request, 'signin/staff_login.html', {'old_member': form})


def staff_dash(request):
    end_date = date.today()
    start_date = end_date + timedelta(days=-30)
    return render(request, 'signin/staff_dash.html',
                  {'active_users': Profile.objects.filter(last_active__range=[start_date, end_date]).count(),
                   'all_users': Profile.objects.all().count(),
                   'today_users': Attendance.objects.filter(date=timezone.now()).count(),
                   })


def new_member(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            username = profile.phone
            password = request.POST.get('zip_code', None)
            user, created = User.objects.get_or_create(username=username, email=profile.email)

            if created:
                user.set_password(password)
                user.save()

                profile.user = user
                profile.last_active = timezone.now()
                profile.save()

                attendance = Attendance(phone_number=username)
                attendance.full_clean()
                attendance.save()

                user = authenticate(username=username, password=password)
                login(request, user)
            return redirect('sign_in')
        return render(request, 'signin/new_member.html', {'profile_form': profile_form})
    else:
        profile_form = ProfileForm()
        return render(request, 'signin/new_member.html', {'profile_form': profile_form})


def view_all_users(request):
    table = ProfileTable(Profile.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'signin/staff_users.html', {'table': table})


def attendance(request):
    return render(request, 'signin/staff_attendance.html',
                  {'dates': Attendance.objects.values('date').annotate(count=Count('date'))})


def whos_here(request):
    table = HereTable(Profile.objects.filter(last_active=timezone.now()))
    RequestConfig(request).configure(table)
    return render(request, 'signin/staff_whos_here.html', {'table': table})


def email(request):
    return render(request, 'signin/staff_email.html')
