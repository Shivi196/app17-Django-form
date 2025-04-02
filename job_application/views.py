from django.shortcuts import render
from .forms import ApplicationForms
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

# Create your views here.

def index(request):
    if request.method == "POST":

        form = ApplicationForms(request.POST)
        if form.is_valid():

            # Getting user input with help of Application form class specified in forms.py
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            # Insert form data into the database
            Form.objects.create(first_name=first_name,last_name=last_name,email=email,date=date,occupation=occupation)

            # Create email content and sending mail
            message_body = f"Your details submitted successfully.. Thank you!! {first_name}"
            email_message = EmailMessage(subject="Form Submission Confirmation!!",body=message_body,to=[email])
            email_message.send()

            # Flash message post sending mail and submit button clicked
            messages.success(request,"Your Form Submitted successfully!!")

    return render(request,"index.html")