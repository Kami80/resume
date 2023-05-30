from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from django.http import HttpResponse
from django.conf import settings
from .models import TopPage, Experience, Education, Skills, Services, Tags, Portfolio, Reviews, Blogs
# Create your views here.

def page(request):

    top_page = TopPage.objects.last()
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    skills = Skills.objects.all()
    num = int(round(len(skills)/2 +0.1))
    skills_1 = skills[:num]
    skills_2 = skills[num:]
    services = Services.objects.all()
    tags = Tags.objects.all()
    portfolios = Portfolio.objects.all()
    reviews = Reviews.objects.all()
    blogs = Blogs.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            body = {
                'full_name': form.cleaned_data['full_name'],
                'subject': form.cleaned_data['subject'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(body['subject'], message, body['email'], [settings.EMAIL_HOST_USER], fail_silently=False) 
                messages.success(request, 'Your mail has successfully submitted!')
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            
            return redirect("page")


    form = ContactForm()
    context = {'top_page':top_page, 'experiences':experiences, 'educations':educations, 'skills_1':skills_1
                , 'skills_2':skills_2, 'services':services, 'tags':tags, 'portfolios':portfolios,
                 'form':form, 'reviews':reviews, 'blogs':blogs, 'skills':skills}
    return render(request, 'index.html', context)