from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from haystack.generic_views import FacetedSearchView as BaseFacetedSearchView
from haystack.query import SearchQuerySet

from .models import Product
from .forms import FacetedProductSearchForm


class HomeView(TemplateView):
    template_name = "home.html"


class ProductView(DetailView):
    template_name = "product.html"
    model = Product


def autocomplete(request):
    sqs = SearchQuerySet().autocomplete(
        content_auto=request.GET.get(
            'query',
            ''))[
        :5]
    s = []
    for result in sqs:
        d = {"value": result.title, "data": result.object.slug}
        s.append(d)
    output = {'suggestions': s}
    return JsonResponse(output)


class FacetedSearchView(BaseFacetedSearchView):

    form_class = FacetedProductSearchForm
    facet_fields = ['category', 'brand']
    template_name = 'search_result.html'
    paginate_by = 3
    context_object_name = 'object_list'
