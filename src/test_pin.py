import pin
import device
import debounce

def test_pin():
    dev = device.Device()
    
    inp = pin.InputPin(1, debounce.Debouncer(0,0,1), dev)
    inp.setup()

    out = pin.OutputPin(2, debounce.Debouncer(0,0,1), dev)
    out.setup()

    #TODO: complete test

