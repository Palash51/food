from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views import generic
from django.http import HttpResponse
from notify.signals import notify
from django.contrib.auth.models import User, Group

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
            import pdb
            pdb.set_trace()
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


class OrderAcceptView(generic.View):
    """order accept"""
    template_name = 'orders/manage_order.html'
    model = OrderItem
    
    def post(self, request, *args, **kwargs):
        """url to redirect to on success"""
        order_id = request.POST['accept']
        order = get_object_or_404(
            OrderItem, pk=order_id)
        
        customer_user = User.objects.get(username=order.customer)
        notify.send(request.user, recipient=customer_user, actor=user_to_send,
                verb='Order Accepted', nf_type='followed_by_one_user')
        messages.success(
            self.request, "You have successfully Accepted the order, start cooking")
        return redirect(reverse('orders:manage'))


class OrderDeleteView(generic.View):
    """order delete"""
    model = OrderItem

    def post(self, request, *args, **kwargs):
        """Delete a Candidate"""
        order_id = request.POST['remove']
        order = get_object_or_404(
            OrderItem, pk=order_id)
        order.delete()
        return redirect(reverse('orders:manage'))


