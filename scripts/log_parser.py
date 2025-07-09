import pandas as pd

def parse_auth_log(log_path):
    """Parse SSH auth logs for failed attempts"""
    data = []
    with open(log_path) as f:
        for line in f:
            if "Failed password" in line:
                parts = line.split()
                data.append({
                    'timestamp': ' '.join(parts[:3]),
                    'user': parts[8],
                    'ip': parts[10]
                })
    return pd.DataFrame(data)
