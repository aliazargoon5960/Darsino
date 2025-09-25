from course_module.models import Course
from .models import Order, OrderDetail

CART_SESSION_ID = 'cart'

class Cart:
    def __init__(self, request):
        self.session = request.session
        self.user = getattr(request, 'user', None)

        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = {}
            self.session[CART_SESSION_ID] = cart

        self.cart = cart

    def unique_id_generator(self, id):
        return f'{id}'

    def add(self, course):
        unique = self.unique_id_generator(course.id)

        if unique not in self.cart:
            self.cart[unique] = {'price': str(course.price), 'id': course.id}
            self.save()

        if self.user and self.user.is_authenticated:
            order, created = Order.objects.get_or_create(user=self.user, is_paid=False)
            OrderDetail.objects.get_or_create(
                order=order,
                course=course,
                defaults={'price': course.price}
            )

    def delete(self, id):
        if id in self.cart:
            del self.cart[id]
            self.save()

        if self.user and self.user.is_authenticated:
            order = Order.objects.filter(user=self.user, is_paid=False).first()
            if order:
                OrderDetail.objects.filter(order=order, course_id=id).delete()


    def remove_cart(self):
        if CART_SESSION_ID in self.session:
            del self.session[CART_SESSION_ID]
            self.save()

        if self.user and self.user.is_authenticated:
            Order.objects.filter(user=self.user, is_paid=False).delete()

    def total_price(self):
        if self.user and self.user.is_authenticated:
            order = Order.objects.filter(user=self.user, is_paid=False).first()
            if order:
                return sum(item.price for item in order.items.all())
            return 0
        else:
            return sum(int(item['price']) for item in self.cart.values())

    def __iter__(self):
        if self.user and self.user.is_authenticated:
            order = Order.objects.filter(user=self.user, is_paid=False).first()
            if order:
                for item in order.items.all():
                    yield {
                        'course': item.course,
                        'price': item.price,
                        'total': item.price,
                        'unique_id': self.unique_id_generator(item.course.id)
                    }
        else:
            cart = self.cart.copy()
            for item in cart.values():
                course = Course.objects.get(id=int(item['id']))
                item['course'] = course
                item['total'] = int(item['price'])
                item['unique_id'] = self.unique_id_generator(course.id)
                yield item

    def save(self):
        self.session.modified = True