import weather
from twilio.rest import Client


def send_sms():
    account_sid = "ACab513427a58a166f093fbe34297cd645"
    auth_token = "2131222bb7f7e4c0fbf6f4037162720d"

    client = Client(account_sid, auth_token)

    client.api.account.messages.create(
        to="+14168876677",
        from_="+12892160213",
        body=weather.getweather(45.4215, -75.6972))
