from django.shortcuts import render
from myapp.forms import PersonForm
from django.http import HttpResponse
from myapp.models import Book
from django.utils.html import strip_tags, escape
from pykakasi import kakasi



def ruby(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')
        # ルビを振る処理を実装
        output_html = 'ルビが振られたHTML'  # ここは実際の処理に合わせて書き換える

        return JsonResponse({'output_html': output_html})

    return JsonResponse({'error': 'POSTメソッドでアクセスしてください'})


def indexs(request):
    if request.method == 'POST':
        # フォームからテキストを取得
        text = request.POST.get('text', '')

        # ルビを振る処理
        kakasi_ = kakasi()
        kakasi_.setMode('J', 'H')
        kakasi_.setMode('K', 'H')
        kakasi_.setMode('H', 'a')
        kakasi_.setMode('s', True)
        kakasi_.setMode('C', False)
        conv = kakasi_.getConverter()
        ruby_text = escape(strip_tags(text))
        ruby_text = conv.do(ruby_text)
        ruby_text = ruby_text.replace('[', '<ruby><rb>')
        ruby_text = ruby_text.replace(']', '</rb><rt></rt></ruby>')

        # 結果をテンプレートに渡す
        context = {'result': ruby_text}
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')

def my_view(request):
    return HttpResponse('Hello, Worlds!')

def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PersonForm()
    return render(request, 'add_person.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})