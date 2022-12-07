from django.http import HttpResponse
from django.shortcuts import redirect,render
from app.models import slider
from books.models import Add_book
from categories.models import category
from app.models import Author,Publisher
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse

def Home(request):

    sliders= slider.objects.all()
    Books= Add_book.objects.all()
    context ={
        'sliders':sliders,
        'books': Books,
    }
    return render(request, "index.html",context)

def About(request):
    return render(request, "about.html")


def Contact(request):
    return render(request, "contact.html")


def Register(request):
    
    return render(request, "account/register.html")

def handleRegister(request):
    if request.method =='POST':
       firstname = request.POST.get('firstname')
       lastname = request.POST.get('lastname')
       username = request.POST.get('username')
       email = request.POST.get('email')
       password = request.POST.get('password')
       
       if User.objects.filter(username = username).exists():
        messages.error(request,'username is already exists')
        return redirect('Register')

       if User.objects.filter(email = email).exists():
        messages.error(request,'email id are already exists')
        return redirect('Register')


    user =User(
        first_name= firstname,
        last_name= lastname,
        username= username,
        email= email,
        )
    user.set_password(password)
    user.save()
    return redirect('login')

   


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username = username, password = password)
        if user is not None and user.is_active:
            login(request,user)
            return redirect('Home')
        else:
            messages.error(request, 'Email and Password are invalid !')
        return redirect('login')



@login_required
def profile(request):
  return render(request, "profile/profile.html")


@login_required
def Profile_Update(request):
    if request.method == 'POST':
       
       first_name = request.POST.get('firstname')
       last_name = request.POST.get('lastname')
       username = request.POST.get('username')
       email = request.POST.get('email')
       password = request.POST.get('password')
       user_id = request.user.id
   

    user =User(
        id =   user_id,
        first_name= first_name,
        last_name= last_name,
        username= username,
        email= email,
        )
    
   
    if password != None and password != "":
        user.set_password(password)
        user.save()
           
    

    return redirect('Profile')

@login_required
def Books(request):
    Books= Add_book.objects.all()
    categories = category.objects.all()
    author = Author.objects.all()
    publisher = Publisher.objects.all()

    context ={
        
        'books': Books,
        'category' : categories,
        'author' : author,
        'publisher' : publisher,
    }
    return render(request, 'books/templates/books.html',context)


@login_required
def Book_Detail(request,id):
    Book_Detail = Add_book.objects.filter( id = id).first()
    context = {
        'book_detail' : Book_Detail,
    }
    
    return render(request, 'books/templates/book_detail.html',context)




def filter_data(request):
    categories=request.GET.getlist('category[]')
    Books=Add_book.objects.all().order_by('-id').distinct()
    if len(categories)> 0:
        Books = Books.filter(category__id__in=categories).distinct()
    t=render_to_string('ajax/book_list.html',{'data': Books})

    return JsonResponse({'data': t})


def Search(request):
   
    if request.method == 'POST':
        searched = request.POST['searched']
       
        book = Add_book.objects.filter(name__icontains=searched)
        # book = Add_book.objects.filter(publisher__id__name=searched)
        # book = Add_book.objects.filter(author__id__name=searched)
        
    return render(request, 'search.html',{'searched':searched,'books': book})