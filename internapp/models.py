from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.
    
class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    join_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.name

class User(models.Model):
    #a user may have one company
    company = models.ForeignKey(Company, blank=True, null=True)
    
    name = models.CharField(max_length=40)
    join_date = models.DateTimeField('date published')
    email = models.EmailField()
    type = models.IntegerField()
    #prefs go in another table
    
    def __unicode__(self):
        return self.name
    
class Job(models.Model):
    #a job has one company
    company = models.ForeignKey(Company)
    #a job can have many followers; a user can follow many jobs
    followers = models.ManyToManyField(User, blank=True, null=True, symmetrical=False)
    
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.title
        
class Rating(models.Model):
    #a rating belongs to a job
    job = models.ForeignKey(Job)
    #a rating also belongs to a user
    user = models.ForeignKey(User)
    company = models.ForeignKey(Company)
    overall = models.IntegerField()
    salary = models.IntegerField()
    hours = models.IntegerField()
    mentorship = models.IntegerField()
    culture = models.IntegerField()
    jobExperience = models.TextField()
    companyExperience = models.TextField()
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    
    def __unicode__(self):
        return self.jobExperience
    
class Preference(models.Model):
    #every specific preference has a user
    user = models.ForeignKey(User)
    type = models.CharField(max_length=50)
    intValue = models.IntegerField()
    stringValue = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.type
        
class RatingForm(ModelForm):
    class Meta:
        model = Rating
        exclude = ('job', 'company', 'user', 'upvotes', 'downvotes')
        widgets = {
        #'salary':forms.IntegerField(attrs={'class':'Slider', 'readonly':'true'})
        }