from django.shortcuts import render
from django.views.generic import (
    ListView, 
    CreateView,
)
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import stocks
from django.views import generic

class PostListView(ListView):
    model = stocks
    template_name = 'home/home.html'
    context_object_name = 'stocks'

class PostCreateView(CreateView):
    model = stocks
    fields = ['amount', 'ingredients']
    template_name = 'home/new_stocks.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

class UserOnlyMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser

class Profile(UserOnlyMixin, generic.DetailView):
    model = stocks
    template_name = 'home/home_info.html'