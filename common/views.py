from django.shortcuts import render



# Create your views here.
def select(request):
    if request.method == 'GET':
        return render(request, 'common/base.html')