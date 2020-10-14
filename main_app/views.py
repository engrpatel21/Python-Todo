from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from .models import WishList

# Create your views here.
def home(request):
    wishs = WishList.objects.all()
    return render(request, 'home.html', {'wishs':wishs})

class AddWish(CreateView):
    model = WishList
    fields = '__all__'
    success_url = '/'
    
def delete_wish(request, wishlist_id):
    wish = WishList.objects.get(id=wishlist_id).delete()
    return redirect('home')