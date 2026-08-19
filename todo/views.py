from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import TodoSerializer
from .models import Todo

from django.shortcuts import get_object_or_404

# TodoListCreateView
# TodoRetrieveView
# TodoCreateView
# TodoUpdateView
# TodoDestroyView======================

class TodoListCreateView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TodoCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TodoRetrieveView(RetrieveAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

class TodoUpdateView(UpdateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class TodoDestroyView(DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)








































# ================GenericAPIVIEW======================

# class TodoListView(GenericAPIView):
#     """Generic  todo"""
#     serializer_class = TodoSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Todo.objects.filter(user=self.request.user)

#     def get(self, request):
#         todos = self.get_queryset()
#         serializer = self.get_serializer(todos, many=True)

#         return Response(serializer.data)

#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data)
#         return Response(serializer.errors)

# class TodoDetailView(GenericAPIView):
#     serializer_class = TodoSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Todo.objects.filter(user=self.request.user)


#     def get(self,request, *args, **kwargs):
#         todo = self.get_object()
#         serializer = self.get_serializer(todo)
#         return Response(serializer.data)


    # def put(self,request, *args, **kwargs):
    #     todo = self.get_object()
    #     serializer = self.get_serializer(todo, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)


    # def patch(self,request, *args, **kwargs):
    #     todo = self.get_object()
    #     serializer = self.get_serializer(todo, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)


    # def delete(self,request, *args, **kwargs):
    #     todo = self.get_object()
    #     todo.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT) 

















































# ================APIVIEW======================
# class TodoListCreateView(APIView):
#     """Todo get and post api view"""

#     def get(self, request):
#         todos = Todo.objects.all()
#         serializer = TodoSerializer(todos, many=True)
#         return Response( serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = TodoSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class TodoDetailView(APIView):
#     """Detail todo"""

#     def get(self,request, pk):
#         todo = get_object_or_404(Todo, pk=pk)
#         serializer = TodoSerializer(todo)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         todo = get_object_or_404(Todo, pk=pk)
#         serializer = TodoSerializer(todo, data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
#     def patch(self,request, pk):
#         todo = get_object_or_404(Todo, pk=pk)
#         serializer = TodoSerializer(todo, data=request.data , partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         todo = get_object_or_404(Todo, pk=pk)
#         todo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



