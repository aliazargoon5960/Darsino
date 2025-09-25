from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .cart_module import Cart
from course_module.models import Course
from .models import Order, OrderDetail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from .models import DiscountCode


class CartDetailView(View):
    def get(self, request):
        cart = Cart(request) 
        return render(request, "cart_module/cart_detail.html", {'cart': cart})

    def post(self, request):
        cart = Cart(request)
        return render(request, "cart_module/cart_detail.html", {'cart': cart})


class CartAddView(View):
    def post(self, request, pk):
        course = get_object_or_404(Course, id=pk)
        cart = Cart(request)
        cart.add(course)  

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'message': 'دوره با موفقیت به سبد خرید اضافه شد 🎉'})
        return redirect('course_module:course_detail', slug=course.slug)


class CartDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        cart = Cart(request)
        cart.delete(id)
        return redirect('cart_module:cart_detail')



class OrderCreationView(LoginRequiredMixin, View):
    def get(self, request):
        return redirect("cart_module:cart_detail")
    
    
    def post(self, request):
        cart = Cart(request)

        if not cart.cart and not cart.total_price():
            return redirect('cart_module:cart_detail')

        order, created = Order.objects.get_or_create(
            user=request.user,
            is_paid=False,
            defaults={'total_price': cart.total_price()}
        )

        if created: 
            for item in cart:
                OrderDetail.objects.create(
                    order=order,
                    course=item['course'],
                    price=item['price']
                )

        return redirect("cart_module:checkout" , order.id)


class CheckOutView(LoginRequiredMixin, View):
    def get(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        return render(request, "cart_module/checkout.html", {'order' : order})

    def post(self, request,pk):
        order = get_object_or_404(Order, id=pk)
        return render(request, "cart_module/checkout.html", {'order' : order})






class ApplyDiscountView(LoginRequiredMixin, View):
    def post(self, request, pk):
        order = get_object_or_404(Order, id=pk, user=request.user, is_paid=False)
        code = request.POST.get('code', '').strip()
        try:
            discount = DiscountCode.objects.get(code__iexact=code, active=True)
        except DiscountCode.DoesNotExist:
            discount = None

        if discount:
            if discount.quantity > 0:
                order.discount = discount
                order.save()

                discount.quantity -= 1
                discount.save()
            else:
                pass

        return redirect('cart_module:checkout', pk=order.id)
