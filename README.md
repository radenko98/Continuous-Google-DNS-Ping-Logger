This Python script continuously pings Google DNS (8.8.8.8) using the ping command with the -t option, which means the ping operation runs indefinitely until stopped manually. 
The script monitors the output of the ping command and performs the following actions based on the result:

  1. If a successful ping reply is received from Google DNS ("Reply from 8.8.8.8:"), it prints a success message along with the current timestamp.
  2. If the ping times out ("Request timed out"), indicating an unsuccessful ping, it prints a failure message along with the current timestamp.
  3. If an unsuccessful ping is followed by a successful ping, it calculates the duration in seconds between the start time of the unsuccessful ping and the time of the successful ping.
     It then logs this duration along with the timestamps in a file named ping_logs.txt.
  4. The script runs indefinitely, continuously monitoring the ping output.

This script is useful for monitoring the connectivity to Google DNS and logging any downtime along with the duration of the downtime.

***HOW TO RUN***

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


![image](https://github.com/radenko98/Continuous-Google-DNS-Ping-Logger/assets/22021972/b5826dff-8d05-4e7d-bab0-8bdc0f878521)

