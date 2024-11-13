from django.http import HttpResponse
from django.shortcuts import render
from websites.models import WebsiteModule
from websites.models import WesiteNewModule,ContactForm


def index(request):
    serWebsiteModule = WebsiteModule.objects.all().order_by('-title_entry')
    myWebsiteModule = WesiteNewModule.objects.all()
    data = {
        'serWebsiteModule': serWebsiteModule,
        'myWebsiteModule': myWebsiteModule
    }

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        date = request.POST.get('date')
        department = request.POST.get('department')
        comments = request.POST.get('comments')

        alldata = ContactForm(
        first_name=first_name,
        email=email,
        phone=phone,
        gender=gender,
        date=date,
        department=department,
        comments=comments
    )
        alldata.save()
        msg = "Data Inserted"
        return render(request, 'index.html', {'data': data, 'msg': msg})
    else:
        return render(request, 'index.html', data)