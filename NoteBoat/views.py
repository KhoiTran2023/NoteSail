from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from .models import *
import random, datetime
# Create your views here.

quotes = ["Be inspiring.", "You can do anything.", "Having a good day?", "Only you can seize the day.", "Find yourself."]

def intro_view(request):
	return render(request, "index/intro.html", {"message": None})

def home_view(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("signin"))
	quote = random.choice(quotes)
	user = request.user
	data = Userdata.objects.get(username = user)
	pinned = data.pinned
	documents = data.docs.all()
	context = {
		"pinned":pinned,
		"user":user,
		"quote":quote,
		"documents":documents,
	}
	return render(request, "landings/home.html", context)

def signin_view(request):
	return render(request, "index/signin.html", {"message": None})

def signin(request):
	username = request.POST["identification"]
	password = request.POST["password"]
	user = authenticate(request, username = username, password = password)
	if user is not None:
		login(request, user)
		return HttpResponseRedirect(reverse("noteboat"))
	else:
		return render(request, "index/signin.html", {"message": "Your username/password was incorrect."})

def register_view(request):
	a = random.randint(100000,999999)
	return render(request, "index/register.html", {"message": a})

def register(request):
	email = request.POST["email"]
	username = request.POST["username"]
	password = request.POST["password"]
	fname = request.POST["fname"]
	rcode = request.POST["rcode"]
	security = request.POST["security"]
	user = User.objects.create_user(username,email,password)
	user.first_name = fname
	user.save()
	f = Userdata(username = username, email = email, rcode = rcode, security = security, fname = fname)
	f.save()
	context = {
		"success":"User successfully created. Log in to continue."
	}
	return render(request, "index/signin.html", context)

def logout_view(request):
	logout(request)
	context = {
	"success":"User successfully signed out."
	}
	return render(request, "index/signin.html", context)

def recover_view(request):
	return render(request, "index/recover.html", {"message": None})

def recover(request):
	fname = request.POST["fname"]
	email = request.POST["email"]
	rcode = int(request.POST["rcode"])
	security = request.POST["security"]
	user = Userdata.objects.get(email = email, fname = fname)
	if user.fname == fname and user.email == email and user.rcode == rcode and user.security == security:
		request.session['pp_redarekt'] = True
		return render(request, "landings/recover2.html", {"user": email})
	return render(request, "index/recover.html", {"message": "One of your credentials were incorrect. Please try again."})

def recover_view2(request):
	if 'pp_redarekt' in request.session:
		del request.session['pp_redarekt']
		return render(request, "landings/recover2.html", {"message": "Great! Enter your new password."})
	raise Http404

def recover_view3(request):
	npass = request.POST["password"]
	email = request.POST["email"]
	user = User.objects.get(email = email)
	user.set_password(npass)
	user.save()
	return render(request, "landings/recover3.html", {"message":None})

def contact_view(request):
	return render(request, "landings/contact.html", {"message":None})

def privacy_view(request):
	return render(request, "landings/privpol.html", {"message":None})

def termsco_view(request):
	return render(request, "landings/termsco.html", {"message":None})

def feedback_view(request):
	current = datetime.datetime.now()
	return render(request, "landings/feedback.html", {"message":None})

def feedback(request):
	name = request.POST["name"]
	feedback = request.POST["feedback"]
	datetime = request.POST["datetime"]
	f = Feedback(name = name, comment = feedback, datetime = datetime)
	f.save()
	return render(request, "landings/feedback.html", {"message": "Feedback sent. Thank you for helping us improve!"})

def aboutus_view(request):
	return render(request, "landings/about.html", {"message":None})

def document(request):
	docname = request.POST["document"]
	doc = Documents.objects.filter(docname = docname).first()
	context = {
		"document":doc
	}
	return render(request, "landings/document.html", context)

def create(request):
	docname = request.POST["createname"]
	f = Documents(docname = docname)
	f.save()
	u = request.user
	user = Userdata.objects.get(username = u)
	user.docs.add(f)
	return HttpResponseRedirect(reverse("noteboat"))

def searchdoc(request):
	docsearch = request.POST["search"]
	u = request.user
	user = Userdata.objects.get(username = u)
	docs = user.docs.filter(docname__contains = docsearch)
	quote = random.choice(quotes)
	pinned = user.pinned
	context = {
		"pinned":pinned,
		"user":user,
		"quote":quote,
		"documents":docs,
	}
	return render(request, "landings/home.html", context)

def pindoc(request):
	namepin = request.POST["pinname"]
	u = request.user
	user = Userdata.objects.get(username = u)
	user.pinned = namepin
	user.save()
	return HttpResponseRedirect(reverse("noteboat"))

def delete(request):
	namedelete = request.POST["deletename"]
	u = request.user
	user = Userdata.objects.get(username = u)
	doc = user.docs.filter(docname = namedelete).first().delete()
	return HttpResponseRedirect(reverse("noteboat"))

def rename(request):
	newname = request.POST["newname"]
	oldname = request.POST["oldname"]
	doc = Documents.objects.filter(docname=oldname).first()
	doc.docname = newname
	doc.save()
	doc = Documents.objects.filter(docname = newname).first()
	context = {
		"document":doc
	}
	return render(request, "landings/document.html", context)

def save_doc(request):
	docname = request.POST["oldname"]
	text = request.POST["text-input"]
	doc = Documents.objects.filter(docname = docname).first()
	doc.text = text
	doc.save()
	context = {
		"document":doc
	}
	return render(request, "landings/document.html", context)