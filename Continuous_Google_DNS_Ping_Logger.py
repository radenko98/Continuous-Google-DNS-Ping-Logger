import os  # Import os module for directory and file handling
import subprocess  # Import the subprocess module to allow running system commands
from datetime import datetime  # Import datetime for timestamping
import time  # Import time module for tracking duration

def create_log_file():
    current_date = datetime.now()  # Get the current date and time
    year_folder = current_date.strftime("%Y")  # Create a string for the year
    log_file_name = current_date.strftime("%Y%m%d_ping_log.txt")  # Create log file name with format "YYYYMMDD_ping_log.txt"
    
    # Create the folder for the year if it doesn't exist
    if not os.path.exists(year_folder):
        os.makedirs(year_folder)  # Create the folder for the current year
    
    # Return the path to the log file within the year folder
    return os.path.join(year_folder, log_file_name)

def ping_google_dns():
    log_file_path = create_log_file()  # Generate the log file path for the current day
    ping_process = subprocess.Popen(
        ['ping', '8.8.8.8', '-l', '128', '-t'],  # Define the ping command with 128-byte payload
        stdout=subprocess.PIPE,  # Capture the standard output of the process
        stderr=subprocess.PIPE,  # Capture the standard error output of the process
        text=True  # Ensure the output is returned as a string rather than bytes
    )
    
    start_time = None  # Initialize a variable to store the start time of an unsuccessful ping period
    current_date = datetime.now().date()  # Store the current date to track changes

    # Loop indefinitely to monitor ping output
    while True:
        output = ping_process.stdout.readline().strip()  # Read a line of output from the ping process and strip any extra whitespace
        if output:  # Check if there is any output
            now = datetime.now()  # Get the current time
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")  # Format the current time for timestamping
            
            # Check if the date has changed, and create a new log file if necessary
            if now.date() != current_date:
                log_file_path = create_log_file()  # Generate a new log file path for the new day
                current_date = now.date()  # Update the current date to the new date
            
            # Check if the output indicates a successful ping response
            if "Reply from 8.8.8.8:" in output:
                print(f"{timestamp}: Ping to Google DNS successful, 128 bytes sent.")  # Print success message to the console
                if start_time is not None:  # If there was a previous unsuccessful ping period
                    end_time = time.time()  # Record the end time of the successful ping
                    duration = round(end_time - start_time, 2)  # Calculate the duration of the failure period in seconds
                    # Log the duration of the failure period and the recovery to the log file
                    with open(log_file_path, "a") as file:
                        file.write(f"{timestamp}: Ping to Google DNS successful after a period of failure. Duration of failure: {duration} seconds\n")
                    start_time = None  # Reset the start time indicator
            
            # Check if the output indicates a request timeout (unsuccessful ping)
            elif "Request timed out" in output:
                print(f"{timestamp}: Ping to Google DNS unsuccessful")  # Print failure message to the console
                if start_time is None:  # If this is the first unsuccessful ping in a series
                    start_time = time.time()  # Record the start time of the unsuccessful ping period
                # Log the unsuccessful ping to the log file
                with open(log_file_path, "a") as file:
                    file.write(f"{timestamp}: Ping to Google DNS unsuccessful\n")

if __name__ == "__main__":
    ping_google_dns()  # Call the function to start pinging Google DNS indefinitely
