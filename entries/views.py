from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def index(request):
    entries = Entry.objects.order_by('-date_posted')
    ##Entry.objects.all().delete()  ## UnComment this to flush the database
    context = {'entries' : entries}
    return render(request,'entries/index.html',context)

def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('index')
    else:
        form = EntryForm()
    context = { 'form' : form }
    return render(request,'entries/add.html',context)



def sendReport(request):
    LastInsertedData = Entry.objects.all().last()
    subject = LastInsertedData.title
    message = LastInsertedData.text+' \n \n \nBY- '+LastInsertedData.author
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['mahesh.chahar@gmail.com','pandeyroshanjuet@gmail.com']
    send_mail( subject, message, email_from, recipient_list )
    entries = Entry.objects.order_by('-date_posted')
    context = { 'entries' : entries}
    return render(request,'entries/index.html',context)
