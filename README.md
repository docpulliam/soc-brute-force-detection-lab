SOC Brute Force Detection Lab
Overview

This project simulates a Security Operations Center (SOC) investigation workflow by detecting and analyzing a simulated brute-force authentication attack using Splunk SIEM and Python.

The lab demonstrates how authentication logs can be ingested into a SIEM platform, analyzed using Splunk Search Processing Language (SPL), and visualized in a security monitoring dashboard to identify suspicious login activity.

A Python script generates simulated authentication events that mimic real-world brute-force login attempts, allowing the detection logic to be tested in a controlled environment.

Python Attack Simulator
        │
        ▼
Authentication Log File (CSV)
        │
        ▼
Splunk Log Ingestion
        │
        ▼
Detection Queries (SPL)
        │
        ▼
SOC Monitoring Dashboard
        │
        ▼
Security Incident Investigation

Technologies Used

Splunk Enterprise (SIEM)

Python 3

Splunk Search Processing Language (SPL)

CSV Log Dataset

Security Monitoring Dashboard

Detection Logic

The detection rule identifies suspicious authentication behavior by detecting repeated failed login attempts from the same source IP or targeting the same user account.

Example SPL detection query:

index=soc_lab
| stats count by username, src_ip
| where count > 5

This query highlights potential brute-force attempts by identifying abnormal login volumes.

Project Components
1. Python Attack Simulator

A Python script generates simulated authentication events to replicate a brute-force attack.

The script continuously writes login attempts to a CSV log file that is monitored by Splunk.

attack_simulator.py

Authentication Log Dataset

The simulated attack produces authentication logs with fields such as:

Timestamp

Username

Source IP

Login Status (success/failure)

auth_attack_log.csv

3. Splunk Log Ingestion

Splunk monitors the authentication log file and indexes the events into the following index:

soc_lab

4. Detection Queries

Custom SPL queries were created to identify suspicious login patterns such as:

Multiple failed login attempts

High authentication volume from a single IP

Potential brute-force behavior

5. SOC Monitoring Dashboard

A Splunk dashboard was created to visualize:

Failed login spikes

Source IP activity

Authentication attempts by user

This simulates the type of monitoring interface used by Security Operations Centers.

Investigation Workflow

Python simulator generates repeated failed login attempts.

Authentication logs are written to a monitored CSV file.

Splunk ingests the log data in real time.

Detection queries identify abnormal login patterns.

Dashboard panels visualize suspicious activity.

An incident investigation report is generated.

Skills Demonstrated

SIEM configuration and monitoring

Log ingestion and parsing

Security event detection

Splunk SPL query development

Security dashboard creation

Attack simulation with Python

Incident investigation documentation

Potential Security Use Cases

This detection approach can help identify:

Brute-force login attempts

Credential stuffing attacks

Unauthorized access attempts

Suspicious authentication behavior

Future Improvements

Integrate threat intelligence lookups for suspicious IPs

Automate alert notifications

Expand detection rules for additional attack patterns

Simulate additional attack types (phishing, lateral movement)

Author

Doc Pulliam

Cybersecurity & Security Automation Enthusiast
Python | SIEM | Detection Engineering | Security Monitoring
