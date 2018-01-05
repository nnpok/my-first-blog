# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-03 22:47
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10000000000), django.core.validators.MinValueValidator(999999999)])),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=70, null=True)),
                ('last_name', models.CharField(max_length=70, null=True)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Other'), ('x', 'Decline to state')], max_length=1)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.PositiveIntegerField(help_text='This will be your future login.', null=True, unique=True, validators=[django.core.validators.MaxValueValidator(10000000000), django.core.validators.MinValueValidator(999999999)])),
                ('preferred_contact_method', models.CharField(choices=[('email', 'Email'), ('phone', 'Phone'), ('none', 'Please do not contact me.')], max_length=5)),
                ('age', models.CharField(choices=[('0-18', '18 and under'), ('19-24', '19-24'), ('25-40', '25-40'), ('41-55', '41-55'), ('56-100', '56+')], max_length=6)),
                ('zip_code', models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100000), django.core.validators.MinValueValidator(9999)])),
                ('previous_experience', models.CharField(choices=[('y', 'Yes'), ('n', 'No')], help_text='Have you meditated before?', max_length=1)),
                ('occupation', models.CharField(blank=True, max_length=70, null=True)),
                ('ethnicity', models.CharField(blank=True, choices=[('white', 'White'), ('hispanic', 'Hispanic or Latino'), ('black', 'Black or African American'), ('native', 'Native American or American Indian'), ('asian', 'Asian or Pacific Islander'), ('other', 'Other')], max_length=8, null=True)),
                ('outreach', models.CharField(blank=True, choices=[('web', 'Website'), ('flyer', 'Flyer'), ('friend', 'Friend'), ('walk', 'Walked by'), ('other', 'Other')], help_text='How did you hear about us?', max_length=6, null=True)),
                ('user', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]