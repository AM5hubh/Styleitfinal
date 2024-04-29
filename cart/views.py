from django.shortcuts import render ,get_object_or_404
from .cart import Cart
from home.models import ShopIT
from django.http import JsonResponse

def cart_summary(request):
    cart =  Cart(request)
    cart_products = cart.get_prods()
    context = {"cart_products":cart_products}
    return render(request, 'cart_summary.html', context)

def cart_add(request):
    cart =  Cart(request)
    if request.POST.get('action')=='post':
        shopIT_id=str(request.POST.get('id'))  

        product = get_object_or_404(ShopIT, id=shopIT_id)

        cart.add(product=product)
        # response = JsonResponse({'name': product.name })
        # cart.__len__()
        cart_quantity=cart.__len__()
        response = JsonResponse({'name': product.name, 'qty': cart_quantity})
        # response =JsonResponse({'qty': cart_quantity })
        return response
    # return render ( request, 'product_page.html')    
    
    

def cart_delete(request):
    pass

def cart_update(request):
    pass