import time
import threading

class IoManager:
    def __init__(self, period) -> None:
        self.period = period
        self.pins = []
        self.callbacks = []
        self.active = True
        self.threadObj = None
        self.threadActive = False

    def registerPin(self, pin, callback):
        self.pins += [pin]
        self.callbacks += [callback]

    def updatePins(self):
        currentTime = time.perf_counter_ns()
        for i in range(len(self.pins)):
            if self.pins[i].update(currentTime):
                self.callbacks[i](self.pins[i].get())

    def _threadFunction(self):
        while self.threadActive:
            self.updatePins()
            time.sleep(self.period)

    def startThread(self):
        if self.threadObj is not None:
            return
        self.threadActive = True
        self.threadObj = threading.Thread(target=self._threadFunction)
        self.threadObj.start()

    def stopThread(self):
        if self.threadObj is None:
            return
        self.threadActive = False
        self.threadObj.join()
        self.threadObj = None


