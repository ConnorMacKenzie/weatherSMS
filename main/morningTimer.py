import time
import schedule
from sms import send_sms


schedule.every().day.at("9:00").do(send_sms)

while True:
    schedule.run_pending()
    time.sleep(1)
