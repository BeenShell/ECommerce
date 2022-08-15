from django.urls import path

from . import views

urlpatterns = [
    # Leave as empty string for base url
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),

    path('makeup/', views.makeup, name="makeup"),
    path('skincare/', views.skincare, name="skincare"),
    path('hair/', views.hair, name="hair"),
    path('fragrance/', views.fragrance, name="fragrance"),
    path('toolsandbrushes/', views.toolsandbrushes, name="toolsandbrushes"),
    path('bathandbody/', views.bathandbody, name="bathandbody"),
    path('salesandclearance/',views.salesandclearance,name="salesandclearance"),
    path('body_lotion/',views.body_lotion ,name="body_lotion"),
    path('body_mist/',views.body_mist ,name="body_mist"),
    path('candles/', views.candles, name="candles"),
    path('fragrance_kids/', views.fragrance_kids, name="fragrance_kids"),
    path('fragrance_men/', views.fragrance_men, name="fragrance_men"),
    path('fragrance_women/', views.fragrance_women, name="fragrance_women"),
    path('makeup_eyes_eyebrow/', views.makeup_eyes_eyebrow, name="makeup_eyes_eyebrow"),
    path('makeup_eyes_eyeliner/', views.makeup_eyes_eyeliner, name="makeup_eyes_eyeliner"),
    path('makeup_eyes_eyepalettes/', views.makeup_eyes_eyepalettes, name="makeup_eyes_eyepalettes"),
    path('makeup_eyes_eyeshadow/', views.makeup_eyes_eyeshadow, name="makeup_eyes_eyeshadow"),
    path('makeup_eyes_mascara/', views.makeup_eyes_mascara, name="makeup_eyes_mascara"),
    path('makeup_face_concealer/', views.makeup_face_concealer, name="makeup_face_concealer"),
    path('makeup_face_contour/', views.makeup_face_contour, name="makeup_face_contour"),
    path('makeup_face_foundation/', views.makeup_face_foundation, name="makeup_face_foundation"),
    path('makeup_face_highlighter/', views.makeup_face_highlighter, name="makeup_face_highlighter"),
    path('makeup_face_powder/', views.makeup_face_powder, name="makeup_face_powder"),
    path('makeup_face_primer/', views.makeup_face_primer, name="makeup_face_primer"),
    path('makeup_face_settingspray/', views.makeup_face_settingspray, name="makeup_face_settingspray"),
    path('makeup_lip_lipgloss/', views.makeup_lip_lipgloss, name="makeup_lip_lipgloss"),
    path('makeup_lip_lipliner/', views.makeup_lip_lipliner, name="makeup_lip_lipliner"),
    path('makeup_lip_lipstick/', views.makeup_lip_lipliner, name="makeup_lip_stick"),
    path('moisturizer/', views.moisturizer, name="moisturizer"),
    path('skincare_cleanser/', views.skincare_cleanser, name="skincare_cleanser"),
    path('skincare_lotion/', views.skincare_lotion, name="skincare_lotion"),
    path('skincare_reatments/', views.skincare_reatments, name="skincare_treatments"),
    path('supplies_gift_sets/', views.supplies_gift_sets, name="supplies_gift_sets"),
    path('search_results', views.search_results, name="search_results"),
    path('view_product/', views.view_product, name="view_product")
]
