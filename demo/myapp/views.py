from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Product, Category, Customer, Bill, BillLine

def home(request):
    return render(request, "home.html")

def product_data_json(request):
    products = Product.objects.select_related("category").values(
        "product_code", "product_name", "price", "category__category_name"
    )
    return JsonResponse(list(products), safe=False)

def get_products(request):
    products = list(Product.objects.values('product_id', 'product_code', 'product_name', 'price', 'category_id'))
    if not products:
        return JsonResponse({'message': 'No products found'}, status=404)
    return JsonResponse(products, safe=False)

def get_category(request):
    categories = list(Category.objects.values('category_id', 'category_code', 'category_name'))
    if not categories:
        return JsonResponse({'message': 'No categories found'}, status=404)
    return JsonResponse(categories, safe=False)

def get_customers(request):
    customers = list(Customer.objects.select_related("segment").values('customer_id', 'customer_code', 'segment__segment_code'))
    if not customers:
        return JsonResponse({'message': 'No customers found'}, status=404)
    return JsonResponse(customers, safe=False)

def get_bills(request):
    bills = list(Bill.objects.select_related('customer').values('bill_id', 'bill_code', 'time_created', 'customer__customer_code'))
    if not bills:
        return JsonResponse({'message': 'No bills found'}, status=404)
    return JsonResponse(bills, safe=False)

def get_bill_details(request):
    billlines = list(BillLine.objects.select_related('product', 'bill').values(
        'bill__bill_code', 
        'product__product_code', 
        'product__product_name', 
        'quantity', 
        'bill__time_created',
        'total_price'
    ))
    if not billlines:
        return JsonResponse({'message': 'No bill details found'}, status=404)
    return JsonResponse(billlines, safe=False)

def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def chart_view1(request):
    return render(request, '1.html')  

def chart_view2(request):
    return render(request, '2.html')  

def chart_view3(request):
    return render(request, '3.html')  

def chart_view4(request):
    return render(request, '4.html')  

def chart_view5(request):
    return render(request, '5.html')  

def chart_view6(request):
    return render(request, '6.html') 

def chart_view7(request):
    return render(request, '7.html') 

def chart_view8(request):
    return render(request, '8.html') 

def chart_view9(request):
    return render(request, '9.html') 

def chart_view10(request):
    return render(request, '10.html') 

def chart_view11(request):
    return render(request, '11.html') 

def chart_view12(request):
    return render(request, '12.html') 

def index(request):
    return render(request, 'index.html')
