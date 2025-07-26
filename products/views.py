from django.shortcuts import render


from products.models import Products

def products_list(request):
    products = Products.objects.all()
    context = {"products": products}
    return render(request, 'products.html', context)


