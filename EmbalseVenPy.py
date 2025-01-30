"""
Python model "EmbalseVenPy.py"
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
    'Agua para consumo': 'agua_para_consumo',
    'Tasa de consumo': 'tasa_de_consumo',
    'Agua que se evapora': 'agua_que_se_evapora',
    'Embalse de agua': 'embalse_de_agua',
    'Irrigación de agua': 'irrigación_de_agua',
    'Tasa de evaporación': 'tasa_de_evaporación',
    'FINAL TIME': 'final_time',
    'INITIAL TIME': 'initial_time',
    'SAVEPER': 'saveper',
    'TIME STEP': 'time_step'
}

__pysd_version__ = "0.9.0"


@cache('step')
def agua_para_consumo():
    """
    Real Name: Agua para consumo
    Original Eqn: MIN( 160 , (Embalse de agua*Tasa de consumo) +Irrigación de agua)
    Units: mm3/Day
    Limits: (None, None)
    Type: component

    MIN( 160 , (Embalse de agua+Irrigación de agua) )
    """
    return np.minimum(160, (embalse_de_agua() * tasa_de_consumo()) + irrigación_de_agua())


@cache('run')
def tasa_de_consumo():
    """
    Real Name: Tasa de consumo
    Original Eqn: 0.5
    Units: 1/Day
    Limits: (None, None)
    Type: constant

    0.5
    """
    return 0.5


@cache('step')
def agua_que_se_evapora():
    """
    Real Name: Agua que se evapora
    Original Eqn: Embalse de agua*Tasa de evaporación
    Units: mm3/Day
    Limits: (None, None)
    Type: component


    """
    return embalse_de_agua() * tasa_de_evaporación()


@cache('step')
def embalse_de_agua():
    """
    Real Name: Embalse de agua
    Original Eqn: INTEG ( Irrigación de agua-Agua para consumo-Agua que se evapora, 1240)
    Units: mm3
    Limits: (None, None)
    Type: component


    """
    return integ_embalse_de_agua()


@cache('run')
def irrigación_de_agua():
    """
    Real Name: Irrigación de agua
    Original Eqn: 100
    Units: mm3/Day
    Limits: (None, None)
    Type: constant


    """
    return 100


@cache('run')
def tasa_de_evaporación():
    """
    Real Name: Tasa de evaporación
    Original Eqn: 0.02
    Units: 1/Day
    Limits: (None, None)
    Type: constant


    """
    return 0.02


@cache('run')
def final_time():
    """
    Real Name: FINAL TIME
    Original Eqn: 50
    Units: Day
    Limits: (None, None)
    Type: constant

    The final time for the simulation.
    """
    return 50


@cache('run')
def initial_time():
    """
    Real Name: INITIAL TIME
    Original Eqn: 0
    Units: Day
    Limits: (None, None)
    Type: constant

    The initial time for the simulation.
    """
    return 0


@cache('step')
def saveper():
    """
    Real Name: SAVEPER
    Original Eqn: TIME STEP
    Units: Day
    Limits: (0.0, None)
    Type: component

    The frequency with which output is stored.
    """
    return time_step()


@cache('run')
def time_step():
    """
    Real Name: TIME STEP
    Original Eqn: 0.0078125
    Units: Day
    Limits: (0.0, None)
    Type: constant

    The time step for the simulation.
    """
    return 0.0078125


integ_embalse_de_agua = functions.Integ(
    lambda: irrigación_de_agua() - agua_para_consumo() - agua_que_se_evapora(), lambda: 1240)
