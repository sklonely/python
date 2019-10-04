from django.shortcuts import render, get_object_or_404
from .models import Vendor
from .forms import VendorForm, RawVendorForm


# Create your views here.
def index(request):
    # 今天先不探討什麼是 render，先記得它會去撈 test.html
    vendor_list = Vendor.objects.all()  # 把所有 Vendor 的資料取出來
    context = {'vendor_list': vendor_list}  # 建立 Dict對應到Vendor的資料，
    return render(request, 'detail.html', context)


def vendor_create_view(request):

    form = RawVendorForm(request.POST or None)
    if form.is_valid():

        form = RawVendorForm()

    context = {'form': form}
    return render(request, "vendor_create.html", context)


def vendor_create_view_ok(request):

    form = VendorForm(request.POST or None)
    if form.is_valid():
        form = VendorForm()

    context = {'form': form}
    return render(request, "vendor_create.html", context)


def singleVendor(request, id):
    vendor_list = get_object_or_404(Vendor, id=id)
    # try:
    #     vendor_list = Vendor.objects.get(id=id)
    # except Vendor.DoesNotExist:
    #     raise Http404

    context = {'vlist': vendor_list}

    return render(request, 'details.html', context)
