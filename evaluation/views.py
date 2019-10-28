from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from enum import Enum
from job import models as job_models
import heapq

# Create your views here.

# 欢迎页
from evaluation import models


def hello(request):
    return render(request, 'index.html')


# 展示主要功能的页面
def mainfun(request):
    return render(request, 'mainfun.html')


# 展示问卷页面
def infoform(request):
    # type = request.GET.get("type_num")
    # print(type_num)
    # a = qtypes.get(type_num, 0)(request)

    # print(type_num)
    return render(request, 'infoform.html')


 # todo：关于类型的数组应该开全局变量还是再查一次数据库
# 展示MBTI测试题
def mbtiShow(request):
    # 获取所有的题目，题目必须满足qtype为mbti
    all_question = models.QuestionTitle.objects.filter(qtype='mbti')
    all_option = models.QuestionOption.objects.all()

    # todo:如何封装返回json的处理类
    # todo:获得对应的option，如何有更高效的方法获得结果
    # todo:应该考虑做分页，那样子会更好

    # print(all_question)
    data = []

    for i in all_question:
        options = []
        for j in all_option:
            if j.titleId == i.id:
               options.append(j.content)

        data.append({
            'type': i.otype,
            'title': i.name,
            'options': options
        })
    context = {
        'status': 1,
        'type': 1,
        'data': data
    }
    # print(all_question)
    # context = {
    #     'result': all_question
    # }
    return context


# 展示霍兰德测试题
def hollanderShow(request):
    all_question = models.QuestionTitle.objects.filter(qtype='Hollander')
    all_option = models.QuestionOption.objects.all()
    data = []

    for i in all_question:
        options = {}
        for j in all_option:
            if j.titleId == i.id:
                options = {
                    'val1': j.value1,
                    'val2': j.value2
                }
        data.append({
            'type': i.otype,
            'title': i.name,
            'options': options
        })
        context = {
            'status': 1,
            'type': 3,
            'data': data

        }

    return context


# 展示职业价值观测试题
def jobValueShow(request):
    all_question = models.QuestionTitle.objects.filter(qtype='JobValue')
    data = []

    for i in all_question:
        data.append({
            'type': i.otype,
            'title': i.name,

        })
        context = {
            'status': 1,
            'type': 2,
            'data': data

        }
    return context


def noShow(request):
    return HttpResponse('无效')


qtypes = {
    '1': mbtiShow,
    '2': hollanderShow,
    '3': jobValueShow,
    '0': noShow,
}


# 获取对应测试题的内容
def getNaire(request):
    type = request.GET.get("type")

    a = qtypes[type](request)

    return JsonResponse(a, safe=False)


# 霍兰德职业类型分类
# class JobType(Enum):
#     常规性 = 1
#     现实型 = 2
#     研究型 = 3
#     管理型 = 4
#     社会型 = 5
#     艺术型 = 6
#


# 计算并处理问卷结果
def calcuNaire(request):
    # todo:这里完成计算内容以及其他的部分，越早越好
    # todo:要修改一下html的结构，有点问题，因为肯定单选要用input
    # todo:在显示的时候最好出现一个可视化的视图

    print(request.GET)
    context = request.GET
    type = request.GET.get("qtype");
    print(type)
    # 如果是mbit
    if type == 1:
        all_question = models.QuestionTitle.objects.filter(qtype='mbti')
        type_map = []
        JobType = {"常规性": 1, "现实型": 2, "研究型": 3, "管理型": 4, "社会型": 5, "艺术型": 6}
        for i in all_question:
            type_map.append(i.otype)

        print(type_map)

        # 统计每一种的数量
    elif type == '2':
        all_question = models.QuestionTitle.objects.filter(qtype='Hollander')
        type_map = []
        JobType = {"常规性": 1, "现实型": 2, "研究型": 3, "管理型": 4, "社会型": 5, "艺术型": 6}
        for i in all_question:
            type_map.append(i.otype)

        # print(type_map)
        # 获取问卷信息

        # 收集各种类型的数量
        # jobtype_arr = [0, 0, 0, 0, 0, 0]
        jobtype_arr = [{"type":0,"val":0},{"type":1,"val":0},{"type":2,"val":0},{"type":3,"val":0},{"type":4,"val":0},{"type":5,"val":0}]
        index = 0
        # 这里是统计
        for j in range(0, len(type_map)):
            res = request.GET.get(str(j), 0)
            if res == '1':
                index = JobType[type_map[j]] - 1
                jobtype_arr[index]["val"] = jobtype_arr[index]["val"] + 1


        # print(jobtype_arr)
        # 统计完jobtype的数量以后，存入数据库
        # todo：最后数据库打上标记，表示已经进行过做题的操作
        # todo：在插入一条新数据之前先通过select确定这个用户是否提交过问卷
        # todo:是否在用户创建之初就插入，如果是，这个flag有什么意义
        hasFinshFlag = 0
        hasFinsh = models.QuestionFillingStatus.objects.filter(userId='yuyuan')
        # 没有这个记录或者其他情况
        if len(hasFinsh) == 0:
            hasFinshFlag = 0    #没有创建，需要新建
            models.QuestionFillingStatus.objects.create(userId='yuyuan', qtype='Hollander', finish='1')
            for i in jobtype_arr:
                models.QuestionResult.objects.create(userId='yuyuan', qtype='Hollander', type=i["type"]+1, value=i["val"])

        elif hasFinsh[0].finish == 1:
            hasFinshFlag = 1    #创建了，直接修改
            for i in jobtype_arr:
                models.QuestionFillingStatus.objects.filter(userId='yuyuan', qtype='Hollander', type=i["type"]+1)\
                    .update(value=i["val"])

        # 接下来处理数据，与职业表进行对照
        # todo: 对于来自其他模块model的怎么办
        all_job = job_models.JobScore.objects.all()
        alljob_arr = []

        hol_arr = []
        for i in all_job:
            hol_arr = [i.htype1,i.htype2,i.htype3,i.htype4,i.htype5,i.htype6]
            # sum = i.htype1 + i.htype2 + i.htype3 + i.htype4 + i.htype5 + i.htype6
            # sum = sum * 0.2
            alljob_arr.append({
                "name": i.name,
                "hol": hol_arr
            })

        print(alljob_arr)


        # 先找到我所收集的数据中最大的三项
        re1 = jobtype_arr
        re1.sort(key=lambda x: x["val"], reverse=True)
        # 取字典前三项？ ok
        re1 = re1[0:3]
        print(re1)

        # 第二步，算出所有职业中对应那三项，与收集数据中相减平方和*0.8，最后一个职业得到一个偏差值
        step2_arr = []
        step3_arr = []
        step4_arr = []
        for i in alljob_arr:
            sum = 0
            sum2 = 0
            for j in list(re1):
                sum = sum + (i["hol"][j["type"]] - j["val"]) * (i["hol"][j["type"]] - j["val"])
            step2_arr.append(sum * 0.8)
            # step2_arr.append({
            #     "name": i.name,
            #     "val": sum*0.8
            # })
            for j in range(0, len(jobtype_arr)):
                sum2 = sum2 + (i["hol"][j] - jobtype_arr[j]["val"])* (i["hol"][j] - jobtype_arr[j]["val"])
                # print(sum2)
            step3_arr.append(sum2 * 0.2)
            step4_arr.append({
                "name": i["name"],
                "val": sum * 0.8 + sum2 * 0.2
            })

        # 第三步，所有项数相乘0.2，尽量减少遍历次数，故此次在第一个循环中处理 ok
        # 第四部，所有的相加并排序
        step4_arr.sort(key=lambda x: x["val"], reverse=False)
        print(step4_arr)
        context = {
            'status': 1,
            'result': step4_arr
        }

    return render(request, 'result.html', context)
