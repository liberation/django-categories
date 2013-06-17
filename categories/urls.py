from django.conf.urls import url
from django.conf.urls import patterns
from django.views.genetric import ListView

from .models import Category

class CategoryTreeList(ListView):
    queryset = Category.objects.filter(level=0)


urlpatterns = patterns('',
    url(r'^$', CategoryTreeList.as_view(),
        name='categories_tree_list'),
)

urlpatterns += patterns('categories.views',
    url(r'^(?P<path>.+)/$', 'category_detail', name='categories_category'),
)
