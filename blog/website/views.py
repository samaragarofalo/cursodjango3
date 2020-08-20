from django.shortcuts import render


# Create your views here.

def hello_blog(request):
    lista = [
        'Django','Python','Git','Html','Banco de dados','Linux',
        'Ngix','Uwsgi','Systemctl'
    ]
    data = {'name':'Curso de Django 3','lista_tecnologia': lista}
    return render(request,'index.html',data)


