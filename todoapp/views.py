from django.shortcuts import render

from django.views.generic import View

from todoapp.models import TaskModel

class TraskListView(View):
    def get(self,request,*args,**kwargs):
        qs=TaskModel.objects.all()
        return render(request,"task_list.html",{"data":qs})

class