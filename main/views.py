from django.shortcuts import render, get_object_or_404

from .models import WishList
from .forms import ProductForm


def index(request):
    return render(request,'index.html',{})

def about(request):
    return render(request,'about.html',{})

def list_page(request, pk):
    """
    View page the wishlist.
    """
    wishlist = get_object_or_404(WishList, pk=pk)
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        product = form.save()
        wishlist.product.add(product)
        wishlist.save()
    elif request.method == 'GET':
        form = ProductForm

    return render(
        request,
        'wishlist.html',
        {
            'wishlist': wishlist,
            'is_owner_list': wishlist.owner == request.user,
            'form': form,
        }
    )
