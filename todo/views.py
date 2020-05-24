from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,DeleteView,UpdateView
from .models import TodoModel
from django.urls import reverse_lazy

# Create your views here.

class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    # models.pyに指定されたフィールドを指定しないとエラーが起きる
    fields = ('title','memo','priority','duedate')
    # urls.pyで指定したclassに戻す
    success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    # urls.pyで指定したclassに戻す
    success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
    template_name = 'Update.html'
    model = TodoModel
    # 更新対象のフィールドを指定する(今回は全部を対象とする)
    fields = ('title','memo','priority','duedate')
    # urls.pyで指定したclassに戻す
    success_url = reverse_lazy('list')