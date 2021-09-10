from django.shortcuts import render
from common.models import BookList
from .models import LoadBook
from common.models import BookList


# Create your views here.
def SearchBarcode(request):
    check = LoadBook.objects.all()

    barcode = request.GET.get('search')
    if barcode:
        search_book = BookList.objects.get(barcode=barcode)
        LoadBook.objects.create(title=search_book.title, barcode=barcode, location=search_book.location)

    data = LoadBook.objects.all()
    return render(request, 'worker/search_screen.html', {'data': data})

def drawmap(request):
    data = LoadBook.objects.all()
    #책 위치값을 한꺼번에 시리얼통신으로 전송하는 코드 작성 필요

    #drawmap에 표시할 제목: 000외 몇 권을 표시하기 위한 코드
    count = len(LoadBook.objects.all())

    searched_book = data[0].title + '외' + str(count-1) + '권'

    return render(request, 'common/draw_map.html', {'searched_book': searched_book, 'type': 'worker'})


    # common에 있는 지도 그리는 template으로 보내는 형태, 근로자가 보내므로 type은 worker인 dictionary 데이터 보냄.
    # 적절하게 searched_book 데이터 바꿀 것.
