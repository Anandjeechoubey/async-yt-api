from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer
from rest_framework import generics

# from rest_framework.pagination import CursorPagination

# Create your views here.

@api_view(['GET'])
def getApi(request):
    routes = [
        '/api/',
        '/api/videos',
    ]
    return Response(routes)


# class ResultsPagination(CursorPagination):
#     page_size = 5
#     page_size_query_param = 'page_size'
#     max_page_size = 100

class VideoListView(generics.ListAPIView):
    ordering = ('-published')
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    #pagination_class = ResultsPagination
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['city']

    # def get_queryset(self):
    #     """
    #     Optionally restricts the queryset by filtering against
    #     query parameters in the URL.
    #     """
    #     query_params = self.request.query_params
    #     name = query_params.get('name', '')
    #     desc = query_params.get('desc', '')
    #     if name:
    #         queryset = Video.objects.filter( title__icontains = name).order_by('published')
    #     if desc:
    #         queryset = Video.objects.filter( description__icontains = desc).order_by('published')
    #     print(query_params)
    #     return queryset