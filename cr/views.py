from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import historyy
from .models import Feedback
from rooms.models import timetable
from .models import historyy
from django.contrib import messages
from .forms import FeedbackForm
from datetime import datetime,time

def prooms(request):
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
                    
        
    
        
        return render(request,"cr/p_room.html",{'list' : list,'time' : time})
    else :
        return render(request,'cr/p_room.html')
    

def history(request):
    his= historyy.objects.all()

    return render(request,"cr/history.html",{
        'his':his
    })



# Create your views here.
def home(request):
    return render(request,"cr/home.html",{})

def tt(request):
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
        return render(request,'search.html',context)
    else :
        # start_time = time(21,3)  # Set the start time to 7:00 PM
        # end_time = time(22,30)    # Set the end time to 8:00 PM

        # current_time = datetime.now().time()

        # if start_time <= current_time <= end_time:
        #     historyy.objects.all().delete()
        #     timetable.objects.all().update(status=1)
            
        return render(request,'search.html')
        

def cancel(request,id):
    et = timetable.objects.get(pk=id)
    return render(request,'cancel.html',{'et':et})

def do_cancel(request,id):
    if request.method == 'POST':
        e_status = request.POST.get("et_status")
        
        tet=timetable.objects.get(pk=id)

        if e_status is None:
            tet.status=False
        else:
            tet.status=True
        
        tet.save()
    return redirect("/cr/home/timetable/")

def rooms(request,id):
        # if request.method=="POST":
        # time=request.POST.get('time')
       
        tid=timetable.objects.get(pk=id)
        time=tid.time
        day = tid.day
        list = [False] * 29
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
                    
        
    
        
        return render(request,"cr/rooms.html",{'list' : list,'time' : time,'tid':tid})



def course(request):
    his= historyy.objects.all()
    return render(request,"cr/history.html",{
        'his':his
    })
def registration_view(request,room,id):
    tid=timetable.objects.get(pk=id)
       
    if request.method=='POST':
        name=request.POST.get("name")
        subject=request.POST.get("subject")
        teacher=request.POST.get("teacher")
        course=tid.course
        day=tid.day
        year=tid.year
        room=room
        time=tid.time

         
        his=historyy()

        his.subject=subject
        his.course=course
        his.day=day
        his.teacher=teacher
        his.year=year
        his.room=room
        his.time=time

        his.save()
        return redirect("/cr/home/timetable/")
    
    return render(request,"cr/registration.html",{'room':room,'tid':tid})


def about(request):
    return render(request,"cr/about.html",{})
def success(request):
    return render(request,"cr/success.html",{})
def feedback(request):
    if request.method == 'POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        course=request.POST.get("course")
        year=request.POST.get("year")
        feedback=request.POST.get("feedback")
        
        data=Feedback()
        return redirect(request,"/cr/home/")
    return render(request, 'cr/contact.html', {})
    
# def feedback(request):
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             # Process the form data, e.g., save it to a database
#             # Redirect or display a thank you message
#             data = form.cleaned_data  # Extract cleaned data from the form
#             # Perform actions based on the form data

#             # Redirect to a success page or another URL
#             return redirect('success_page')

#     else:
#         form = FeedbackForm()

#     return render(request, 'cr/contact.html', {'form': form})