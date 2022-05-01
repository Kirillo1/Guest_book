from django.shortcuts import render, redirect

from book.forms import GuestBookForm
from book.models import GuestBook


def index_view(request):
    guest_books = GuestBook.objects.filter(status="active").order_by("-time_of_creation")
    return render(request, 'index.html', {'guest_books': guest_books})


def create_book_view(request):
    if request.method == 'GET':
        form = GuestBookForm()
        return render(request, 'book_create.html', {"form": form})
    else:
        form = GuestBookForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            mail = form.cleaned_data.get('mail')
            post_text = form.cleaned_data.get('post_text')
            new_business = GuestBook.objects.create(name=name, mail=mail, post_text=post_text)
            return redirect("index")
        return render(request, 'book_create.html', {"form": form})


def book_update(request, pk):
    guest_book = GuestBook.objects.get(pk=pk)
    if request.method == 'GET':
        form = GuestBookForm(initial={
            'name': guest_book.name,
            'mail': guest_book.mail,
            'post_text': guest_book.post_text,
        })
        return render(request, 'book_update.html', {'guest_book': guest_book, 'form': form})
    else:
        form = GuestBookForm(data=request.POST)
        if form.is_valid():
            guest_book.name = form.cleaned_data.get('name')
            guest_book.mail = form.cleaned_data.get('mail')
            guest_book.post_text = form.cleaned_data.get('post_text')
            guest_book.save()
            return redirect("index")
        return render(request, 'book_update.html', {'guest_book': guest_book, 'form': form})
