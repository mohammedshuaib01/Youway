from django.db.models import Sum

def cart_count(request):
    count=0
    if request.user.is_authenticated:
        if request.user.cart.get_cart_item.count()>0:
          data=request.user.cart.cartitems.filter(is_order_placed=False).values_list('quantity').aggregate(total=Sum('quantity'))
          count=data.get('total')
        #    count=request.user.cart.cartitems.filter(is_order_placed=False).count()

    return {"item_count": count}