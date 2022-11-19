"""
Entrypoint file that sets up and starts REST API server for the module.
"""

from os import getenv
from logging import getLogger
from bottle import run
from api import setup_logging

setup_logging()
log = getLogger("main")

def main():
    log.info(
        "%s running on %s at port %s",
        getenv("MODULE_NAME"),
        getenv("INGRESS_HOST"),
        getenv("INGRESS_PORT"),
    )

    # start the server
    run(
        host=getenv("INGRESS_HOST"),
        port=getenv("INGRESS_PORT"),
        quiet=True,
    )

if __name__ == "__main__":
    main()
