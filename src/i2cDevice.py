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

    def _read_pin(self, id):
        return self.bus.read_byte_data(self.address, id)

    def _write_pin(self, id, value):
        self.bus.write_byte_data(self.address, id, value)

    def update(self, id):
        if self.pins[id] == device.INPUT:
            self.data[id] = self._read_pin(id)
        else:
            self._write_pin(id, self.data[id])
