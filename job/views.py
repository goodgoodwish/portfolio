from django.shortcuts import render, get_object_or_404
from .models import Job


# Create your views here.
def home(request):
    jobs = Job.objects.all()
    context = {"jobs": jobs}
    return render(request, "job/home.html", context)

def job(request, job_id):
    # job = Job.objects.get(id=job_id)
    job = get_object_or_404(Job, pk=job_id)
    context = {"job": job}
    return render(request, "job/job.html", context)
