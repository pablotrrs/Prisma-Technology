from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ListadoVenta,FiltrarPorEstado, RegistrarVentaLocal, EditarVentaLocal, eliminarItemCajero,AnularVentaCajero,ListarItem, VerDetalle, AgregarItem, CambiarEstado, eliminarItem, ListadoVentaCajero, FinalizarVenta, VerItems, ReporteCuentaCorrienteClientes, verComprobantePago, ReporteVentasVendedores, AnularVenta, reporteVentasPorSucursal

urlpatterns = [

    path('listado_ventas/', login_required(ListadoVenta),
         name='listar_ventas'),
    path('registrar_venta_local/', login_required(RegistrarVentaLocal.as_view()),
         name='registrar_venta_local'),
    path('ingresar_monto/<int:pk>/',
         login_required(EditarVentaLocal.as_view()), name='ingresar_monto'),
    path('listado_itemsventa/<int:venta>/',
         login_required(ListarItem), name='listar_itemsventa'),
    path('listar_ventas_por_estado/', login_required(FiltrarPorEstado), name="listar_ventas_por_estado"),
    path('registrar_itemventa/<int:sucursal>/<int:venta>',
         login_required(VerDetalle), name='registrar_itemventa'),
    path('registrar_itemventa/<int:sucursal>/<int:venta>/AgregarItem/',
         login_required(AgregarItem), name='agregar_item'),
    path('listado_ventas/<int:id>/<int:cliente>/',
         login_required(CambiarEstado), name='cambiar_estado'),
    path('eliminar_item/<int:venta>/<int:item>/',
         login_required(eliminarItem), name='eliminar_item'),
    path('eliminar_item_cajero/<int:venta>/<int:item>/',
         login_required(eliminarItemCajero), name='eliminar_item_cajero'),
    path('listado_ventas_cajero/', login_required(ListadoVentaCajero),
         name='listar_ventas_cajero'),
    path('finalizar_venta/<int:venta>/',
         login_required(FinalizarVenta), name='finalizar_venta'),
    path('ver_items/<int:venta>/', login_required(VerItems), name='ver_items'),
    path('reporte_cuenta_corriente_clientes/', login_required(
        ReporteCuentaCorrienteClientes), name='reporte_cuenta_corriente_clientes'),
    path('ver_comprobante/<int:venta_id>/', login_required(verComprobantePago), name= 'ver_comprobante'),
    path('reporte_ventas_vendedor/', login_required(
        ReporteVentasVendedores), name='reporte_ventas_vendedor'),
    path('anular_venta/<int:venta>/', login_required(AnularVenta), name = 'anular_venta'),
    path('reporte_ventas_por_sucursal/', login_required(reporteVentasPorSucursal), name='reporte_ventas_por_sucursal'),
    path('anular_venta_cajero/<int:venta>/', login_required(AnularVentaCajero), name = 'anular_venta_cajero'),
        
]
