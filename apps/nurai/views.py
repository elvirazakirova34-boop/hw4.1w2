from django.shortcuts import render

# Create your views here.
def index(request):
    title = "Главная страница"
    main_header = "Добро пожаловать!"
    return render(request, 'index.html', locals())

def contacts(request):
    phone = "+996 700 123 456"
    address = "г. Бишкек, ул. Ибраимова 115"
    return render(request, 'contacts.html', locals())