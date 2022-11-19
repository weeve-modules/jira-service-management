"""
This file implements input aspect of the module.
It receives data over REST API and passes it to the validation and processing.
"""

from queue import Queue
from bottle import post, request, response
from logging import getLogger
from module.validator import data_validation
from api.processing_thread import ProcessingThread

# set up logging
log = getLogger("request_handler")

# declare queue storing data
data_Q = Queue()

# initialise processing thread
data_processing_thread = ProcessingThread(data_Q)
data_processing_thread.start()


@post("/")
def request_handler():
    """
    Handles incoming data.
    """

    global data_Q
    global data_processing_thread

    try:
        # receive data from the previous module
        received_data = request.json

        log.debug("Received data: %s", received_data)

        # validate incoming data
        validation_error = data_validation(received_data)

        if validation_error:
            # invalid data
            response.status = 400
            return validation_error

        log.debug("Validation successful.")

        # data accepted, so add data to the queue
        data_Q.put(received_data)

        try:
            log.debug("Invoking the thread to process new data")
            data_processing_thread.resume()

        except Exception as e:
            log.error(f"Failed to invoke a thread to process new data. {e}")

        # notify previous module that data has been received
        return "OK - data accepted"

    except Exception as e:
        response.status = 400
        return f"Exception occurred while sending your data to the endpoint. {e}"
