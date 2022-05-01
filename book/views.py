from django.shortcuts import render

from book.models import GuestBook


def index_view(request):
    guest_books = GuestBook.objects.filter(status="active").order_by("-time_of_creation")
    return render(request, 'index.html', {'guest_books': guest_books})
