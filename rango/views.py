from django.shortcuts import render 
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm

def index(request):
	category_list = Category.objects.order_by('-likes')[:5]
	context_dict = {'categories': category_list}
	#context_dict = {'boldmessage': "I come, I see, I conquer!"}
	return render(request, 'rango/index.html', context_dict)
	#return HttpResponse("Rango says hey there world!<br/><a href='/rango/about/'>About</a>")

def about(request):
	return render(request, 'rango/about.html', "")
	#return HttpResponse("About page. <br/><a href='/rango/'>Index</a>") 

def category(request, category_name_slug):
	context_dict = {}

	try:
		category = Category.objects.get(slug=category_name_slug)
		context_dict['category_name'] = category.name
		
		pages = Page.objects.filter(category=category)
		context_dict['pages'] = pages
		context_dict['category'] = category
	except Category.DoesNotExist:
		pass

	return render(request, 'rango/category.html', context_dict)

def add_category(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print form.erros
	else:
		form = CategoryForm()

	return render(request, 'rango/add_category.html', {'form': form})


