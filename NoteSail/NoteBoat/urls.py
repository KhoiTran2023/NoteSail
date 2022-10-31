from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.intro_view, name = "index"),
    path('noteboat/authenticate/signin', views.signin_view, name = "signin"),
    path('noteboat/authenticate/signin=true', views.signin, name = "signintry"),
    path('noteboat/authenticate/register', views.register_view, name = "register"),
    path('noteboat/authenticate/register=true', views.register, name = "registertry"),
    path('noteboat/authenticate/logout=true', views.logout_view, name = "logout"),
    path('noteboat/authenticate/recover', views.recover_view, name = "recover"),
    path('noteboat/authenticate/recover=true', views.recover, name = "recovertry"),
    path('noteboat/authenticate/recover/50/100', views.recover_view2, name = "recovertwo"),
    path('noteboat/authenticate/recover/100/100', views.recover_view3, name = "recoverthree"),
    path('noteboat/dashboard', views.home_view, name = "noteboat"),
    path('contact', views.contact_view, name = "contact"),
    path('privacy', views.privacy_view, name = "privacy"),
    path('terms&conditions', views.termsco_view, name = "termsco"),
    path('contact/feedback', views.feedback_view, name = "feedbak"),
    path('contact/feedback=true', views.feedback, name = "feedbacktry"),
    path('aboutus', views.aboutus_view, name = "aboutus"),
    path('document', views.document, name = "document"),
    path('createdoc', views.create, name = "createdoc"),
    path('noteboat/dashboard/searchdoc', views.searchdoc, name = "searchdoc"),
    path('noteboat/dashboard/pin', views.pindoc, name = "pindoc"),
    path('noteboat/dashboard/delete', views.delete, name = "delete"),
    path('document/rename', views.rename, name = "rename"),
    path('document/save', views.save_doc, name = "save"),
]