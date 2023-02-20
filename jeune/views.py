from django.shortcuts import render, redirect
from jeune.models import subscribers
import datetime
from jeune.forms import SubscribersForm, MailMessageForm
from django.contrib import messages
from django.core.mail import send_mail
from django_pandas.io import read_frame
from django.db.models import Q
# Create your views here.


def dashboard(request):
    today = datetime.date.today()
    year = today.year
    month = today.month
    getAllOfThem = subscribers.objects.all()
    email_count = subscribers.objects.all().count()
    new_email_this_month_count = subscribers.objects.filter(created_at__year=year, created_at__month=month).count()
    unsubscribed_email_count = subscribers.objects.exclude(status="True").count()
    return render(request, 'jeune/dashbord.html', {'getAllOfThem':getAllOfThem, 
    'email_count':email_count, 'new_email_this_month_count':new_email_this_month_count, 
    'unsubscribed_email_count':unsubscribed_email_count})

def welcome(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if subscribers.objects.filter(Q(email=instance.email)).exists() and subscribers.objects.filter(Q(status=True)):
                messages.warning(request, 'Subscriber already exist!')
                return redirect('/unsubscribe')
            form.save()
            messages.success(request, 'User successfully subscribed')
            return redirect('/welcome')
    else:
        form = SubscribersForm()
    context = {
       'form': form,
    }
    return render(request, "jeune/welcome.html", context)

def emails(request):
    emails = subscribers.objects.exclude(status=False)
    df = read_frame(emails, fieldnames=['email'])
    mail_list = df['email'].values.tolist()
    # print(mail_list)

    if request.method == 'POST':
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()

            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            send_mail(
            title,
            message,
            '',
            mail_list,
            fail_silently=False,
            )

            messages.success(request, 'Message has been sent to the mail list')
            return redirect('/welcome')
    else:
        form = MailMessageForm()
        context = {
            'form': form,
        }
    return render(request, "jeune/emails.html", context)

def unsubscribe(request):
    form = SubscribersForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        subscribers.objects.filter(email=instance.email).update(status = False)
        if  subscribers.objects.filter(email=instance.email).exists():
            messages.success(request, 'User has been unsubscribed successfully!')
            return redirect('/unsubscribe')
        else:
            messages.success(request, 'Sorry, we did not find your email!')
            return redirect('/unsubscribe')
    context = {
    "form" : form,
    }
    return render(request, "jeune/unsubscribe.html", context)

# Code to print the lists of all the time zones
# import pytz

# print('Timezones')
# for timeZone in pytz.all_timezones:
#     print(timeZone)