import json

def correlate_alerts(alert_path):
    """Basic alert correlation by source IP"""
    with open(alert_path) as f:
        alerts = json.load(f)
    
    ip_counts = {}
    for alert in alerts:
        ip = alert['src_ip']
        ip_counts[ip] = ip_counts.get(ip, 0) + 1
    
    return ip_counts
