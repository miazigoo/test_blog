from django.shortcuts import render
from .models import News
from django.views.generic import (
    ListView, 
    DeleteView, 
    DetailView, 
    CreateView,
    UpdateView
    )

# Create your views here.
class ShowNewsView(ListView):
    model=News
    template_name='news/news_list.html'
    context_object_name='posts'
    ordering = ['-date']



    def get_context_data(self, **kwargs):
        context = super(ShowNewsView,self).get_context_data(**kwargs)
        context["post_news"] = News.objects.order_by('-date')[:1].get
        print(context)
        return context


# class CreateNewsView(CreateView):
#     model = News
#     fields = ['title', 'text', 'img']
#     context_object_name = 'creat'

#     def form_valid(self, form):
#         form.instance.avtor = self.request.user


class CreateNewsView(CreateView):
    model = News
    fields = ['title', 'text', 'img']

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super(PostCreationView, self).form_valid(form)

    def form_invlaid(self, form):
        form = PostCreationForm(instance=form)
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('blog-home')