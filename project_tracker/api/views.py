from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Card
from .serializers import CardSerializer

# Create your views here.

@api_view(['GET'])
def get_routes(request):
    routes = [
        {
            'Endpoint': '/api/cards',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of cards.'
        },
        {
            'Endpoint': '/api/cards/<str:pk>',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single card object.'
        },
        {
            'Endpoint': '/api/cards',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new card with data sent in post request. '
        },
        {
            'Endpoint': '/api/cards/<str:pk>',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates an existing card with data sent in post request. '
        },
        {
            'Endpoint': '/api/cards/<str:pk>',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing card.'
        },
        
    ]
    return Response(routes)

@api_view(['GET'])
def get_cards(request):
    cards = Card.objects.all()
    serializer = CardSerializer(cards, many=True)
    return Response(serializer.data)