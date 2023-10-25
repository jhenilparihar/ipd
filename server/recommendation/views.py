from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Crop

# Create your views here.


class RecommendView(APIView):
    def get(self, request):
        # crop = Crop.objects.all()
        # return Response({"Crop": crop})
        return Response({"Response: 200"})
