
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

# Read
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

# Create
def book_create(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            price=request.POST['price']
        )
        return redirect('book_list')

    return render(request, 'book_form.html')

# Update
def book_update(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.price = request.POST['price']
        book.save()
        return redirect('book_list')

    return render(request, 'book_update.html', {'book': book})

# Delete
def book_delete(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.delete()

    return redirect('book_list')

