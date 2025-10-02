from django.shortcuts import render
from . models import Article
from django.views.generic import ListView, DetailView


class ArticleListView(ListView):
    model = Article
    template_name = "blog_module/article_list.html"
    context_object_name = "articles"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = context.get('page_obj') 
        if page:
            context['start_index'] = (page.number - 1) * page.paginator.per_page
        else:
            context['start_index'] = 0
        return context



class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog_module/article_detail.html"
    context_object_name = "article"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

