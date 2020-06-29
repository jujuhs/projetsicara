from django.http import HttpResponse
from .serializers import PhotoSerializer
from .models import Photo
from rest_framework import viewsets


from django.views.decorators.csrf import ensure_csrf_cookie
@ensure_csrf_cookie


class PhotoViewSet(viewsets.ModelViewSet):
    queryset=Photo.objects.all()
    serializer_class = PhotoSerializer

    def post(self, request):
        name=request.data['name']
        photo=request.data['photo']
        Photo.objects.create(name=name, photo=photo)
        return HttpResponse({'message': 'image enregistrée'})

