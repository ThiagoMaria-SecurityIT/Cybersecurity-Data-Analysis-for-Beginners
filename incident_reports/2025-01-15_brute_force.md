# SECURITY INCIDENT REPORT (BEGINNER)

**Date**: 2025-01-15  
**Time First Detected**: 09:15 AM  
**Analyst**: Jane Doe  
**Priority**: Medium  <- Attention here

---

## 1. What Happened  
☑️ **Type of Incident**:  
- [X] Brute force attack  
- [ ] Suspicious web request  
- [ ] Unauthorized access  

☑️ **Where Found**:  
- Log file: `auth.log`  
- Notebook: `01-log-analysis/log_analysis.ipynb`  

☑️ **Technical Details**:  
| Affected System | Attacker IP    | Times Observed | First Occurrence |  
|-----------------|----------------|----------------|-------------------|  
| SSH Server      | 192.168.1.15   | 5 attempts     | 09:01 AM          |  

---

## 2. How You Found It  
🔍 **Steps Taken**:  
1. Ran Cell 3 in the notebook to count failed logins  
2. Saw 5 failed root login attempts from 192.168.1.15  
3. Verified by checking raw `auth.log` entries  

💡 **Key Evidence**:  
```log
Jan 15 09:01:25 server1 sshd[12345]: Failed password for root from 192.168.1.15
Jan 15 09:01:25 server1 sshd[12345]: Failed password for root from 192.168.1.15
[...]
```

---

## 3. Immediate Actions  
☑️ **What You Did**:  
- [X] Saved notebook results to `notebooks/01-log-analysis/sample_output/`  
- [X] Checked `web_access.csv` for same IP (no matches found)  
- [X] Notified supervisor via email  

⏱️ **Timeline**:  
| Time     | Action Taken                     |  
|----------|----------------------------------|  
| 09:15 AM | Detected pattern in notebook     |  
| 09:20 AM | Verified log entries             |  
| 09:25 AM | Drafted this report              |  

---

## Email Template (Actual Submission)  
**Subject**: [Medium] Brute Force Attempts on SSH Server  

**Body**:  
"Hi Team Lead,  

At 09:15 AM, I detected:  
- 5 failed root login attempts from 192.168.1.15  

Evidence:  
- Analysis: `notebooks/01-log-analysis/log_analysis.ipynb`  
- Raw logs: `datasets/sample_logs/auth.log`  

Recommended next steps:  
1. Block IP 192.168.1.15 in firewall  
2. Check if this IP appears in other logs  

Let me know if you need more details.  

Regards,  
Jane Doe  
Junior Security Analyst  
