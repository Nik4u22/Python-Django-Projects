from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from apps.iLibrary.models import Book, IssueBook, Student, Employee
from django.core.files.storage import FileSystemStorage
from datetime import datetime, timedelta
from django.contrib import messages
# Create your views here

def user_login(request):
    authenticationForm = AuthenticationForm()
    if request.method == "POST":
        authenticationForm = AuthenticationForm(request, data=request.POST or None)
        if authenticationForm.is_valid():
            username = authenticationForm.cleaned_data["username"]
            password = authenticationForm.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user=user)
                return redirect('home')
        else:
            print(authenticationForm.errors)
    
    return render(request, ("login.html"), {"authenticationForm": authenticationForm})
    
def home(request):
    books = Book.objects.all()
    return render(request, ('home.html'), {'books': books})

def add_book(request):
    if request.method=="POST":
        # Data Fetching
        user = request.user
        book_name = request.POST.get("book_name")
        book_author = request.POST.get("book_author")
        book_description = request.POST.get("book_description")
        image_url = upload_image(request)
        book_image_path = image_url.split('/')[-1]
        print("book_image_path: ", book_image_path)
    
        # Create model object and set the data
        book = Book()
        book.user = user
        book.name = book_name
        book.author = book_author
        book.description = book_description
        book.image = book_image_path
        book.date_added = datetime.now()
    
        # Save the object
        book.save()
        
        return redirect("home")

    return render(request, "add_book.html", {})
    
def upload_image(request):
    if request.method == 'POST' and request.FILES['book_image']:
        upload = request.FILES['book_image']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        return file_url

def delete_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    return redirect("home")

def get_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, "update_book.html", {
        'book': book,
    })
    
def update_book(request, book_id):
 
    if request.method == "POST":
         # Data Fetching
        # Data Fetching
        user = request.user
        book_name = request.POST.get("book_name")
        book_author = request.POST.get("book_author")
        book_description = request.POST.get("book_description")
        image_url = upload_image(request)
        book_image_path = image_url.split('/')[-1]
        
        # Create model object and set the data
        book = Book.objects.get(pk=book_id)
        # Create model object and set the data
        book.user = user
        book.name = book_name
        book.author = book_author
        book.description = book_description
        book.image = book_image_path
        #book.date_added = datetime.now()
        # Save the object
        book.save()
        
        return redirect("home")
 
def issue_book(request):
    if request.method=="POST":
        # Data Fetching
        user = request.user
        book = Book()
        student = Student()
        book_id = request.POST.get("book_id")
        if book_id == "":
            messages.warning(request, "Please enter book Id")
        else:
            try:
                book = Book.objects.get(pk=book_id)  
            except book.DoesNotExist:
                messages.warning(request, "Invalid book Id")
    
                
        issuee_id = request.POST.get("issuee_id")
        if issuee_id == "" and book.name != "":
            messages.warning(request, "Please enter issuee Id")
        else:
            try:
                student = Student.objects.get(pk=issuee_id)
            except student.DoesNotExist:
                messages.warning(request, "Invalid issuee Id")

        if book_id != "" and issuee_id != "":
            if book.name != "" and student.name != "":
                if book.is_issued == False:
                    issue_date = request.POST.get("issue_date")
                    renew_date = date_extend(issue_date)
                    
                    # Create model object and set the data
                    issue_book = IssueBook()
                    issue_book.user = user
                    issue_book.book_id = book
                    issue_book.issuee_id = issuee_id
                    issue_book.issue_date = datetime.strptime(issue_date, "%d-%m-%Y")
                    issue_book.renew_date = datetime.strptime(renew_date, "%d-%m-%Y")
                    issue_book.date_added = datetime.now()
                    # Save the object
                    issue_book.save()
                    messages.success(request, "Book issued")
                    
                    book.is_issued = True
                    book.save()
                    return redirect("home")    
                else:
                    messages.success(request, "Book is already issued")
                    
    return render(request, "issue_book.html", {})   

def date_extend(date):
    format = "%d-%m-%Y"  # The format
    current_date = datetime.strptime(date, format)
    end_date = current_date + timedelta(days=16) # Adding 14 days.
    end_date_formatted = end_date.strftime('%d-%m-%Y')
    return end_date_formatted

def return_book(request):
    if request.method=="POST":
        # Data Fetching
        user = request.user
        book = Book()
        book_id = request.POST.get("book_id")
        if book_id == "":
            messages.warning(request, "Please enter book Id")
        else:
            try:
                book = Book.objects.get(pk=book_id)  
            except book.DoesNotExist:
                messages.warning(request, "Invalid book Id")
    
                
        if book_id != "":
            if book.is_issued == True:
                # Create model object and set the data
                issue_book = IssueBook.objects.get(book_id=book_id)
                issue_book.delete()
                #messages.success(request, "Book returned")
                
                book.is_issued = False
                book.user = user
                book.save()
                return redirect("home")    
            else:
                messages.warning(request, "Book is already returned")
                        
    return render(request, "return_book.html", {})   

def renew_book(request):
    if request.method=="POST":
        # Data Fetching
        user = request.user
        book = Book()
        book_id = request.POST.get("book_id")
        if book_id == "":
            messages.warning(request, "Please enter book Id")
        else:
            try:
                book = Book.objects.get(pk=book_id)  
            except book.DoesNotExist:
                messages.warning(request, "Invalid book Id")
    
                
        if book_id != "":
            if book.is_issued == True:
                # Create model object and set the data
                issue_book = IssueBook.objects.get(book_id=book_id)
                issue_date = request.POST.get("issue_date")
                print("issue_date:", issue_date)
                renew_date = date_extend(issue_date)
                
                # Create model object and set the data
                issue_book.user = user
                issue_book.renew_date = datetime.strptime(renew_date, "%d-%m-%Y")
                # Save the object
                issue_book.save()
                #messages.success(request, "Book issued")
                return redirect("home")    
            elif book.is_issued == False:
                messages.warning(request, "Issue Book first") 
            else:
                messages.warning(request, "Book is already returned")
                        
    return render(request, "renew_book.html", {})   
