class Device:
    def __init__(self) -> None:
        pass

    def update(self, id):
        pass

    def set(self, id, value):
        pass

    def get(self, id):
        pass


class I2CDevice(Device):
    def __init__(self) -> None:
        super().__init__()

    def update(self, id):
        return super().update(id)

    def set(self, id, value):
        return super().set(id, value)

    def get(self, id):
        return super().get(id)


class GPIODevice(Device):
    def __init__(self) -> None:
        super().__init__()
    def update(self, id):
        return super().update(id)
    def set(self, id, value):
        return super().set(id, value)
    def get(self, id):
        return super().get(id)
