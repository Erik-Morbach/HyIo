import time
import threading
import queue
import functools
import traceback


class IoManager:
    def __init__(self, period) -> None:
        self.period = period
        self.pins = []
        self.callbacks = []
        self.queue = queue.Queue()
        self.active = True
        self.updateThreadObj = None
        self.callbackThreadObj = None
        self.threadActive = False
        self.lastError = ""

    def registerPin(self, pin, callback):
        self.pins += [pin]
        self.callbacks += [callback]

    def updatePins(self):
        currentTime = time.perf_counter_ns()
        for i in range(len(self.pins)):
            if self.pins[i].update(currentTime):
                func = functools.partial(self.callbacks[i], self.pins[i].get())
                self.queue.put(func, block=True)

    def _updateThreadFunction(self):
        while self.threadActive:
            self.updatePins()
            time.sleep(self.period)

    def _callbackThreadFunction(self):
        while self.threadActive:
            if self.queue.empty():
                time.sleep(self.period)
                continue
            current = self.queue.get(block=True)
            try:
                current()
            except BaseException:
                self.lastError = traceback.format_exc()

    def startThread(self):
        if self.threadActive:
            return
        self.threadActive = True
        self.callbackThreadObj = threading.Thread(target=self._callbackThreadFunction)
        self.updateThreadObj = threading.Thread(target=self._updateThreadFunction)

        self.callbackThreadObj.start()
        self.updateThreadObj.start()

    def stopThread(self):
        if not self.threadActive:
            return
        self.threadActive = False

        if self.updateThreadObj is not None:
            self.updateThreadObj.join()

        if self.callbackThreadObj is not None:
            self.callbackThreadObj.join()

        self.updateThreadObj = self.callbackThreadObj = None
