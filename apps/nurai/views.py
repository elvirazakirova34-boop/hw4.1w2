from django.shortcuts import render

def index(request):
    title = "Главная"
    description = "Это наш учебный проект на Django"
    return render(request, 'index.html', locals()) # locals() передает title и description

def contacts(request):
    title = "Наши контакты"
    phone = "+996 700 11 22 33"
    address = "г. Ош, ул. Ленина"
    return render(request, 'contacts.html', locals())