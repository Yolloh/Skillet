from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,Http404
from  django.urls import reverse
from django.shortcuts import get_object_or_404,render,get_list_or_404,redirect
from .models import Question,Choice,Status
from login.models import UserProfile
from django.contrib.auth.decorators import login_required


@login_required(login_url = '/')
def s_pop(request):
    current_user = request.user
    qlist = Question.objects.all()
    for x in qlist:
        Status.objects.get_or_create(User = current_user,question = x)
    return HttpResponseRedirect(reverse('quiz:disp',args = (first_question().id,)))

def no_of_Question():
    return len(Question.objects.all())

def first_question():
    list = Question.objects.all()
    list = list[0]
    return list

def last_question():
    list = Question.objects.all()
    len_lst = len(list)
    list = list[len_lst-1]
    return list

def next_question(pk):
    pk = int(pk)
    if pk != last_question():
        list = Question.objects.filter(id__gt = pk)
        list = list[0]
        return list
    else:
        return None

def prev_question(pk):
    pk = int(pk)
    if pk != first_question().id:
        list = Question.objects.filter(id__lt = pk) 
        len_lst  = len(list)
        len_lst = len_lst-1
        list = list[len_lst]
        return list
    else:
        return None

def nth_question(pk):
    qlist = Question.objects.all()
    pk = int(pk)
    pk = pk -1
    return qlist[pk]
    

@login_required(login_url = '/')
def disp(request,pk):
    question = get_object_or_404(Question,pk=pk)
    current_user = request.user
    if request.method == 'POST':
        nav = request.POST['nav']
        ans(request,pk)
        if nav  == 'Next':
            return disp_next_question(question,pk)
        elif nav == 'Previous':
            prev_q = prev_question(pk)
            return HttpResponseRedirect(reverse('quiz:disp',args = (prev_q.id,)))
        else:
            nth_q = nth_question(nav)
            return HttpResponseRedirect(reverse('quiz:disp',args = (nth_q.id,)))
    else:
        return disp_question(request,pk,current_user,question)

@login_required(login_url = '/')
#actually ans post always
def ans(request,pk):
    current_user = request.user
    question = get_object_or_404(Question,pk=pk)
    status, created = Status.objects.get_or_create(User = current_user,question = question) 
    user = UserProfile.objects.get(user = current_user.id)
    status.Qstatus = request.POST['status']
    status.save()
    #saving time
    #user could jack data sent
    if user.rmin >= request.POST['min']:  
        user.rmin = request.POST['min']
        user.rsec = request.POST['sec']
        user.save()
    try:
        value = request.POST['choice']
        selected_choice = question.choice_set.get(pk = value)
    except(KeyError, Choice.DoesNotExist):
        #last ans is correct
        if status.selected == cans(question):
            dec_mark(user)
            status.selected = -1
            status.save()   
    else: 
        #ans is correct
        if(selected_choice.answer == 'Yes' ):
            #two times same correct answer
            if selected_choice.id != status.selected:
                add_mark(user)
        else:
            if status.selected != -1:
                #not first time answering the question
                pre_choice = Choice.objects.get(pk = status.selected)
                if pre_choice.answer == 'Yes':
                    #wrong ans afer corect ans
                    dec_mark(user)
        #ans first time
        status.selected = value
        status.save()


def add_mark(mark):
    mark.mark += 1
    mark.save()

def dec_mark(mark):
    mark.mark -= 1 
    mark.save()

# correct ans
def cans(question):
    list = question.choice_set.all()
    for x in list:
        if x.answer == 'Yes':
            return x.id


def disp_question(request,pk,current_user,question):
    #get request
    pre_question = prev_question(pk)
    current_status = Status.objects.get(User= current_user,question = question)
    status = get_list_or_404(Status,User = current_user)
    user = UserProfile.objects.get(user = current_user.id)
    dic ={
    'question' : question,
    'first_question': first_question,
    'last_question' : last_question,
    'pre_question' : pre_question,
    'next_question': next_question,
    'status'  : status,
    'current_status' : current_status, 
    'user' : user,
   }
    return render(request,'quiz/index.html',dic)

def disp_next_question(question,pk):
    next_Question = next_question(pk)
    if(next_Question != None):
            return HttpResponseRedirect(reverse('quiz:disp',args = (next_Question.id,)))
    else:
        return redirect('login:logout')
        #return HttpResponse("Thank You") #need to check how many left unanswerd

def timer(request):
    if request.method == 'POST':
        current_user = request.user
        user = UserProfile.objects.get(user = current_user.id)
        if user.rmin >= request.POST['min']:  
            user.rmin = request.POST['min']
            user.rsec = request.POST['sec']
            user.save()
            print user.rmin
        return HttpResponse(status=204)
    