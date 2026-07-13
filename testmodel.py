from flet_core import page

from model.model import Model
from UI.controller import Controller
from UI.view import View
model=Model()
model.buildGraphPesato(2015)
print("Num nodi:", model.getNumNodi())
print("Num archi:", model.getNumArchi())
print(len(model.getAllNodes()))