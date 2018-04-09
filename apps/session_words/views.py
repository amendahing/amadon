from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
import datetime

def index(request):
    return render(request, "session_words/index.html")


def process(request):
    if request.method == "POST":
        if "word" not in request.POST:
            word = ""
            return redirect("/session_words")
        else:
            word = request.POST['word']
            print word


        if "color" not in request.POST:
            color = "black"
        else:
            color = request.POST['color']


        if not "size" in request.POST:
            size = "16px"
        else:
            size = "32px"
        # if request.POST['size'] == True:
        #     size = "22px"


        if "log" not in request.session:
            request.session['log'] = []

        data = {
            "userword": word,
            "datetime": strftime("%B %d, %Y")+ " at " + strftime("%I:%M %p"),
            "color": color,
            "size": size
        }


        display = request.session['log']
        display.append(data)
        request.session['log'] = display

        print data
        return redirect("/session_words")


def clear(request):
    request.session['log'] = []
    return redirect("/session_words")
