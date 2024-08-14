from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import (
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    ListAPIView,
    DestroyAPIView,
)
from ..models import ProductRating
from ..serializers import ProductRatingSerializer
from ..permissions import IsStaffEditorPermissions
from ..authentication import TokenAuthentication


class ProductRatingDetailView(RetrieveAPIView):
    perm_name = 'products.view_productrating'
    queryset = ProductRating.objects.all()
    serializer_class = ProductRatingSerializer
    lookup_field = 'pk'
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsStaffEditorPermissions]


class ProductRatingCreateView(CreateAPIView):
    perm_name = 'products.add_productrating'
    queryset = ProductRating.objects.all()
    serializer_class = ProductRatingSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsStaffEditorPermissions]

    def create(self, request, *args, **kwargs):
        from .product import Product
        data_dict = request.data
        id_field = str(data_dict['product'])
        if len(id_field) > 35:
            if selected_product := Product.objects.filter(uu_id=id_field).first():
                data_dict['product'] = selected_product.id
        serializer = self.get_serializer(data=data_dict)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data})
        return Response({"message": "failed", "details": serializer.errors})


class ProductRatingUpdateView(UpdateAPIView):
    perm_name = 'products.change_productrating'
    queryset = ProductRating.objects.all()
    serializer_class = ProductRatingSerializer
    lookup_field = 'pk'
    permission_classes = [IsStaffEditorPermissions]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "mobile number updated successfully"})
        return Response({"message": "failed", "details": serializer.errors})


class ProductRatingListView(ListAPIView):
    perm_name = 'products.view_productrating'
    queryset = ProductRating.objects.all()
    serializer_class = ProductRatingSerializer
    lookup_field = 'pk'
    permission_classes = [IsStaffEditorPermissions]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def list(self, request, *args, **kwargs):
        instance = self.get_serializer(self.get_queryset(), many=True, context={"request": self.request})
        if page := self.paginate_queryset(self.filter_queryset(self.get_queryset())):
            serializer = self.get_serializer(page, many=True, context={"request": self.request})
            return self.get_paginated_response(serializer.data)
        return Response(instance.data)


class ProductRatingDeleteView(DestroyAPIView):
    name = 'products.delete_productrating'
    queryset = ProductRating.objects.all()
    serializer_class = ProductRatingSerializer
    lookup_field = 'pk'
    permission_classes = [IsStaffEditorPermissions]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def perform_destroy(self, instance):
        super().perform_destroy(instance=instance)
