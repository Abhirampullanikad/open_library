
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.urls import reverse
from bookapp.models import Book
from Account.models import UserProfile
from .models import Cart,CartItem
import stripe
from django.conf import settings



def userlistBook(request):
    books=Book.objects.all()
    
        
    
    return render(request,'user/userinterface.html',{'books':books})

def userDetailView(request,book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'user/userdetail.html', {'book': book})




def search_Book(request):
    query=None
    books=None
    
    if 'q' in request.GET:
        query=request.GET.get('q')
        books=Book.objects.filter(Q(title__icontains=query))
    
    else:
        books=[]
       
        
    return render(request, 'user/search_results.html', {
        'books': books,
        'query': query
    })


def user(request):
    books=Book.objects.all()
    return render(request,'user/userinterface.html',{books:'books'})



def add_to_cart(request, book_id):
    
    if 'username' not in request.session:
        return redirect('Account:login')

    username = request.session['username']
    user = UserProfile.objects.get(username=username)
   
    book = Book.objects.get(id=book_id)

    if book.quantity > 0:
        cart_obj, created = Cart.objects.get_or_create(user=user)
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart_obj, book=book)

        if not item_created:
            cart_item.quantity += 1
            cart_item.save()

    return redirect('userapp:viewcart')

def view_cart(request):
    
    if 'username' not in request.session:
        return redirect('Account:login')

    username = request.session['username']
    user = UserProfile.objects.get(username=username)
    
    cart,created=Cart.objects.get_or_create(user=user)
    cart_items=cart.cartitem_set.all()
    cart_item=CartItem.objects.all()
    total_price=sum(item.book.price*item.quantity for item in cart_items)
    total_items=cart_items.count()
    
    
    context={'cart_items':cart_items,'cart_item':cart_item,'total_price':total_price,'total_items':total_items}
    return render(request,'user/cart.html',context)

def increase_quantity(request,item_id):
    cart_item=CartItem.objects.get(id=item_id)
    if cart_item.quantity<cart_item.book.quantity:
        
        cart_item.quantity+=1
        cart_item.save()
    return redirect('userapp:viewcart')

def decrease_quantity(request,item_id):
    cart_item=CartItem.objects.get(id=item_id)
    if cart_item.quantity>1:
        
        cart_item.quantity-=1
        cart_item.save()
        
    return redirect('userapp:viewcart')

def remove_from_cart(request,item_id):
    
    try:
        
        cart_item=CartItem.objects.get(id=item_id)
        cart_item.delete()
        
    except CartItem.DoesNotExist:
        
        pass
    
    return redirect('userapp:viewcart')
          





def create_checkout_session(request):
    cart_items = CartItem.objects.all()
    
    if cart_items:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        
        if request.method == 'POST':
            line_items = []
            for cart_item in cart_items:
                if cart_item.book:
                    line_item = {
                        'price_data': {
                            'currency': 'inr',
                            'unit_amount': int(cart_item.book.price * 100),
                            'product_data': {
                                'name': cart_item.book.title
                            },
                        },
                        'quantity': 1
                    }
                    line_items.append(line_item)
            
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=line_items,
                mode='payment',
                success_url=request.build_absolute_uri(reverse('userapp:success')),
                cancel_url=request.build_absolute_uri(reverse('userapp:cancel')),
            )
            
            return redirect(checkout_session.url, code=303)
    

    
     # Fallback redirect if no cart items

def success(request):
    cart_items = CartItem.objects.all()
    
    for cart_item in cart_items:
        product = cart_item.book
        if product.quantity >= cart_item.quantity:
            product.quantity -= cart_item.quantity
            product.save()
            
    cart_items.delete()
    
    return render(request, 'user/success.html')

def cancel(request):
    return render(request, 'user/cancel.html')

