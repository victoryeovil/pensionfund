from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField
from autoslug import AutoSlugField
from events.models import Event

# Create your models here.
CHOICES = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Internship', 'Internship'),
    ('Remote', 'Remote'),
)


class ApplicantProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, related_name='APPLICANT_profile')
    full_name = models.CharField(max_length=200, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    resume = models.FileField(upload_to='resumes', null=True, blank=True)
    grad_year = models.IntegerField(blank=True)
    looking_for = models.CharField(
        max_length=30, choices=CHOICES, default='Full Time', null=True)
    slug = AutoSlugField(populate_from='user', unique=True)

    def get_absolute_url(self):
        return "/applicant_profile/{}".format(self.slug)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username


choice = (
    ('ab', 'ab'),
    ('bc', 'bc')
)

golf = (
    ('as', 'as'),
    ('bv', 'bv')

)


class Application(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name='event_type', on_delete=models.CASCADE)
    fund_name = models.CharField(max_length=250)
    user_email = models.EmailField(max_length=250)
    principal_officer = models.CharField(max_length=250)
    principal_officer_email = models.EmailField(max_length=250)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    zapf_affiliation = models.BooleanField()
    booking_type = models.CharField(max_length=250, choices=choice, null=False)
    shirt_size = models.CharField(max_length=250, choices=golf)
    play_golf = models.BooleanField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username
