from django.shortcuts import render, HttpResponse
# from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import openai

# Create your views here.
def index(request):
    return render(request, "index.html")

# davinci:ft-personal-2023-02-12-17-35-55
# @csrf_exempt
def reply_bot(request):
    message = request.POST.get("input_data")
    context = '''Keeping in mind the following data, answer the question,also greet the users, tell them that you provide your services on Upwork and Fiverr:
    {"name":"Nayyar Abbas", "services":"web development, web scraping, games development, data visualization", "web development skill":"Master", "game dev skill":"Entry level", "web scraping skill":"master", "data visualization skill":"intermmediate", "web dev tools": "Python, Django, Flask, Php, react", "game dev tools": "Unity", "scraping tools": "python beautifulsoup pandas selenium and requests", "phone number":"+923338043673", "email":"ph0150163@gmail.com"}
    Question: '''
    openai.api_key = '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'
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message,
            temperature=0.9,
            max_tokens=30,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
        )
        print(response)
        response = response['choices'][0]['text']
    except Exception as e:
        print(e)
        response = "Some error occurred, please contact Nayyar Abbas"
    user_message = f'<br clear="both"> <div class="item right"> <div class="msg"> <p>{message}</p> </div> </div>'
    response_data = f'<div class="item"><div class="icon"><i class="fa fa-user"></i></div><div class="msg"><p>{response}</p></div></div>'
    return JsonResponse({"userm": user_message,
                         "resp": response_data,
                         })

