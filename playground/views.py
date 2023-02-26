"""render will show html pages for us"""
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
# to perform OR operator
from django.db.models import Q, F
from store.models import Product


def say_hello(request):
	""""basic function to show hello page"""
	# filtering Products
	# Products: inventory < 10 OR price < 20
	querySet = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
	return render(request, 'hello.html', {'name':'ahmad fraz', 'products': list(querySet)})
