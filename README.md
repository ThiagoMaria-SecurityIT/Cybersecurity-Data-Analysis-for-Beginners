# Cybersecurity Data Analysis for Beginners - Under construction 🚧 July 09, 2025 - Contributions are Welcome! 🚧
🚧 Again: This repository is under construction - Codes and content will be revised until July 30, 2025  🚧  
This repository will be a hands-on training to guide new cybersecurity analysts  


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

## About the Author   

**Thiago Maria - From Brazil to the World 🌎**  
*Senior Security Information Professional | Passionate Programmer | AI Developer*

With a professional background in security analysis and a deep passion for programming, I created this Github acc to share some knowledge about security information, cybersecurity, Python and AI development practices. Most of my work here focuses on implementing security-first approaches in developer tools while maintaining usability.

Lets Connect:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/thiago-cequeira-99202239/)  
[![Hugging Face](https://img.shields.io/badge/🤗Hugging_Face-AI_projects-yellow)](https://huggingface.co/ThiSecur)

 
## Ways to Contribute:   
 Want to see more upgrades? Help me keep it updated!    
 [![Sponsor](https://img.shields.io/badge/Sponsor-%E2%9D%A4-red)](https://github.com/sponsors/ThiagoMaria-SecurityIT) 
