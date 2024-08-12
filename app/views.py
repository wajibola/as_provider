from django.http import HttpResponse, JsonResponse
from .models import ASInfo
from .serializers import ASInfoSerializer
from rest_framework import views, status

# Create your views here.

class ASInfoView(views.APIView):
    def get(self, request, as_number, format=None):
        """
        Return information about Autonomous System based on AS number
        """
        as_info = ASInfo.objects.filter(as_number=as_number)
        
        if as_info.exists():
            serializer = ASInfoSerializer(as_info, many=True)
            return JsonResponse({'status': status.HTTP_200_OK, 'data': serializer.data}, status=status.HTTP_200_OK)
        return JsonResponse({'status': status.HTTP_404_NOT_FOUND, 'data': {}}, status=status.HTTP_404_NOT_FOUND)

class IPASInfoView(views.APIView):
    def get(self, request, ip, format=None):
        """
        Return information about Autonomous System based on IP address
        """
        as_info = ASInfo.objects.filter(range_end__gt=ip).filter(range_start__lte=ip)

        if as_info.exists():
            serializer = ASInfoSerializer(as_info, many=True)
            return JsonResponse({'status': status.HTTP_200_OK, 'data': serializer.data}, status=status.HTTP_200_OK)
        return JsonResponse({'status': status.HTTP_404_NOT_FOUND, 'data': {}}, status=status.HTTP_404_NOT_FOUND)
