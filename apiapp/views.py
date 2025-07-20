
from apiapp import views
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .serializer import ApiSerializer
from .models import apimodel
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])#Read operation
def read_api(request):
    apidetails=apimodel.objects.all()
    serializer=ApiSerializer(apidetails,many=True)
    return Response(serializer.data)

@api_view(['POST'])#create operation
def create_api(request):
    serializercrt=ApiSerializer(data=request.data,many=True)
    if serializercrt.is_valid():
        serializercrt.save()
        return Response(serializercrt.data,status=201)
    else:
        return Response(serializercrt.errors,status=400)


@api_view(['POST'])#update opertaion
def update_api(request,id):
    apidetails = get_object_or_404(apimodel, id=id)
    serializerupt=ApiSerializer(instance=apidetails,data=request.data,partial=True)
    if serializerupt.is_valid():
        serializerupt.save()
        return Response(serializerupt.data,status=200)
    else:
        return Response(serializerupt.data,status=400)

@api_view(['DELETE']) #delete operation
def delete_api(request,id):
    apidetails = get_object_or_404(apimodel, id=id)
    serializerdel=ApiSerializer()
    apidetails.delete()
    return Response('Item deleted successfully...!')

@api_view(['GET']) #to delete wanted view
def view_api(request,uname):
    apidetails = get_object_or_404(apimodel, uname=uname)
    Serializerview=ApiSerializer(apidetails)
    return Response(Serializerview.data)





