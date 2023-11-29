from django.shortcuts import render

# Create your views here.
def bootstrap1(request):
    return render(request,'bootstrap1.html')
def carousel_indicators(request):
    return render(request,'carousel_indicators.html')
def carousels(request):
    return render(request,'carousels.html')
def breadcrumb(request):
    return render(request,'breadcrumb.html')