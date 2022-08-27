from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .forms import PostForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.files.storage import FileSystemStorage




# #Home View
@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = "base.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context

# Signup View
class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
        
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("post_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

# PostList View (Index)
@method_decorator(login_required, name='dispatch')
class PostList(TemplateView):
    template_name = "post_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shop_name = self.request.GET.get("shop_name")
        if shop_name != None:
            context["posts"] = Post.objects.filter(shop_name__icontains=shop_name, user=self.request.user)
        # We add a header context that includes the search param
            context["header"] = f"Searching for {shop_name}"
        
        else:
            context["posts"] = Post.objects.filter(user=self.request.user)
            context["header"] = "Your Mom n Spots"
        return context

# Create PostCreate View 
class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('post_create')
    template_name = 'post_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all()
        context['posts'] = posts
        return context


# # uploading image function based view to PostCreate

# def upload(request):
#     context = {}
#     if request.method == 'POST':
#         uploaded_file = request.FILES('img')
#         fs = FileSystemStorage()
#         name = fs.save(uploaded_file.name, uploaded_file)
#         context['url'] = fs.url(name)
#     return render(request, 'upload.html', context)
