from django.shortcuts import render , redirect
from .models import *
from .forms import BookForm , CategoryForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST , request.FILES)
        if add_book.is_valid():
            add_book.save()
            
        add_category = CategoryForm(request.POST )
        if add_category.is_valid():
            add_category.save()
    
    context = {
        'booksKey': Book.objects.all,
        'categoryKey' : Category.objects.all,
        'formKey' : BookForm(),
        'formKeyCateg' : CategoryForm,
        'allBooksKey' : Book.objects.filter(active=True).count(),
        'allBooksSoldKey' : Book.objects.filter(status='sold').count(),
        'allBooksRentalKey' : Book.objects.filter(status='rental').count(),
        'allBooksAvailbleKey' : Book.objects.filter(status='available').count()
    }
    return render(request , 'pages/index.html' , context)

def books(request):
    context = {
        'booksKey': Book.objects.all,
        'categoryKey' : Category.objects.all,
    }
    return render(request , 'pages/books.html' , context) 

def update(request , id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_save = BookForm(request.POST , request.FILES ,instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = BookForm(instance=book_id)
        
    context = { 'updateKey' : book_save}
    return render(request , 'pages/update.html' , context)

def delete(request , id):
    book_delete = Book.objects.get(id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')
    return render(request , 'pages/delete.html')