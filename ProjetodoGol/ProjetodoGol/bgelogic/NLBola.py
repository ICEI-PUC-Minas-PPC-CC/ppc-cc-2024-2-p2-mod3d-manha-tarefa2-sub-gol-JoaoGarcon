# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    CON0000 = nodes.ConditionKeyPressed()
    ACT0001 = nodes.ActionApplyImpulse()
    CON0002 = nodes.ConditionKeyPressed()
    CON0003 = nodes.ConditionKeyPressed()
    ACT0004 = nodes.ActionApplyLocation()
    CON0005 = nodes.ConditionKeyPressed()
    CON0006 = nodes.ConditionKeyPressed()
    ACT0007 = nodes.ActionApplyLocation()
    ACT0008 = nodes.ActionApplyLocation()
    ACT0009 = nodes.ActionApplyLocation()
    PAR0010 = nodes.ParameterObjectAttribute()
    PAR0011 = nodes.ParameterObjectAttribute()
    CON0012 = nodes.ConditionCompareVecs()
    CON0013 = nodes.ConditionKeyPressed()
    ACT0014 = nodes.ActionRestartGame()
    CON0015 = nodes.ConditionAnd()
    CON0000.key_code = bge.events.SPACEKEY
    CON0000.pulse = True
    ACT0001.local = False
    ACT0001.condition = CON0000
    ACT0001.game_object = "NLO:Bola"
    ACT0001.point = mathutils.Vector((0.0, -0.6000000238418579, 10.0))
    ACT0001.impulse = mathutils.Vector((0.0, -2.0, 0.4000000059604645))
    CON0002.key_code = bge.events.DKEY
    CON0002.pulse = True
    CON0003.key_code = bge.events.WKEY
    CON0003.pulse = True
    ACT0004.local = True
    ACT0004.condition = CON0005
    ACT0004.game_object = "NLO:Bola"
    ACT0004.movement = mathutils.Vector((0.0, 0.5, 0.0))
    CON0005.key_code = bge.events.SKEY
    CON0005.pulse = True
    CON0006.key_code = bge.events.AKEY
    CON0006.pulse = True
    ACT0007.local = True
    ACT0007.condition = CON0003
    ACT0007.game_object = "NLO:Bola"
    ACT0007.movement = mathutils.Vector((0.0, -0.699999988079071, 0.0))
    ACT0008.local = True
    ACT0008.condition = CON0006
    ACT0008.game_object = "NLO:Bola"
    ACT0008.movement = mathutils.Vector((0.5, 0.0, 0.0))
    ACT0009.local = True
    ACT0009.condition = CON0002
    ACT0009.game_object = "NLO:Bola"
    ACT0009.movement = mathutils.Vector((-0.5, 0.0, 0.0))
    PAR0010.game_object = "NLO:Bola"
    PAR0010.attribute_name = "worldPosition"
    PAR0011.game_object = "NLO:Linha Gol"
    PAR0011.attribute_name = "worldPosition"
    CON0012.all = {'x': False, 'y': True, 'z': False}
    CON0012.threshold = 1.0
    CON0012.param_a = PAR0010
    CON0012.param_b = PAR0011
    CON0012.operator = 3
    CON0013.key_code = bge.events.RKEY
    CON0013.pulse = True
    ACT0014.condition = CON0015
    CON0015.condition_a = CON0012
    CON0015.condition_b = CON0013
    network.add_cell(CON0000)
    network.add_cell(CON0002)
    network.add_cell(CON0005)
    network.add_cell(ACT0009)
    network.add_cell(PAR0011)
    network.add_cell(CON0013)
    network.add_cell(ACT0001)
    network.add_cell(ACT0004)
    network.add_cell(PAR0010)
    network.add_cell(CON0003)
    network.add_cell(ACT0007)
    network.add_cell(CON0012)
    network.add_cell(CON0015)
    network.add_cell(CON0006)
    network.add_cell(ACT0014)
    network.add_cell(ACT0008)
    owner["IGNLTree_Bola"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__Bola')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_Bola")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
