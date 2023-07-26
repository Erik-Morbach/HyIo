import device

class Pin:
    def __init__(self, id, debouncer, device) -> None:
        self.id = id
        self.debouncer = debouncer
        self.device = device

    def setup(self, mode=device.NONE):
        self.device.setup(self.id, mode)

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

class InputPin(Pin):
    def __init__(self, id, debouncer, device) -> None:
        super().__init__(id, debouncer, device)

    def setup(self):
        return super().setup(device.INPUT)

    def update(self, currentTime):
        self.debouncer.updateValueIfNeed(currentTime, self._updatePinOnDeviceFunction)
        self.debouncer.addToBufferIfNeed(currentTime, self._getFromDeviceFunction)

class OutputPin(Pin):
    def __init__(self, id, debouncer, device) -> None:
        super().__init__(id, debouncer, device)
        self._lastOutValue = 0

    def update(self, currentTime):
        self.debouncer.addToBufferIfNeed(currentTime, self._lastOutValue)
        self.debouncer.updateValueIfNeed(currentTime, self._setPinOnDeviceFunction)

    def set(self, value):
        self._lastOutValue = value

