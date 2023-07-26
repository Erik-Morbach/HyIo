import smbus

import device


class I2CDevice(device.Device):
    def __init__(self, address) -> None:
        super().__init__()
        DEVICE_BUS = 1
        self.write_cmd = 0x02
        self.read_cmd = 0x01
        self.bus = smbus.SMBus(DEVICE_BUS)
        self.address = address
        self.data = {}
        self.pins = {}

    def setup(self, id, mode):
        self.pins[id] = mode

    def _read_pin(self, id):
        return self.bus.read_byte_data(self.address, id)

    def _write_pin(self, id, value):
        self.bus.write_byte_data(self.address, id, value)

    def update(self, id):
        if self.pins[id] == "output":
            self.data[id] = self._read_pin(id)
        else:
            self._write_pin(id, self.data[id])

    def set(self, id, value):
        self.data[id] = value

    def get(self, id):
        return self.data[id]


