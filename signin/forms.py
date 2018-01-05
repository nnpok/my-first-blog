from django import forms
from .models import Profile, Attendance


class AttendanceForm(forms.ModelForm):

    class Meta:
        model = Attendance
        fields = ('phone_number',)


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
