from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Platformtype
from .models import Queue
from .models import Testbeds
import pymysql


def index(request):
    return HttpResponse("Hello,word!")


def detail(request):
    # platformType_list = Platformtype.objects.order_by('-platformTypeID')[:67]
    # context = {'platformType_list' : platformType_list}
    # book_list = Book.objects.order_by('-pub_date')[:5]
    # context = {'book_list': book_list}
    # sql = "SELECT queueId,testbed,build,status,suite,MAX(creationDate),lastChangeDate,finishDate FROM queue GROUP BY testbed ORDER BY testbed"
    sql = "select b.queueId,  b.testbed,b.build, b.`status`,b.creationDate from (SELECT testbed, max(creationDate) as maxdate from queue group by testbed) as a INNER JOIN queue as b on a.testbed = b.testbed and a.maxdate = b.creationDate order by b.testbed "
    queue_list = Queue.objects.raw(sql)
    # queue_list = Queue.objects.raw('select * from queue')
    # queue_list = Queue.objects.order_by('-creationdate')[:100]
    platformt_list = Platformtype.objects.all()
    testbeds_list = Testbeds.objects.all().order_by('testbed')
    # queue_list = Queue.objects.all()[:2]
    # queue_list001 = Queue.objects.order_by('-creationdate').filter(testbed='')
    # queue_list = Queue.objects.order_by('-creationdate')[:100]

    # db = pymysql.connect("localhost", "root", "password", "autoSmoke")
    # # data = cursor1.fetchone()  # 将一条结果放入data
    # # data = cursor1.fetchmany(3)#将3条数据放入data
    # cursor = db.cursor()
    # sql = "SELECT testbed,build,`status`,suite,MAX(creationDate),lastChangeDate,finishDate FROM queue GROUP BY testbed ORDER BY testbed"
    # cursor.execute(sql)
    # rr = cursor.fetchall()
    # pri nt(type(rr))
    # db.close()
    # cursor.close()

    mylist = []
    # a = 1
    #
    # for obj in queue_list[1:]:
    #     tupleList = {}
    #
    #     tupleList["testbedID"] = a
    #     tupleList["testbed"] =obj.testbed[3:]
    #     tupleList["status"] =obj.status
    #     tupleList["build"] =obj.build[3:]
    #     tupleList["suite"] =obj.suite
    #     tupleList["creationdate"] =obj.creationdate
    #     tupleList["finishdate"] =obj.finishdate
    #     mylist.append(tupleList)

    testbed_num = 1
    testbed_busy_sum = 0
    testbed_free_sum = 0

    for a in testbeds_list:
        tupleList = {}
        tupleList["testbedID"] = testbed_num
        tupleList["testbed"] = a.testbed
        for b in queue_list:
            if b.testbed[3:] == a.testbed:
                if b.status < 3:
                    tupleList["status"] = "busy"
                    testbed_busy_sum = testbed_busy_sum + 1
                else:
                    tupleList["status"] = "free"
                    testbed_free_sum = testbed_free_sum + 1
                tupleList["build"] = b.build[3:]
                tupleList["suite"] = b.suite
                tupleList["creationdate"] = b.creationdate
                if b.finishdate == "0000-00-00 00:00:00" and b.status != 0:
                    tupleList["finishdate"] = "unfinished"
                else:
                    tupleList["finishdate"] = b.finishdate
        mylist.append(tupleList)
        testbed_num = testbed_num + 1
        # mylist.sort(key=lambda x:x[1])
        my_sum_busy_list = []
        my_sum_free_list = []
        my_sum_busy_list.append(testbed_busy_sum)
        my_sum_free_list.append(testbed_free_sum)

    # context = {'queue_list': queue_list, 'testbeds_list':testbeds_list,'platform_list': platformt_list}
    context = {'queue_list_my': mylist, 'my_sum_busy_list_dict': my_sum_busy_list,'my_sum_free_list_dict': my_sum_free_list}

    print(type(mylist))

    # print(len(queue_list[5]))
    # print(len(platformt_list))
    # print(len(testbeds_list))
    # print(type(queue_list))
    print(testbeds_list[1].testbed)
    print(testbeds_list[1].testbedID)

    # print(queue_list)

    print(queue_list[1].username)
    # print(queue_list[1].testbed)
    # print(queue_list.index[])
    # print(type(queue_list[2]))
    # print(type(platformt_list))
    # print(platformt_list[0])
    # print(queue_list[0].queueId)
    print(queue_list[1].build)
    print(queue_list[1].status)
    print(queue_list[1].suite)
    print(queue_list[1].testbed)
    # queue_list[0].testbed = queue_list[0].testbed[3:]#切片

    # queue_list[0].username = "asd"
    # print(queue_list[0].userName)
    # print(queue_list[0].creationDate)
    # print(queue_list[0].finishDate)
    # print(queue_list[0].lastChangeDate)
    return render(request, 'lib/detail.html', context)


# return HttpResponseRedirect(rev    erse('lib:detail'))
# return HttpResponse(context)


def addBook(request):
    # if request.method == 'POST':
    #     temp_name = request.POST['name']
    #     temp_author = request.POST['author']
    #     temp_pub_house = request.POST['pub_house']
    #
    # from django.utils import timezone
    # temp_book = Book(name=temp_name, author=temp_author, pub_house=temp_pub_house, pub_date=timezone.now())
    # temp_book.save()
    #
    # return HttpResponseRedirect(reverse('lib:detail'))
    pass


def deleteBook(request, book_id):
    # bookID = book_id
    # Book.objects.filter(id=bookID).delete()
    # return HttpResponseRedirect(reverse('lib:detail'))
    pass


# Create your views here.

def platformt(request):
    # book_list = Book.objects.order_by('-pub_date')[:5]
    # context = {'book_list': book_list}
    # # platformType_list = Platformtype.objects.order_by('-platformTypeID')[:10]
    # # context = {'platformType_list' : platformType_list}
    # return  render(request,'lib/detail.html',context)
    pass


def detail_queue(request):
    # platformType_list = Platformtype.objects.order_by('-platformTypeID')[:67]
    # context = {'platformType_list' : platformType_list}
    # book_list = Book.objects.order_by('-pub_date')[:5]
    # contex = {'book_list': book_list}
    # queue_list = Queue.objects.order_by('-creationDate')
    # context = {'queue_list': queue_list}
    # return render(request, 'lib/detail.html', context)
    pass
