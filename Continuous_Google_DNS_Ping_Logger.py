import subprocess
from datetime import datetime
import time

def ping_google_dns():
    # Open ping command in subprocess
    ping_process = subprocess.Popen(['ping', '8.8.8.8', '-t'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    start_time = None  # Variable to store the start time of unsuccessful ping

    # Loop indefinitely to monitor ping output
    while True:
        output = ping_process.stdout.readline().strip()
        if output:
            # Check if ping was successful or not
            if "Reply from 8.8.8.8:" in output:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                if start_time is not None:  # If there was an unsuccessful ping before
                    end_time = time.time()  # Get the end time of successful ping
                    duration = round(end_time - start_time, 2)  # Calculate duration in seconds
                    print(f"{timestamp}: Ping to Google DNS successful. Duration: {duration} seconds")
                    with open("ping_logs.txt", "a") as file:
                        file.write(f"{timestamp}: Ping to Google DNS successful. Duration: {duration} seconds\n")
                    start_time = None  # Reset start time
                else:
                    print(f"{timestamp}: Ping to Google DNS successful")
            elif "Request timed out" in output:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"{timestamp}: Ping to Google DNS unsuccessful")
                if start_time is None:  # If this is the first unsuccessful ping
                    start_time = time.time()  # Record the start time

                with open("ping_logs.txt", "a") as file:
                    file.write(f"{timestamp}: Ping to Google DNS unsuccessful\n")

if __name__ == "__main__":
    ping_google_dns()
