from azure.communication.email import EmailClient
message = {
    "content": {
        "subject": "This is the subject",
        "plainText": "This is the body",
        "html": "<html><h1>This is the body</h1></html>"
    },
    "recipients": {
        "to": [
            {
                "address": "<will.lang@decima.xyz>",
                "displayName": "Will Lang"
            }
        ]
    },
    "senderAddress": "<donotreply@xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.azurecomm.net>"
}
POLLER_WAIT_TIME = 10

try:
    email_client = EmailClient.from_connection_string("endpoint=https://decima-email.unitedstates.communication.azure.com/;accesskey=7rUGF7k2R8z0orCzK6sYZ4PpaSZTEjAFX0AdEIoMKm4K5eMskng7JQQJ99AJACULyCp2Fes8AAAAAZCStcLk")

    poller = email_client.begin_send(message)

    time_elapsed = 0
    while not poller.done():
        print("Email send poller status: " + poller.status())

        poller.wait(POLLER_WAIT_TIME)
        time_elapsed += POLLER_WAIT_TIME

        if time_elapsed > 18 * POLLER_WAIT_TIME:
            raise RuntimeError("Polling timed out.")

    if poller.result()["status"] == "Succeeded":
        print(f"Successfully sent the email (operation id: {poller.result()['id']})")
    else:
        raise RuntimeError(str(poller.result()["error"]))

except Exception as ex:
    print(ex)
