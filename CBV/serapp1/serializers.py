from rest_framework import serializers
from .models import *
# class Bookserializers(serializers.Serializer):
#     title = serializers.CharField(max_length=16)
#     price = serializers.IntegerField()
#     # 使用下面这种可以该名称
#     # jiaqian = serializers.IntegerField(source='price')
#
#     def create(self, validated_data):
#         newbook = Books.objects.create(**self.validated_data)
#         return newbook
#     def update(self, instance, validated_data):
#         Books.objects.filter(pk=instance.pk).update(**self.validated_data)
#         update_book = Books.objects.get(pk=instance.pk)
#         return update_book

class Bookserializers(serializers.ModelSerializer):

    class Meta:
        model = Books
        # fields = '__all__'
        fields = ['title','price']
