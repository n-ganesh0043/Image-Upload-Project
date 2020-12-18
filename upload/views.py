from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View
from .models import Imageupload
# Create your views here.

class image(View):
    def get(self,request):
        return render(request,"content.html")
    def post(self,request):
        nm=request.POST.get('image_nm')
        upim=request.FILES['file_up1']
        Imageupload(name=nm,img_upload=upim).save()
        messages.success(request,"PRODUCT SAVED SUCCESSFULLY!!!!!!!!!!")
        return redirect('image')

def gallery(request):
    upm=Imageupload.objects.all()
    return render(request,"gallery.html",{"data":upm})