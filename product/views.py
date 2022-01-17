from django.shortcuts import render
from django.views.generic import ListView, DetailView
from product.models import ProductModel, CategoryModel, BrandModel, ProductTagModel, ColorModel, SizeModel
from django.db.models import Max, Min

# Create your views here.


class ProductListView(ListView):
    template_name = "shop.html"
    paginate_by = 3

    def get_queryset(self):
        qs = ProductModel.objects.order_by('-pk')
        q = self.request.GET.get('q')
        category = self.request.GET.get('cat')
        brand = self.request.GET.get('brand')
        tag = self.request.GET.get('tag')
        sort = self.request.GET.get('sort')
        size = self.request.GET.get('size')
        color = self.request.GET.get('color')
        price = self.request.GET.get('price')

        if q:
            qs = qs.filter(title__icontains=q)

        if category:
            qs = qs.filter(category_id=category)

        if brand:
            qs = qs.filter(brand_id=brand)

        if tag:
            qs = qs.filter(tags__id=tag)

        if color:
            qs = qs.filter(colors__id=color)

        if size:
            qs = qs.filter(sizes__id=size)

        if price:
            price_from, price_to = price.split(';')
            qs = qs.filter(real_price__gte=price_from, real_price__lte=price_to)

        if sort:
            if sort == 'price':
                qs = qs.order_by('real_price')
            elif sort == '-price':
                qs = qs.order_by('-real_price')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        context['brands'] = BrandModel.objects.all()
        context['colors'] = ColorModel.objects.all()
        context['sizes'] = SizeModel.objects.all()
        context['tags'] = ProductTagModel.objects.all()

        context['min_price'], context['max_price'] = ProductModel.objects.aggregate(
            Min('real_price'),
            Max('real_price'),
        ).values()
        return context


class ProductDetailView(DetailView):
    template_name = 'shop-details.html'
    model = ProductModel

