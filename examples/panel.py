import time
from debounce import Debouncer
import i2cDevice
from ioManager import IoManager
from pin import InputPin

dev = i2cDevice.I2CDevice(0x10)

selectors = InputPin(0x0, Debouncer(16, 16, 2), dev)
buttons = InputPin(0x1, Debouncer(16, 16, 2), dev)

manager = IoManager(16)


def onChangeSelectors(value):
    print("Selector0 = ", value&0xF)
    print("Selector1 = ", value&0xF0)


def onChangeButtons(value):
    print("Buttons = ", value&0xF0)

manager.registerPin(buttons, onChangeButtons)
manager.registerPin(selectors, onChangeSelectors)

manager.startThread()

time.sleep(10)

manager.stopThread()

