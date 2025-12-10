from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404
from .models import Destination, DestinationImage
from .serializers import DestinationSerializer

# API Views
class DestinationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Destination.objects.all().order_by('-created_at')
    serializer_class = DestinationSerializer

class DestinationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class DeleteDestinationImageAPIView(APIView):
    def delete(self, request, image_id):
        image = get_object_or_404(DestinationImage, id=image_id)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Template Views
def destination_list(request):
    return render(request, 'destinations/list.html')

def destination_detail(request, pk):
    return render(request, 'destinations/detail.html', {'destination_id': pk})

def destination_create(request):
    return render(request, 'destinations/create.html')

def destination_update(request, pk):
    return render(request, 'destinations/update.html', {'destination_id': pk})