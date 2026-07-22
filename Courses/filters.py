import django_filters
from .models import Course

class CourseFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    price_gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    slug = django_filters.CharFilter(lookup_expr='exact')
    
    class Meta:
        model = Course
        fields = ['name', 'price', 'slug']