# Cybersecurity Data Analysis for Beginners

**Hands-on training for security monitoring using ISO27001/NIST controls**  
![Security Analytics](https://img.shields.io/badge/domain-security_analytics-blue) 
![Level](https://img.shields.io/badge/level-beginner-green) 
![Framework](https://img.shields.io/badge/framework-ISO27001/NIST-orange)
![License](https://img.shields.io/badge/license-MIT-purple)

---

## 🎯 Your First Day as a Junior Analyst
*"You've just joined our Security Operations Center (SOC). These exercises mirror real tasks you'll perform daily, simplified for learning."*

### 🔍 Starter Kit
```bash
datasets/
├── sample_logs/       # Auth/web logs to analyze
├── sample_alerts/     # SIEM alerts to investigate
└── simulated_attacks/ # Safe attack patterns

scripts/               # Ready-to-use analysis tools
notebooks/            # Guided investigation playbooks
```

---

## 🚦 Priority Decision Guide
*(Based on NIST SP 800-61r2)*
| Indicator          | Critical | High | Medium | Low |
|--------------------|----------|------|--------|-----|
| **Root/admin**     | ✅       | ✅   | ❌     | ❌  |
| **>5 attempts/min**| ✅       | ✅   | ❌     | ❌  |
| **Data exposure**  | ✅       | ❌   | ❌     | ❌  |

**Example**:  
`5 failed root logins = HIGH priority`

---

## 🛠️ Core Workflows
### 1. Log Analysis ([`01-log-analysis`](notebooks/01-log-analysis))
**Skills**:  
- Detect brute force attacks in `auth.log`  
- Classify incident priority  
**Framework**: NIST SP 800-92 (Log Management)  
```python
# Find failed logins
failed = log_data[log_data['status'] == 'Failed']
```

### 2. Alert Triage ([`02-user-behavior`](notebooks/02-user-behavior))
**Skills**:  
- Correlate alerts with vulnerability data  
- Identify false positives  
**Framework**: ISO27001 A.9 (Access Control)

---

## 🚨 Incident Reporting
All findings flow to:  
```markdown
incident_reports/
└── TEMPLATE.md  # Standardized reporting format
```
**Sample Email**:  
```text
Subject: [HIGH] Brute Force Attempts - SSH Server  
Body:  
- Detected: 5 root login failures from 192.168.1.15  
- Action: IP blocked in firewall  
- Evidence: notebooks/01-log-analysis/output/  
```

---

## 🏗️ Repository Structure
```
.
├── datasets/              # Training data
├── notebooks/             # Step-by-step guides
├── scripts/               # Reusable tools
├── incident_reports/      # Reporting templates
└── priority_exercises/    # Classification practice
```

---

## 🧑‍💻 Getting Started
1. Install requirements:  
   ```bash
   pip install pandas matplotlib jupyter
   ```
2. Run your first analysis:  
   ```bash
   jupyter notebook notebooks/01-log-analysis
   ```
3. File a report using `incident_reports/TEMPLATE.md`

---

## 📚 Framework Alignment
| Notebook | ISO27001 | NIST SP |
|----------|----------|---------|
| 01-log-analysis | A.12.4 | 800-92 |
| 02-user-behavior | A.9.4 | 800-115 |

---

## 🤝 Contribution Guidelines
- Add new datasets with `scripts/data_generator.py`  
- Keep all data synthetic (no real logs/IPs)  
- Reference controls from ISO/NIST docs  

> 💡 *Pro Tip: Use the `priority_exercises/` folder (Under construction - July 2025) to test your skills before working with real data!*  

---

