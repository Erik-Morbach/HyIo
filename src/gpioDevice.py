import device

import wiringpi as wp

class GPIODevice(device.Device):
    def __init__(self) -> None:
        super().__init__()
        wp.wiringPiSetupGpio()

    def update(self, id):
        return super().update(id)

    def setup(self, id, mode):
        if mode == "output": wp.pinMode(id, 1)
        else: wp.pinMode(id, 0)

    def set(self, id, value):
        wp.digitalWrite(id, value)

    def get(self, id):
        return wp.digitalRead(id)

