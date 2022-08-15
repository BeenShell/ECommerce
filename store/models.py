from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    phone = models.FloatField(max_length=25, null=True)
    def __str__(self):
        return str(self.name)

class Product(models.Model):
    FEATURED = 'Featured'
    BATHBODY = 'BathBody'
    FRAGRANCE = 'Fragrance'
    HAIR = 'Hair'
    MAKEUP = 'Makeup'
    SALES = 'Sales'
    SKINCARE = 'Skincare'
    TOOL_BRUSH = 'ToolBrush'
    MAKEUP_FACE_FOUNDATION='Foundation'
    MAKEUP_FACE_POWDER='Face Powder'
    MAKEUP_FACE_CONCEALER='Face Concealer'
    MAKEUP_FACE_HIGHLIGHTER='Face Highlighter'
    MAKEUP_FACE_SETTINGSPRAY='Face Setting Spray'
    MAKEUP_FACE_PRIMER='Face Primer'
    MAKEUP_FACE_CONTOUR='Face Contour'
    MAKEUP_EYES_MASCARA='Eyes Mascara'
    MAKEUP_EYES_EYELINER='Eyes Eyeliner'
    MAKEUP_EYES_EYEBROW='Eye EyeBrow'
    MAKEUP_EYES_EYESHADOW='Eye EyeShadow'
    MAKEUP_EYES_EYEPALETTES='Eye Palettes'
    MAKEUP_LIP_LIPSTICK='Lip-Lipstick'
    MAKEUP_LIP_LIPGLOSS='Lip-Lip Gloss'
    MAKEUP_LIP_LIPLINER='Lip-Lip Liner'
    BODY_LOTION='Body Lotion'
    BODY_MIST='Body Mist'
    MOISTURIZER='Moisturizer'
    CANDLES='Candles'
    SUPPLIES_GIFT_SETS='Beauty Supplies And Gift Sets'
    FRAGRANCE_WOMEN='Fragrance Women'
    FRAGRANCE_MEN='Fragrance Men'
    FRAGRANCE_KIDS='Fragrance Kids'
    SKINCARE_CLEANSER='Cleanser'
    SKINCARE_LOTION='Lotion'
    SKINCARE_REATMENTS='Reatments'




    PRODUCT_CHOICES = [
            (FEATURED, FEATURED),
            (BATHBODY, BATHBODY),
            (FRAGRANCE, FRAGRANCE),
            (HAIR, HAIR),
            (MAKEUP, MAKEUP),
            (SALES, SALES),
            (SKINCARE, SKINCARE),
            (TOOL_BRUSH, TOOL_BRUSH),
            (MAKEUP_FACE_FOUNDATION, MAKEUP_FACE_FOUNDATION),
            (MAKEUP_FACE_POWDER, MAKEUP_FACE_POWDER),
            (MAKEUP_FACE_CONCEALER, MAKEUP_FACE_CONCEALER),
            (MAKEUP_FACE_HIGHLIGHTER, MAKEUP_FACE_HIGHLIGHTER),
            (MAKEUP_FACE_SETTINGSPRAY, MAKEUP_FACE_SETTINGSPRAY),
            (MAKEUP_FACE_PRIMER, MAKEUP_FACE_PRIMER),
            (MAKEUP_FACE_CONTOUR, MAKEUP_FACE_CONTOUR),
            (MAKEUP_EYES_MASCARA, MAKEUP_EYES_MASCARA),
            (MAKEUP_EYES_EYELINER, MAKEUP_EYES_EYELINER),
            (MAKEUP_EYES_EYEBROW, MAKEUP_EYES_EYEBROW),
            (MAKEUP_EYES_EYESHADOW, MAKEUP_EYES_EYESHADOW),
            (MAKEUP_EYES_EYEPALETTES, MAKEUP_EYES_EYEPALETTES),
            (MAKEUP_LIP_LIPSTICK, MAKEUP_LIP_LIPSTICK),
            (MAKEUP_LIP_LIPGLOSS, MAKEUP_LIP_LIPGLOSS),
            (MAKEUP_LIP_LIPLINER, MAKEUP_LIP_LIPLINER),
            (BODY_LOTION, BODY_LOTION),
            (BODY_MIST, BODY_MIST),
            (MOISTURIZER, MOISTURIZER),
            (CANDLES, CANDLES),
            (SUPPLIES_GIFT_SETS, SUPPLIES_GIFT_SETS),
            (FRAGRANCE_WOMEN, FRAGRANCE_WOMEN),
            (FRAGRANCE_MEN, FRAGRANCE_MEN),
            (FRAGRANCE_KIDS, FRAGRANCE_KIDS),
            (SKINCARE_CLEANSER, SKINCARE_CLEANSER),
            (SKINCARE_LOTION, SKINCARE_LOTION),
            (SKINCARE_REATMENTS, SKINCARE_REATMENTS),
    ]
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    type = models.CharField(max_length=100, choices=PRODUCT_CHOICES, default=FEATURED)
    description = models.CharField(max_length=1000000000, default='Product')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name)
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except BaseException:
            url = ''
        return url


class Order(models.Model):

    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if not i.product.digital:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.address)

