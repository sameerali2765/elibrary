from django.http import HttpResponse
from django.shortcuts import redirect,render
from app.models import slider
from books.models import Add_book
from videos.models import Video
from categories.models import category
from app.models import Author,Publisher
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
from .forms import ContactForm
from django.core.mail import send_mail,EmailMultiAlternatives

def Home(request):

    sliders= slider.objects.all().order_by('-id')
    videos= Video.objects.all().order_by('-id')
    Books= Add_book.objects.all().order_by('-id')
    Bookslimit= Add_book.objects.all().order_by('-id')[:6]
    categories = category.objects.all().order_by('-id')[:4]
    context ={
        'sliders':sliders,
        'books': Books,
        'bookcategory': categories,
        'booklimit' :Bookslimit,
        'videos' : videos,
    }
    return render(request, "index.html",context)


def About(request):
    return render(request, "about.html")


def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            
            html = render_to_string('email/contact.html',{
                'message': message,
                'name': name,
                'email': email,
                'subject' : subject,
            })

        subject=' Contact Form'
        from_email ='sameerali2765@gamil.com'
        msg="Welcome to Elibrary"
        to ='mubee332@gmail.com'
        send_mail(subject,from_email,msg,[to],html_message=html)
        return redirect('Contact')
    else:
        form = ContactForm()
    return render(request, "contact.html", {'form': form})




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
   

    user = User.objects.get(id=user_id)
    user.first_name = first_name
    user.last_name = last_name
    user. username = username
    user.email = email

    if password != None and password != "":
        user.set_password(password)
    user.save()
    return redirect('profile')

@login_required
def Books(request):
    Books= Add_book.objects.all().order_by('-id')
    categories = category.objects.all().order_by('-id')
    author = Author.objects.all().order_by('-id')
    publisher = Publisher.objects.all().order_by('-id')
   
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
    Books = Add_book.objects.all().order_by('-id')
    categories=request.GET.getlist('category[]')
    publishers=request.GET.getlist('publisher[]')
    authors=request.GET.getlist('author[]')
    
    book=Add_book.objects.all().order_by('-id').distinct()

    if len(categories) > 0:
        Books = book.filter(category__id__in=categories).distinct()
    if len(publishers) > 0:
        Books = book.filter(publisher__id__in=publishers).distinct()
    if len(authors) > 0:
        Books = book.filter(author__id__in=authors).distinct()
    
    t=render_to_string('ajax/books.html',{'books': Books})

    return JsonResponse({'data': t})


def Search(request):
   
    if request.method == 'POST':
        searched = request.POST['searched']
       
        book = Add_book.objects.filter(name__icontains=searched)
        # book = Add_book.objects.filter(publisher__id__name=searched)
        # book = Add_book.objects.filter(author__id__name=searched)
        
    return render(request, 'search.html',{'searched':searched,'books': book})

 

