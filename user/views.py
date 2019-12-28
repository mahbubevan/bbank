from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from . models import User
# Create your views here.

# List View Here
class UserListView(generic.ListView):
    template_name = 'user/list_user.html'
    model = User


class UserDetailView(generic.DetailView):
    template_name = 'user/detail_user.html'
    model = User


class UserCreateView(generic.CreateView):
    template_name = 'user/create_user.html'
    model = User
    fields = [
            'name',
            'email', 'password', 'location',
            'blood_group','age','gender',
            'status', 'helping_count',
        ]


class UserUpdateView(generic.UpdateView):
    model = User
    template_name = 'user/update_user.html'
    fields = [
        'name','email','age','status','location',
    ]


class UserDeleteView(generic.DeleteView):
    # template_name = 'user/delete_user.html'
    model = User
    success_url = reverse_lazy('user:list')

    def get(self,request,*args,**kwargs):
        return self.post(request,*args,**kwargs)
