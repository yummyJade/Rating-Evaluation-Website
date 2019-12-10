from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from job import models as job_models
import json
# Create your views here.


def guidecontent(request):
    idnum = request.GET.get("id")
    data = job_models.CareerGuide.objects.filter(id=idnum)
    context = {
        'status': 200,
        'data': data
    }
    # print(context)
    return render(request, 'content.htm', context)


# 展示职业列表
def jobList(request):
    all_data = job_models.recruitInfo.objects.all()
    data = []
    for x in all_data:
        temp = {
            'jobname': x.jobname,
            'salary': x.salary,
            'company': x.company,
            'educationB': x.educationB,
            'worktime': x.worktime,
            'recruitNum': x.recruitNum,
            'zone': x.zone,
            'age': x.old
        }
        data.append(temp)

    context = {
        'status': 1,
        'data': data
    }

    return render(request, 'jobList.html', context)
    # return HttpResponse(json.dumps(context, ensure_ascii=False), content_type="application/json,charset=utf-8")