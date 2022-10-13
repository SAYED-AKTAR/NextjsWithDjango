from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from .models import CustomUser
# Create your views here.

class index(APIView):
    def get(self, request, format=None):
        return JsonResponse({"msg": "GET Request", "status": "202"})


    def post(self, request, format=None):
        obj = CustomUser(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=request.POST['password'],
            address=request.POST['address'],
            role=request.POST['role'],
            photo=request.FILES['photo'],
        )
        obj.save()
        return JsonResponse({"msg": "POST Request", "status": 202})


    def put(self, request, format=None):
        return JsonResponse({"msg": "PUT Request", "status": 202})


    def patch(self, request, format=None):
        return JsonResponse({"msg": "PATCH Request", "status": 202})


    def delete(self, request, format=None):
        return JsonResponse({"msg": "DELETE Request", "status": 202})
