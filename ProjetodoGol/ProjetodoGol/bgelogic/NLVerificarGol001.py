# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    owner["IGNLTree_Verificar Gol.001"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__Verificar Gol.001')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_Verificar Gol.001")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
