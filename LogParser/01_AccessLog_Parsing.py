
'''
# Sample Apache access log entries
192.168.1.1 - - [01/Jul/2022:12:34:56 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.1 - - [01/Jul/2022:12:34:57 +0000] "GET /styles.css HTTP/1.1" 200 5678
192.168.1.2 - - [01/Jul/2022:12:35:01 +0000] "POST /login HTTP/1.1" 302 9012
192.168.1.1 - - [01/Jul/2022:12:35:05 +0000] "GET /images/logo.png HTTP/1.1" 200 3456
192.168.1.3 - - [01/Jul/2022:12:35:10 +0000] "GET /about.html HTTP/1.1" 200 6789
192.168.1.1 - - [01/Jul/2022:12:35:15 +0000] "GET /contact.html HTTP/1.1" 200 2345
'''

import re
from collections import defaultdict

response_times = defaultdict(list)
request_counts = defaultdict(int)
ip_counts = defaultdict(int)

# Sample log entries
with open('access.log', 'r') as file:
    log_entries = file.readlines()

for log in log_entries:
    # Regex pattern to match the log format
    # pattern=r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}) - - \[(.*?)\] \"(.*?)\" (\d{3}) (\d+)'
    pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(.*?)" (\d+) (\d+)'
    match = re.match(pattern, log)
    
    if match:
        ip_address, timestamp, request, status_code, response_time = match.groups()       
        print(f"IP Address: {ip_address}, Timestamp: {timestamp}, Request: {request}, Status Code: {status_code}, Response Time: {response_time}")
        response_times[request].append(int(response_time))
        request_counts[request] += 1
        ip_counts[ip_address] += 1

# Calculate average response time for each request, print top 1
for request, times in sorted(response_times.items(), key=lambda x: sum(x[1]) / len(x[1]), reverse=True)[:1]:
    avg_response_time = sum(times) / len(times)
    print(f"Request: {request}, Average Response Time: {avg_response_time:.2f} ms")

# Print top 1 most requested URL
for request, count in sorted(request_counts.items(), key=lambda x: x[1], reverse=True)[:1]:
    print(f"Most Requested URL: {request}, Count: {count}")

# Print top 1 IP address with the most requests
for ip_address, count in sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)[:1]:
    print(f"IP Address: {ip_address}, Count: {count}")  