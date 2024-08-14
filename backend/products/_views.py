from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def product_view_old_ways(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").all()
    data_list = []
    if model_data:
        for data in model_data:
                data_dict = dict(title=data.title, content=data.content, price=data.price)
                data_list.append(data_dict)
    return JsonResponse(data={
        "data": data_list
    })


@api_view(['POST'])
def product_view_with_rest(request, *args, **kwargs):
    """
    DRF Api View
    """
    model_data, data_list = Product.objects.all().order_by("?").all(), []
    if model_data:
        for data in model_data:
            data_dict = model_to_dict(data, fields=["id", "title", "price"])
            data_list.append(data_dict)
    return Response({"data": data_list})


@api_view(['GET'])
def product_get(request, pk):
    try:
        snippet = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(snippet)
    return Response(serializer.data)


@api_view(['POST'])
def product_view(request, *args, **kwargs):
    """
    DRF Api View via POST
    """
    model_data, data_list = Product.objects.all().order_by("?").all(), []
    if model_data:
        for instance in model_data:
            data = ProductSerializer(instance=instance).data
            data_list.append(data)
    return Response({"data": data_list})


@api_view(['POST'])
def product_create(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        return JsonResponse(instance.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
