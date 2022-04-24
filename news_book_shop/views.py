from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views import View
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from news_book_shop.models import News
from news_book_shop.serializers import NewsSerializer


class NewsPageApiView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


    # def get_news(self, request):
    #     if request.method == 'GET':
    #         news = News.objects.all()
    #         serializer = NewsSerializer(News, many=True)
    #         return Response(serializer.data)
