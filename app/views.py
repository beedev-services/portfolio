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
    updated = Updated.objects.all().values()
    context = {
        'contact': contact,
        'updated': updated,
    }
    print(updated)
    return render(request, 'contact.html', context)

# ---------- Resume Landing
def resume(request):
    return render(request, 'resume.html')

# ---------- Current Projects Landing
def current(request):
    currProj = CurrentProject.objects.all().values()
    updated = Updated.objects.all().values()
    context = {
        'currProj': currProj,
        'updated': updated,
    }
    # print(currProj)
    return render(request, 'main/current.html', context)

# ---------- Past Projects Landing
def past(request):
    pastProj = PastProject.objects.all().values()
    context = {
        'pastProj': pastProj,
    }
    print(pastProj)
    return render(request, 'main/past.html', context)

# ---------- All Projects Landing
def allProjects(request):
    return render(request, 'allProjects.html')

# ---------- Front End Projects
def frontEnd(request):
    return render(request, 'allProjects/frontEnd.html')

# ---------- Back End Projects
def backEnd(request):
    return render(request, 'allProjects/backEnd.html')

# ---------- Full Stack Projects
def fullStack(request):
    return render(request, 'allProjects/fullStack.html')

# ---------- Organization Projects
def organization(request):
    return render(request, 'allProjects/organizations.html')

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
        types = UPDATETYPE
        context = {
            'contact': Contact.objects.all().values(),
            'updated': Updated.objects.all().values(),
            'types': UPDATETYPE,
        }
        print(types)
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
        return render(request, 'admin/addProj.html')

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

# ---------- Create Project Type

# ---------- Create Current Projects

# ---------- Create Past Projects

# ---------- Create Skill

# ---------- Create Work

# ---------- Create Education


# ---------- Created Updated
def createUpdated(request):
    Updated.objects.create(
        whyUpdate=request.POST['whyUpdate'],
        updateType_id=request.POST['updateType'],
    )
    return redirect('/24/dashboard/')

# ---------- Created Contact
def createContact(request):
    Contact.objects.create(
        email=request.POST['email'],
        linkedIn=request.POST['linkedIn'],
        github=request.POST['github'],
    )
    return redirect('/24/dashboard/')


# -------------------- Update Routes


# ---------- Update Project Type

# ---------- Update Current Projects

# ---------- Update Past Projects

# ---------- Update Skill

# ---------- Update Work

# ---------- Update Education

# ---------- Update Update Type

# ---------- Update Updated


# -------------------- Delete Routes


# ---------- Delete Project Type

# ---------- Delete Current Projects

# ---------- Delete Past Projects

# ---------- Delete Skill

# ---------- Delete Work

# ---------- Delete Education

# ---------- Delete Update Type

# ---------- Delete Updated