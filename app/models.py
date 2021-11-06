from django.db import models

STATUS = [
    {"id": 0, "status": "Current"},
    {"id": 1, "status": "Past"}
]
TYPE = [
    {"id": 0, "type": "Front End"},
    {"id": 1, "type": "Back End"},
    {"id": 2, "type": "Full Stack"},
    {"id": 3, "type": "Organization"}
]
UPDATETYPE = [
    {"id": 0, "updateType": "Current"},
    {"id": 1, "updateType": "Past"},
    {"id": 2, "updateType": "All"},
    {"id": 3, "updateType": "Resume"},
    {"id": 4, "updateType": "Contact"}
]

class UserManager(models.Manager):
    def validate(self, form):
        errors = {}

        usernameCheck = self.filter(username=form['username'])
        if usernameCheck:
            errors['username'] ='Sorry that username has been taken please chose a different one'

        if len(form['password']) < 5:
            errors['password'] = 'Password must be at least 5 characters long'
        
        if form['password'] != form['confirm']:
            errors['password'] = 'Password do not match'

        return errors

class User(models.Model):
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    objects = UserManager()

class Contact(models.Model):
    email = models.CharField(max_length=100)
    linkedIn = models.CharField(max_length=255)
    github = models.CharField(max_length=255)

class CurrentProject(models.Model):
    currName = models.CharField(max_length=255)
    currDesc = models.CharField(max_length=255)
    currImg = models.CharField(max_length=255)
    currSource = models.CharField(max_length=255, blank=True)
    currLink = models.CharField(max_length=255, blank=True)
    cOrder = models.IntegerField()

class PastProject(models.Model):
    pastName = models.CharField(max_length=255)
    pastDesc = models.CharField(max_length=255)
    pastImg = models.CharField(max_length=255)
    pastSource = models.CharField(max_length=255, blank=True)
    pastLink = models.CharField(max_length=255, blank=True)
    pOrder = models.IntegerField()

class Skill(models.Model):
    skillName = models.CharField(max_length=50, unique=True)

class Work(models.Model):
    position = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    dates = models.CharField(max_length=255)
    jobDesc01 = models.CharField(max_length=100)
    jobDesc02 = models.CharField(max_length=100, blank=True)
    jobDesc03 = models.CharField(max_length=100, blank=True)
    jobDesc04 = models.CharField(max_length=100, blank=True)
    wOrder = models.IntegerField()

class Education(models.Model):
    school = models.CharField(max_length=255)
    gradDate = models.CharField(max_length=50)
    course = models.CharField(max_length=255)
    eOrder = models.IntegerField()

class Updated(models.Model):
    whyUpdate = models.CharField(max_length=255)
    updateType = models.IntegerField(choices=UPDATETYPE, default=0)
    updatedAt = models.DateField(auto_now=True)

class AllProjects(models.Model):
    projName = models.CharField(max_length=255)
    projDesc = models.CharField(max_length=255, blank=True)
    projSource = models.CharField(max_length=255, blank=True)
    projLink = models.CharField(max_length=255, blank=True)
    projOrg = models.CharField(max_length=255, blank=True)
    theType = models.IntegerField(choices=TYPE, default=0)
    theStatus = models.IntegerField(choices=STATUS, default=0)
