from debounce import Debouncer
from device import Device
from pin import Pin


# maybe this doesn't make sense. Since we should use callbacks,
# how do we specify a callback function inside a json. It could be the name of
# a external script, but we lose some context
# user can define a local/global vars, then set her to execute external scripts
"""
{
    "i2c-0": {
        "address": 0x20
    },
    "pin":{
        "id":0,
        "debouncer": {
            "updatePeriod": 0,
            "addPeriod": 0,
            "blockSize": 0
        },
        "device": "i2c-0",
        "device": "gpio",
        "device": "sim",
        "mode": "input"
    }
}
"""
