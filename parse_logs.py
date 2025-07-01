import re
import pandas as pd
from datetime import datetime

LOG_PATH = "sample_logs/auth_sample.log"

def parse_auth_log(path=LOG_PATH):
    # Pattern for classic syslog format
    pattern = re.compile(r'^(\w{3}\s+\d+\s[\d:]+)\s(\S+)\s(\S+)\[(\d+)\]:\s(.*)')
    entries = []

    with open(path, 'r', encoding="utf-8", errors="ignore") as f:
        for line in f:
            match = pattern.match(line)
            if match:
                timestamp_str, host, service, pid, message = match.groups()
                try:
                    timestamp = datetime.strptime(timestamp_str, '%b %d %H:%M:%S')
                    timestamp = timestamp.replace(year=datetime.now().year)
                except:
                    timestamp = datetime.now()
                entries.append({
                    'timestamp': timestamp,
                    'host': host,
                    'service': service,
                    'pid': pid,
                    'message': message
                })

    df = pd.DataFrame(entries)
    return df

if __name__ == "__main__":
    df_logs = parse_auth_log()
    df_logs.to_csv("parsed_logs.csv", index=False)
    print("[+] Logs parsed and saved to parsed_logs.csv")

