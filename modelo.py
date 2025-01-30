"""
Python model "modelo.py"
Translated using PySD version 0.9.0
"""
from __future__ import division
import numpy as np
from pysd import utils
import xarray as xr

from pysd.py_backend.functions import cache
from pysd.py_backend import functions

_subscript_dict = {}

_namespace = {
    'TIME': 'time',
    'Time': 'time',
    'tasa adopción': 'tasa_adopción',
    'Impuesto de emisión': 'impuesto_de_emisión',
    'Restriccion movilidad': 'restriccion_movilidad',
    'Incentivo vehículo electico': 'incentivo_vehículo_electico',
    'LCOE panel': 'lcoe_panel',
    'cociente paridad de red': 'cociente_paridad_de_red',
    'Panel price': 'panel_price',
    'Residential Electricity Demand': 'residential_electricity_demand',
    'publicidad': 'publicidad',
    'Efecto de publicidad': 'efecto_de_publicidad',
    'Tamaño panel': 'tamaño_panel',
    'Escenario tecnologia': 'escenario_tecnologia',
    'Escenarios': 'escenarios',
    'Demanta total de energia': 'demanta_total_de_energia',
    'desecho de vehículos eléctricos': 'desecho_de_vehículos_eléctricos',
    'desecho vehículos convencionales': 'desecho_vehículos_convencionales',
    'Costo de operación y mantenimiento vehículo eléctrico':
    'costo_de_operación_y_mantenimiento_vehículo_eléctrico',
    'Demanda residencial total': 'demanda_residencial_total',
    'Tiempo de vida vehículo combustion': 'tiempo_de_vida_vehículo_combustion',
    'Escenario chatarrización': 'escenario_chatarrización',
    'costo de vida de vehículo convencional': 'costo_de_vida_de_vehículo_convencional',
    'Precio vehículo eléctrico': 'precio_vehículo_eléctrico',
    'Costos totales vehículos eléctricos': 'costos_totales_vehículos_eléctricos',
    'precio litro de gasolina': 'precio_litro_de_gasolina',
    'Atractividad relativa de vehículos eléctricos':
    'atractividad_relativa_de_vehículos_eléctricos',
    'Capacidad a construir': 'capacidad_a_construir',
    'Demanda electricidad vehiculos electricos': 'demanda_electricidad_vehiculos_electricos',
    'Factor de disponibilidad': 'factor_de_disponibilidad',
    'Factor de emision': 'factor_de_emision',
    'Emisiones sector electrico': 'emisiones_sector_electrico',
    'CO2 Emissions': 'co2_emissions',
    'Margen': 'margen',
    'Conocimiento': 'conocimiento',
    'energía': 'energía',
    'Emision por km': 'emision_por_km',
    'Emisiones vehículos': 'emisiones_vehículos',
    'escenario publicidad': 'escenario_publicidad',
    'Emision por litro': 'emision_por_litro',
    'Atractividad de vehículos convencionales': 'atractividad_de_vehículos_convencionales',
    'demanda de vehículos': 'demanda_de_vehículos',
    'capacidad de km a recorrer con bateria': 'capacidad_de_km_a_recorrer_con_bateria',
    'Relacion estaciones de carga': 'relacion_estaciones_de_carga',
    'Estaciones de carga': 'estaciones_de_carga',
    'Inicio capacidad a construir': 'inicio_capacidad_a_construir',
    'Conocimiento de la tecnología': 'conocimiento_de_la_tecnología',
    'kWh requeridos en bateria': 'kwh_requeridos_en_bateria',
    'Costo de cada km recorrido en un vehículo convencional':
    'costo_de_cada_km_recorrido_en_un_vehículo_convencional',
    'Costo de cada km recorrido en un vehículo eléctrico':
    'costo_de_cada_km_recorrido_en_un_vehículo_eléctrico',
    'Litros de gasolina necesarios para recorres 1 km':
    'litros_de_gasolina_necesarios_para_recorres_1_km',
    'vehículos convencionales en uso': 'vehículos_convencionales_en_uso',
    'Costos totales vehículos convencioanles': 'costos_totales_vehículos_convencioanles',
    'Crecimiento estaciones de carga': 'crecimiento_estaciones_de_carga',
    'Tasa de crecimiendo vehículos': 'tasa_de_crecimiendo_vehículos',
    'Tiempo de vida vehículo': 'tiempo_de_vida_vehículo',
    'Precio vehículos convencionales': 'precio_vehículos_convencionales',
    'Estaciones necesarias': 'estaciones_necesarias',
    'Venta de vehículos eléctricos': 'venta_de_vehículos_eléctricos',
    'Estaciones de carga necesarias': 'estaciones_de_carga_necesarias',
    'vehículos totales': 'vehículos_totales',
    'Estaciones de gasolina': 'estaciones_de_gasolina',
    'Electric Vehicles': 'electric_vehicles',
    'km promedio por año por vehículo': 'km_promedio_por_año_por_vehículo',
    'venta de vehículos convencionales': 'venta_de_vehículos_convencionales',
    'capacidad construcción promedio': 'capacidad_construcción_promedio',
    'Capacidad construida': 'capacidad_construida',
    'Capacidad en construccion': 'capacidad_en_construccion',
    'Capacidad obsoleta': 'capacidad_obsoleta',
    'Capacidad solar': 'capacidad_solar',
    'Demanda': 'demanda',
    'Efecto precio en capacidad a construir': 'efecto_precio_en_capacidad_a_construir',
    'Efecto precio en incremento demanda': 'efecto_precio_en_incremento_demanda',
    'incremento promedio de la demanda': 'incremento_promedio_de_la_demanda',
    'Tiempo promedio construccion': 'tiempo_promedio_construccion',
    'variacion en la demanda': 'variacion_en_la_demanda',
    'Generacion total paneles': 'generacion_total_paneles',
    'promedio de vida': 'promedio_de_vida',
    'precio de electricidad': 'precio_de_electricidad',
    'precio': 'precio',
    'Consumo por hogar': 'consumo_por_hogar',
    'Demanda residencial hogares no potenciales ni adaptadores':
    'demanda_residencial_hogares_no_potenciales_ni_adaptadores',
    'Demanda residencial adaptadores': 'demanda_residencial_adaptadores',
    'otros cargos': 'otros_cargos',
    'Fraccion de adopcion': 'fraccion_de_adopcion',
    'Hogares dispuestos a adoptar': 'hogares_dispuestos_a_adoptar',
    'Costo fijo': 'costo_fijo',
    'crecimiento neto': 'crecimiento_neto',
    'Demanda residencial hogares potenciales': 'demanda_residencial_hogares_potenciales',
    'Días en mes': 'días_en_mes',
    'Efecto de paridad de red en hogares dispuestos a adoptar':
    'efecto_de_paridad_de_red_en_hogares_dispuestos_a_adoptar',
    'Generación solar panel hogar': 'generación_solar_panel_hogar',
    'Hogares': 'hogares',
    'Household PV adopters': 'household_pv_adopters',
    'Población': 'población',
    'Hogares potenciales': 'hogares_potenciales',
    'Horas sol': 'horas_sol',
    'personas por hogar': 'personas_por_hogar',
    'Tasa de contacto': 'tasa_de_contacto',
    'tasa crecimiento hogares potenciales': 'tasa_crecimiento_hogares_potenciales',
    'tasa crecimiento': 'tasa_crecimiento',
    'Cargo distribución': 'cargo_distribución',
    'FINAL TIME': 'final_time',
    'INITIAL TIME': 'initial_time',
    'SAVEPER': 'saveper',
    'TIME STEP': 'time_step'
}

__pysd_version__ = "0.9.0"


@cache('step')
def tasa_adopción():
    """
    Real Name: tasa adopción
    Original Eqn: (Efecto de paridad de red en hogares dispuestos a adoptar*1.25)*(Hogares potenciales\ *Efecto de publicidad+Tasa de contacto*Fraccion de adopcion*Hogares potenciales*Household PV adopters /(Household PV adopters+Hogares potenciales))
    Units: 
    Limits: (None, None)
    Type: component

    ('Hogares potenciales adoptadores'*p +(q-p)*('Hogares Adoptadores') - 
        q/'Hogares potenciales adoptadores' * ('Hogares Adoptadores') ^2 )
    """
    return (efecto_de_paridad_de_red_en_hogares_dispuestos_a_adoptar() *
            1.25) * (hogares_potenciales() * efecto_de_publicidad() + tasa_de_contacto() *
                     fraccion_de_adopcion() * hogares_potenciales() * household_pv_adopters() /
                     (household_pv_adopters() + hogares_potenciales()))


@cache('run')
def impuesto_de_emisión():
    """
    Real Name: Impuesto de emisión
    Original Eqn: 1
    Units: 
    Limits: (None, None)
    Type: constant


    """
    return 1


@cache('run')
def restriccion_movilidad():
    """
    Real Name: Restriccion movilidad
    Original Eqn: 1
    Units: 
    Limits: (None, None)
    Type: constant

    https://www.carroya.com/noticias/guia-para-conductores/conoce-cuales-vehicu
        los-estan-exentos-del-pico-y-placa-en-bogota-4507
    """
    return 1


@cache('run')
def incentivo_vehículo_electico():
    """
    Real Name: Incentivo vehículo electico
    Original Eqn: 1
    Units: 
    Limits: (None, None)
    Type: constant


    """
    return 1


@cache('step')
def lcoe_panel():
    """
    Real Name: LCOE panel
    Original Eqn: WITH LOOKUP ( Time, ([(0,0)-(300,300)],(1,250),(79.8165,184.211),(133.945,157.895),(174.312,151.316),(190.826\ ,155.263),(203.67,152.632),(213.761 ,148.684),(222.936,148.684),(233.945,148.684),(243.119,148.684),(257.798,146.053),(\ 268.807,146.053),(277.982,146.053),(283.486 ,143.421),(300,136.842),(300,135) ))
    Units: 
    Limits: (None, None)
    Type: component

    https://www.eia.gov/outlooks/aeo/pdf/electricity_generation.pdf
    """
    return functions.lookup(time(), [
        1, 79.8165, 133.945, 174.312, 190.826, 203.67, 213.761, 222.936, 233.945, 243.119, 257.798,
        268.807, 277.982, 283.486, 300, 300
    ], [
        250, 184.211, 157.895, 151.316, 155.263, 152.632, 148.684, 148.684, 148.684, 148.684,
        146.053, 146.053, 146.053, 143.421, 136.842, 135
    ])


@cache('step')
def cociente_paridad_de_red():
    """
    Real Name: cociente paridad de red
    Original Eqn: ((precio de electricidad/(LCOE panel))*Panel price)/10
    Units: 
    Limits: (None, None)
    Type: component


    """
    return ((precio_de_electricidad() / (lcoe_panel())) * panel_price()) / 10


@cache('run')
def panel_price():
    """
    Real Name: Panel price
    Original Eqn: 2
    Units: 
    Limits: (None, None)
    Type: constant


    """
    return 2


@cache('step')
def residential_electricity_demand():
    """
    Real Name: Residential Electricity Demand
    Original Eqn: Demanda residencial total/1e+06
    Units: GWh/yr
    Limits: (None, None)
    Type: component


    """
    return demanda_residencial_total() / 1e+06


@cache('step')
def publicidad():
    """
    Real Name: publicidad
    Original Eqn: IF THEN ELSE(Escenarios=1, 0.8 , IF THEN ELSE(Escenarios=2, 1 , IF THEN ELSE(Escenarios\ =3, 1.2 , 0.8 ) ) )
    Units: 
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(
        escenarios() == 1, 0.8,
        functions.if_then_else(escenarios() == 2, 1,
                               functions.if_then_else(escenarios() == 3, 1.2, 0.8)))


@cache('step')
def efecto_de_publicidad():
    """
    Real Name: Efecto de publicidad
    Original Eqn: 0.01*publicidad
    Units: 
    Limits: (None, None)
    Type: component


    """
    return 0.01 * publicidad()


@cache('step')
def tamaño_panel():
    """
    Real Name: Tamaño panel
    Original Eqn: IF THEN ELSE(Escenarios=1 :OR: Escenarios=4, 2.5, 2.5 )
    Units: 
    Limits: (None, None)
    Type: component

    2.5
    """
    return functions.if_then_else(escenarios() == 1 or escenarios() == 4, 2.5, 2.5)


@cache('step')
def escenario_tecnologia():
    """
    Real Name: Escenario tecnologia
    Original Eqn: IF THEN ELSE( Escenarios=1 :OR: Escenarios= 4 , 1 , 2 )
    Units: 
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(escenarios() == 1 or escenarios() == 4, 1, 2)


@cache('run')
def escenarios():
    """
    Real Name: Escenarios
    Original Eqn: 4
    Units: 
    Limits: (None, None)
    Type: constant


    """
    return 4


@cache('step')
def demanta_total_de_energia():
    """
    Real Name: Demanta total de energia
    Original Eqn: max(0,Demanda-Generacion total paneles)
    Units: 
    Limits: (None, None)
    Type: component


    """
    return np.maximum(0, demanda() - generacion_total_paneles())


@cache('step')
def desecho_de_vehículos_eléctricos():
    """
    Real Name: desecho de vehículos eléctricos
    Original Eqn: Electric Vehicles/Tiempo de vida vehículo
    Units: 
    Limits: (None, None)
    Type: component


    """
    return electric_vehicles() / tiempo_de_vida_vehículo()


@cache('step')
def desecho_vehículos_convencionales():
    """
    Real Name: desecho vehículos convencionales
    Original Eqn: vehículos convencionales en uso/Tiempo de vida vehículo combustion
    Units: 
    Limits: (None, None)
    Type: component


    """
    return vehículos_convencionales_en_uso() / tiempo_de_vida_vehículo_combustion()


@cache('step')
def costo_de_operación_y_mantenimiento_vehículo_eléctrico():
    """
    Real Name: Costo de operación y mantenimiento vehículo eléctrico
    Original Eqn: Costo de cada km recorrido en un vehículo eléctrico*km promedio por año por vehículo\ *Tiempo de vida vehículo
    Units: 
    Limits: (None, None)
    Type: component


    """
    return costo_de_cada_km_recorrido_en_un_vehículo_eléctrico(
    ) * km_promedio_por_año_por_vehículo() * tiempo_de_vida_vehículo()


@cache('step')
def demanda_residencial_total():
    """
    Real Name: Demanda residencial total
    Original Eqn: Demanda residencial hogares potenciales+Demanda residencial adaptadores+Demanda residencial hogares no potenciales ni adaptadores\ +Demanda electricidad vehiculos electricos
    Units: 
    Limits: (None, None)
    Type: component


    """
    return demanda_residencial_hogares_potenciales() + demanda_residencial_adaptadores(
    ) + demanda_residencial_hogares_no_potenciales_ni_adaptadores(
    ) + demanda_electricidad_vehiculos_electricos()


@cache('step')
def tiempo_de_vida_vehículo_combustion():
    """
    Real Name: Tiempo de vida vehículo combustion
    Original Eqn: IF THEN ELSE(Escenario chatarrización=1, 25 , 15 )
    Units: 
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(escenario_chatarrización() == 1, 25, 15)


@cache('run')
def escenario_chatarrización():
    """
    Real Name: Escenario chatarrización
    Original Eqn: 2
    Units: 
    Limits: (None, None)
    Type: constant


    """
    return 2


@cache('step')
def costo_de_vida_de_vehículo_convencional():
    """
    Real Name: costo de vida de vehículo convencional
    Original Eqn: Costo de cada km recorrido en un vehículo convencional*km promedio por año por vehículo\ *Tiempo de vida vehículo
    Units: 
    Limits: (None, None)
    Type: component


    """
    return costo_de_cada_km_recorrido_en_un_vehículo_convencional(
    ) * km_promedio_por_año_por_vehículo() * tiempo_de_vida_vehículo()


@cache('step')
def precio_vehículo_eléctrico():
    """
    Real Name: Precio vehículo eléctrico
    Original Eqn: WITH LOOKUP ( Time, ([(0,0)-(2040,3.40282e+38)],(2020,1e+08),(2022,8.5e+07),(2025,7.3e+07),(2030,6.5e+07\ ),(2035,6e+07),(2040,5.5e+07) ))
    Units: 
    Limits: (None, None)
    Type: component


    """
    return functions.lookup(time(), [2020, 2022, 2025, 2030, 2035, 2040],
                            [1e+08, 8.5e+07, 7.3e+07, 6.5e+07, 6e+07, 5.5e+07])


@cache('step')
def costos_totales_vehículos_eléctricos():
    """
    Real Name: Costos totales vehículos eléctricos
    Original Eqn: Costo de operación y mantenimiento vehículo eléctrico+Precio vehículo eléctrico\ *Incentivo vehículo electico
    Units: 
    Limits: (None, None)
    Type: component


    """
    return costo_de_operación_y_mantenimiento_vehículo_eléctrico(
    ) + precio_vehículo_eléctrico() * incentivo_vehículo_electico()


@cache('step')
def precio_litro_de_gasolina():
    """
    Real Name: precio litro de gasolina
    Original Eqn: Impuesto de emisión*9030/3.78541
    Units: 
    Limits: (None, None)
    Type: component


    """
    return impuesto_de_emisión() * 9030 / 3.78541


@cache('step')
def atractividad_relativa_de_vehículos_eléctricos():
    """
    Real Name: Atractividad relativa de vehículos eléctricos
    Original Eqn: (Costos totales vehículos convencioanles/(Costos totales vehículos eléctricos+Costos totales vehículos convencioanles ))*Conocimiento*Relacion estaciones de carga/Restriccion movilidad
    Units: 
    Limits: (None, None)
    Type: component


    """
    return (costos_totales_vehículos_convencioanles() /
            (costos_totales_vehículos_eléctricos() + costos_totales_vehículos_convencioanles())
            ) * conocimiento() * relacion_estaciones_de_carga() / restriccion_movilidad()


@cache('step')
def capacidad_a_construir():
    """
    Real Name: Capacidad a construir
    Original Eqn: DELAY3(Inicio capacidad a construir, Tiempo promedio construccion)+IF THEN ELSE(Time\ =2022, 7/0.125, 0 )
    Units: 
    Limits: (None, None)
    Type: component


    """
    return delay_inicio_capacidad_a_construir_tiempo_promedio_construccion_inicio_capacidad_a_construir_3(
    ) + functions.if_then_else(time() == 2022, 7 / 0.125, 0)


@cache('step')
def demanda_electricidad_vehiculos_electricos():
    """
    Real Name: Demanda electricidad vehiculos electricos
    Original Eqn: Electric Vehicles*km promedio por año por vehículo*kWh requeridos en bateria/capacidad de km a recorrer con bateria
    Units: 
    Limits: (None, None)
    Type: component


    """
    return electric_vehicles() * km_promedio_por_año_por_vehículo() * kwh_requeridos_en_bateria(
    ) / capacidad_de_km_a_recorrer_con_bateria()


@cache('step')
def factor_de_disponibilidad():
    """
    Real Name: Factor de disponibilidad
    Original Eqn: IF THEN ELSE(Time<=2023, 0.5 , 0.5 )
    Units: 
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(time() <= 2023, 0.5, 0.5)


@cache('step')
def factor_de_emision():
    """
    Real Name: Factor de emision
    Original Eqn: IF THEN ELSE(Time<=2023, 130 , 130 )
    Units: 
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(time() <= 2023, 130, 130)


@cache('step')
def emisiones_sector_electrico():
    """
    Real Name: Emisiones sector electrico
    Original Eqn: Demanta total de energia*Factor de emision
    Units: 
    Limits: (None, None)
    Type: component


    """
    return demanta_total_de_energia() * factor_de_emision()


@cache('step')
def co2_emissions():
    """
    Real Name: CO2 Emissions
    Original Eqn: Emisiones sector electrico+Emisiones vehículos
    Units: Ton
    Limits: (None, None)
    Type: component


    """
    return emisiones_sector_electrico() + emisiones_vehículos()


@cache('step')
def margen():
    """
    Real Name: Margen
    Original Eqn: (energía-(Demanta total de energia))/(Demanta total de energia)
    Units: 
    Limits: (None, None)
    Type: component


    """
    return (energía() - (demanta_total_de_energia())) / (demanta_total_de_energia())


@cache('step')
def conocimiento():
    """
    Real Name: Conocimiento
    Original Eqn: IF THEN ELSE(Escenario tecnologia=1, Conocimiento de la tecnología , escenario publicidad\ )
    Units: 
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(escenario_tecnologia() == 1, conocimiento_de_la_tecnología(),
                                  escenario_publicidad())


@cache('step')
def energía():
    """
    Real Name: energía
    Original Eqn: Capacidad construida*Factor de disponibilidad*360*24
    Units: 
    Limits: (None, None)
    Type: component


    """
    return capacidad_construida() * factor_de_disponibilidad() * 360 * 24


@cache('step')
def emision_por_km():
    """
    Real Name: Emision por km
    Original Eqn: Emision por litro*Litros de gasolina necesarios para recorres 1 km
    Units: 
    Limits: (None, None)
    Type: component


    """
    return emision_por_litro() * litros_de_gasolina_necesarios_para_recorres_1_km()


@cache('step')
def emisiones_vehículos():
    """
    Real Name: Emisiones vehículos
    Original Eqn: Emision por km*km promedio por año por vehículo*vehículos convencionales en uso/1000
    Units: mton
    Limits: (None, None)
    Type: component


    """
    return emision_por_km() * km_promedio_por_año_por_vehículo() * vehículos_convencionales_en_uso(
    ) / 1000


@cache('step')
def escenario_publicidad():
    """
    Real Name: escenario publicidad
    Original Eqn: WITH LOOKUP ( Time, ([(2020,0)-(2060,1)],(2020,0.2),(2021,0.25),(2022,0.3),(2023,0.35),(2024,0.4),(2025\ ,0.5),(2026,0.6),(2027,0.7),(2028,0.88),(2029,0.9),(2030,1),(2031,1),(2040,1),(2050\ ,1),(2060,1),(2522.94,1) ))
    Units: 
    Limits: (None, None)
    Type: component

    https://ieeexplore.ieee.org/abstract/document/7001717
    """
    return functions.lookup(time(), [
        2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2040, 2050, 2060,
        2522.94
    ], [0.2, 0.25, 0.3, 0.35, 0.4, 0.5, 0.6, 0.7, 0.88, 0.9, 1, 1, 1, 1, 1, 1])


@cache('run')
def emision_por_litro():
    """
    Real Name: Emision por litro
    Original Eqn: 2.3
    Units: kg/l
    Limits: (None, None)
    Type: constant

    https://forococheselectricos.com/2020/02/cuanto-contamina-extraer-petroleo-
        y-convertirlo-en-gasolina-o-diesel.html#: 
        :text=Dicho%20de%20otra%20forma%2C%20un,consumo%20de%20combustible%20es%20i
        nferior).
    """
    return 2.3


@cache('step')
def atractividad_de_vehículos_convencionales():
    """
    Real Name: Atractividad de vehículos convencionales
    Original Eqn: 1-Atractividad relativa de vehículos eléctricos
    Units: 
    Limits: (None, None)
    Type: component


    """
    return 1 - atractividad_relativa_de_vehículos_eléctricos()


@cache('step')
def demanda_de_vehículos():
    """
    Real Name: demanda de vehículos
    Original Eqn: desecho de vehículos eléctricos+desecho vehículos convencionales+vehículos totales\ *Tasa de crecimiendo vehículos
    Units: 
    Limits: (None, None)
    Type: component


    """
    return desecho_de_vehículos_eléctricos() + desecho_vehículos_convencionales(
    ) + vehículos_totales() * tasa_de_crecimiendo_vehículos()


@cache('step')
def capacidad_de_km_a_recorrer_con_bateria():
    """
    Real Name: capacidad de km a recorrer con bateria
    Original Eqn: WITH LOOKUP ( Time, ([(0,0)-(3000,300)],(2020,160),(2025,180),(2030,200),(2040,250) ))
    Units: 
    Limits: (None, None)
    Type: component

    https://www-sciencedirect-com.ezproxy.unal.edu.co/science/article/pii/S0306
        261919312711
    """
    return functions.lookup(time(), [2020, 2025, 2030, 2040], [160, 180, 200, 250])


@cache('step')
def relacion_estaciones_de_carga():
    """
    Real Name: Relacion estaciones de carga
    Original Eqn: min(Estaciones de carga/Estaciones de gasolina,1)
    Units: 
    Limits: (None, None)
    Type: component


    """
    return np.minimum(estaciones_de_carga() / estaciones_de_gasolina(), 1)


@cache('step')
def estaciones_de_carga():
    """
    Real Name: Estaciones de carga
    Original Eqn: INTEG ( Crecimiento estaciones de carga, 202)
    Units: 
    Limits: (None, None)
    Type: component

    https://www.larepublica.co/economia/colombia-el-tercer-pais-de-la-region-co
        n-mas-estaciones-de-carga-publicas-y-privadas-3370038
    """
    return integ_estaciones_de_carga()


@cache('step')
def inicio_capacidad_a_construir():
    """
    Real Name: Inicio capacidad a construir
    Original Eqn: IF THEN ELSE(Time<2024, 0 , capacidad construcción promedio*Efecto precio en capacidad a construir\ )
    Units: 
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(
        time() < 2024, 0,
        capacidad_construcción_promedio() * efecto_precio_en_capacidad_a_construir())


@cache('step')
def conocimiento_de_la_tecnología():
    """
    Real Name: Conocimiento de la tecnología
    Original Eqn: WITH LOOKUP ( Time, ([(2020,0)-(2060,1)],(2020,0.2),(2021,0.2),(2022,0.22),(2023,0.3),(2024,0.35),(2025\ ,0.4),(2026,0.42),(2027,0.5),(2028,0.6),(2029,0.64),(2030,0.7),(2031,0.9),(2040,0.9\ ),(2050,1),(2060,1),(2522.94,1) ))
    Units: 
    Limits: (None, None)
    Type: component

    https://ieeexplore.ieee.org/abstract/document/7001717
    """
    return functions.lookup(time(), [
        2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2040, 2050, 2060,
        2522.94
    ], [0.2, 0.2, 0.22, 0.3, 0.35, 0.4, 0.42, 0.5, 0.6, 0.64, 0.7, 0.9, 0.9, 1, 1, 1])


@cache('run')
def kwh_requeridos_en_bateria():
    """
    Real Name: kWh requeridos en bateria
    Original Eqn: 24
    Units: 
    Limits: (None, None)
    Type: constant

    https://puntoycarga.com/punto-de-recarga/kw-bateria-coche-electrico/
    """
    return 24


@cache('step')
def costo_de_cada_km_recorrido_en_un_vehículo_convencional():
    """
    Real Name: Costo de cada km recorrido en un vehículo convencional
    Original Eqn: Litros de gasolina necesarios para recorres 1 km*precio litro de gasolina
    Units: 
    Limits: (None, None)
    Type: component


    """
    return litros_de_gasolina_necesarios_para_recorres_1_km() * precio_litro_de_gasolina()


@cache('step')
def costo_de_cada_km_recorrido_en_un_vehículo_eléctrico():
    """
    Real Name: Costo de cada km recorrido en un vehículo eléctrico
    Original Eqn: precio de electricidad*kWh requeridos en bateria/capacidad de km a recorrer con bateria
    Units: $
    Limits: (None, None)
    Type: component


    """
    return precio_de_electricidad() * kwh_requeridos_en_bateria(
    ) / capacidad_de_km_a_recorrer_con_bateria()


@cache('run')
def litros_de_gasolina_necesarios_para_recorres_1_km():
    """
    Real Name: Litros de gasolina necesarios para recorres 1 km
    Original Eqn: 1/7.5
    Units: 
    Limits: (None, None)
    Type: constant


    """
    return 1 / 7.5


@cache('step')
def vehículos_convencionales_en_uso():
    """
    Real Name: vehículos convencionales en uso
    Original Eqn: INTEG ( venta de vehículos convencionales-desecho vehículos convencionales, 6.19e+06)
    Units: carros
    Limits: (None, None)
    Type: component


    """
    return integ_vehículos_convencionales_en_uso()


@cache('step')
def costos_totales_vehículos_convencioanles():
    """
    Real Name: Costos totales vehículos convencioanles
    Original Eqn: costo de vida de vehículo convencional+Precio vehículos convencionales
    Units: 
    Limits: (None, None)
    Type: component


    """
    return costo_de_vida_de_vehículo_convencional() + precio_vehículos_convencionales()


@cache('step')
def crecimiento_estaciones_de_carga():
    """
    Real Name: Crecimiento estaciones de carga
    Original Eqn: max(Estaciones de carga necesarias-Estaciones de carga,0)
    Units: 
    Limits: (None, None)
    Type: component


    """
    return np.maximum(estaciones_de_carga_necesarias() - estaciones_de_carga(), 0)


@cache('step')
def tasa_de_crecimiendo_vehículos():
    """
    Real Name: Tasa de crecimiendo vehículos
    Original Eqn: WITH LOOKUP ( Time, ([(0,0)-(3000,10)],(2020,0.021),(2025,0.015),(2030,0.01),(2035,0.005),(2040,0),(2050\ ,0) ))
    Units: 
    Limits: (None, None)
    Type: component

    Se tiene en cuenta el crecimiento poblacional y se espera que la población deje de 
        crecer entre el 2040 y 2050        Dane
    """
    return functions.lookup(time(), [2020, 2025, 2030, 2035, 2040, 2050],
                            [0.021, 0.015, 0.01, 0.005, 0, 0])


@cache('run')
def tiempo_de_vida_vehículo():
    """
    Real Name: Tiempo de vida vehículo
    Original Eqn: 8.3
    Units: 
    Limits: (None, None)
    Type: constant

    Información tomada del promedio (ver archivo de excel)
    """
    return 8.3


@cache('run')
def precio_vehículos_convencionales():
    """
    Real Name: Precio vehículos convencionales
    Original Eqn: 9.2e+07
    Units: 
    Limits: (None, None)
    Type: constant

    https://www.larepublica.co/empresas/precio-promedio-de-los-usados-crecio-33
        -21-segun-reporte-de-mercado-libre-vis-3297096
    """
    return 9.2e+07


@cache('run')
def estaciones_necesarias():
    """
    Real Name: Estaciones necesarias
    Original Eqn: 0.033
    Units: 
    Limits: (None, None)
    Type: constant


    """
    return 0.033


@cache('step')
def venta_de_vehículos_eléctricos():
    """
    Real Name: Venta de vehículos eléctricos
    Original Eqn: Atractividad relativa de vehículos eléctricos*demanda de vehículos
    Units: 
    Limits: (None, None)
    Type: component


    """
    return atractividad_relativa_de_vehículos_eléctricos() * demanda_de_vehículos()


@cache('step')
def estaciones_de_carga_necesarias():
    """
    Real Name: Estaciones de carga necesarias
    Original Eqn: Estaciones necesarias*Electric Vehicles
    Units: 
    Limits: (None, None)
    Type: component


    """
    return estaciones_necesarias() * electric_vehicles()


@cache('step')
def vehículos_totales():
    """
    Real Name: vehículos totales
    Original Eqn: vehículos convencionales en uso+Electric Vehicles
    Units: 
    Limits: (None, None)
    Type: component

    El dato de los carros se toma de 
        https://www.eltiempo.com/economia/sectores/colombia-en-cifras-segun-el-regi
        stro-unico-nacional-de-transito-455152
    """
    return vehículos_convencionales_en_uso() + electric_vehicles()


@cache('run')
def estaciones_de_gasolina():
    """
    Real Name: Estaciones de gasolina
    Original Eqn: 10000
    Units: 
    Limits: (None, None)
    Type: constant


    """
    return 10000


@cache('step')
def electric_vehicles():
    """
    Real Name: Electric Vehicles
    Original Eqn: INTEG ( Venta de vehículos eléctricos-desecho de vehículos eléctricos, 7537)
    Units: Numbers of cars
    Limits: (None, None)
    Type: component

    https://caracol.com.co/radio/2022/04/05/economia/1649195552_552385.html
    """
    return integ_electric_vehicles()


@cache('run')
def km_promedio_por_año_por_vehículo():
    """
    Real Name: km promedio por año por vehículo
    Original Eqn: 24000
    Units: 
    Limits: (None, None)
    Type: constant

    https://www.autofact.cl/blog/comprar-auto/antecedentes/kilometraje-promedio
        -auto
    """
    return 24000


@cache('step')
def venta_de_vehículos_convencionales():
    """
    Real Name: venta de vehículos convencionales
    Original Eqn: demanda de vehículos*Atractividad de vehículos convencionales
    Units: 
    Limits: (None, None)
    Type: component


    """
    return demanda_de_vehículos() * atractividad_de_vehículos_convencionales()


@cache('run')
def capacidad_construcción_promedio():
    """
    Real Name: capacidad construcción promedio
    Original Eqn: 2
    Units: 
    Limits: (None, None)
    Type: constant


    """
    return 2


@cache('step')
def capacidad_construida():
    """
    Real Name: Capacidad construida
    Original Eqn: INTEG ( Capacidad a construir-Capacidad obsoleta, 17.5)
    Units: 
    Limits: (None, None)
    Type: component


    """
    return integ_capacidad_construida()


@cache('step')
def capacidad_en_construccion():
    """
    Real Name: Capacidad en construccion
    Original Eqn: INTEG ( Inicio capacidad a construir-Capacidad a construir, 10)
    Units: 
    Limits: (None, None)
    Type: component


    """
    return integ_capacidad_en_construccion()


@cache('step')
def capacidad_obsoleta():
    """
    Real Name: Capacidad obsoleta
    Original Eqn: Capacidad construida/promedio de vida
    Units: 
    Limits: (None, None)
    Type: component


    """
    return capacidad_construida() / promedio_de_vida()


@cache('step')
def capacidad_solar():
    """
    Real Name: Capacidad solar
    Original Eqn: Household PV adopters*Tamaño panel/1000
    Units: MW
    Limits: (None, None)
    Type: component


    """
    return household_pv_adopters() * tamaño_panel() / 1000


@cache('step')
def demanda():
    """
    Real Name: Demanda
    Original Eqn: INTEG ( variacion en la demanda, 66000)
    Units: 
    Limits: (None, None)
    Type: component


    """
    return integ_demanda()


@cache('step')
def efecto_precio_en_capacidad_a_construir():
    """
    Real Name: Efecto precio en capacidad a construir
    Original Eqn: WITH LOOKUP ( precio, ([(0,0)-(400,2.5)],(0,0),(170,0),(170.031,1),(250,1),(250,1.5),(350,1.5),(350,2),(400\ ,2) ))
    Units: 
    Limits: (None, None)
    Type: component


    """
    return functions.lookup(precio(), [0, 170, 170.031, 250, 250, 350, 350, 400],
                            [0, 0, 1, 1, 1.5, 1.5, 2, 2])


@cache('step')
def efecto_precio_en_incremento_demanda():
    """
    Real Name: Efecto precio en incremento demanda
    Original Eqn: WITH LOOKUP ( precio, ([(0,0.7)-(400,1.5)],(0,1.25),(29.3578,1.22281),(31.8043,1.20877),(59.9388,1.11404)\ ,(69.7248,1.05088),(80.01,1),(112.538,0.931579),(130.01,0.9),(179.817,0.892982),(211.621\ ,0.861404),(232.416,0.836842),(248.318,0.829825),(266.667,0.822807),(313.15,0.801754\ ),(400,0.8) ))
    Units: 
    Limits: (None, None)
    Type: component


    """
    return functions.lookup(precio(), [
        0, 29.3578, 31.8043, 59.9388, 69.7248, 80.01, 112.538, 130.01, 179.817, 211.621, 232.416,
        248.318, 266.667, 313.15, 400
    ], [
        1.25, 1.22281, 1.20877, 1.11404, 1.05088, 1, 0.931579, 0.9, 0.892982, 0.861404, 0.836842,
        0.829825, 0.822807, 0.801754, 0.8
    ])


@cache('run')
def incremento_promedio_de_la_demanda():
    """
    Real Name: incremento promedio de la demanda
    Original Eqn: 0.03
    Units: 
    Limits: (None, None)
    Type: constant


    """
    return 0.03


@cache('run')
def tiempo_promedio_construccion():
    """
    Real Name: Tiempo promedio construccion
    Original Eqn: 4
    Units: 
    Limits: (None, None)
    Type: constant


    """
    return 4


@cache('step')
def variacion_en_la_demanda():
    """
    Real Name: variacion en la demanda
    Original Eqn: Demanda*incremento promedio de la demanda*Efecto precio en incremento demanda
    Units: 
    Limits: (None, None)
    Type: component


    """
    return demanda() * incremento_promedio_de_la_demanda() * efecto_precio_en_incremento_demanda()


@cache('step')
def generacion_total_paneles():
    """
    Real Name: Generacion total paneles
    Original Eqn: Generación solar panel hogar*Household PV adopters/1e+06
    Units: 
    Limits: (None, None)
    Type: component


    """
    return generación_solar_panel_hogar() * household_pv_adopters() / 1e+06


@cache('run')
def promedio_de_vida():
    """
    Real Name: promedio de vida
    Original Eqn: 20
    Units: 
    Limits: (None, None)
    Type: constant


    """
    return 20


@cache('step')
def precio_de_electricidad():
    """
    Real Name: precio de electricidad
    Original Eqn: Cargo distribución+otros cargos+precio
    Units: 
    Limits: (None, None)
    Type: component


    """
    return cargo_distribución() + otros_cargos() + precio()


@cache('step')
def precio():
    """
    Real Name: precio
    Original Eqn: WITH LOOKUP ( Margen, ([(-1,0)-(2,800)],(-0.08,800),(0,500),(0.201,450),(0.4,300),(0.401,250),(0.6,200),(\ 0.601,150),(0.8,125),(0.8001,100),(1,100) ))
    Units: 
    Limits: (None, None)
    Type: component


    """
    return functions.lookup(margen(), [-0.08, 0, 0.201, 0.4, 0.401, 0.6, 0.601, 0.8, 0.8001, 1],
                            [800, 500, 450, 300, 250, 200, 150, 125, 100, 100])


@cache('run')
def consumo_por_hogar():
    """
    Real Name: Consumo por hogar
    Original Eqn: 200*12
    Units: 
    Limits: (None, None)
    Type: constant


    """
    return 200 * 12


@cache('step')
def demanda_residencial_hogares_no_potenciales_ni_adaptadores():
    """
    Real Name: Demanda residencial hogares no potenciales ni adaptadores
    Original Eqn: (Hogares-Household PV adopters-Hogares potenciales)*Consumo por hogar
    Units: 
    Limits: (None, None)
    Type: component


    """
    return (hogares() - household_pv_adopters() - hogares_potenciales()) * consumo_por_hogar()


@cache('step')
def demanda_residencial_adaptadores():
    """
    Real Name: Demanda residencial adaptadores
    Original Eqn: (Consumo por hogar-Generación solar panel hogar)*Household PV adopters
    Units: 
    Limits: (None, None)
    Type: component


    """
    return (consumo_por_hogar() - generación_solar_panel_hogar()) * household_pv_adopters()


@cache('run')
def otros_cargos():
    """
    Real Name: otros cargos
    Original Eqn: 200
    Units: 
    Limits: (None, None)
    Type: constant


    """
    return 200


@cache('run')
def fraccion_de_adopcion():
    """
    Real Name: Fraccion de adopcion
    Original Eqn: 1
    Units: 
    Limits: (None, None)
    Type: constant


    """
    return 1


@cache('step')
def hogares_dispuestos_a_adoptar():
    """
    Real Name: Hogares dispuestos a adoptar
    Original Eqn: (Hogares-Hogares potenciales-Household PV adopters)*(Efecto de paridad de red en hogares dispuestos a adoptar\ )
    Units: 
    Limits: (None, None)
    Type: component


    """
    return (hogares() - hogares_potenciales() -
            household_pv_adopters()) * (efecto_de_paridad_de_red_en_hogares_dispuestos_a_adoptar())


@cache('run')
def costo_fijo():
    """
    Real Name: Costo fijo
    Original Eqn: (2.09632e+11)*12
    Units: 
    Limits: (None, None)
    Type: constant


    """
    return (2.09632e+11) * 12


@cache('step')
def crecimiento_neto():
    """
    Real Name: crecimiento neto
    Original Eqn: Población*tasa crecimiento
    Units: 
    Limits: (None, None)
    Type: component


    """
    return población() * tasa_crecimiento()


@cache('step')
def demanda_residencial_hogares_potenciales():
    """
    Real Name: Demanda residencial hogares potenciales
    Original Eqn: Consumo por hogar*Hogares potenciales
    Units: 
    Limits: (None, None)
    Type: component


    """
    return consumo_por_hogar() * hogares_potenciales()


@cache('run')
def días_en_mes():
    """
    Real Name: Días en mes
    Original Eqn: 360
    Units: 
    Limits: (None, None)
    Type: constant


    """
    return 360


@cache('step')
def efecto_de_paridad_de_red_en_hogares_dispuestos_a_adoptar():
    """
    Real Name: Efecto de paridad de red en hogares dispuestos a adoptar
    Original Eqn: WITH LOOKUP ( cociente paridad de red, ([(0,0)-(10,10)],(0,1),(0.5,0.7),(0.7,0.6),(0.8,0.5),(1,0.25) ))
    Units: 
    Limits: (None, None)
    Type: component


    """
    return functions.lookup(cociente_paridad_de_red(), [0, 0.5, 0.7, 0.8, 1],
                            [1, 0.7, 0.6, 0.5, 0.25])


@cache('step')
def generación_solar_panel_hogar():
    """
    Real Name: Generación solar panel hogar
    Original Eqn: Días en mes*Horas sol*Tamaño panel
    Units: 
    Limits: (None, None)
    Type: component


    """
    return días_en_mes() * horas_sol() * tamaño_panel()


@cache('step')
def hogares():
    """
    Real Name: Hogares
    Original Eqn: Población/personas por hogar
    Units: 
    Limits: (None, None)
    Type: component


    """
    return población() / personas_por_hogar()


@cache('step')
def household_pv_adopters():
    """
    Real Name: Household PV adopters
    Original Eqn: INTEG ( tasa adopción, 100)
    Units: Number of Households
    Limits: (None, None)
    Type: component


    """
    return integ_household_pv_adopters()


@cache('step')
def población():
    """
    Real Name: Población
    Original Eqn: INTEG ( crecimiento neto, 4.95e+07)
    Units: 
    Limits: (None, None)
    Type: component


    """
    return integ_población()


@cache('step')
def hogares_potenciales():
    """
    Real Name: Hogares potenciales
    Original Eqn: INTEG ( tasa crecimiento hogares potenciales-tasa adopción, 3)
    Units: 
    Limits: (None, None)
    Type: component


    """
    return integ_hogares_potenciales()


@cache('run')
def horas_sol():
    """
    Real Name: Horas sol
    Original Eqn: 4.8
    Units: 
    Limits: (None, None)
    Type: constant

    Dato tomado de Data de IDEAM 
        http://atlas.ideam.gov.co/basefiles/6.Anexo_Promedios-mensuales-de-brillo-s
        olar.pdf
    """
    return 4.8


@cache('run')
def personas_por_hogar():
    """
    Real Name: personas por hogar
    Original Eqn: 3.1
    Units: 
    Limits: (None, None)
    Type: constant

    Información tomada de: 
        https://www.dane.gov.co/index.php/estadisticas-por-tema/demografia-y-poblac
        ion/censo-nacional-de-poblacion-y-vivenda-2018/como-vivimos
    """
    return 3.1


@cache('run')
def tasa_de_contacto():
    """
    Real Name: Tasa de contacto
    Original Eqn: 0.025
    Units: 
    Limits: (None, None)
    Type: constant


    """
    return 0.025


@cache('step')
def tasa_crecimiento_hogares_potenciales():
    """
    Real Name: tasa crecimiento hogares potenciales
    Original Eqn: Hogares dispuestos a adoptar
    Units: 
    Limits: (None, None)
    Type: component


    """
    return hogares_dispuestos_a_adoptar()


@cache('run')
def tasa_crecimiento():
    """
    Real Name: tasa crecimiento
    Original Eqn: 0.0117/12
    Units: 
    Limits: (None, None)
    Type: constant


    """
    return 0.0117 / 12


@cache('step')
def cargo_distribución():
    """
    Real Name: Cargo distribución
    Original Eqn: Costo fijo/Demanda residencial total
    Units: 
    Limits: (None, None)
    Type: component


    """
    return costo_fijo() / demanda_residencial_total()


@cache('run')
def final_time():
    """
    Real Name: FINAL TIME
    Original Eqn: 2050
    Units: Year
    Limits: (None, None)
    Type: constant

    The final time for the simulation.
    """
    return 2050


@cache('run')
def initial_time():
    """
    Real Name: INITIAL TIME
    Original Eqn: 2024
    Units: Year
    Limits: (None, None)
    Type: constant

    The initial time for the simulation.
    """
    return 2024


@cache('step')
def saveper():
    """
    Real Name: SAVEPER
    Original Eqn: TIME STEP
    Units: Year
    Limits: (0.0, None)
    Type: component

    The frequency with which output is stored.
    """
    return time_step()


@cache('run')
def time_step():
    """
    Real Name: TIME STEP
    Original Eqn: 0.125
    Units: Year
    Limits: (0.0, None)
    Type: constant

    The time step for the simulation.
    """
    return 0.125


delay_inicio_capacidad_a_construir_tiempo_promedio_construccion_inicio_capacidad_a_construir_3 = functions.Delay(
    lambda: inicio_capacidad_a_construir(), lambda: tiempo_promedio_construccion(),
    lambda: inicio_capacidad_a_construir(), lambda: 3)

integ_estaciones_de_carga = functions.Integ(lambda: crecimiento_estaciones_de_carga(), lambda: 202)

integ_vehículos_convencionales_en_uso = functions.Integ(
    lambda: venta_de_vehículos_convencionales() - desecho_vehículos_convencionales(),
    lambda: 6.19e+06)

integ_electric_vehicles = functions.Integ(
    lambda: venta_de_vehículos_eléctricos() - desecho_de_vehículos_eléctricos(), lambda: 7537)

integ_capacidad_construida = functions.Integ(
    lambda: capacidad_a_construir() - capacidad_obsoleta(), lambda: 17.5)

integ_capacidad_en_construccion = functions.Integ(
    lambda: inicio_capacidad_a_construir() - capacidad_a_construir(), lambda: 10)

integ_demanda = functions.Integ(lambda: variacion_en_la_demanda(), lambda: 66000)

integ_household_pv_adopters = functions.Integ(lambda: tasa_adopción(), lambda: 100)

integ_población = functions.Integ(lambda: crecimiento_neto(), lambda: 4.95e+07)

integ_hogares_potenciales = functions.Integ(
    lambda: tasa_crecimiento_hogares_potenciales() - tasa_adopción(), lambda: 3)
