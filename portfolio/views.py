from .models import Experience, Education, Company, Recipe
from .forms import ContactForm

from django.contrib import messages
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import get_object_or_404, render, redirect


def index_view(request):
    return render(request, 'index.html', {})

def experience_view(request):
    experiences = list(Experience.objects.all())
    return render(request, 'experience.html', {'list': experiences})

def education_view(request):
    educations = list(Education.objects.all())
    return render(request, 'education.html', {'list': educations})

def more_view(request):
    return render(request, 'more.html', {})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            name = request.POST.get('your_name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            template = get_template('contact_template.txt')
            context = Context({
                'from': name,
                'email': email,
                'message': message, 
            })
            content = template.render(context)
            email = EmailMessage(
                'New contact form submission',
                content,
                'porfolio website',
                ['laurencapelluto@gmail.com'],
                headers = {'Reply-To': email }
            )
            email.send()
            messages.success(request, 'Email sent successfully.')
            return render(request, 'index.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def recipes_index(request):
    recipes = list(Recipe.objects.all())
    return render(request, 'recipes.html', {'recipes': recipes})