from django.shortcuts import render
from .models import Trains
from apiapp.serializers import TrainsSerializers
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def trainapi(request,id=0):
    if request.method == 'GET':
        trains=Trains.objects.all()
        print(trains)
        trains_serializers=TrainsSerializers(trains,many=True)
        return JsonResponse(trains_serializers.data,safe=False)
    elif request.method=='POST':
        trains=JSONParser().parse(request)
        trains_serializers=TrainsSerializers(data=trains)
        if trains_serializers.is_valid():
            trains_serializers.save()
            return JsonResponse("data add successfully",safe=False)
        return JsonResponse("not added")
    elif request.method=="PUT":
        trainid=JSONParser().parse(request)
        trainsdata=Trains.objects.get(id=trainid['id'])
        train_serializer=TrainsSerializers(trainsdata,data=trainid)
        if train_serializer.is_valid():
            train_serializer.save()
            return JsonResponse("It is successfully updated",safe=False)
        return JsonResponse("Not Updated",safe=False)
    elif request.method=="DELETE":
        var1=Trains.objects.get(id=id)
        var1.delete()
        return JsonResponse("It is deleted Successfully.....",safe=False)
    
def index(request):
    serializer=TrainsSerializers
    return render(request,"index.html",{'serializer':serializer})
    
