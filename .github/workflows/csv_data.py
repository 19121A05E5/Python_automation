import datetime
import time

def main():
    # Your script's main functionality here
    print("Executing script at:", datetime.datetime.now())

def run_daily():
    while True:
        # Check if it's time to execute the script (e.g., 10 am)
        now = datetime.datetime.now()
        if now.hour == 10 and now.minute == 0:
            main()  # Execute the script
            # Wait until the next day
            tomorrow = now + datetime.timedelta(days=1)
            tomorrow = tomorrow.replace(hour=10, minute=0, second=0, microsecond=0)
            time.sleep((tomorrow - now).total_seconds())
        else:
            # Wait for 1 minute and check again
            time.sleep(60)

if __name__ == "__main__":
    run_daily()
