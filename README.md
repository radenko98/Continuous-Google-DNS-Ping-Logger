This Python script helps you monitor the stability of your internet connection and detect periods of downtime. It continuously pings Google's public DNS server (8.8.8.8) with a 128-byte payload, running indefinitely until manually stopped.

The script uses the -t and -l options with the ping command to keep the operation continuous. It analyzes the ping responses and performs the following actions:

1. Successful Ping: When a reply is received from Google DNS ("Reply from 8.8.8.8:"), the script prints a success message with the current timestamp to the console.
2. Unsuccessful Ping: If the ping times out ("Request timed out"), indicating a failure, the script prints a failure message with the current timestamp to the console.
3. Transition from Failure to Success: If a previously unsuccessful ping is followed by a successful ping, the script calculates the duration of the downtime in seconds.

It logs this duration, along with the relevant timestamps, in a file named ping_logs.txt.
The script continuously monitors these conditions, providing real-time feedback and logging any interruptions in connectivity. This makes it a valuable tool for tracking network stability and identifying periods of downtime.


***HOW TO RUN as a executable that can be run on Windows without needing Python installed***

Just download the RAR file and extract it using WinRar and start the "Continuous_Google_DNS_Ping_Logger.exe"



***HOW TO RUN as a Python Script***

To run the provided Python scripts, you can follow these general steps:

1. Install Python:
If you haven't installed Python on your system, you can download and install it from the official Python website: https://www.python.org/downloads/.


2. Run Scripts:
Open a command prompt or terminal window.
Navigate to the directory where the scripts are located using the cd command. For example:

***cd path\to\script\directory***

Run script using the python command. For example:

*python Continuous-Google-DNS-Ping-Logger.py*

![image](https://github.com/radenko98/Continuous-Google-DNS-Ping-Logger/assets/22021972/f28a6887-ddc4-4ca7-8dfd-8b846723db9b)

It will look like this

![image](https://github.com/radenko98/Continuous-Google-DNS-Ping-Logger/assets/22021972/f04ab2ad-d3aa-4e12-98b6-34eedadfadf2)

![image](https://github.com/radenko98/Continuous-Google-DNS-Ping-Logger/assets/22021972/c670dbd0-fd68-4e6e-84d7-20bdd6b1e8ca)


