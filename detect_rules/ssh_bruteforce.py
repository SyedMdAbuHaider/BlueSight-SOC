import pandas as pd
from collections import Counter

def detect_ssh_bruteforce(df, threshold=5):
    suspicious_ips = []
    failed_df = df[df['message'].str.contains("Failed password")]
    ips = failed_df['message'].str.extract(r'from ([\\d\\.]+)')[0]
    ip_counts = Counter(ips.dropna())

    for ip, count in ip_counts.items():
        if count >= threshold:
            suspicious_ips.append({"ip": ip, "attempts": count})

    return suspicious_ips

if __name__ == "__main__":
    df_logs = pd.read_csv("parsed_logs.csv")
    alerts = detect_ssh_bruteforce(df_logs)
    print("Suspicious IPs (possible SSH brute force):")
    for alert in alerts:
        print(f"IP: {alert['ip']}, Failed Attempts: {alert['attempts']}")

