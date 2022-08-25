from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Home view
@method_decorator(login_required, name='dispatch')
class Home(View):
    def get(self, request):
        return HttpResponse("Mom n Spot Home Page")


# Post List view
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

# Creating Post view
class PostCreate(CreateView):
    model = Post
    fields = ['shop_name', 'img', 'story', 'category', 'neighborhood', 'address']
    template_name = "post_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreate, self).form_valid(form)

    # def get_success_url(self):
    #     return reverse('post')

# Signup view
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
            return HttpResponse("signed up")
            # return redirect("mom_n_pops_list")


