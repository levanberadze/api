from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer


@api_view(['GET', 'POST'])
def index(request):

    if request.method == "POST":
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'car created successfully'})
        else:
            return Response({'errors': serializer.errors})

    cars = Car.objects.all()
    serializer = CarSerializer(instance=cars, many=True)



    return Response(serializer.data)



