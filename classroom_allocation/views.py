from django.shortcuts import render
from rooms.models import timetable
from cr.models import historyy


def homes(request):
    if request.method=="POST":
        searchyear=request.POST.get('year')
        searchcourse=request.POST.get('course')
        ttsearch=timetable.objects.filter(year=searchyear,course=searchcourse)
        tthis = historyy.objects.filter(year=searchyear,course=searchcourse)
        uc=set()
        for entry in ttsearch:
            name = entry.name
            subject = entry.subject
            color=entry.color
            combination = (name, subject, color)
            uc.add(combination)
        sc = sorted(uc, key=lambda combination: combination[1])
        my_list = []
        
        for t in ttsearch:
            row = []
            for h in tthis:
                if t.time == h.time and t.day == h.day:
                    row.extend([h.time, h.day, h.teacher, h.status, h.subject, h.color,h.id,0,h.room])
                    my_list.append(row)
                    break
            else:
                row.extend([t.time, t.day, t.teacher, t.status, t.subject, t.color,0,t.id,t.room])
                my_list.append(row)

        context = {
            'data':my_list,
            'data2':sc,
            'data3':tthis,
            'year':searchyear,
            'course':searchcourse,
        }
        return render(request,'home.html',context)
    else :
        return render(request,'home.html')

def proom(request):
    if request.method=="POST":
        time=request.POST.get('time')
        # day = datetime.now().strftime('%A')
        # day = day.upper()[:3]
        day = 'MON'
        list = [False]*29
        data=timetable.objects.filter(day=day,time=time)
        data1 = historyy.objects.filter(day = day,time=time)
        
        for i in range(29):
            for d in data:
                if d.room==i:
                    if not list[i]:
                        if d.teacher:
                            list[i]=True
            for d in data1:
                if d.room==i:
                    if not list[i]:
                        if d.teacher:
                            list[i]=True
                    
        
    
        
        return render(request,"p_room.html",{'list' : list,'time' : time})
    else :
        return render(request,'p_room.html')
# def homes(request):
#     if request.method=="POST":
#         searchyear=request.POST.get('year')
#         searchcourse=request.POST.get('course')
#         ttsearch=timetable.objects.filter(year=searchyear,course=searchcourse)
#         uc=set()
#         for entry in ttsearch:
#             name = entry.name
#             subject = entry.subject
#             color=entry.color
#             combination = (name, subject, color)
#             uc.add(combination)
#         sc = sorted(uc, key=lambda combination: combination[1])
#         context = {
#             'data':ttsearch,
#             'data2':sc
#         }
#         return render(request,'home.html',context)
#     else :
#         return render(request,'home.html')

def abouts(request):
    return render(request,"about.html",{})

def feedbacks(request):
    return render(request,"contact.html",{})