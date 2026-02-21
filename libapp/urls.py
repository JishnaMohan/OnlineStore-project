from django.urls import path
from .import views
from .views import* 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("signup",views.user_register,name='bookstore_Signup'),
    path("",views.user_login,name='bookstore_login'),
    path("home",views.user_home,name='bookstore_home'),
    path("about", views.user_about, name='bookstore_about'),
    path("stories",views.user_stories, name='bookstore_stories'),
    path("poems",views.user_poems, name='bookstore_poems'),
    path("bio & memory",views.user_bio , name='bookstore_bio'),
    path("contact", views.user_contact, name='bookstore_contact'),
    path("cart",views.user_cart, name='bookstore_cart'),
    path("orders",views.user_orders, name='bookstore_orders'),
    path("wishlist",views.user_wishlist, name='bookstore_wishlist'),
    path("bookdetails/<book_id>",views.book_desc,name='book_details'),
    path("admin_home",views.admin_home,name='admin_homepage'),
    path("admin_book",views.admin_updatebook, name='admin_bookupdate'),
    path("admin_orderlist",views.admin_order,name='admin_showorder'),
    path("admin_userlist",views.admin_userlist,name='admin_showuser'),
    path("logout",views.logoutpage,name='page_logout'),
    path("purchase/<id>",views.book_purchase,name='book_purchase'),
    path("Book_Order/<int:book_id>/", views.book_order, name='book_order'),
    path("Payment_Success/<id>",views.payment_success,name='payment_success'),
    path('add-to-wishlist/<int:id>/', views.add_to_wishlist, name='add_to_wishlist'),

    # path("book_action/<book_id>",views.book_action,name="book_action")
]
urlpatterns+=static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)