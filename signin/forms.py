from django import forms
from .models import Profile, Attendance, User, phone_exists, unique_signin
from django.core.exceptions import ValidationError


class AttendanceForm(forms.ModelForm):

    class Meta:
        model = Attendance
        fields = ('phone_number',)


class StaffForm(forms.Form):
    phone_number = forms.CharField(max_length=10, validators=[phone_exists])


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('first_name',
                  'last_name',
                  'email',
                  'gender',
                  'phone',
                  'preferred_contact_method',
                  'age',
                  'zip_code',
                  'previous_experience',
                  'occupation',
                  'ethnicity',
                  'outreach',
                  )
