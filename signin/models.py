from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.core.exceptions import ValidationError


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, default=None)
    first_name = models.CharField(max_length=70, null=True)
    last_name = models.CharField(max_length=70, null=True)
    MALE = 'm'
    FEMALE = 'f'
    OTHER = 'o'
    DECLINE_TO_STATE = 'x'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
        (DECLINE_TO_STATE, 'Decline to state'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False)
    email = models.EmailField(max_length=254, null=True)
    phone = models.PositiveIntegerField(validators=[MaxValueValidator(10000000000),
                                                    MinValueValidator(999999999)],
                                        blank=False, unique=True,
                                        help_text="This will be your future login.",
                                        null=True)
    EMAIL = 'email'
    PHONE = 'phone'
    NONE = 'none'
    CONTACT_CHOICES = (
        (EMAIL, 'Email'),
        (PHONE, 'Phone'),
        (NONE, 'Please do not contact me.')

    )
    preferred_contact_method = models.CharField(choices=CONTACT_CHOICES,
                                                max_length=5, blank=False)
    OO0_18 = '0-18'
    OO19_24 = '19-24'
    OO25_40 = '25-40'
    OO41_55 = '41-55'
    OO56_100 = '56-100'
    AGE_CHOICES = (
        (OO0_18, '18 and under'),
        (OO19_24, '19-24'),
        (OO25_40, '25-40'),
        (OO41_55, '41-55'),
        (OO56_100, '56+'),
    )
    age = models.CharField(choices=AGE_CHOICES, max_length=6, blank=False)
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(100000),
                                                       MinValueValidator(9999)],
                                           blank=False,
                                           null=True)
    YES = 'y'
    NO = 'n'
    BOOLEAN_CHOICES = (
        (YES, 'Yes'),
        (NO, 'No')
    )
    previous_experience = models.CharField(choices=BOOLEAN_CHOICES, blank=False,
                                           verbose_name="Have you meditated before?",
                                           max_length=1)

    occupation = models.CharField(max_length=70, blank=True, null=True)
    WHITE = 'white'
    HISPANIC = 'hispanic'
    BLACK = 'black'
    NATIVE = 'native'
    ASIAN = 'asian'
    OTHER = 'other'
    ETHNICITY_CHOICES = (
        (WHITE, 'White'),
        (HISPANIC, 'Hispanic or Latino'),
        (BLACK, 'Black or African American'),
        (NATIVE, 'Native American or American Indian'),
        (ASIAN, 'Asian or Pacific Islander'),
        (OTHER, 'Other')
    )
    ethnicity = models.CharField(choices=ETHNICITY_CHOICES, blank=True, null=True,
                                 max_length=8)
    WEB = 'web'
    FLYER = 'flyer'
    FRIEND = 'friend'
    WALKED_BY = 'walk'
    MARKETING_CHOICES = (
        (WEB, 'Website'),
        (FLYER, 'Flyer'),
        (FRIEND, 'Friend'),
        (WALKED_BY, 'Walked by'),
        (OTHER, 'Other')
    )
    outreach = models.CharField(choices=MARKETING_CHOICES,
                                blank=True, null=True,
                                verbose_name="How did you hear about us?",
                                max_length=6)
    staff = models.BooleanField(default=False)
    last_active = models.DateField(default=timezone.now)
    objects = models.Manager()


def phone_exists(phone):
    if not User.objects.filter(username=phone).exists():
        raise ValidationError(
            'That phone number is not associated with a user.'
        )


def unique_signin(phone):
    if Attendance.objects.filter(phone_number=phone, date=timezone.now()).exists():
        raise ValidationError(
            'You have already signed in today.'
        )


class Attendance(models.Model):
    phone_number = models.PositiveIntegerField(validators=[MaxValueValidator(10000000000),
                                                           MinValueValidator(999999999),
                                                           phone_exists,
                                                           unique_signin])
    date = models.DateField(default=timezone.now)
    objects = models.Manager()


# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()
