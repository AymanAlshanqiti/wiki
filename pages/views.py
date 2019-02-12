from django.shortcuts import render
from .models import Page

def list(request):
	context = {
	"pages" : Page.objects.all()
	}
	return render(request, "list.html", context)
	# pages = Page.objects.all()
	# return Page.get_absolute_url(pages)

def detail(request, page_id):
	context = {
		"page" : Page.objects.get(id = page_id)
	}
	return render(request, "detail.html", context) 


