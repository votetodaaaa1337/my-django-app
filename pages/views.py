from django.shortcuts import render

def about_company(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

