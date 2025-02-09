from django.urls import path
#from inmuebleslist_app.api.views import inmueble_list, inmueble_detalle
from inmuebleslist_app.api.views import InmuebleListAV, InmuebleDetalleAV, PersonaList, PersonaDetail, EmpresaList, EmpresaDetail, InteresadoList, InteresadoDetail, PersonaFilteredList
urlpatterns=[
    path('list/', InmuebleListAV.as_view(), name='inmueble-list'),
    path('<int:pk>/', InmuebleDetalleAV.as_view(), name='inmueble-detalle'),
    #EMPRESA
    path('listEmpresa/', EmpresaList.as_view(), name='empresa-list'),
    path('<int:pk>/', EmpresaList.as_view(), name='empresa-detalle'),
    #INTERESADO
    path('listInteresado/', InteresadoList.as_view(), name='intersado-list'),
    path('<int:pk>/', InteresadoDetail.as_view(), name='intersado-detalle'),
    #PERSONA
    path('listPersona/', PersonaList.as_view(), name='persona-list'),
    path('pe/<int:pk>/', PersonaDetail.as_view(), name='persona-detalle'),
    path('personas/filtradas/', PersonaFilteredList.as_view(), name='persona-filtradas'),

]
