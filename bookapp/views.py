from django.shortcuts import render
from .forms import AuthorForm,BookForm
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.db.models import Q


from django.shortcuts import redirect


# Create your views here.

from .models import Book


def listBook(request):
    books=Book.objects.all()
    
    paginator=Paginator(books,4)
    page_number=request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)
        
    
    return render(request,'listbook.html',{'books':books,'page':page})

def detailsview(request,book_id):
    book=Book.objects.get(id=book_id)
    return render(request,'detailsview.html',{'book':book})

def updateBook(request,book_id):
    book=Book.objects.get(id=book_id)
    
    if request.method=='POST':
        
        form=BookForm(request.POST,request.FILES,instance=book)
        
        if form.is_valid():
            form.save()
            
        return redirect('/')
    else:
            
            form=BookForm(instance=book)
            
    return render(request,'updateview.html',{'form':form})
        

def DeleteView(request,book_id):
    
    book=Book.objects.get(id=book_id)
    
    if request.method=='POST':
        
        book.delete()
        
        return redirect('/')
    
    return render(request,'deleteview.html',{'book':book})

def createBook(request):
    books=Book.objects.all()
    
    if request.method=='POST':
        form=BookForm(request.POST,request.FILES)
        
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
            form=BookForm()
    return render(request,'book.html',{'form':form,'books': books})
    
def create_Author(request):
    if request.method=='POST':
        
        form=AuthorForm(request.POST)
        
        if form.is_valid():
            form.save()
            
        return redirect('/')
    else:
            form=AuthorForm()
            
    return render(request,'author.html',{'form':form})


def index(request):
    return render(request,'base.html')

def search_Book(request):
    query=None
    books=None
    
    if 'q' in request.GET:
        query=request.GET.get('q')
        books=Book.objects.filter(Q(title__icontains=query))
    
    else:
        books=[]
       
        
    return render(request,'search.html',{'books':books,'query':query})

def search_Author(request):
    query=None
    Author=None
    
    if 'q' in request.GET:
        query=request.GET.get('q')
        Author=Book.objects.filter(Q(author__icontains=query))
        
    else:
        Author=[]
        
    return render(request,'searchauthor.html',{'Author':Author,'query':query})
    

        
        

    
    