from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import generics, status
from rest_framework.response import Response

from app.models import Post
from app.serializers import PostSerializer, PostListSerializer


def index(request):
    return render(request, 'index.html', {})


def gallery(request):
    return render(request, 'gallery.html', {})


def reservation(request):
    return render(request, 'reservation.html', {})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def design_consultation(request):
    if request.method == 'POST':
        return HttpResponse('Thank you for choosing us.')





























class PostView(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Post created')
        else:
            return Response(serializer.errors)

    def list(self, request, *args, **kwargs):
        try:
            # posts = Post.objects.filter(Q(title='test') & Q(description='test'))
            title = request.query_params.get('title')
            posts = Post.objects.filter(Q(title=title) & Q(description='test'))
            serializer = PostListSerializer(posts, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PostRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostListSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            post = Post.objects.get(pk=pk)
            serializer = self.serializer_class(post)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response('Post does not exist', status=status.HTTP_404_NOT_FOUND)

    # def update(self, request, *args, **kwargs):
    # def delete(self, request, *args, **kwargs):
