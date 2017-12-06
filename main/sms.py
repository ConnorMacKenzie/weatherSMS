import weather
from twilio.rest import Client


def send_sms():
    account_sid = "account"
    auth_token = "token"

    client = Client(account_sid, auth_token)

    client.api.account.messages.create(
        to="+number",
        from_="+number",
        body=weather.getweather(45.4215, -75.6972))
