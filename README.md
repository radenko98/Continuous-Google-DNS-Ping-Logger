This Python script helps you monitor the stability of your internet connection and detect periods of downtime. It continuously pings Google's public DNS server (8.8.8.8) with a 128-byte payload, running indefinitely until manually stopped.

The script uses the -t and -l options with the ping command to keep the operation continuous. It analyzes the ping responses and performs the following actions:

1. Successful Ping: When a reply is received from Google DNS ("Reply from 8.8.8.8:"), the script prints a success message with the current timestamp to the console.
2. Unsuccessful Ping: If the ping times out ("Request timed out"), indicating a failure, the script prints a failure message with the current timestamp to the console.
3. Transition from Failure to Success: If a previously unsuccessful ping is followed by a successful ping, the script calculates the duration of the downtime in seconds.

It logs this duration, along with the relevant timestamps, in a file named ping_logs.txt.
The script continuously monitors these conditions, providing real-time feedback and logging any interruptions in connectivity. This makes it a valuable tool for tracking network stability and identifying periods of downtime.


***Why is it better to run 128-byte payload then standard 32-byte payload when testing network stability and identifying periods of downtime.***

Running a 128-byte payload instead of the standard 32-byte payload when testing network stability and identifying periods of downtime can provide a more comprehensive and realistic assessment of the network's performance. Here are some reasons why:
1. Closer to Real-World Traffic:
**Typical Data Load:** In real-world applications, data packets often carry more than 32 bytes. Using a larger payload size, such as 128 bytes, can more closely simulate actual data transmission conditions, providing a more accurate reflection of network stability and performance.

2. Increased Sensitivity to Network Issues:
**Packet Fragmentation:** Larger packets are more susceptible to issues like fragmentation, especially in networks with lower Maximum Transmission Units (MTUs). Testing with a 128-byte payload can help identify problems that may not be evident with smaller packets.
**Error Detection:** Larger packets have a higher chance of encountering errors or loss, as they occupy more bandwidth and may be affected by various network conditions. This can make it easier to detect intermittent issues or marginal links.

3. Bandwidth Utilization Testing:
**Network Strain:** Sending larger packets can put more strain on the network, helping to test the network's ability to handle higher data loads. This can be especially useful for identifying bottlenecks or limitations in network infrastructure.

4. More Accurate Latency Measurement:
**Latency Testing:** Larger packets can provide a better measure of latency in some cases, as they may take longer to traverse the network and thus more accurately reflect delays introduced by routers, switches, and other networking equipment.

5. Detection of Throttling or Traffic Shaping:
**Network Policies:** Some networks implement policies that throttle or shape traffic based on packet size. By using a larger payload, you can detect if there are specific policies in place that might affect performance differently for small vs. larger packets.

6. Enhanced Diagnostic Information:
**ICMP Packet Analysis:** Larger ICMP Echo Request packets can sometimes carry additional diagnostic information, allowing for more detailed analysis of network performance characteristics.

**Conclusion:**
Using a 128-byte payload for ping tests offers a more realistic and thorough examination of network behavior, which is crucial for accurately assessing network stability, performance, and downtime. It helps in detecting issues that might not be apparent with smaller packets and provides a better simulation of typical network usage scenarios.

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


![Snimak ekrana 2024-07-30 234253](https://github.com/user-attachments/assets/315ef91a-86c4-4db3-8696-341592ba9928)


