from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'totalitem' not in request.session:
        request.session['totalitem'] = []

    if 'totalprice' not in request.session:
        request.session['totalprice'] = []
    return render(request, "amadon/index.html")

def process(request):
    if request.method == "POST":
        print "PURCHASED!", request.POST['amount'], request.POST['product']
        amount = int(request.POST['amount'])
        product = request.POST['product']

        if request.POST['product'] == "tshirt":
            price = 19
        if request.POST['product'] == "sweater":
            price = 29
        if request.POST['product'] == "cup":
            price = 4
        if request.POST['product'] == "book":
            price = 50

        total = price * amount
        request.session['totalitem'].append(amount)
        request.session['totalprice'].append(total)
        request.session['price'] = total
        return redirect("/amadon/checkout")

def checkout(request):
    sum = 0
    totalprice = 0

    for i in request.session['totalitem']:
        sum = sum + i

    for x in request.session['totalprice']:
        totalprice = totalprice + x

    request.session['totalitemsum'] = sum
    request.session['grandtotalprice'] = totalprice

    return render(request, "amadon/checkout.html")
