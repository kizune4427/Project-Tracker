from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

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
    return JsonResponse(routes, safe=False)