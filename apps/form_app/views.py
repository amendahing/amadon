from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "form_app/index.html")

def process(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comments'] = request.POST['comments']

        return redirect("/form_app/results")
    else:
        return redirect("/form_app")

def results(request):
    response = "Hello, I am your first request!"
    return render(request, "form_app/results.html")
