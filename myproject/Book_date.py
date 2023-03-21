import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from myapp.models import Book
from datetime import date

book = Book(title='Python入門', author='山田太郎', published_date=date(2022, 1, 1), isbn='1234567890')
book.save()

books = Book.objects.all()
for book in books:
    print(book.title)
