from django.http import HttpResponse

from app1.models import app1

def test(request):
	test1 = app1(name="john")
	test1.save()
	return HttpResponse("app is ok,kkk")

def addinfotodb(request):
	get_value = request.GET.get('name')
	result_list = app1.objects.create(name=get_value)
	return getallinfofromdb(request)

def updateinfotodb(request):
	get_value = request.GET.get('id')
	name_value = request.GET.get('name')
	result_list = app1.objects.filter(id=get_value).update(name=name_value)
	return getallinfofromdb(request)

def deleteinfotodb(request):
	get_value = request.GET.get('id')
	result_list = app1.objects.filter(id=get_value).delete()
	return getallinfofromdb(request)

def getallinfofromdb(request):
	result_list = app1.objects.all()
	httpresult = "id \t name<br>"
	for item in result_list:
		print(item.name)
		httpresult += str(item.id)
		httpresult += '\t'
		httpresult += item.name
		httpresult += '<br>'
	return HttpResponse(httpresult)

def getinfofromdb(request):
	get_value = request.GET.get('id')
	result_list = app1.objects.filter(id=get_value)
	httpresult = "id \t name<br>"
	for item in result_list:
		print(item.name)
		httpresult += str(item.id)
		httpresult += '\t'
		httpresult += item.name
		httpresult += '<br>'
	return HttpResponse(httpresult)

def clearallinfofromdb(request):
	app1.objects.all().delete()
	return getallinfofromdb(request)