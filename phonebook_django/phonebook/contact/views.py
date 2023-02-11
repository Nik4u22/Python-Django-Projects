from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from .form import ContactBookForm, SearchForm
from django.db.models import Q
from .models import ContactBook

# Create your views here.
def loginview(request):
    authenticationForm = AuthenticationForm()
    if request.method == "POST":
        authenticationForm = AuthenticationForm(request, data=request.POST or None)
        if authenticationForm.is_valid():
            username = authenticationForm.cleaned_data["username"]
            password = authenticationForm.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user=user)
                return redirect("index")
        else:
            print(authenticationForm.errors)
    
    return render(request, ("login.html"), {"authenticationForm": authenticationForm})
    
def index(request):
    contacts = ContactBook.objects.filter(user=request.user).order_by("-created")
    searchForm = SearchForm()
    if request.method=="POST":
        searchForm = SearchForm(request.POST or None)
        if searchForm.is_valid():
            search_term = request.POST.get("search")
            return redirect("search", search_term)
    else:
        print(searchForm.errors)
    return render(request,template_name="index.html", context={"contacts" : contacts, "searchForm" : searchForm})

def registration(request):
    userCreationForm = UserCreationForm()
    if request.method == "POST":
        userCreationForm = UserCreationForm(request.POST or None)
        if userCreationForm.is_valid():
            username = userCreationForm.cleaned_data["username"]
            password = userCreationForm.cleaned_data["password1"]
            userCreationForm = userCreationForm.save()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user=user)
                return redirect("index")
        else:
            print(userCreationForm.errors)
            
    return render(request, ('registration.html'), {"userCreationForm": userCreationForm})

def create(request):
    contactBookForm = ContactBookForm()
    if request.method == 'POST':
        contactBookForm = ContactBookForm(request.POST or None, request.FILES or None)
        if contactBookForm.is_valid():
            contactBookForm = contactBookForm.save(commit=False)
            contactBookForm.user = request.user
            contactBookForm.save()
            return redirect("index")

        else:
            print(contactBookForm.errors)
            
    return render(request, ('create.html'), {"contactBookForm": contactBookForm})

def contactBookDetail(request, pk):
    contact = ContactBook.objects.get(id=pk)
    return render (request, ('details.html'), {'contact': contact})

def search(request, search_term):
    filteredData = ContactBook.objects.filter(Q(mobile_number__icontains=search_term) | Q(name__icontains=search_term))
    print(filteredData)
    return render(request,('search.html'), {"filteredData" : filteredData})