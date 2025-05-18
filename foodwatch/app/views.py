from django.shortcuts import redirect, render
from django.views import View
 

class TopView(View):
    def get(self, request):
        print("get")
        return render(request, "top.html")

class SignUpView(View):
    def get(self, request):
        return render(request, "sign_up.html")
    
    def post(self, request):
        print(request.POST)
        return redirect("top")
