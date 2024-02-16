from rest_framework import generics
from .models import Animal , Category
from .serializers import CategorySerializer , AnimalSerializer
from django.core.cache import cache 
from rest_framework.response import Response
from rest_framework import status , viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class AnimalList(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    
    
    def list(self, request, *args, **kwargs):
        cache_key = "animals_list"
        cache_time = 60 * 3
        data = cache.get(cache_key)
        if not data:
            animals = Animal.objects.all()
            data = AnimalSerializer(animals , many =True).data
            cache.set(cache_key, data , cache_time)
        return Response(data)
        
        
        
    
class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    
    

class AnimalBatchDeleteView(APIView):
    
    def delete(self ,request , *args , **kwargs):
        ids = request.data.get('ids',[])
        
        if not ids:
            return Response({"error: no ids provided"},status =status.HTTP_400_BAD_REQUEST  )
        
        Animal.objects.filter(id__in= ids).delete()
        return Response(status =status.HTTP_204_NO_CONTENT  )
    
    
class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    
    @action(detail = False, methods = ['post'])
    def mark_endangered(self, request):
        ids = request.data.get('ids',[])
        animals = Animal.objects.filter(id__in = ids)
        
        animals.update(status = 'Endangered!')
        return Response({'status': 'marked endangered' }, status =status.HTTP_204_NO_CONTENT  )