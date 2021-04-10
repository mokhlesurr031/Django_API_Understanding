from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Person
from .serializers import PersonSerializer


@csrf_exempt
def person_data_list(request):


    if request.method == 'GET':
        persons = Person.objects.all()

        # print(f"Person: {persons}")

        serializer = PersonSerializer(persons, many=True)

        # print(f'Serializer: {serializer}')

        json_data = JsonResponse(serializer.data, safe=False)

        # print(json_data)

        return json_data

    if request.method == 'POST':
        data = JSONParser().parse(request)

        print(data)

        serializer = PersonSerializer(data=data)

        print(serializer)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def person_data_detail(request, pk):

    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return HttpResponse("No Person in table")


    if request.method == 'GET':
        serializer = PersonSerializer(person)
        json_data = JsonResponse(serializer.data, safe=False)
        return json_data

    elif request.method == 'DELETE':
        person.delete()
        return HttpResponse("Deleted")

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PersonSerializer(person, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


