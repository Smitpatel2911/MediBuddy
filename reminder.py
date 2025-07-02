from datetime import datetime
from time import sleep
from plyer import notification
import smtplib as smp
import pandas as pd

def check_reminders():
    while True:
        now = datetime.now().strftime("%H:%M")
        df = pd.read_csv("schedule.csv")
        for index, row in df.iterrows():
            med_time = row["Time"][:5]
            if now == med_time:
                notification.notify(
                    title = "💊 Medicine Reminder",
                    message = f"Take {row['Dosage']} of {row['Medicine']}",
                    timeout=10
                )
        sleep(60)  # check every minute