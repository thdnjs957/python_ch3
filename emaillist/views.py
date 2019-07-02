from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from emaillist.models import Emaillist


def index(request):
    emaillist = Emaillist.objects.all().order_by('-id')
    data = {'emaillist': emaillist}

    for t in emaillist:
        print(t)

    return render(request, 'emaillist/index.html', data)  # template 쪽으로 data 보내기

def form(request):
    return render(request, 'emaillist/form.html')

def add(request):

    # DB와 연결된 애가 아님 막 생성됨
    emaillist = Emaillist()

    # parameter 뽑는거 and setAttribute함
    emaillist.first_name = request.POST['fn']
    emaillist.last_name = request.POST['ln']
    emaillist.email = request.POST['email']

    emaillist.save()  # 이제 DB에 반영되면서 영속화 됨

    return HttpResponseRedirect('/emaillist')

