from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.http import HttpResponse
import json
from .forms import WebURLForm
from django.views.decorators.csrf import csrf_exempt
from .models import WebURL,WordUnknown

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class WebURLFormView(TemplateView):
    template_name="go/index.html"

    def index(request):
        #form = WebURL.objects.all().values().order_by('-pub_date')[0]['weburl_text']
        form = WebURL.objects.all().values().order_by('-pub_date')[0]['weburl_text']
        print(form)
        context={'previousurl': form}
        if request.method == 'POST':
            form=WebURLForm(request.POST or None)
            print(request.POST)
            if form.is_valid():
                form.save()
            context={'form': form}
            #print(form)
            return render(request,'go/index.html',context)
        return render(request, "go/index.html", context)


    @csrf_exempt
    def FormToDB(request):
        if request.method == 'POST':
            form=WebURLForm(request.POST or None)
            print(request.POST)
            if form.is_valid():
                form.save()
            context={'form': form}
            #print(form)
            return render(request,'go/index.html',context)
class ShowExcelView(TemplateView):
    template_name="go/showExcel.html"

def MyView(request):
    ...
    query_results = WordUnknown.objects.all()
    ...
    #return a response to your template and add query_results to the context
