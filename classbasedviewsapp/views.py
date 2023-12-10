from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class GetInput(View):
      def get(self,request):
          return  render(request, "get.html")
class PostInput(View):
      def get(self, request):
          return render(request, "post.html")
class Add(View):
    def get(self,request):
        x=int(request.GET["t1"])
        y=int(request.GET["t2"])
        z=x+y
        return HttpResponse("The sum is "+str(z))
    def post(self,request):
        x=int(request.POST["t1"])
        y=int(request.POST["t2"])
        z=x+y
        return HttpResponse("The sum is "+str(z))