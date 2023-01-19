from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import contacts, subscriber, announcement
from .mail import mailall
from django.contrib import messages
import re, os
#from . import clie
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import threading
from subprocess import call


def home(request):
  suber = subscriber()
  announces = announcement.objects.all()
  if request.method == "POST":
    suber.username = request.POST.get('name')
    suber.email = request.POST.get('email')
    suber.phone = request.POST.get('phone')
    suber.address = request.POST.get('address')
    suber.city = request.POST.get('city')
    suber.country = request.POST.get('country')
    suber.postalcode = request.POST.get('postalcode')
    suber.save()
  return render(request, "home.html", {"announces": announces})
  
def about(request):
  suber = subscriber()
  if request.method == "POST":
    suber.username = request.POST.get('name')
    suber.email = request.POST.get('email')
    suber.phone = request.POST.get('phone')
    suber.address = request.POST.get('address')
    suber.city = request.POST.get('city')
    suber.country = request.POST.get('country')
    suber.postalcode = request.POST.get('postalcode')
    suber.save()
  return render(request, "about.html")
  
def service(request):
  suber = subscriber()
  if request.method == "POST":
    suber.username = request.POST.get('name')
    suber.email = request.POST.get('email')
    suber.phone = request.POST.get('phone')
    suber.address = request.POST.get('address')
    suber.city = request.POST.get('city')
    suber.country = request.POST.get('country')
    suber.postalcode = request.POST.get('postalcode')
    suber.save()
  return render(request, "service.html")
  
def price(request):
  suber = subscriber()
  if request.method == "POST":
    suber.username = request.POST.get('name')
    suber.email = request.POST.get('email')
    suber.phone = request.POST.get('phone')
    suber.address = request.POST.get('address')
    suber.city = request.POST.get('city')
    suber.country = request.POST.get('country')
    suber.postalcode = request.POST.get('postalcode')
    suber.save()
  return render(request, "price.html")
  
def team(request):
  suber = subscriber()
  if request.method == "POST":
    suber.username = request.POST.get('name')
    suber.email = request.POST.get('email')
    suber.phone_num = request.POST.get('phone')
    suber.address = request.POST.get('address')
    suber.city = request.POST.get('city')
    suber.country = request.POST.get('country')
    suber.postalcode = request.POST.get('postalcode')
    suber.save()
  return render(request, "team.html")

def contact(request):
  contact_form = contacts()
  if "Name" in request.POST:
    contact_form.username = request.POST.get("Name")
    contact_form.email = request.POST.get("Email")
    contact_form.phone = request.POST.get("Phone")
    contact_form.message = request.POST.get("Message")
    contact_form.save()
    return redirect("/contact")
    
  return render(request, "contact.html")
  
@login_required(login_url="/admin/")
def sendmail(request):
  sub = subscriber.objects.all()
  announce = announcement()
  if request.method == "POST":
    subject = request.POST.get("subject")
    msg = request.POST.get("msg")
    announce.subject = subject
    announce.message = msg
    announce.save()
    
    origmsg = ""
    for k in msg.split("."):
      if k != "":
        origmsg += f"<p>{k}.</p>\n"
    num = 0
    for i in sub:
      mailall(request, subject, i.username, origmsg, i.email)
      num += 1
    if num != 0:
      print("yes")
      messages.success(request, "Email sent successfully!")
      return redirect("/sendmail/")
    else:
      print("no")
      messages.error(request, "There is no subscriber to send!")
      return redirect("/sendmail/")
  return render(request, "mail.html")
 