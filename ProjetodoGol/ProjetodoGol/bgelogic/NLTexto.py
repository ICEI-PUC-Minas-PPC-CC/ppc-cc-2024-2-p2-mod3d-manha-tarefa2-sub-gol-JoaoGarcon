# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    CON0000 = nodes.ConditionCompareVecs()
    PAR0001 = nodes.ParameterObjectAttribute()
    CON0002 = nodes.ConditionCompareVecs()
    PAR0003 = nodes.ParameterObjectAttribute()
    CON0004 = nodes.ConditionCompareVecs()
    PAR0005 = nodes.ParameterObjectAttribute()
    CON0006 = nodes.ConditionAnd()
    CON0007 = nodes.ConditionAnd()
    ACT0008 = nodes.ActionMoveTo()
    CON0009 = nodes.ConditionAnd()
    CON0010 = nodes.ConditionKeyPressed()
    ACT0011 = nodes.ActionRestartGame()
    ACT0012 = nodes.ActionMoveTo()
    PAR0013 = nodes.ParameterObjectAttribute()
    PAR0014 = nodes.ParameterObjectAttribute()
    CON0015 = nodes.ConditionCompareVecs()
    CON0016 = nodes.ConditionOr()
    CON0017 = nodes.ConditionCompareVecs()
    CON0018 = nodes.ConditionAnd()
    CON0019 = nodes.ConditionAnd()
    PAR0020 = nodes.ParameterObjectAttribute()
    PAR0021 = nodes.ParameterObjectAttribute()
    PAR0022 = nodes.ParameterObjectAttribute()
    PAR0023 = nodes.ParameterObjectAttribute()
    CON0024 = nodes.ConditionCompareVecs()
    CON0025 = nodes.ConditionCompareVecs()
    CON0026 = nodes.ConditionCompareVecs()
    CON0027 = nodes.ConditionCompareVecs()
    PAR0028 = nodes.ParameterObjectAttribute()
    CON0029 = nodes.ConditionAnd()
    ACT0030 = nodes.ActionMoveTo()
    CON0031 = nodes.ConditionKeyPressed()
    CON0032 = nodes.ConditionAnd()
    ACT0033 = nodes.ActionRestartGame()
    CON0000.all = {'x': False, 'y': True, 'z': False}
    CON0000.threshold = 1.0
    CON0000.param_a = PAR0001
    CON0000.param_b = mathutils.Vector((0.0, -63.5, 0.0))
    CON0000.operator = 3
    PAR0001.game_object = "NLO:Bola"
    PAR0001.attribute_name = "worldPosition"
    CON0002.all = {'x': True, 'y': False, 'z': False}
    CON0002.threshold = 0.0
    CON0002.param_a = PAR0003
    CON0002.param_b = mathutils.Vector((-17.600000381469727, 0.0, 0.0))
    CON0002.operator = 2
    PAR0003.game_object = "NLO:Bola"
    PAR0003.attribute_name = "worldPosition"
    CON0004.all = {'x': True, 'y': False, 'z': False}
    CON0004.threshold = 0.0
    CON0004.param_a = PAR0005
    CON0004.param_b = mathutils.Vector((22.0, 0.0, 0.0))
    CON0004.operator = 3
    PAR0005.game_object = "NLO:Bola"
    PAR0005.attribute_name = "worldPosition"
    CON0006.condition_a = CON0002
    CON0006.condition_b = CON0004
    CON0007.condition_a = CON0000
    CON0007.condition_b = CON0006
    ACT0008.condition = CON0007
    ACT0008.moving_object = "NLO:Texto GOL"
    ACT0008.destination_point = mathutils.Vector((36.0, -12.0, 38.0))
    ACT0008.dynamic = False
    ACT0008.speed = 500.0
    ACT0008.distance = 0.5
    CON0009.condition_a = ACT0008
    CON0009.condition_b = CON0010
    CON0010.key_code = bge.events.RKEY
    CON0010.pulse = True
    ACT0011.condition = CON0009
    ACT0012.condition = CON0015
    ACT0012.moving_object = "NLO:Texto Reiniciar"
    ACT0012.destination_point = mathutils.Vector((27.0, 94.0, 30.0))
    ACT0012.dynamic = False
    ACT0012.speed = 400.0
    ACT0012.distance = 0.5
    PAR0013.game_object = "NLO:Linha Gol"
    PAR0013.attribute_name = "worldPosition"
    PAR0014.game_object = "NLO:Bola"
    PAR0014.attribute_name = "worldPosition"
    CON0015.all = {'x': False, 'y': True, 'z': False}
    CON0015.threshold = 1.0
    CON0015.param_a = PAR0014
    CON0015.param_b = PAR0013
    CON0015.operator = 3
    CON0016.condition_a = CON0019
    CON0016.condition_b = CON0018
    CON0017.all = {'x': False, 'y': True, 'z': False}
    CON0017.threshold = 1.0
    CON0017.param_a = PAR0028
    CON0017.param_b = mathutils.Vector((0.0, -63.53799819946289, 0.0))
    CON0017.operator = 3
    CON0018.condition_a = CON0025
    CON0018.condition_b = CON0024
    CON0019.condition_a = CON0027
    CON0019.condition_b = CON0026
    PAR0020.game_object = "NLO:Bola"
    PAR0020.attribute_name = "worldPosition"
    PAR0021.game_object = "NLO:Bola"
    PAR0021.attribute_name = "worldPosition"
    PAR0022.game_object = "NLO:Bola"
    PAR0022.attribute_name = "worldPosition"
    PAR0023.game_object = "NLO:Bola"
    PAR0023.attribute_name = "worldPosition"
    CON0024.all = {'x': True, 'y': False, 'z': False}
    CON0024.threshold = 0.0
    CON0024.param_a = PAR0023
    CON0024.param_b = mathutils.Vector((-50.5, 0.0, 0.0))
    CON0024.operator = 2
    CON0025.all = {'x': True, 'y': False, 'z': False}
    CON0025.threshold = 0.0
    CON0025.param_a = PAR0022
    CON0025.param_b = mathutils.Vector((-17.600000381469727, 0.0, 0.0))
    CON0025.operator = 3
    CON0026.all = {'x': True, 'y': False, 'z': False}
    CON0026.threshold = 0.0
    CON0026.param_a = PAR0021
    CON0026.param_b = mathutils.Vector((22.0, 0.0, 0.0))
    CON0026.operator = 2
    CON0027.all = {'x': True, 'y': False, 'z': False}
    CON0027.threshold = 0.0
    CON0027.param_a = PAR0020
    CON0027.param_b = mathutils.Vector((50.0, 0.0, 0.0))
    CON0027.operator = 3
    PAR0028.game_object = "NLO:Bola"
    PAR0028.attribute_name = "worldPosition"
    CON0029.condition_a = CON0017
    CON0029.condition_b = CON0016
    ACT0030.condition = CON0029
    ACT0030.moving_object = "NLO:Texto Errou"
    ACT0030.destination_point = mathutils.Vector((36.0, -12.0, 38.0))
    ACT0030.dynamic = False
    ACT0030.speed = 500.0
    ACT0030.distance = 0.5
    CON0031.key_code = bge.events.RKEY
    CON0031.pulse = True
    CON0032.condition_a = ACT0030
    CON0032.condition_b = CON0031
    ACT0033.condition = CON0032
    network.add_cell(PAR0001)
    network.add_cell(PAR0003)
    network.add_cell(PAR0005)
    network.add_cell(CON0010)
    network.add_cell(PAR0013)
    network.add_cell(PAR0020)
    network.add_cell(PAR0022)
    network.add_cell(CON0025)
    network.add_cell(CON0027)
    network.add_cell(CON0031)
    network.add_cell(CON0000)
    network.add_cell(CON0004)
    network.add_cell(PAR0014)
    network.add_cell(PAR0021)
    network.add_cell(CON0026)
    network.add_cell(CON0002)
    network.add_cell(CON0015)
    network.add_cell(CON0019)
    network.add_cell(PAR0028)
    network.add_cell(CON0006)
    network.add_cell(ACT0012)
    network.add_cell(CON0017)
    network.add_cell(PAR0023)
    network.add_cell(CON0007)
    network.add_cell(CON0024)
    network.add_cell(ACT0008)
    network.add_cell(CON0018)
    network.add_cell(CON0009)
    network.add_cell(CON0016)
    network.add_cell(ACT0011)
    network.add_cell(CON0029)
    network.add_cell(ACT0030)
    network.add_cell(CON0032)
    network.add_cell(ACT0033)
    owner["IGNLTree_Texto"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__Texto')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_Texto")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
