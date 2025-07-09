# Cybersecurity Data Analysis for Beginners

**Practical data analysis applied to foundational security controls from ISO27001 and NIST frameworks**

![Security Analytics](https://img.shields.io/badge/domain-security_analytics-blue) ![Level](https://img.shields.io/badge/level-beginner-green) ![Framework](https://img.shields.io/badge/framework-ISO27001/NIST-orange)

## Purpose

This repository bridges the gap between cybersecurity operations and data analysis by providing hands-on examples of monitoring and analyzing security controls referenced in:

- **ISO27001**: Specifically Annex A controls (A.9 Access Control, A.12 Operations Security, etc.)
- **NIST Publications**: SP 800-53 (Security Controls), SP 800-92 (Log Management), SP 800-40 (Vulnerability Management)

## Repository Structure

```
Cybersecurity-Data-Analysis-for-Beginners
│ 
├── datasets/              # Sanitized security datasets
│   ├── sample_logs/       # Web/Auth logs for analysis
│   ├── sample_alerts/     # Security alert samples
│   └── simulated_attacks/ # Safe training data
│
├── notebooks/            # Guided analytical workflows
│   ├── 01-log-analysis/            # NIST SP 800-92 implementation
│   ├── 02-user-behavior/           # ISO27001 A.9 monitoring
│   ├── 03-vulnerability-tracking/  # NIST SP 800-40 examples
│   └── 04-threat-detection/        # ISO27001 A.12 operations
│
└── scripts/              # Reusable security analysis tools
    ├── log_parser.py         # Log normalization
    ├── alert_correlation.py   # NIST-inspired correlation
    └── report_generator.py    # Control effectiveness reporting
```

## Key Learning Path

1. **Fundamentals**:
   - Security log structure and normalization
   - Basic statistical analysis of security events
   - Control effectiveness metrics

2. **ISO27001 Focus Areas**:
   - Access control monitoring (A.9)
   - Operational security analysis (A.12)
   - Incident detection indicators (A.16)

3. **NIST-Aligned Analysis**:
   - Log management (SP 800-92)
   - Vulnerability trending (SP 800-40)
   - Anomaly detection fundamentals

## Usage Guidance

1. Start with `/notebooks/01-log-analysis` for foundational skills
2. Use datasets in conjunction with notebooks
3. Modify scripts for your own security monitoring needs

## Contribution

This repository welcomes:
- Additional ISO/NIST-aligned analysis examples
- Improvements to existing analysis methods
- Quality sanitized datasets for training purposes

**Note**: All datasets are artificially generated and contain no real organizational/personal data.

---

*"What gets measured gets managed" - Applied to security controls*
