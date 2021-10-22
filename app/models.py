from django.db import models

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

class PastProject(models.Model):
    pastName = models.CharField(max_length=255)
    pastDesc = models.CharField(max_length=255)
    pastImg = models.CharField(max_length=255)
    pastSource = models.CharField(max_length=255, blank=True)
    pastLink = models.CharField(max_length=255, blank=True)

class Skill(models.Model):
    skillName = models.CharField(max_length=50, unique=True)

class Work(models.Model):
    position = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    dates = models.CharField(max_length=255)
    jobDesc = models.TextField()

class Education(models.Model):
    school = models.CharField(max_length=255)
    gradDate = models.CharField(max_length=50)
    course = models.CharField(max_length=255)

class UpdateType(models.Model):
    typeUpdate = models.CharField(max_length=255)

class Updated(models.Model):
    whyUpdate = models.CharField(max_length=255)
    updatedType = models.ForeignKey(UpdateType, related_name='updates', on_delete=models.CASCADE)
    updatedAt = models.DateField(auto_now=True)

class ProjectType(models.Model):
    projType = models.CharField(max_length=255)

class ProjectStatus(models.Model):
    projStatus = models.CharField(max_length=255)

class AllProjects(models.Model):
    projName = models.CharField(max_length=255)
    projDesc = models.CharField(max_length=255, blank=True)
    projSource = models.CharField(max_length=255, blank=True)
    projLink = models.CharField(max_length=255, blank=True)
    projOrg = models.CharField(max_length=255, blank=True)
    theType = models.ForeignKey(ProjectType, related_name='projTypes', on_delete=models.CASCADE)
    theStatus = models.ForeignKey(ProjectStatus, related_name='projStat', on_delete=models.CASCADE)
