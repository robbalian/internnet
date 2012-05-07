from django.template import Context, loader
from django.shortcuts import get_object_or_404, render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from internapp.models import Job, User, Rating, Company
from django.db.models import Avg

def index(request):
    job_list = Job.objects.all().order_by('title')
    return render_to_response('internapp/index.html', {'job_list': job_list})
    
def detail(request, job_id):
    p = get_object_or_404(Job, pk=job_id)
    overall = Rating.objects.filter(job_id=job_id).aggregate(Avg('overall'))
    salary = Rating.objects.filter(job_id=job_id).aggregate(Avg('salary'))
    hours = Rating.objects.filter(job_id=job_id).aggregate(Avg('hours'))
    mentorship = Rating.objects.filter(job_id=job_id).aggregate(Avg('mentorship'))
    culture = Rating.objects.filter(job_id=job_id).aggregate(Avg('culture'))
    
    return render_to_response('internapp/detail.html', {'job': p, 'overall': overall, 'salary': salary, 'hours': hours, 'mentorship': mentorship, 'culture': culture}, context_instance=RequestContext(request))

def company(request, company_id):
    p = get_object_or_404(Company, pk=company_id)
    job_list = Job.objects.filter(company_id=company_id).order_by('title')
    overall = Rating.objects.filter(company_id=company_id).aggregate(Avg('overall'))
    mentorship = Rating.objects.filter(company_id=company_id).aggregate(Avg('mentorship'))
    culture = Rating.objects.filter(company_id=company_id).aggregate(Avg('culture'))
    return render_to_response('internapp/company.html', {'company': p, 'job_list': job_list, 'overall': overall, 'mentorship': mentorship, 'culture': culture}, context_instance=RequestContext(request))
    
def vote(request, job_id):
    p = get_object_or_404(Job, pk=job_id)
    return render_to_response('internapp/vote.html', {'job': p})
    