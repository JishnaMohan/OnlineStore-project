from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from .forms import*
from .models import*
from django.utils import timezone
from django.shortcuts import get_object_or_404
from datetime import timedelta

def user_register(request):
    if request.method == 'POST':
        book_username =request.POST.get("username")
        passwd =request.POST.get("password")
        passwd2 =request.POST.get("password_match")
        if passwd==passwd2: 
            Book_Signup.objects.create(
                book_user=book_username,
                book_password=passwd )
            return redirect('bookstore_login')
        else:
            return HttpResponse("Password mismatch")
    return render(request,'bookstore_signup.html')
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_homepage')
            else:
                return redirect('bookstore_home')
        try:
                    user = Book_Signup.objects.get(
                        book_user=username,
                        book_password=password
                    )
                    return redirect('bookstore_home')
        except Book_Signup.DoesNotExist:
                    return HttpResponse("Invalid username or password")
    return render(request, 'bookstore_login.html')

def logoutpage(request):
    logout(request)
    return redirect('/')

def user_home(request):
    return render(request,'bookstore_home.html')

def user_about(request):
    return render(request,'bookstore_about.html')

def user_stories(request):
    story_books = Book_Store.objects.filter(book_category__name="Stories")
    quantity = request.POST.get('output')
    return render(request,'bookstore_stories.html',{'books':story_books,'qty':quantity})

def user_poems(request):
    poem_books = Book_Store.objects.filter(book_category__name="Poems")
    return render(request,'bookstore_poems.html',{'books':poem_books})

def user_bio(request):
     bio_books = Book_Store.objects.filter(book_category__name="Autobiographies & Memories")
     return render(request,'bookstore_bio.html',{'books':bio_books})

def add_to_wishlist(request, id):
    if request.method == "POST":
        book = get_object_or_404(Book_Store, id=id)
        if not Wishlist.objects.filter(user=request.user, book_name=book.book_name).exists():
            Wishlist.objects.create(
                user=request.user,
                book_name=book.book_name,
                book_price=book.book_price,
                book_image=book.book_image
            )
    return redirect('bookstore_stories')

def user_contact(request):
     return render(request,'bookstore_contact.html')


def user_cart(request): 
    cart_book = Cart.objects.all()
    if request.method == "POST":
        if request.POST.get("buy_now"):
            cart_id = request.POST.get("buy_now")
            cart_item = get_object_or_404(Cart, id=cart_id)
            book_id = cart_item.book.id
            return redirect('book_purchase', id=book_id)
        elif request.POST.get("remove_item"):
            cart_id = request.POST.get("remove_item")
            Cart.objects.filter(id=cart_id).delete()
            return redirect('bookstore_cart')
    return render(request,'bookstore_cart.html',{'cart_book':cart_book})



def user_orders(request): 
     order_book = Order.objects.all()
     return render(request,'bookstore_myorder.html',{'order':order_book})

def user_wishlist(request):
    items = Wishlist.objects.filter(user=request.user)
    return render(request,'bookstore_wishlist.html', {'items': items})

def book_desc(request,book_id):
    details = get_object_or_404(Book_Store,id=book_id)
    quantity = request.POST.get('output') 
    if request.method == 'POST':
        action = request.POST.get("action")
        if action == "add_to_cart":
             Cart.objects.create(
                book = details,   
                quantity = quantity
            )
             return redirect("bookstore_cart")
        elif action == "buy_now" :
            return redirect("book_purchase" ,id=details.id)
    return render(request,'bookstore_bdescription.html',{'product_detail':details,'qty':quantity})

def book_purchase(request,id):
    details =Book_Store.objects.get(id=id)
    if request.method == 'POST':
        payment = request.POST.get("payment_method")
    return render(request,'bookstore_purchase.html',{'product_detail':details})
     
def book_order(request,book_id):
    detail = Book_Store.objects.get(id=book_id)
    return render(request, 'bookstore_purchase.html', {'product_detail': detail})

def payment_success(request,id):
    b_details =Book_Store.objects.get(id=id)   
    payment = request.POST.get('payment_method')
    Order.objects.create(
            o_user=request.user.username, 
            book=b_details,           
            payment_method =payment,        
            order_date=timezone.now(),              
            status='Ordered'
        )      
    return render(request,'paymentsuccess.html',{'bk_details':b_details,'payment_method': payment})


     

# admin

def admin_home(request):
    total_user = Book_Signup.objects.count()
    last_7_days = timezone.now().date() - timedelta(days=7)
    weekly_sales = Order.objects.filter(order_date__gte=last_7_days).count()
    context = {
        'total': total_user,
        'weekly_sales': weekly_sales
    }
    return render(request, 'bookstore_admin_homepage.html', context)


def admin_updatebook(request):
    if request.method == 'POST':
        category_id = request.POST.get('category')
        if not category_id:
            return HttpResponse("Category is required")
        category = get_object_or_404(Category, id=category_id)
        Book_Store.objects.create(
            book_category=category,
            book_name=request.POST.get("bname"),
            author_name=request.POST.get("author"),
            publish_date=request.POST.get("publish"),
            book_price=request.POST.get("price"),
            numbers=request.POST.get("quantity"),
            book_image=request.FILES.get("bimg")
        )
        
    categories = Category.objects.all()
    return render(request,'bookstore_admin_book.html',{'categories': categories})


def admin_order(request):
    orders = Order.objects.all()  
    return render(request, 'bookstore_admin_orderlist.html', {'orders': orders})


def admin_userlist(request):
    customers = Book_Signup.objects.all()
    return render(request,'bookstore_admin_userlist.html',{'userlist': customers})















    

        
   


