
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from TurfApp.models import TurfDb
from TurfApp.serializers import Turf_Serializer




class TurfListCreateView(APIView):

    # Get all turfs
    def get(self, request):
        qs = TurfDb.objects.all()
        serializer_instance = Turf_Serializer(qs, many=True)
        return Response(data=serializer_instance.data)

    # Create a turf
    def post(self, request):
        form_data = request.data
        serializer_instance = Turf_Serializer(data=form_data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)

        else:
            return Response(data=serializer_instance.errors)




class TurfRetrieveUpdateDeleteView(APIView):

    # Retrieve 
    def get(self, request, pk):
        turf_obj = get_object_or_404(TurfDb, id=pk)
        serializer_instance = Turf_Serializer(turf_obj)
        return Response(data=serializer_instance.data)

    # Update 
    def put(self, request, pk):
        form_data = request.data
        turf_obj = get_object_or_404(TurfDb, id=pk)

        serializer_instance = Turf_Serializer(
            data=form_data,
            instance=turf_obj
        )

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)

        else:
            return Response(data=serializer_instance.errors)

    # Delete 
    def delete(self, request, pk):
        turf_obj = get_object_or_404(TurfDb, id=pk)
        turf_obj.delete()

        return Response(data={
            "Message": "Turf deleted successfully!"
        })
