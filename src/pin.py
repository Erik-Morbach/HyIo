class Pin:
    def __init__(self, id, debouncer, device) -> None:
        self.id = id
        self.debouncer = debouncer
        self.device = device

    def _updatePinOnDeviceFunction(self, value):
        self.device.update(self.id)

    def _setPinOnDeviceFunction(self, value):
        self.device.set(self.id, value)

    def _getFromDeviceFunction(self):
        return self.device.get(self.id)

    def update(self, currentTime):
        pass

    def get(self):
        return self.debouncer.get()

    def set(self, value):
        pass

def InputPin(Pin):
    def update(self, currentTime):
        self.debouncer.updateValueIfNeed(currentTime, self._updatePinOnDeviceFunction)
        self.debouncer.addToBufferIfNeed(currentTime, self._getFromDeviceFunction)

def OutputPin(Pin):
    def update(self, currentTime):
        self.debouncer.addToBufferIfNeed(currentTime, self._lastOutValue)
        self.debouncer.updateValueIfNeed(currentTime, self._setPinOnDeviceFunction)

    def set(self, value):
        self._lastOutValue = value


#class Pin:
#    def __init__(self, id, key, period, halDevice) -> None:
#        self.id = id
#        self.key = key
#        self.hal = halDevice
#        self.mtx = threading.Lock()
#        self.period = (int)(period*10**9)
#        self.lastUpdate = 0

#    def _readPin(self):
#        value = self.hal.read(self.key)

#    def update(self, currentTime):
#        if currentTime - self.lastUpdate < self.period:
#            return
#        self.lastUpdate = currentTime
#        self._readPin()

#    def get(self):
#        return 1 if self.currentSum>=self.blockSize else 0

#    def set(self, value):
#        self.hal.write(self.key, value)

