# Postmortem: August 12, 2024 Outage

## Issue Summary
- **Outage Duration:**  
  - **Start Time:** August 12, 2024, 02:00 PM GMT  
  - **End Time:** August 12, 2024, 03:15 PM GMT
- **Impact:**  
  The outage affected 90% of users, preventing them from accessing the main dashboard of the web application. Users encountered a 503 Service Unavailable error, leading to a significant decrease in user activity and an influx of customer support inquiries.
- **Root Cause:**  
  A sudden traffic surge due to an unannounced marketing campaign overwhelmed the server. The automatic scaling feature failed to activate, resulting in service disruption.

## Timeline
- **02:00 PM** - Issue detected by a monitoring alert indicating a drop in successful requests.
- **02:02 PM** - Engineering team notified and investigation began.
- **02:10 PM** - Initial focus on the application code; no issues found.
- **02:20 PM** - Investigation shifted to server load; logs indicated a traffic surge.
- **02:30 PM** - Identified the root cause as a failure in the automatic scaling mechanism.
- **02:35 PM** - Incident escalated to DevOps for manual scaling.
- **02:50 PM** - Additional server instances added; load normalized.
- **03:15 PM** - Application fully restored; users could access the dashboard.

## Root Cause and Resolution
- **Root Cause:**  
  The outage was caused by a sudden surge in traffic due to an unplanned marketing email campaign. A misconfiguration in the server’s scaling thresholds prevented the automatic scaling feature from activating, overwhelming the server.
- **Resolution:**  
  The immediate resolution was to manually scale the server by adding more instances. The scaling thresholds were then corrected to ensure proper automatic scaling in the future.

## Corrective and Preventative Measures
- **Improvements and Fixes:**
  - **Scaling Configuration:** Review and update scaling thresholds to better handle sudden traffic spikes.
  - **Traffic Monitoring:** Enhance real-time monitoring for unusual traffic patterns that may require proactive scaling.
  - **Automated Alerts:** Implement alerts for automatic scaling failures.
  - **Collaboration with Marketing:** Establish a protocol for better communication with marketing to anticipate traffic changes.

- **Tasks:**
  1. Update and test the server’s auto-scaling thresholds.
  2. Implement traffic alerts for sudden spikes.
  3. Enhance monitoring for unusual traffic patterns.
  4. Develop a communication protocol between engineering and marketing teams.
