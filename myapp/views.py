from django.shortcuts import render
from django.http import HttpResponse
from .ultils import autoLike
from .models import FacebookUser
# Create your views 
def index_view(request):
    if request.method == 'GET':
        users = FacebookUser.objects.all()
        context = {
            'users': users
        }
        return render(request,'index.html',context)
    if request.method == 'POST':
        so1 = request.POST['so1']
        so2 = request.POST['so2']
        so3= int(so1) + int(so2)

        context = {
            'ketqua': so3
        }

        return render(request,'index.html',context)

def auto_like(request):
    autoLike()
    return HttpResponse("da like")

# def tingtong(request):
#     if request.mothod == 'GET':
#         return render(request,'index.html')
#     if request.method == 'POST':
#         so1 = request.POST['so1']
#         so2 = request.POST['so2']
#         so3= int(so1) + int(so2)
#         context = {
#             'ketqua': so3
#         }
#         return render(request,'index.html',context)

