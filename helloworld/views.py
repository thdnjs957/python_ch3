from django.db.models import Max, F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from helloworld.models import Counter


def hello(request):
    return render(request, 'helloworld/hello.html') # templates 기본 위치는 설정해놔서 생략

def hello2(request, id = 0): # 디폴트 0
    return HttpResponse(f'id:{id}')  # url 로 넘어오는 값 받기

def hello3(request):
    jsonresult = {
        'result': 'susccess',
        'data': ['hello', 1, 2, True, ('a', 'b', 'c')]
    }

    return JsonResponse(jsonresult)


# queryset

# order_no update
def counter_update(request):
    # groupno = 1 이고 orderno >= 2 의 게시물의
    # orderno를 1씩 증가
    # where 조건이 있으면 filter를 건다
    # __gt, __lt, __gte , __lte > < >= <=
    Counter.objects.filter(groupno=1).filter(orderno__gte=2).update(orderno=F('orderno') + 1)  # F 객체는 현재 객체라는 뜻
    # queryset은 update 지원

    # 이렇게 하지말기 만개면 만개
    # for c in r:
    #     c.orderno = c.orderno + 1
    #     c.save

    return HttpResponse('ok')


def counter_add(request):
    c = Counter()
    c.groupno = 1
    c.depth = 1
    c.orderno = 1
    c.save()

    c = Counter()
    c.groupno = 1
    c.depth = 1
    c.orderno = 2
    c.save()

    c = Counter()
    c.groupno = 1
    c.depth = 1
    c.orderno = 3
    c.save()

    return HttpResponse('ok')


def counter_max(request):
    value = Counter.objects.aggregate(max_groupno=Max('groupno'))
    print(value)
    max_groupno = 0 if value["max_groupno"] is None else value["max_groupno"]
    return HttpResponse(f'max groupno:{max_groupno}')