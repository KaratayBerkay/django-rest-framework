from django.http import JsonResponse
from rest_framework.generics import (
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    ListAPIView,
    DestroyAPIView,
)
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import AuthUsersSerializer

def api_home(request, *args, **kwargs):
    return JsonResponse(
        data={
            "message": "Hi you have reached to api home.",
            "text": "Hi you have reached to api home.",
            "request": dict(request),
            "args": args,
            "kwargs": kwargs
        }
    )



class UserListView(ListAPIView):
    perm_name = 'products.view_user'
    queryset = User.objects.all()
    serializer_class = AuthUsersSerializer
    lookup_field = 'pk'
    # permission_classes = [IsStaffEditorPermissions]
    # authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]

    def list(self, request, *args, **kwargs):
        instance = self.get_serializer(self.get_queryset(), many=True, context={"request": self.request})
        if page := self.paginate_queryset(self.filter_queryset(self.get_queryset())):
            serializer = self.get_serializer(page, many=True, context={"request": self.request})
            return self.get_paginated_response(serializer.data)
        return Response(instance.data)