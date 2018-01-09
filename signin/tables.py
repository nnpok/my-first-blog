import django_tables2 as tables
from .models import Profile

class ProfileTable(tables.Table):
    class Meta:
        model = Profile
        exclude = ('user', 'id')
        template = 'django_tables2/bootstrap.html'


class HereTable(tables.Table):
    class Meta:
        model = Profile
        exclude = ('user', 'id', 'email', 'phone',
                   'preferred_contact_method', 'zip_code',
                   'outreach', 'last_active')
        template = 'django_tables2/bootstrap.html'
