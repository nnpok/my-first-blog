from django.shortcuts import render
from .forms import AttendanceForm, ProfileForm
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from signin.models import Attendance


def sign_in(request):
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.date = timezone.now()
            username = attendance.phone_number
            attendance.save()

            user = User.objects.get(username=username)
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
    return render(request, 'signin/staff_dash.html')


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