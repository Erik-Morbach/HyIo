from debounce import Debouncer
from device import Device
from pin import Pin

debounceMapper = {}
deviceMapper = {}


def createPin(id, debouncerId, deviceId):
    return Pin(id, debounceMapper[debouncerId], deviceMapper[deviceId])


def createDebouncer(id, updatePeriod, addPeriod, blockSize):
    debounceMapper[id] = Debouncer(updatePeriod, addPeriod, blockSize)


def createDevice(id):
    deviceMapper[id] = Device()


def createI2CDevice(id, address):
    pass


def createGPIODevice(id):
    pass


def parseYml(ymlObj):
    pass
