#!/usr/bin/env python3
"""
Log Analysis Script for Junior Security Analysts
NIST Alignment: SP 800-92 (Log Management)
ISO27001: A.12.4 (Logging)
"""

import pandas as pd
from datetime import datetime
import argparse

# Priority Classification Matrix
PRIORITY_MATRIX = {
    'root': {'threshold': 1, 'level': 'HIGH'},
    'admin': {'threshold': 1, 'level': 'HIGH'},
    '*': {'threshold': 5, 'level': 'MEDIUM'}  # Default for other accounts
}

def analyze_logs(log_path, output_report_path):
    """Main analysis function"""
    print(f"\n🔍 Analyzing {log_path}...")
    
    # Load and parse logs
    try:
        log_data = pd.read_csv(log_path)
        print(f"Loaded {len(log_data)} log entries")
    except Exception as e:
        print(f"❌ Error loading log file: {e}")
        return

    # Filter failed logins
    failed_logins = log_data[log_data['status'] == 'Failed']
    if len(failed_logins) == 0:
        print("✅ No failed login attempts found")
        return

    # Calculate attack velocity
    time_span = (pd.to_datetime(failed_logins['timestamp'].max()) - 
                 pd.to_datetime(failed_logins['timestamp'].min())).total_seconds() / 60
    attempts_per_min = len(failed_logins) / max(1, time_span)  # Prevent division by zero

    # Classify priority
    target_account = failed_logins['username'].iloc[0]
    priority_rules = PRIORITY_MATRIX.get(target_account, PRIORITY_MATRIX['*'])
    priority = priority_rules['level'] if attempts_per_min >= priority_rules['threshold'] else 'LOW'

    # Generate report
    report = f"""
# SECURITY INCIDENT REPORT
**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Analyst**: [YOUR_NAME]
**Priority**: {priority}

## Findings
- Target account: `{target_account}`
- Source IP: `{failed_logins['source_ip'].iloc[0]}`
- Attempts: {len(failed_logins)} ({attempts_per_min:.1f}/min)
- Time range: {failed_logins['timestamp'].min()} to {failed_logins['timestamp'].max()}

## Recommended Actions
1. Block IP in firewall
2. Reset credentials for {target_account}
3. Verify system integrity
"""

    # Save report
    try:
        with open(output_report_path, 'w') as f:
            f.write(report)
        print(f"📝 Report saved to {output_report_path}")
        print("=== Priority Classification ===")
        print(f"Account: {target_account} | Velocity: {attempts_per_min:.1f}/min → {priority}")
    except Exception as e:
        print(f"❌ Error saving report: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Analyze auth logs for brute force attempts')
    parser.add_argument('--log', default='../datasets/sample_logs/auth_processed.csv', 
                       help='Path to auth log file')
    parser.add_argument('--output', default='../incident_reports/incident_report.md',
                       help='Output report path')
    
    args = parser.parse_args()
    
    print("""
    ░██████╗░█████╗░░█████╗░██╗░░██╗
    ██╔════╝██╔══██╗██╔══██╗██║░░██║
    ╚█████╗░██║░░╚═╝███████║███████║
    ░╚═══██╗██║░░██╗██╔══██║██╔══██║
    ██████╔╝╚█████╔╝██║░░██║██║░░██║
    ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝
    Simple Log Analyzer v1.0 (NIST-aligned)
    """)
    
    analyze_logs(args.log, args.output)
