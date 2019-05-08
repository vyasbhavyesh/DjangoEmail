from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import NameForm, ContactForm
from django.core.validators import validate_email

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


def thanks(request):
    return render(request, 'thanks.html')


def EmailTest(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        csv_file = request.FILES["csv_file"]
        file_data = csv_file.read().decode("utf-8")
        if form.is_valid():
            to = form.cleaned_data['To'].split(',')
            cc = form.cleaned_data['cc'].split(',')
            bcc = form.cleaned_data['bcc'].split(',')
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = ['vyasbhavyesh@gmail.com']

            print(to, cc,bcc, sender, subject, message,len(file_data))

            #send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()

    return render(request, 'name.html', {'form': form})