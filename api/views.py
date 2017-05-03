from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse as response

"""AIzaSyC4IwU6NFM4FIMa0y1lIIIwrlNW90yxSZc"""
def index( request ):
    return response( { 'akash': 'more'} )
