from django.shortcuts import redirect
from rest_framework import viewsets
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from .serializers import *
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.decorators import api_view


def reverse_to_submit(request):
    """ Redirects to submitData """
    return redirect('submitData')


class MountainList(viewsets.ModelViewSet):
    queryset = Mountain.objects.all()
    serializer_class = MountainSerializer


class MountainCreate(ListAPIView):
    queryset = Mountain.objects.all()
    serializer_class = MountainSerializer

    def post(self, request):
        serializer_for_writing = self.serializer_class(data=request.data)
        serializer_for_writing.is_valid(raise_exception=True)
        serializer_for_writing.save()
        return Response(data=serializer_for_writing.data, status=status.HTTP_201_CREATED)


class ImageViewSet(ListAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

    def post(self, request, *args, **kwargs):
        title_request = request.data['title']
        image_request = request.data['image']
        title = Images.objects.create(title=title_request)
        title.image = image_request
        title.save()
        return Response("Image uploaded!", status=status.HTTP_200_OK)


@api_view(['GET'])
def get_data(request, pk):
    try:
        mountain = Mountain.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=404)

    serializer = MountainSerializer(mountain)
    return Response(serializer.data)


@api_view(['PATCH'])
def update_data(request, pk):
    try:
        mountain = Mountain.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response({'state': 0, 'message': 'Mountain does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if mountain.status != 'New':
        return Response({'state': 0, 'message': 'Mountain status is not "New"'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = MountainUpdateSerializer(mountain, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'state': 1}, status.HTTP_200_OK)
    return Response({'state': 0, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

