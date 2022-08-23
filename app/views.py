from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def base(request):
    return render(request, 'base.html')


def services(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')


def main(request):
    return render(request, 'main.html')


def blog_details(request):
    return render(request, 'blog_details.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')


def portfolio(request):
    return render(request, 'portfolio.html')
