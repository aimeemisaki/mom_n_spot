from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django import forms
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Tags
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.files.storage import FileSystemStorage

# Home view
@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = "base.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context

def upload(request):
    return render(request, 'upload.html')


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



class PostCreate(CreateView):
    model = Post
    fields = ('shop_name', 'address', 'neighborhood', 'story', 'category')
    success_url = 'post_list'
    template_name = 'post_create.html'

# uploading image function based view to PostCreate
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES('img')
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)











# # Post detail view
# class PostDetail(DetailView):
#     model = Post
#     template_name = "post_detail.html"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["posts"] = Post.objects.all()
#         return context



# PostCreateForm
# class PostCreateForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         exclude = ('user', )
    
#     def __init__(self, *args, **kwargs):
#         self.user = kwargs.pop('user')
#         super(PostCreateForm, self).__init__(*args, **kwargs)
    
#     # To make sure that no mom n spot has the same address
#     def clean_address(self):
#         address = self.cleaned_data['address']
#         if Post.objects.filter(user=self.user, address=address).exists():
#             raise forms.ValidationError("This Mom n Spot already exists in your list.")
#         return Post.shop_name


# # Creating Post view
# @method_decorator(login_required, name='dispatch')
# class PostCreate(CreateView):
#     template_name = "post_create.html"
#     form_class = PostCreateForm
#     # fields = ['shop_name', 'img', 'story', 'category', 'neighborhood', 'address']

    
#     def form_valid(self, forms):
#         self.object = forms.save(commit=False)
#         self.object.user = self.request.user
#         # form.instance.user = self.request.user
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())

#     # Initial Data
#     def get_initial(self, *args, **kwargs):
#         initial = super(PostCreate, self).get_initial(**kwargs)
#         return initial

#     # User is supplied from view during form creation
#     def get_form_kwargs(self, *args, **kwargs):
#         kwargs = super(PostCreate, self).get_form_kwargs(*args, **kwargs)
#         kwargs['user'] = self.request.user
#         return kwargs

        # return super(PostCreate, self).form_valid(form)
    # def get_succcess_url(self):
    #     return reverse('artist_list', kwargs={'pk': self.object.pk})
    

# artist = Artist.objects.get(pk=pk)
#         Song.objects.create(title=title, length=length, artist=artist)

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


