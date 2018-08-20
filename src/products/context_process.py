from .models import Category

def Catelist(request):
	cats=Category.objects.all()
	
	return {"cat_list":cats}