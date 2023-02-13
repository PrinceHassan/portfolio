from django.shortcuts import render, HttpResponse
# from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import openai

# Create your views here.
def index(request):
    return render(request, "index.html")


# @csrf_exempt
def reply_bot(request):
    message = request.POST.get("input_data")
    openai.api_key = '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'
    try:
        response = openai.Completion.create(
            model="davinci:ft-personal-2023-02-12-17-35-55",
            prompt=message,
            temperature=0.9,
            max_tokens=30,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
        )
        print(response)
        response = response['choices'][0]['text'].split('END')[0]
    except Exception as e:
        print(e)
        response = "Some error occurred, please contact Nayyar Abbas"
    user_message = f'<br clear="both"> <div class="item right"> <div class="msg"> <p>{message}</p> </div> </div>'
    response_data = f'<div class="item"><div class="icon"><i class="fa fa-user"></i></div><div class="msg"><p>{response}</p></div></div>'
    return JsonResponse({"userm": user_message,
                         "resp": response_data,
                         })

