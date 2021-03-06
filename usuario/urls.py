from django.urls import path
from django.contrib.auth.decorators import login_required
from usuario.views import InicioUsuarios,ListadoUsuario,EditarUsuario,CambiarEstadoUsuario, RegistrarVendedor, RegistrarSupervisor, RegistrarCajero, RegistrarAdministrativo, RegistrarGerenteGeneral
urlpatterns = [
    
    path('inicio_usuarios/', login_required(InicioUsuarios.as_view()), name='inicio_usuarios'),
    path('listado_usuarios/', login_required(ListadoUsuario.as_view()),name='listar_usuarios'),
    path('registrar_gerente/', login_required(RegistrarGerenteGeneral.as_view()),name = 'registrar_gerentegeneral'),
    path('actualizar_usuario/<int:pk>/', login_required(EditarUsuario.as_view()), name = 'actualizar_usuario'),
    path('registrar_vendedor/', login_required(RegistrarVendedor.as_view()),name = 'registrar_vendedor'),
    path('registrar_supervisor/', login_required(RegistrarSupervisor.as_view()),name = 'registrar_supervisor'),
    path('registrar_cajero/', login_required(RegistrarCajero.as_view()),name = 'registrar_cajero'),
    path('registrar_administrativo/', login_required(RegistrarAdministrativo.as_view()),name = 'registrar_administrativo'),
    path('cambiar_estado/<int:pk>/', login_required(CambiarEstadoUsuario.as_view()), name = 'cambiar_estado'),

    
]

