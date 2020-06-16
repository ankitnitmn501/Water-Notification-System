import time
from plyer import notification

if __name__== "__main__":
    while True:
        notification.notify(
            title = "**Please Drink Water Now!!",
            message="The National Academies of Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
            app_icon= "G:\water_notification system\icon.ico",
            timeout=50
        )
        time.sleep(10)