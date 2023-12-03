from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json

def emp_data_view(request):
    emp_data = {'eno':101,'ename':'Rohit','esal':1000,'eaddr':'Hyderabad'}
    resp='<h1>Employee No:{}<br>Employee Name:{}<br>Employee Salary:{}<br>Employee Address:{}</h1>'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eaddr'])
    return HttpResponse(resp)
def emp_data_json_view(request):
    emp_data = {'eno':101,'ename':'Rohit','esal':1000,'eaddr':'Hyderabad'}
    # jsn_data = json.dump(emp_data)
    # return HttpResponse(jsn_data,content_type='application/json')
    return JsonResponse(emp_data)

from django.views.generic import View
class JsonCBV(View):
    def get(self,request,*args,**kwargs):
       emp_data = {'eno':101,'ename':'Rohit','esal':1000,'eaddr':'Hyderabad'}
       return JsonResponse(emp_data)
    
from testApp.mixin import JsonResponseMinxin
class JsonCBV2(JsonResponseMinxin,View):
    def get(self,request,*args,**kwargs):
        emp_data={'eno':100,'ename':'Sunny Leone','esal':1000,'eaddr':'Hyderabad'}
        return self.render_to_json_response(emp_data)

