import subprocess  # Import the subprocess module to allow running system commands
from datetime import datetime  # Import datetime for timestamping
import time  # Import time module for tracking duration

def ping_google_dns():
    # Open ping command in subprocess with 128 bytes of data
    ping_process = subprocess.Popen(
        ['ping', '8.8.8.8', '-l', '128', '-t'],  # Define the ping command with 128-byte payload
        stdout=subprocess.PIPE,  # Capture the standard output of the process
        stderr=subprocess.PIPE,  # Capture the standard error output of the process
        text=True  # Ensure the output is returned as a string rather than bytes
    )
    
    start_time = None  # Initialize a variable to store the start time of an unsuccessful ping period

    # Loop indefinitely to monitor ping output
    while True:
        output = ping_process.stdout.readline().strip()  # Read a line of output from the ping process and strip any extra whitespace
        if output:  # Check if there is any output
            # Check if the output indicates a successful ping response
            if "Reply from 8.8.8.8:" in output:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get the current time for timestamping
                print(f"{timestamp}: Ping to Google DNS successful, 128 bytes sent.")  # Print success message to the console
                if start_time is not None:  # If there was a previous unsuccessful ping period
                    end_time = time.time()  # Record the end time of the successful ping
                    duration = round(end_time - start_time, 2)  # Calculate the duration of the failure period in seconds
                    # Log the duration of the failure period and the recovery to the log file
                    with open("ping_logs.txt", "a") as file:
                        file.write(f"{timestamp}: Ping to Google DNS successful after a period of failure. Duration of failure: {duration} seconds\n")
                    start_time = None  # Reset the start time indicator
            # Check if the output indicates a request timeout (unsuccessful ping)
            elif "Request timed out" in output:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get the current time for timestamping
                print(f"{timestamp}: Ping to Google DNS unsuccessful")  # Print failure message to the console
                if start_time is None:  # If this is the first unsuccessful ping in a series
                    start_time = time.time()  # Record the start time of the unsuccessful ping period
                # Log the unsuccessful ping to the log file
                with open("ping_logs.txt", "a") as file:
                    file.write(f"{timestamp}: Ping to Google DNS unsuccessful\n")

if __name__ == "__main__":
    ping_google_dns()  # Call the function to start pinging Google DNS indefinitely
