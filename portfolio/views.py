from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def reply_bot(request):
    message = request.POST.get("inputData")



    return HttpResponse(response_data)