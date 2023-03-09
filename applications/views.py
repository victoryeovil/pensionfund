from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from events.models import *
from .models import *
from .forms import *


# Create your views here.
@login_required
def apply_job(request, slug):
    user = request.user
    job = get_object_or_404(Event, slug=slug)
    applied, created = AppliedJobs.objects.get_or_create(job=job, user=user)
    applicant, creation = Applicants.objects.get_or_create(
        job=job, applicant=user)
    return HttpResponseRedirect('/job/{}'.format(job.slug))


@login_required
def edit_profile(request):
    you = request.user
    profile = ApplicantProfile.objects.filter(user=you).first()
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = you
            data.save()
            return redirect('my-profile')
    else:
        form = ProfileUpdateForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'candidates/candidates/edit_profile.html', context)


@login_required
def edit_apply_event(request):
    if request.method == "POST":
        user = User.objects.get(user=request.user)
        application_form = EventApplicationForm(instance=user, data=request.POST)
        if application_form.is_valid():
            application_form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        address = User.objects.get(pk=id, user=request.user)
        address_form = EventApplicationForm(instance=address)
    return render(request, "account/dashboard/edit_addresses.html", {"form": address_form})



def apply_event(request):
    if request.method == "POST":
        event_form = EventApplicationForm(data=request.POST)
        if event_form.is_valid():
            event_form = event_form.save(commit=False)
            event_form.user = request.user
            event_form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        event_form = EventApplicationForm()
    return render(request, "application/edit_addresses.html", {"form": event_form})