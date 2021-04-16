from django.shortcuts import render,redirect
from .models import*
import datetime
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User as djangouser


# Create your views here.

def index(request,warning="",error="",success =""):
    if request.user.is_authenticated:
        for ass in Assignment.objects.all():
            ass.add()
        try:
            student = request.user.student
        except:
            if request.user.is_superuser:
                student = Student(rollNo=0,user=request.user)
                student.save()
            else:
                return home(request)
        assignments = student.assignment.all()
        return render(request,"assignments/index.html",{
            "assignments": assignments,
            "error":error,
            "warning":warning,
            "success":success
        })
    else:
        return home(request)


def delete_task(request):
    if request.method=="POST":
        if "rmtask" in request.POST:
            task_id= int(request.POST["rmtask"])
            if task_id in StudentAssignment.objects.values_list("id",flat=True):
                today=datetime.datetime.now()
                task=StudentAssignment.objects.get(pk=task_id)
                task.complete_date=today.date()
                task.done=True
                task.save()


    return redirect("/")


def completed(request):
    if request.user.is_authenticated:
        student = request.user.student
        assignments = student.assignment.all()
        return render(request,"assignments/history.html",{
            "assignments":assignments
        })

    redirect("/")
        
         
def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            P = request.POST
            if "username" in P and "password1" in P and "password2" in P and "email" in P and "roll_no" in P:
                print("working")
                username = P['username']
                password = P['password1']
                confirmPassword =P['password2']
                email = P["email"] 
                roll_no = P["roll_no"]

                try:
                    testuser = djangouser.objects.get(username=username)
                    if testuser:
                        return render(request,"registration/register.html",{
                        "error":"Username unavailable"
                        })
                except:
                    pass
                try :
                    testuser = djangouser.objects.get(email=email)
                    if testuser:
                        return render(request,"registration/register.html",{
                        "error":"Email already registered"
                        })
                except:
                    pass
                if password == confirmPassword:
                    
                    newuser = djangouser.objects.create(username=username,password=password,email=email)
                    newuser.save()
                    student = Student(rollNo=roll_no, user = newuser)
                    student.save()
                    newuser.save()

                    login(request,newuser)
                    for assess in Assignment.objects.all():
                        newss = StudentAssignment(student=student,assignment=assess)
                        newss.save()
                    return redirect('/')
                return render(request,"registration/register.html",{
                    "error":"password is not same as confirm passowrd"
                })
            return render(request,"registration/register.html",{
                "error":"Invalid credentials"
            })
            
        return render(request,"registration/register.html")
    
    return index(request,warning="You have already logged in!")
    

def login_manually(request):
    if not request.user.is_authenticated :
        if request.method =="POST":
            if "username" in request.POST and "password" in request.POST:
                username = request.POST["username"]
                password = request.POST["password"]

                try:
                    user = djangouser.objects.get(username=username)
                except:
                    return home(request,error="Invalid Username")


                if authenticate(request,username=username,password=password):
                    login(request,user)
                    return redirect("/")

                if password==user.password:
                    login(request,user)
                    return redirect("/")
                return home(request,error="invalid password")
            
        return redirect("/accounts/login/")
    return index(request)

    

def home(request,error="",general=""):
    if request.user.is_authenticated:
        return index(request,error="You have already logged in!")
    else:
        context={
            "error":error,
            "general":general
        }
        return render(request,"registration/login_signup.html",context)


def logout(request):
    if request.user.is_authenticated:
        return index(request,error="couldn't log out")
    return home(request,general="Logged out succesfully")


def assignment(request,ass_id):
    if request.user.is_authenticated:
        task =StudentAssignment.objects.get(pk=ass_id)
        return render(request,"assignments/assignment.html",{
            "assignment":task
        })

    return home(request,error="You haven't logged in yet!")


def solutions(request,ass_id):
    if request.user.is_authenticated:
        task =StudentAssignment.objects.get(pk=ass_id).assignment.studentassignment.all()
        ss = StudentAssignment.objects.get(pk=ass_id)
        return render(request,"assignments/solutions.html",{
            "assignments":task,
            "ss":ss
        })

    return home(request,error="You haven't logged in yet!")


def Solution_specific(request,ass_id):
    if request.user.is_authenticated:
        task =StudentAssignment.objects.get(pk=ass_id)
        solutions = task.solution.all()
        date = task.solution.first().submission_date
        return render(request,"assignments/solution.html",{
            "assignment":task,
            "solutions":solutions,
            "date":date
        })

    else:
        return home(request,error="You haven't logged in yet!")


def submit(request,ass_id):
    if request.user.is_authenticated:
        if StudentAssignment.objects.get(pk=ass_id).submitted==False:
            if request.method =="GET":
                if "n" in request.GET and int(request.GET["n"])<21:
                    n=request.GET["n"]
                    return render(request,"assignments/submit.html",{
                        "n":n,
                        "range":range(int(n)),
                        "ass_id":ass_id
                        })
                else:
                    return render(request,"assignments/submit.html",{
                        "ass_id":ass_id
                    })

            else:
                print("yessssssss4444",end="\n\n\n")
                P= request.POST
                if "n" in P:
                    print(int(P["n"]))
                    
                    assignment = StudentAssignment.objects.get(pk=ass_id)
                    if "img0" in request.FILES:
                        for i in range(int(P["n"])):
                            img = "img" + str(i)
                            if img in request.FILES:
                                print("yessssssss",end="\n\n\n")
                                image= request.FILES[img]
                                print(image)
                                Solution = solution(assignment=assignment)
                                Solution.save()


                                image_name= "solution"+str(assignment.id) +"_"+ str(Solution.id)+".jpeg"
                                savefile(image,image_name)
                                
                                Solution.image=image_name
                                Solution.save()
                        assignment.submitted=True
                        assignment.save()
                return redirect(("/solution/submit/"+str(ass_id)))

        return index(request,error="You have already submitted your solution")
    return home(request,error="You haven't logged in yet!")

def savefile(f,filename):
    with open('static/images/'+ filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)



