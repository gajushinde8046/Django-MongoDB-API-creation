from .models import empData

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def post(request):
    if request.method == 'POST':
        payload = json.loads(request.body)

        empID = payload['empID']
        empName = payload['empName']
        empMobile = payload['empMobile']

        empAddress = payload['empAddress']
        # productDiscription = payload['productDiscription']

        a = empData(empID=empID, empName=empName, empMobile=empMobile,empAddress=empAddress)
        try:
            a.save()
            response = json.dumps([{'Success':'product added successfully!'}])
        except:

            response = json.dumps([{'Error': 'product could not be added!'}])

    return HttpResponse(response, content_type='text/json')
from django.shortcuts import render





@csrf_exempt
def get(request, empID):

    if request.method == 'GET':
        try:
            a = empData.objects.get(empID=empID)
            # response = json.dumps([{'Success':'product fetched successfully!'}])  
            response = json.dumps([{ 'empID': a.empID, 'Employee Name': a.empName ,'Mobile': a.empMobile,'Address': a.empAddress}])
        except:
            response = json.dumps([{ 'Error': 'No Product with this ID'}])
    return HttpResponse(response, content_type='text/json')
# Create your views here.
from django.shortcuts import render

# Create your views here.
