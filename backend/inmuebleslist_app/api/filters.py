import django_filters
from inmuebleslist_app.models import Inmueble, Empresa, Persona

class PersonaFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(field_name="nombrePersona", lookup_expr="icontains")

    class Meta:
        model = Persona
        fields = ['nombre']