from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('contact/', views.contact),
    path('resume/', views.resume),
    path('currentProjects/', views.current),
    path('pastProjects/', views.past),
    path('logout/', views.logout),
    path('notAuth/', views.notAuth),
    path('24/', views.mainAdmin),
    path('24/24/', views.mainReg),
    path('24/login/', views.login),
    path('24/register/', views.register),
    path('24/dashboard/', views.dashboard),
    path('24/createContact/', views.createContact),
    path('24/createUpdated/', views.createUpdated),
    path('24/<int:updated_id>/editU/', views.editU),
    path('24/<int:updated_id>/updateU/', views.updateU),
    path('24/createCurr/', views.createCurr),
    path('24/createPast/', views.createPast),
    path('24/createAllProj/', views.createAllProj),
    path('24/createSkill/', views.createSkill),
    path('24/createWork/', views.createWork),
    path('24/createEd/', views.createEd),
    path('24/resume/', views.addResume),
    path('24/projects/', views.addProjects),
    path('allProjects/', views.allProjects),
    path('allProjects/frontEnd/', views.frontEnd),
    path('allProjects/backEnd/', views.backEnd),
    path('allProjects/fullStack/', views.fullStack),
    path('allProjects/organization/', views.organization),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)