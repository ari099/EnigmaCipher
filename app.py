import os, sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

class Ui(QtWidgets.QMainWindow):
   def __init__(self):
      super(Ui, self).__init__()
      uic.loadUi('enigma_cipher.ui', self)

      # Rotor Sliders
      self.rotorOne = self.findChild(QtWidgets.QSlider, 'RotorI')
      self.rotorOne.valueChanged.connect(self.rotorOneSlide)
      self.rotorTwo = self.findChild(QtWidgets.QSlider, 'RotorII')
      self.rotorTwo.valueChanged.connect(self.rotorTwoSlide)
      self.rotorThree = self.findChild(QtWidgets.QSlider, 'RotorIII')
      self.rotorThree.valueChanged.connect(self.rotorThreeSlide)

      # Rotor Labels
      self.rotorOneValue = self.findChild(QtWidgets.QLabel, 'RotorIShiftValue')
      self.rotorTwoValue = self.findChild(QtWidgets.QLabel, 'RotorIIShiftValue')
      self.rotorThreeValue = self.findChild(QtWidgets.QLabel, 'RotorIIIShiftValue')

      # Show the app dialog
      self.show()
   
   # ###################################### UI EVENT HANDLERS ######################################
   def rotorOneSlide(self):
      self.rotorOneValue.setText(str(self.rotorOne.value()))

   def rotorTwoSlide(self):
      self.rotorTwoValue.setText(str(self.rotorTwo.value()))

   def rotorThreeSlide(self):
      self.rotorThreeValue.setText(str(self.rotorThree.value()))



app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
