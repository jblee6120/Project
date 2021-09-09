from django.http.response import HttpResponse
from django.shortcuts import render
from common.models import BookList
from django.contrib import messages

# Create your views here.
def searchbook(request):
    booklist = BookList.objects.all()

    search_key = request.GET.get('search_key')
    if search_key:
        booklist = booklist.filter(title__icontains=search_key)

    return render(request, 'visitor/search_screen.html',{'booklist':booklist})


# def searchedbooklist(request):
#     all_book_list = BookList.objects.all()
#     search_key = request.GET.get('search_key')
#     if search_key :
#         booklist = all_book_list.filter(title__icontains=search_key)

#         return render(request, 'visitor/searched_booklist.html', {'booklist':booklist})

def drawmap(request, id):
    searched_book = BookList.objects.get(id=id)
    return render(request, 'common/draw_map.html', {'searched_book':searched_book, 'type' : 'visitor'} )
    #common에 있는 지도 그리는 template으로 보내는 형태, 이용자가 보내므로 type은 visitor인 dictionary 데이터 보냄.