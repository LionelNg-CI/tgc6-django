from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Book, Author
from .forms import BookForm, AuthorForm


# Create your views here.


def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.template.html', {'books': books})


def authors(request):
    authors = Author.objects.all()
    return render(request, 'books/authors.template.html', {'authors': authors})


def create_book(request):
    if request.method == 'POST': #1
        create_form = BookForm(request.POST) #2

        # check if the form has valid values
        if create_form.is_valid(): #3
            create_form.save() #4
            return redirect(reverse(index))
        else:
            # 5. if does not have valid values, re-render the form
            return render(request, 'books/create.template.html', {
                'form': create_form
            })
    else:
        create_form = BookForm()
        return render(request, 'books/create.template.html', {
            'form': create_form
        })

def create_author(request):
    if request.method == 'POST': #1
        create_form = AuthorForm(request.POST) #2

        # check if the form has valid values
        if create_form.is_valid(): #3
            create_form.save() #4
            return redirect(reverse(index))
        else:
            # 5. if does not have valid values, re-render the form
            return render(request, 'books/create.author.template.html', {
                'form': create_form
            })
    else:
        create_form = AuthorForm()
        return render(request, 'books/create.author.template.html', {
            'form': create_form
        })


def update_book(request, book_id):
    # 1. retrieve the book which we are editing
    book_being_updated = get_object_or_404(Book, pk=book_id)

    # 2 - create the form and fill it with data from book instance
    book_form = BookForm(instance=book_being_updated)

    return render(request, 'books/update.template.html', {
        "form": book_form
    })