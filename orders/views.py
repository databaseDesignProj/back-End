from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Cafe, Menu, Order, OrderDetails, Basket, BasketDetails

# '홍길동' 사용자로 자동 로그인하는 뷰
def user_login(request):
    user, created = User.objects.get_or_create(username='홍길동')
    login(request, user)
    return HttpResponse("홍길동으로 로그인되었습니다.")

# 카페 선택 뷰
@login_required
def select_cafe(request):
    cafes = Cafe.objects.all()
    return render(request, 'select_cafe.html', {'cafes': cafes})

# 메뉴 선택 뷰
@login_required
def select_menu(request, cafe_id):
    menus = Menu.objects.filter(cafe_id=cafe_id)
    return render(request, 'select_menu.html', {'menus': menus})

# 장바구니에 추가 뷰
@login_required
def add_to_basket(request, menu_id):
    menu = Menu.objects.get(id=menu_id)
    # 장바구니 로직
    return HttpResponse(f"{menu.name} 장바구니에 추가됨")

# 장바구니 보기 뷰
@login_required
def view_basket(request):
    # 장바구니 로직
    basket = {} # 임시 예시
    return render(request, 'basket.html', {'basket': basket})

# 결제 및 주문 처리 뷰
@login_required
def checkout(request):
    # 결제 및 주문 처리 로직
    return HttpResponse("결제 및 주문 처리 완료")

# 주문 내역 보기 뷰
@login_required
def view_order_history(request):
    orders = Order.objects.filter(customer=request.user).order_by('-order_time')
    order_details = {order: OrderDetails.objects.filter(order=order) for order in orders}
    return render(request, 'order_history.html', {'orders': orders, 'order_details': order_details})
