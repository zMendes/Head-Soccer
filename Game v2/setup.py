import cx_Freeze
import pygame as pg
import random
from random import randrange
from os import path
import time
import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

executables = [cx_Freeze.Executable("Mecanicas.py")]
cx_Freeze.setup(
         name= "Head Soccer",
         option = {"build_exe": {"packages":["pygame"], 
                                 "include_files": ["background.png", "menu.jpg", "Placar.png", "goa1.png", "goal2.png", "back1.wav", "Football_punts.wav", "referee.wav", "head1.png", "head2.png"]}},
         executables = executables,
         version="1.0.0"
         )
