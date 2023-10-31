from django.shortcuts import render
from .models import Articles
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def home_view(request):
    return render(request, 'home.html')

def list_articles(request):
    articles = Articles.objects.all()
    return render(request, 'list_articles.html', {'articles': articles})

def article_detail(request, article_slug):
    article = get_object_or_404(Articles, slug=article_slug)
    return render(request, 'article_detail.html', {'article': article})

def contact(request):
    success_msg = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            message += "\n\nMessage sent by: " + name
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                ['enesbarut99@gmail.com'],
                fail_silently=False,
            )
            success_msg = "Merci ! Votre message a bien été envoyé."
            form = ContactForm()  # Reset the form on success
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form, 'success_msg': success_msg})
