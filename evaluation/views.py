from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from enum import Enum
from job import models as job_models
import heapq
import json
from evaluation import models
# Create your views here.

# 欢迎页


def test(request):
    # start_response('200 OK', [('Content-Type','text/html')])
    # #return ["Hello World"] # python2
    # return [b"Hello World"] # python3
    return HttpResponse("hello world")


def hello(request):
    # print("在这里")
    if request.session.get('user_id', '') != '':
        # print(request.session.get('user_id', ''))
        return render(request, 'index.html')
    else:
        return redirect('login.html')



# 展示主要功能的页面
# todo: 控制展示出来的数量
def mainfun(request):
    # 需要展示求职数据
    all_guide = job_models.CareerGuide.objects.all()
    data = all_guide
    context = {
        'status': 200,
        'data': data
    }
    return render(request, 'mainfun.html', context)



# 展示问卷页面
def infoform(request):
    # type = request.GET.get("type_num")
    # print(type_num)
    # a = qtypes.get(type_num, 0)(request)

    # print(type_num)
    return render(request, 'infoform.html')


# 展示MBTI测试题
def mbtiShow(request):
    # 获取所有的题目，题目必须满足qtype为mbti
    all_question = models.QuestionTitle.objects.filter(qtype='mbti')
    all_option = models.QuestionOption.objects.all()
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
            'type': 2,
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
            'type': 3,
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
    # print("type"+ type)
    a = qtypes[type](request)
    # print(a)

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


# 统计两次的结果并推荐
def recommendJob(request):

    jobtype_arr = [{"type": 0, "val": 0}, {"type": 1, "val": 0}, {"type": 2, "val": 0}, {"type": 3, "val": 0},
                   {"type": 4, "val": 0}, {"type": 5, "val": 0},{

                       "type": 6, "val": 0}, {"type": 7, "val": 0}, {"type": 8, "val": 0}, {"type": 9, "val": 0},
                   {"type": 10, "val": 0}, {"type": 11, "val": 0}, {"type": 12, "val": 0}, {"type": 13, "val": 0},
                   {"type": 14, "val": 0}, {"type": 15, "val": 0},
                   {"type": 16, "val": 0}, {"type": 17, "val": 0}, {"type": 18, "val": 0}, {"type": 19, "val": 0}
                   ]
    # 从数据库里查询
    # 首先获取result表中各项的数据
    userid = request.session.get('user_id','yuyuan')
    is_allfinish = models.QuestionFillingStatus.objects.filter(userId=userid)
    if len(is_allfinish) == 2:

        result_arr = models.QuestionResult.objects.filter(userId=userid)
        for i in result_arr:
            if i.qtype == "Hollander":
                index = int(i.type) - 1
                jobtype_arr[index]["val"] = i.value
            elif i.qtype == "JobValue":
                index = int(i.type - 1) + 6
                jobtype_arr[index]["val"] = i.value



        all_job = job_models.JobScore.objects.all()
        alljob_arr = []

        hol_arr = []
        for i in all_job:
            hol_arr = [i.htype1, i.htype2, i.htype3, i.htype4, i.htype5, i.htype6, i.valtype1, i.valtype2, i.valtype3,
                       i.valtype4, i.valtype5, i.valtype6, i.valtype7, i.valtype8, i.valtype9, i.valtype10, i.valtype11,
                       i.valtype12, i.valtype13]
            # sum = i.htype1 + i.htype2 + i.htype3 + i.htype4 + i.htype5 + i.htype6
            # sum = sum * 0.2
            alljob_arr.append({
                "name": i.name,
                "hol": hol_arr
            })

        # print(alljob_arr)

        # 先找到我所收集的数据中最大的三项
        re1 = jobtype_arr
        re1.sort(key=lambda x: x["val"], reverse=True)
        # 取字典前三项？ ok
        re1 = re1[0:3]
        # print(re1)

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
            for j in range(0, len(jobtype_arr) - 1):
                # print(j)
                sum2 = sum2 + (i["hol"][j] - jobtype_arr[j]["val"]) * (i["hol"][j] - jobtype_arr[j]["val"])
                # print(sum2)
            step3_arr.append(sum2 * 0.2)
            step4_arr.append({
                "name": i["name"],
                "val": sum * 0.8 + sum2 * 0.2
            })

        # 第三步，所有项数相乘0.2，尽量减少遍历次数，故此次在第一个循环中处理 ok
        # 第四部，所有的相加并排序
        step4_arr.sort(key=lambda x: x["val"], reverse=False)
        # print(step4_arr)
        # print(step4_arr[0:3])
        data = step4_arr[0:3]
        context = {
            'status': 1,
            'data': data
        }
    else:
        context = {
            'status': 0,
            'message': '请先完成所有测试'
        }
    return render(request, 'recommandResult.html', context)




# 计算并处理问卷结果
def calcuNaire(request):
    userid = request.session.get('user_id', 'yuyuan')
    # print("userid", userid)
    # print(request.GET)
    context = request.GET
    type = request.GET.get("qtype");
    # print(type)
    # 如果是mbit

    if type == '1':
        all_question = models.QuestionTitle.objects.filter(qtype='mbti')
        type_map = []
        JobType = {"E": 1, "I": 2, "S": 3, "N": 4, "T": 5, "F": 6, "J": 7, "P": 8}
        JobType2 = {"1": 1, "2": 2, "3": 3, "4": 4, }
        for i in all_question:
            type_map.append(i.otype)

        # print(type_map)
        # 统计每一种的数量
        jobtype_arr = [{"type": 0, "val": 0}, {"type": 1, "val": 0}, {"type": 2, "val": 0}, {"type": 3, "val": 0},
                       {"type": 4, "val": 0}, {"type": 5, "val": 0}, {"type": 6, "val": 0}, {"type": 7, "val": 0}]
        index = 0
        # 这里是统计
        sum = 0
        for j in range(0, len(type_map)):
            res = request.GET.get(str(j), 0)
            # print(res);
            # if res != '0':
            #     index = JobType[type_map[j]] - 1
            #     jobtype_arr[index]["val"] = jobtype_arr[index]["val"] + int(res)
            #     sum = sum + int(res)
            if res != 0:
                index = (JobType2[type_map[j]] - 1) * 2 + int(res) - 1
                jobtype_arr[index]["val"] = jobtype_arr[index]["val"] + 1
                sum = sum + int(res)


        # 返回单次的结果
        # 在每两种中挑选一个出来
        type = ""
        for i in range(0, len(jobtype_arr), 2):

            val1 = jobtype_arr[i]["val"]
            val2 = jobtype_arr[i+1]["val"]
            if val1 > val2:
                type += list(JobType.keys())[list(JobType.values()).index(jobtype_arr[i]["type"] + 1)]
            else:
                type += list(JobType.keys())[list(JobType.values()).index(jobtype_arr[i+1]["type"] + 1)]

        # print(type)
        # 得到结果后再数据库查询对应的类型 filter为type
        allresult = models.QuestionResultTwo.objects.filter(type=type)
        # print(allresult)
        i = allresult[0]
        data = {
            "type": i.type,
            "feature": i.feature,
            "contri": i.contri,
            "leaderP": i.leaderP,
            "studyP": i.studyP,
            "trend": i.trend,
            "solveP": i.solveP,
            "workE": i.workE,
            "suggest": i.suggest,
            "weakness": i.weakness
        }

        context = {
            'data': data
        }
        return render(request, 'result1.html', context)

    elif type == '2':
        all_question = models.QuestionTitle.objects.filter(qtype='Hollander')
        type_map = []
        JobType = {"常规型": 1, "现实型": 2, "研究型": 3, "管理型": 4, "社会型": 5, "艺术型": 6}
        for i in all_question:
            type_map.append(i.otype)


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



        # 统计完jobtype的数量以后，存入数据库
        print(jobtype_arr)
        hasFinshFlag = 0
        hasFinsh = models.QuestionFillingStatus.objects.filter(userId=userid, qtype='Hollander')

        # 没有这个记录或者其他情况
        if len(hasFinsh) == 0:
            hasFinshFlag = 0    #没有创建，需要新建
            models.QuestionFillingStatus.objects.create(userId=userid, qtype='Hollander', finish='1')
            for i in jobtype_arr:
                models.QuestionResult.objects.create(userId=userid, qtype='Hollander', type=i["type"]+1, value=i["val"])

        elif len(hasFinsh[0].finish) == 1:
            hasFinshFlag = 1    #创建了，直接修改
            for i in jobtype_arr:
                # print(i["val"])
                models.QuestionResult.objects.filter(userId=userid, qtype='Hollander', type=i["type"]+1)\
                    .update(value=i["val"])

        # 返回对应的数据
        # 把返回结果从数据库中找出来
        resultDes_arr = models.QuestionResultOne.objects.filter(qtype='Hollander')
        # print(resultDes_arr[0].des1)
        # 先对数据进行排序 jobtype_arr
        jobtype_arr.sort(key=lambda x: x["val"], reverse=True)
        res1 = jobtype_arr[0:3]
        context = []
        data = []
        # 最后通过type要找到对应的类型文字i描述
        for i in res1:
            data.append({
                'type': list(JobType.keys())[list(JobType.values()).index(i["type"]+1)],
                'des1': resultDes_arr[i["type"]].des1,
                'des2': resultDes_arr[i["type"]].des2,
            })


        context = {
            'status': 200,
            'data': data
        }

        # print(context)
        return render(request, 'result2.html', context)

    elif type == '3':
        all_question = models.QuestionTitle.objects.filter(qtype='JobValue')
        type_map = []
        JobType = {"利他主义": 1, "美感": 2, "智力挑战": 3, "成就感": 4, "自主": 5, "社会地位": 6, "管理": 7, "经济报酬": 8, "社会交际": 9, "安全感": 10, "舒适": 11, "团队": 12, "新奇": 13}
        for i in all_question:
            type_map.append(i.otype)

        # 获取问卷信息

        # 收集各种类型的数量
        # jobtype_arr = [0, 0, 0, 0, 0, 0]
        jobtype_arr = [{"type": 0, "val": 0}, {"type": 1, "val": 0}, {"type": 2, "val": 0}, {"type": 3, "val": 0},
                       {"type": 4, "val": 0}, {"type": 5, "val": 0}, {"type": 6, "val": 0}, {"type": 7, "val": 0}, {"type": 8, "val": 0}, {"type": 9, "val": 0},
                       {"type": 10, "val": 0}, {"type": 11, "val": 0},{"type": 12, "val": 0},{"type": 13, "val": 0}]
        index = 0
        # 这里是统计
        sum = 0
        for j in range(0, len(type_map)):
            res = request.GET.get(str(j), 0)
            # print(res);
            if res != '0':
                index = JobType[type_map[j]] - 1
                jobtype_arr[index]["val"] = jobtype_arr[index]["val"] + int(res)
                sum = sum + int(res)


        # 统计完jobtype的数量以后，存入数据库
        hasFinshFlag = 0
        hasFinsh = models.QuestionFillingStatus.objects.filter(userId=userid,qtype='JobValue')
        # print(hasFinsh)
        # 没有这个记录或者其他情况
        if len(hasFinsh) == 0:
            hasFinshFlag = 0  # 没有创建，需要新建
            models.QuestionFillingStatus.objects.create(userId=userid, qtype='JobValue', finish='1')
            for i in jobtype_arr:
                models.QuestionResult.objects.create(userId=userid, qtype='JobValue', type=i["type"] + 1,
                                                     value=i["val"])

        elif len(hasFinsh[0].finish) == 1:
            hasFinshFlag = 1  # 创建了，直接修改
            for i in jobtype_arr:
                models.QuestionResult.objects.filter(userId=userid, qtype='JobValue', type=i["type"] + 1) \
                    .update(value=i["val"])

        # 返回单次的结果
        # 把返回结果从数据库中找出来
        resultDes_arr = models.QuestionResultOne.objects.filter(qtype='JobValue')
        # print(resultDes_arr[0].des1)
        # 先对数据进行排序 jobtype_arr
        res2 = jobtype_arr
        data2 = []
        for i in res2:
            # data2.append({
            #     'type': list(JobType.keys())[list(JobType.values()).index(i["type"] + 1)],
            #     'val': i["val"]
            # })
            data2.append(i["val"])

        jobtype_arr.sort(key=lambda x: x["val"], reverse=True)
        res1 = jobtype_arr[0:3]
        context = []
        data = []

        # 最后通过type要找到对应的类型文字i描述
        for i in res1:
            # print(i)
            data.append({
                'type': list(JobType.keys())[list(JobType.values()).index(i["type"] + 1)],
                'des1': resultDes_arr[i["type"]].des1,
                'des2': ""
            })

        # context = {
        #     'status': 200,
        #     'data': data,
        #     'data':
        # }


        print(data2)
        # return render(request, 'result3.html', context)
        return render(request, 'result3.html', {
            'data1': json.dumps(data),
            'data2': json.dumps(data2),
            'sum': json.dumps(sum)
        })


        # return render(request, 'result.html', context)
