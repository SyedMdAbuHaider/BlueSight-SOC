from flask import Flask, render_template
import pandas as pd
import json

app = Flask(__name__)

@app.route("/")
def index():
    df = pd.read_csv("parsed_logs.csv")

    total_events = len(df)
    failed_ssh = df[df["message"].str.contains("Failed password", na=False)]
    root_logins = df[df["message"].str.contains("session opened for user root", na=False)]

    ip_counts = failed_ssh["message"].str.extract(r'from ([\d\.]+)')[0].value_counts()
    suspicious_ips = ip_counts[ip_counts > 3].to_dict()

    chart_data = {
        "ips": list(ip_counts.index),
        "counts": [int(c) for c in ip_counts.values]
    }

    return render_template("index.html",
                           total_events=total_events,
                           failed_ssh=len(failed_ssh),
                           root_logins=len(root_logins),
                           suspicious_ips=suspicious_ips,
                           chart_data=json.dumps(chart_data))

if __name__ == "__main__":
    app.run(debug=True)

