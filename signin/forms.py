from django import forms
from .models import Profile, Attendance, User, phone_exists
from django.core.exceptions import ValidationError


class AttendanceForm(forms.ModelForm):

    class Meta:
        model = Attendance
        fields = ('phone_number',)


class StaffForm(forms.Form):
    phone_number = forms.IntegerField(max_value=10000000000, min_value=999999999,
                                      validators=[phone_exists])


def phone_exists(self):
    if not User.objects.filter(username=self).exists():
        raise ValidationError(
            'That phone number is not associated with a user.'
        )


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
