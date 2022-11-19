"""
Thread class for processing data. We process data in the separate thread
to avoid new incoming data loss if processing takes very long time.
"""

from threading import Thread, Event
from module.module import module_main
from logging import getLogger

# set up logging
log = getLogger("processing_thread")

class ProcessingThread(Thread):
    def __init__(self, data_queue):
        super(ProcessingThread, self).__init__()
        self.data_queue = data_queue
        self.msg_received = Event()

    def run(self):
        while self.msg_received.wait(timeout=None):
            while not self.data_queue.empty():
                # pass data to the module logic
                send_error = module_main(self.data_queue.get())

                if send_error:
                    log.error(send_error)
                    continue

                log.debug("Data sent.")

            self.msg_received.clear()

    def resume(self):
        self.msg_received.set()
