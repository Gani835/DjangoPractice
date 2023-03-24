# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['AC54ce74bd21fefd93bfe4472daab01578']
auth_token = os.environ['7d6918aba574e77e0a7dc0648f1d77b3']
client = Client(account_sid, auth_token)

call = client.calls.create(
                        twiml='<Response><Say>Ahoy, World!</Say></Response>',
                        to='+919160381228',
                        from_='+16158575633'
                    )

print(call.sid)
