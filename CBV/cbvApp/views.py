from django.shortcuts import render,HttpResponse

# Create your views here.

# from django.views import View
#
# class BookView(View):
#
#     def get(self,request):
#         return HttpResponse('get')
#     def post(self,request):
#         return HttpResponse('post')


# class View():
#
#     def as_view(cls, **initkwargs):
#         def view(self):
#             return self.dispatch()
#         return view
#
#     def dispatch(self, request, *args, **kwargs):
#         if request.method.lower() in self.http_method_names:
#             handler = getattr( self, request.method.lower(), self.http_method_not_allowed )
#         else:
#             handler = self.http_method_not_allowed
#         return handler(request, *args, **kwargs)

# 2222

from rest_framework.views import APIView

class BookView(APIView):

    def get(self,request):
        return HttpResponse('get')
    def post(self,request):
        return HttpResponse('post')


# class APIView(View):
#     def as_view(cls, **initkwargs):
#         view = super().as_view(**initkwargs)
#         return csrf_exempt(view)
#
#     def dispatch(self, request, *args, **kwargs):
#         # 构建新的request对象
#         request = self.initialize_request(request, *args, **kwargs)
#         self.request = request
#         # 初始化：认证、权限、限流组件三件套
#
#         if request.method.lower() in self.http_method_names:
#             handler = getattr( self, request.method.lower(), self.http_method_not_allowed )
#         else:
#             handler = self.http_method_not_allowed
#         return handler(request, *args, **kwargs)