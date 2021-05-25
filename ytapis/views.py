from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer
from rest_framework import generics

# Create your views here.

@api_view(['GET'])
def getApi(request):
    routes = [
        '/api/',
        '/api/videos',
    ]
    return Response(routes)

@api_view(['GET'])
def getVideos(request):
    vidoes = Video.objects.all()
    serializer = VideoSerializer(vidoes, many=True)
    return Response(serializer.data)

class VideoListView(generics.ListAPIView):
    queryset = Video.objects.all().order_by('published')
    serializer_class = VideoSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['city']

    def get_queryset(self):
        """
        Optionally restricts the queryset by filtering against
        query parameters in the URL.
        """
        query_params = self.request.query_params
        name = query_params.get('name', '')
        desc = query_params.get('desc', '')
        if name:
            queryset = Video.objects.filter( title__icontains = name).order_by('published')
        if desc:
            queryset = Video.objects.filter( description__icontains = desc).order_by('published')
        print(query_params)
        return queryset