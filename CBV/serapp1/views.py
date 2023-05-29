from django.shortcuts import render,HttpResponse

# Create your views here.

from rest_framework.views import APIView
# 不使用djangO自带的HttpResponse  而是用rest_framework的Response可以将返回值变成json
from rest_framework.response import Response
from .models import *
from .serializers import *

######################### 一、 APIView  ############################################


# class BookView(APIView):
#
#     def get(self,request):
#         books = Books.objects.all()
#         serializer = Bookserializers(instance=books,many=True)
#
#         return Response(serializer.data)
#
#     def post(self,request):
#         serializer = Bookserializers(data=request.data)
#         if serializer.is_valid():
#             # Books.objects.create(**serializer.validated_data)
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
# class BookDetailView(APIView):
#
#     def get(self,request,id):
#         book = Books.objects.get(pk=id)
#         serializer = Bookserializers(instance=book,many=False)
#         return Response(serializer.data)
#
#     def put(self,request,id):
#
#         serializer = Bookserializers(instance=Books.objects.get(pk=id),data=request.data)
#         if serializer.is_valid():
#             # Books.objects.filter(pk=id).update(**serializer.validated_data)
#             # serializer.instance = Books.objects.get(pk=id)
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#
#     def delete(self,request,id):
#         Books.objects.get(pk=id).delete()
#         return Response()


# ######################### 二、 GenericAPIView  ############################################
# from rest_framework.generics import GenericAPIView
#
# class BookView(GenericAPIView):
#     queryset = Books.objects.all()
#     serializer_class = Bookserializers
#
#     def get(self, request):
#         # books = Books.objects.all()
#         # serializer = Bookserializers(instance=self.get_queryset(),many=True)
#         # self.get_serializer_class()等于Bookserializers
#         # self.get_serializer_class()(instance=self.get_queryset(),many=True)
#         serializer = self.get_serializer(instance=self.get_queryset(),many=True)
#         return Response(serializer.data)
#
#     def post(self,request):
#         # serializer = Bookserializers(data=request.data)
#         # serializer = self.get_serializer_class()(data=request.data)
#         # 三行作用相同
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             # Books.objects.create(**serializer.validated_data)
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
# class BookDetailView(GenericAPIView):
#     queryset = Books.objects.all()
#     serializer_class = Bookserializers
#
#     def get(self,request,pk):
#         # book = Books.objects.get(pk=id)
#         # serializer = Bookserializers(instance=book,many=False)
#         serializer = self.get_serializer(instance=self.get_object(),many=False)
#         return Response(serializer.data)
#
#     def put(self,request,pk):
#         # serializer = Bookserializers(instance=Books.objects.get(pk=id),data=request.data)
#         serializer = self.get_serializer(instance=self.get_object(),data=request.data)
#         if serializer.is_valid():
#             # Books.objects.filter(pk=id).update(**serializer.validated_data)
#             # serializer.instance = Books.objects.get(pk=id)
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#     def delete(self,request,pk):
#         # Books.objects.get(pk=id).delete()
#         self.get_object().delete()
#         return Response()


#  #################### 三、mixins  #########################################
# from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin
# from rest_framework.generics import GenericAPIView
# class BookView(ListModelMixin,CreateModelMixin,GenericAPIView):
#     queryset = Books.objects.all()
#     serializer_class = Bookserializers
#
#     def get(self,request):
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)
#
# class BookDetailView(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,GenericAPIView):
#     queryset = Books.objects.all()
#     serializer_class = Bookserializers
#
#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#     def put(self,request,pk):
#         return self.update(request,pk)
#     def delete(self,request,pk):
#         return self.destroy(request,pk)


# #  #################### mixins再封装版  #########################################

# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# class BookView(ListCreateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = Bookserializers
#
# class BookDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Books.objects.all()
#     serializer_class = Bookserializers

# #  #################### ViewSet 重新构建分发机制  #########################################

from rest_framework.viewsets import ViewSet
class BookView(ViewSet):

    def get_all(self,request):
        return Response('GETALL')
    def add_object(self,request):
        return Response('POST')
    def get_object(self,request,pk):
        return Response('GETONE')
    def update_object(self,request,pk):
        return Response('PUT')
    def delete_object(self,request,pk):
        return Response('DELETE')

#  #################### 四、GenericViewSet  #########################################

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin

class BookView(GenericViewSet,ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset = Books.objects.all()
    serializer_class = Bookserializers

# #  #################### 五、ModelViewSet  #########################################

from rest_framework.viewsets import ModelViewSet

class BookView(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = Bookserializers