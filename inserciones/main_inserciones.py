from empleados import *
from aerolinea_aeropuertos import *

"""
Inserciones para la base de datos viajesDB.sqlite3
"""

#  INSERCIONES DE EMPLEADOS Y SUS DERIVADOS
insertar_usuario(4000)
insertar_telefonos()
insertar_empleado()
insertar_pasaporte()
insertar_puesto()

#   INSERCIONES DE AEROLINEAS, AEROPUERTOS Y SUS DERIVADOS
insertar_aerolineas()
insertar_aeropuerto()
insertar_fabricantes()
insertar_aviones(300)
insertar_empleado_aerolinea()
insertar_empleados_aeropuerto()
insertar_aeropuerto_aerolinea()

#   INSERCIONES DE VUELOS Y SUS DERIVADOS
insertar_vuelo(2000)
insertar_clase()
insertar_asiento()
insertar_equipaje_tiquete()
insertar_controlador_vuelo()

#    INSERCIONES DE HORARIOS
insertar_horarios()
insertar_horario_trabajo()
insertar_horario_servicio()

#    INSERCIONES DE BODEGAS Y TALLERES
insertar_taller()
insertar_bodega()
insertar_bodega_avion()
insertar_taller_avion()
insertar_factura()
insertar_danho()
insertar_repuesto()
