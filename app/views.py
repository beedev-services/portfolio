from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

# -------------------- Main Landing Pages

# ---------- Index Landing
def index(request):
    return render(request, 'index.html')

# ---------- Contact Landing
def contact(request):
    contact = Contact.objects.all().values()
    updated = Updated.objects.filter(updateType=4)
    context = {
        'contact': contact,
        'updated': updated,
    }
    print(updated)
    return render(request, 'contact.html', context)

# ---------- Resume Landing
def resume(request):
    skills = Skill.objects.order_by('skillName')
    ed = Education.objects.order_by('eOrder', 'school')
    work = Work.objects.order_by('wOrder', 'company')
    updated = Updated.objects.filter(updateType=3)
    context = {
        'skills': skills,
        'ed': ed,
        'work': work,
        'updated': updated,
    }
    return render(request, 'resume.html', context)

# ---------- Current Projects Landing
def current(request):
    currProj = CurrentProject.objects.order_by('cOrder')
    updated = Updated.objects.filter(updateType=0)
    context = {
        'currProj': currProj,
        'updated': updated,
    }
    # print(currProj)
    return render(request, 'main/current.html', context)

# ---------- Past Projects Landing
def past(request):
    pastProj = PastProject.objects.order_by('pOrder')
    updated = Updated.objects.filter(updateType=1)
    context = {
        'pastProj': pastProj,
        'updated': updated,
    }
    print(pastProj)
    return render(request, 'main/past.html', context)

# ---------- All Projects Landing
def allProjects(request):
    return render(request, 'allProjects.html')

# ---------- Front End Projects
def frontEnd(request):
    front = AllProjects.objects.filter(theType=0)
    updated = Updated.objects.filter(updateType=6)
    context = {
        'front': front,
        'updated': updated,
    }
    return render(request, 'allProjects/frontEnd.html', context)

# ---------- Back End Projects
def backEnd(request):
    back = AllProjects.objects.filter(theType=1)
    updated = Updated.objects.filter(updateType=7)
    context = {
        'back': back,
        'updated': updated,
    }
    return render(request, 'allProjects/backEnd.html', context)

# ---------- Full Stack Projects
def fullStack(request):
    full = AllProjects.objects.filter(theType=2)
    updated = Updated.objects.filter(updateType=2)
    context = {
        'full': full,
        'updated': updated,
    }
    return render(request, 'allProjects/fullStack.html', context)

# ---------- Organization Projects
def organization(request):
    org = AllProjects.objects.filter(theType=3)
    updated = Updated.objects.filter(updateType=5)
    context = {
        'org': org,
        'updated': updated,
    }
    return render(request, 'allProjects/organizations.html', context)

# ---------- Admin Landing
def mainAdmin(request):
    if "user_id" not in request.session:
        return render(request, 'admin/enter.html')
    else:
        return redirect('/24/dashboard/')

def mainReg(request):
    return render(request, 'admin/register.html')

def dashboard(request):
    if 'user_id' not in request.session:
        messages.error(request, 'Access Denied.  Please see Admin')
        return redirect('/notAuth/')
    else:
        # types = UPDATETYPE
        updated = Updated.objects.all().values()
        context = {
            'contact': Contact.objects.all().values(),
            'updated': Updated.objects.all().values(),
            'types': UPDATETYPE,
        }
        print("updates:", updated)
        return render(request, 'admin/dashboard.html', context)

def logout(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        request.session.clear()
        return redirect('/')

def notAuth(request):
    return render(request, 'notAuth.html')

def addProjects(request):
    if 'user_id' not in request.session:
        messages.error(request, 'Access Denied.  Please see Admin')
        return redirect('/notAuth/')
    else:
        current=CurrentProject.objects.order_by('cOrder')
        past=PastProject.objects.order_by('pOrder')
        cAll=AllProjects.objects.filter(theStatus=0)
        pAll=AllProjects.objects.filter(theStatus=1)
        context = {
            'status': STATUS,
            'type': TYPE,
            'current': current,
            'past': past,
            'cAll': cAll,
            'pAll': pAll,
        }
        return render(request, 'admin/addProj.html', context)

def addResume(request):
    if 'user_id' not in request.session:
        messages.error(request, 'Access Denied.  Please see Admin')
        return redirect('/notAuth/')
    else:
        return render(request, 'admin/addResume.html')


# -------------------- Create Routes


# ---------- Register Route
def register(request):
    if request.method == 'GET':
        return redirect('/24/24/')
    errors = User.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('/notAuth/')
    hashedPw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    newUser = User.objects.create(
        username = request.POST['username'],
        password = hashedPw
    )
    request.session['user_id'] = newUser.id
    return redirect('/24/dashboard/')

# ---------- Login Route
def login(request):
    user = User.objects.filter(username = request.POST['username'])
    if user:
        userLogin = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), userLogin.password.encode()):
            request.session['user_id'] = userLogin.id
            return redirect('/24/dashboard/')
        messages.error(request, 'Invalid Credentials')
        return redirect('/notAuth/')
    messages.error(request, 'That Username is not in our system, Please see Admin to gain access')
    return redirect('/notAuth/')

# ---------- Create Current Projects
def createCurr(request):
    CurrentProject.objects.create(
        currName=request.POST['currName'],
        currDesc=request.POST['currDesc'],
        currImg=request.POST['currImg'],
        currSource=request.POST['currSource'],
        currLink=request.POST['currLink'],
        cOrder=request.POST['cOrder'],
    )
    return redirect('/24/projects/')

# ---------- Create Past Projects
def createPast(request):
    PastProject.objects.create(
        pastName=request.POST['pastName'],
        pastDesc=request.POST['pastDesc'],
        pastImg=request.POST['pastImg'],
        pastSource=request.POST['pastSource'],
        pastLink=request.POST['pastLink'],
        pOrder=request.POST['pOrder'],
    )
    return redirect('/24/projects/')

# ---------- Create All Project
def createAllProj(request):
    AllProjects.objects.create(
        projName=request.POST['projName'],
        projDesc=request.POST['projDesc'],
        projSource=request.POST['projSource'],
        projLink=request.POST['projLink'],
        projOrg=request.POST['projOrg'],
        theType=request.POST['theType'],
        theStatus=request.POST['theStatus']
    )
    return redirect('/24/projects/')

# ---------- Create Skill
def createSkill(request):
    Skill.objects.create(
        skillName=request.POST['skillName'],
    )
    return redirect('/24/resume/')

# ---------- Create Work
def createWork(request):
    Work.objects.create(
        position=request.POST['position'],
        company=request.POST['company'],
        dates=request.POST['dates'],
        jobDesc01=request.POST['jobDesc01'],
        jobDesc02=request.POST['jobDesc02'],
        jobDesc03=request.POST['jobDesc03'],
        jobDesc04=request.POST['jobDesc04'],
        wOrder=request.POST['wOrder'],
    )
    return redirect('/24/resume/')

# ---------- Create Education
def createEd(request):
    Education.objects.create(
        school=request.POST['school'],
        gradDate=request.POST['gradDate'],
        course=request.POST['course'],
        eOrder=request.POST['eOrder'],
    )
    return redirect('/24/resume/')

# ---------- Created Updated
def createU(request):
    Updated.objects.create(
        whyUpdate=request.POST['whyUpdate'],
        updateType=request.POST['updateType'],
    )
    return redirect('/24/dashboard/')

# ---------- Created Contact
def createC(request):
    Contact.objects.create(
        email=request.POST['email'],
        linkedIn=request.POST['linkedIn'],
        github=request.POST['github'],
    )
    return redirect('/24/dashboard/')


# -------------------- Edit Routes

# ---------- edit Updated
def editU(request, updated_id):
    if 'user_id' not in request.session:
        messages.error(request, 'Access Denied.  Please see Admin')
        return redirect('/notAuth/')
    else:
        update = Updated.objects.get(id=updated_id)
        context = {
            'update': update,
            'types': UPDATETYPE,
        }
        return render(request, 'admin/edits/editUpdates.html', context)

def editAllProj(request, allprojects_id):
    if 'user_id' not in request.session:
        messages.error(request, 'Access Denied.  Please see Admin')
        return redirect('/notAuth/')
    else:
        proj = AllProjects.objects.get(id=allprojects_id)
        context = {
            'proj': proj,
            'status': STATUS,
            'type': TYPE,
        }
        return render(request, 'admin/edits/editAllProj.html', context)


# -------------------- Update Routes


# ---------- Update Updated
def updateU(request, updated_id):
    toUpdate = Updated.objects.get(id=updated_id)
    toUpdate.whyUpdate=request.POST['whyUpdate']
    toUpdate.updateType=request.POST['updateType']
    toUpdate.save()
    return redirect('/24/dashboard/')

def updateAllProj(request, allprojects_id):
    toUpdate = AllProjects.objects.get(id=allprojects_id)
    toUpdate.projName=request.POST['projName']
    toUpdate.projDesc=request.POST['projDesc']
    toUpdate.projSource=request.POST['projSource']
    toUpdate.projLink=request.POST['projLink']
    toUpdate.projOrg=request.POST['projOrg']
    toUpdate.theType=request.POST['theType']
    toUpdate.theStatus=request.POST['theStatus']
    toUpdate.save()
    return redirect('/24/projects/')
