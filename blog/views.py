from django.shortcuts import render


# Introduction page details
def Index(request):
    template_name = 'index.html'
    return render(request, template_name)


# Homepage details
def Home(request):
    template_name = 'home.html'
    return render(request, template_name)


# Portfolio page 1 details
def Portfolio_1(request):
    template_name = 'portfolio.html'
    return render(request, template_name)
