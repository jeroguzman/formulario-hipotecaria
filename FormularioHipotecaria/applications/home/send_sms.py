# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACd0cc447942fc865739ea385408ad8c95'
auth_token = 'b5b3ef6606bec4bc25d6bf6f9ae23266'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Prueba MS HIPOTECARIA.",
                     from_='+12058753823',
                     to='+526624644275'
                 )

print(message.sid)