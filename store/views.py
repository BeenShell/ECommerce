from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *
from .utils import cookieCart, cartData, guestOrder





def search_results(request):
    data = cartData(request)
    cartItems = data['cartItems']

    if request.method=='POST':
        searched= request.POST['searched']
        cartItems = data['cartItems']
        product = Product.objects.filter(description__contains=searched)
        context = {'cartItems': cartItems, 'searched': searched, 'product': product}
        return render(request, 'store/search_results.html', context)

    else:
        context = {'cartItems': cartItems}
        return render(request, 'store/search_results.html', context)



def view_product(request):

    data = cartData(request)
    cartItems = data['cartItems']
    context = {'cartItems': cartItems}
    return render(request, 'store/view.html', context)



def store(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.filter(type=Product.FEATURED)
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)


def cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)


def checkout(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)


def makeup(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    makeup = Product.objects.filter(type=Product.MAKEUP)
    context = {'makeup': makeup, 'cartItems': cartItems}
    return render(request, 'store/makeup.html', context)


def skincare(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    skincare = Product.objects.filter(type=Product.SKINCARE)
    context = {'skincare': skincare, 'cartItems': cartItems}
    return render(request, 'store/skincare.html', context)


def hair(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    hair = Product.objects.filter(type=Product.HAIR)
    context = {'hair': hair, 'cartItems': cartItems}
    return render(request, 'store/hair.html', context)


def fragrance(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    fragrance = Product.objects.filter(type=Product.FRAGRANCE)
    context = {'fragrance': fragrance, 'cartItems': cartItems}
    return render(request, 'store/fragrance.html', context)


def toolsandbrushes(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    toolsandbrushes = Product.objects.filter(type=Product.TOOL_BRUSH)
    context = {'toolsandbrushes': toolsandbrushes, 'cartItems': cartItems}
    return render(request, 'store/toolsandbrushes.html', context)


def bathandbody(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    bathandbody = Product.objects.filter(type=Product.BATHBODY)
    context = {'bathandbody': bathandbody, 'cartItems': cartItems}
    return render(request, 'store/bathandbody.html', context)


def salesandclearance(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    salesandclearance = Product.objects.filter(type=Product.SALES)
    context = {'salesandclearance': salesandclearance, 'cartItems': cartItems}
    return render(request, 'store/salesandclearance.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment submitted..', safe=False)







###Sub Pages Start Here###


def makeup_face_foundation(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    makeup_face_foundation = Product.objects.filter(type=Product.MAKEUP_FACE_FOUNDATION)
    context = {'make_faceup_foundation': makeup_face_foundation, 'cartItems': cartItems}
    return render(request, 'store/makeup_face_foundation.html', context)


def makeup_face_powder(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    makeup_face_powder = Product.objects.filter(type=Product.MAKEUP_FACE_POWDER)
    context = {'makeup_face_powder': makeup_face_powder, 'cartItems': cartItems}
    return render(request, 'store/makeup_face_powder.html', context)


def makeup_face_concealer(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    makeup_face_concealer = Product.objects.filter(type=Product.MAKEUP_FACE_CONCEALER)
    context = {'makeup_face_concealer': makeup_face_concealer, 'cartItems': cartItems}
    return render(request, 'store/makeup_face_concealer.html', context)


def makeup_face_highlighter(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    makeup_face_highlighter = Product.objects.filter(type=Product.MAKEUP_FACE_HIGHLIGHTER)
    context = {'makeup_face_highlighter': makeup_face_highlighter, 'cartItems': cartItems}
    return render(request, 'store/makeup_face_highlighter.html', context)



def makeup_face_settingspray(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    makeup_face_settingspray = Product.objects.filter(type=Product.MAKEUP_FACE_SETTINGSPRAY)
    context = {'makeup_face_settingspray': makeup_face_settingspray, 'cartItems': cartItems}
    return render(request, 'store/makeup_face_settingspray.html', context)


def makeup_face_primer(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    makeup_face_primer = Product.objects.filter(type=Product.MAKEUP_FACE_PRIMER)
    context = {'makeup_face_primer': makeup_face_primer, 'cartItems': cartItems}
    return render(request, 'store/makeup_face_primer.html', context)


def makeup_face_contour(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    makeup_face_contour = Product.objects.filter(type=Product.MAKEUP_FACE_CONTOUR)
    context = {'makeup_face_contour': makeup_face_contour, 'cartItems': cartItems}
    return render(request, 'store/makeup_face_contour.html', context)


def makeup_eyes_mascara(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    makeup_eyes_mascara = Product.objects.filter(type=Product.MAKEUP_EYES_MASCARA)
    context = {'makeup_eyes_mascara': makeup_eyes_mascara, 'cartItems': cartItems}
    return render(request, 'store/makeup_eyes_mascara.html', context)


def makeup_eyes_eyeliner(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    makeup_eyes_eyeliner = Product.objects.filter(type=Product.MAKEUP_EYES_EYELINER)
    context = {'makeup_eyes_eyeliner': makeup_eyes_eyeliner, 'cartItems': cartItems}
    return render(request, 'store/makeup_eyes_eyeliner.html', context)


def makeup_eyes_eyebrow(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    makeup_eyes_eyebrow = Product.objects.filter(type=Product.MAKEUP_EYES_EYEBROW)
    context = {'makeup_eyes_eyebrow': makeup_eyes_eyebrow, 'cartItems': cartItems}
    return render(request, 'store/makeup_eyes_eyebrow.html', context)


def makeup_eyes_eyeshadow(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    makeup_eyes_eyeshadow = Product.objects.filter(type=Product.MAKEUP_EYES_EYESHADOW)
    context = {'makeup_eyes_eyeshadow': makeup_eyes_eyeshadow, 'cartItems': cartItems}
    return render(request, 'store/makeup_eyes_eyeshadow.html', context)


def makeup_eyes_eyepalettes(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    makeup_eyes_eyepalettes = Product.objects.filter(type=Product.MAKEUP_EYES_EYEPALETTES)
    context = {'makeup_eyes_eyepalettes': makeup_eyes_eyepalettes, 'cartItems': cartItems}
    return render(request, 'store/makeup_eyes_eyepalettes.html', context)


def makeup_lip_lipstick(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    makeup_lip_lipstick = Product.objects.filter(type=Product.MAKEUP_LIP_LIPSTICK)
    context = {'makeup_lip_lipstick': makeup_lip_lipstick, 'cartItems': cartItems}
    return render(request, 'store/makeup_lip_lipstick.html', context)


def makeup_lip_lipgloss(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    makeup_lip_lipgloss = Product.objects.filter(type=Product.MAKEUP_LIP_LIPGLOSS)
    context = {'makeup_lip_lipgloss': makeup_lip_lipgloss, 'cartItems': cartItems}
    return render(request, 'store/makeup_lip_lipgloss.html', context)


def makeup_lip_lipliner(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    makeup_lip_lipliner = Product.objects.filter(type=Product.MAKEUP_LIP_LIPLINER)
    context = {'makeup_lip_lipliner': makeup_lip_lipliner, 'cartItems': cartItems}
    return render(request, 'store/makeup_lip_lipliner.html', context)


def body_lotion(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    body_lotion = Product.objects.filter(type=Product.BODY_LOTION)
    context = {'body_lotion': body_lotion, 'cartItems': cartItems}
    return render(request, 'store/body_lotion.html', context)


def body_mist(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    body_mist = Product.objects.filter(type=Product.BODY_MIST)
    context = {'body_mist': body_mist, 'cartItems': cartItems}
    return render(request, 'store/body_mist.html', context)


def moisturizer(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    moisturizer = Product.objects.filter(type=Product.MOISTURIZER)
    context = {'moisturizer': moisturizer, 'cartItems': cartItems}
    return render(request, 'store/moisturizer.html', context)


def candles(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    candles = Product.objects.filter(type=Product.CANDLES)
    context = {'candles': candles, 'cartItems': cartItems}
    return render(request, 'store/candles.html', context)


def supplies_gift_sets(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    supplies_gift_sets = Product.objects.filter(type=Product.SUPPLIES_GIFT_SETS)
    context = {'supplies_gift_sets': supplies_gift_sets, 'cartItems': cartItems}
    return render(request, 'store/supplies_gift_sets.html', context)


def fragrance_women(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    fragrance_women = Product.objects.filter(type=Product.FRAGRANCE_WOMEN)
    context = {'fragrance_women': fragrance_women, 'cartItems': cartItems}
    return render(request, 'store/fragrance_women.html', context)


def fragrance_men(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    fragrance_men = Product.objects.filter(type=Product.FRAGRANCE_MEN)
    context = {'fragrance_men': fragrance_men, 'cartItems': cartItems}
    return render(request, 'store/fragrance_men.html', context)


def fragrance_kids(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    fragrance_kids = Product.objects.filter(type=Product.FRAGRANCE_KIDS)
    context = {'fragrance_kids': fragrance_kids, 'cartItems': cartItems}
    return render(request, 'store/fragrance_kids.html', context)


def skincare_cleanser(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    skincare_cleanser = Product.objects.filter(type=Product.SKINCARE_CLEANSER)
    context = {'skincare_cleanser': skincare_cleanser, 'cartItems': cartItems}
    return render(request, 'store/skincare_cleanser.html', context)


def skincare_lotion(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    skincare_lotion = Product.objects.filter(type=Product.SKINCARE_LOTION)
    context = {'skincare_lotion': skincare_lotion, 'cartItems': cartItems}
    return render(request, 'store/skincare_lotion.html', context)


def skincare_reatments(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    skincare_reatments = Product.objects.filter(type=Product.SKINCARE_REATMENTS)
    context = {'skincare_reatments': skincare_reatments, 'cartItems': cartItems}
    return render(request, 'store/skincare_reatments.html', context)

