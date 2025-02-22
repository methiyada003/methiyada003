from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def newbook(request):
    return render(request, 'main/newbook.html')

def popular(request):
    return render(request, 'main/popular.html')

def status_base(request):
    return render(request, 'status/status_base.html')

def study(request):
    return render(request, 'category/study.html')

def documentary(request):
    return render(request, 'category/documentary.html')

def language(request):
    return render(request, 'category/language.html')

def novel(request):
    return render(request, 'category/novel.html')

def lifestyle(request):
    return render(request, 'category/lifestyle.html')

def sports(request):
    return render(request, 'category/sports.html')

def health(request):
    return render(request, 'category/health.html')

def dharma(request):
    return render(request, 'category/dharma.html')

def entertainment(request):
    return render(request, 'category/entertainment.html')

def technology(request):
    return render(request, 'category/technology.html')

def law(request):
    return render(request, 'category/law.html')