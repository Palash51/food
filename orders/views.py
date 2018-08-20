from django.shortcuts import render, redirect
from django.views import generic
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem, Order
from .task import order_created
from account.models import OrderMeal, UserProfile


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         customer=request.user.profile.username,
                                         product=item['product'],
                                         price=item['price'],
                                         calories=item['product'].calories,
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()
            order_created(order.id)
            request.session['order_id'] = order.id
            # redirect to the payment
            return redirect('shop:product_list')
            # return redirect('payment:process')

    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/create.html',
                  {'cart': cart, 'form': form})


class OrderHistory(generic.ListView):
    """orders list views"""
    template_name = 'dashboard/table.html'
    model = OrderItem

    def get_queryset(self):
        """"""
        queryset = OrderItem.objects.filter(
            customer=self.request.user.profile.username)
        return queryset

class ManageOrders(generic.ListView):
    """"""
    template_name = 'orders/manage_order.html'
    model = OrderItem

    def get_queryset(self):
      """"""
      all_orders = OrderItem.objects.all()
      # import pdb
      # pdb.set_trace()
      return all_orders

