from django.shortcuts import render, redirect
from .forms import OForm
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from software.models import software
# Create your views here.

def download(request):
	return render(request=request, template_name="download/download.html", context={"download": software.objects.all()})

def upload_stw(request):
	form = OForm()
	if request.method == "post":
		form = OForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('download:soft_list')
	return render(request, "download/upload.html", {"form": form})

def soft_list(request):
	#software = software.objects.all()
	if request.GET:
	 	query = request.GET['q']
	 	# software = get_data_queryset(str(query))
	return render(request, "download/soft_list.html", {"software": software.objects.all()})


def delete_stw(request, pk):
	software = software.objects.get(pk=pk)
	software.delete()
	return redirect("download:soft_list")


def get_data_queryset(query=None):
	queryset = []
	queries = query.split(" ")
	for q in queries:
		software = software.objects.filter(
				Q(name_icontains=q) |
				Q(title_icontains=q)
			)

		for software in software:
			queryset.append(software)

	return list(set(queryset))



def api_data(request):
	software = software.objects.all()
	if request.method == "GET":
		dict_type = {"software": list(software.values("title", "name"))}

		return JsonResponse(dict_type)


@csrf_exempt
def update_api_data(request, pk):
	software = software.objects.get(pk=pk)
	if request.method == "GET":
		return JsonResponse({"name": software.name, "title": software.title})


	else:
		json_data = request.body.decode('utf-8')
		update_data = json.loads(json_data)
		software.title = update_data['title']


		return JsonResponse({"message": "Sucessfully completed!!"})