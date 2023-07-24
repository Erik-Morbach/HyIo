import time
import threading

class IoManager:
    def __init__(self, period) -> None:
        self.period = period
        self.pins = []
        self.active = True

    def registerPin(self, pin):
        self.pins += [pin]

    def updatePins(self):
        currentTime = time.perf_counter_ns()
        for pin in self.pins:
            pin.update(currentTime)

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

    def startSubProcess(self):
        pass

    def stopSubProcess(self):
        pass


