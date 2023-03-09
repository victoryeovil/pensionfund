from django import forms
from django.contrib.auth.models import User
from django.http import request

from .models import ApplicantProfile, Application, CHOICES, golf, choice


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ApplicantProfile
        fields = ['full_name', 'country', 'location',
                  'resume', 'grad_year', 'looking_for']


class EventApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['event', 'fund_name', 'user_email', 'principal_officer', 'principal_officer_email',
                  'address', 'phone', 'zapf_affiliation', 'booking_type', 'shirt_size', 'play_golf'
                  ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['event'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Event'})
        self.fields['fund_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Fund Name'})
        self.fields['user_email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['principal_officer'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Principal Officer'})
        self.fields['principal_officer_email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Principal officer email'})
        self.fields['address'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Address'})
        self.fields['phone'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'phone number'})
        self.fields['zapf_affiliation'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'ZAPF Affiliation'})
        self.fields['booking_type'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'SELECT BOOKING'})
        self.fields['shirt_size'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'SELECT Shirt Size'})
        self.fields['play_golf'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Play Golf?'})
