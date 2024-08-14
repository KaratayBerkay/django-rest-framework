from rest_framework.response import Response
from rest_framework import generics, authentication

from ..models import Product
from ..serializers import ProductSerializer
from ..permissions import IsStaffEditorPermissions
from ..authentication import TokenAuthentication


class ProductDetailView(generics.RetrieveAPIView):
    perm_name = 'products.view_product'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    permission_classes = [IsStaffEditorPermissions]


class ProductCreateView(generics.CreateAPIView):
    perm_name = 'products.add_product'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    permission_classes = [IsStaffEditorPermissions]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data})
        return Response({"message": "failed", "details": serializer.errors})


class ProductUpdateView(generics.UpdateAPIView):
    perm_name = 'products.change_product'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [IsStaffEditorPermissions]
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "mobile number updated successfully"})
        return Response({"message": "failed", "details": serializer.errors})


class ProductListView(generics.ListAPIView):
    perm_name = 'products.view_product'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [IsStaffEditorPermissions]
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]

    def list(self, request, *args, **kwargs):
        instance = self.get_serializer(self.get_queryset(), many=True, context={"request": self.request})
        if page := self.paginate_queryset(self.filter_queryset(self.get_queryset())):
            serializer = self.get_serializer(page, many=True, context={"request": self.request})
            return self.get_paginated_response(serializer.data)
        return Response(instance.data)


class ProductDeleteView(generics.DestroyAPIView):
    perm_name = 'products.delete_product'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [IsStaffEditorPermissions]
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]

    def perform_destroy(self, instance):
        super().perform_destroy(instance=instance)
