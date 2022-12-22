"""
This file implements module's main logic.
Data outputting should happen here.

Edit this file to implement your module.
"""
import requests
import json
import base64
from os import getenv
from logging import getLogger

log = getLogger("module")

url = f"{getenv('ATLASSIAN_DOMAIN')}/rest/servicedeskapi/request"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic " + base64.b64encode(f'{getenv("ATLASSIAN_EMAIL")}:{getenv("ATLASSIAN_API_TOKEN")}'.encode("ascii")).decode("ascii"),
}


def module_main(received_data: any) -> str:
    """
    Send received data to the next module by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Outputting ...")

    try:
        payload = json.dumps({
            "serviceDeskId": getenv("SERVICE_DESK_ID"),
            "requestTypeId": getenv("REQUEST_TYPE_ID"),
            "requestFieldValues": {
                "summary": received_data[getenv("SUMMARY_LABEL")],
                "description": received_data[getenv("DESCRIPTION_LABEL")]
            }
        })

        resp = requests.request(
            "POST",
            url,
            data=payload,
            headers=headers
        )

        if resp.status_code == 201:
            return None
        else:
            return resp.text

    except Exception as e:
        return f"Exception in the module business logic: {e}"
