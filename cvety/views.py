from django.shortcuts import render, get_object_or_404
from .models import Cvety
from  orders.forms import OrderForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
# from .forms import CvetyFilterForm

# Create your views here.

def cvety_list(request):
    cvetys = Cvety.objects.all()
    form = OrderForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("?sended=True")
    return render(request, "cvety/cvety_list.html", {'cvetys': cvetys, 'form': form, "sended": request.GET.get("sended", False)})




# def cvety_list(request):
#     cvetys = Cvety.objects.all()
#     form = OrderForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("{}?sended=True".format(reverse("cvety")))
    # form = CvetyFilterForm(request.GET)
    # if form.is_valid():
    #     if form.cleaned_data["min_price"]:
    #         cvetys=cvetys.filter(price__gte=form.cleaned_data["min_price"])
    #     if form.cleaned_data["max_price"]:
    #         cvetys=cvetys.filter(price__lte=form.cleaned_data["max_price"])
    #     if form.cleaned_data["ordering"]:
    #         cvetys = cvetys.order_by(form.cleaned_data["ordering"])
    # return render(request, "cvety/cvety_list.html", {"cvetys": cvetys, "form": form, "sended": request.GET.get("sended", False)})

def cvety_ditail(request, cvety_id):
    cvety = get_object_or_404(Cvety, id=cvety_id)
    form = OrderForm(request.POST or None, initial={"cvety": cvety })
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("{}?sended=True".format(reverse("cvety", kwargs={"cvety_id": cvety_id})))
    return  render(request, "cvety/cvety_ditail.html", {
        "cvety": cvety,
        "form": form,
        "sended": request.GET.get("sended", False)
        })

