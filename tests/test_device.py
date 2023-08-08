import HyIo.device


def test_device():
    dev = HyIo.device.Device()

    dev.setup(1, HyIo.device.INPUT)
    dev.setup(2, HyIo.device.OUTPUT)
    dev.setup(3, HyIo.device.INPUT)
    dev.setup(4, HyIo.device.OUTPUT)

    for inp in [1, 3]:
        assert dev.get(inp) == 0
        dev.set(inp, 1)
        assert dev.get(inp) == 0
    for out in [2, 4]:
        assert dev.get(out) == 0
        dev.set(out, 1)
        assert dev.get(out) == 1
