import pandas as pd

def detect_root_logins(df):
    root_df = df[df['message'].str.contains("session opened for user root")]
    return root_df

if __name__ == "__main__":
    df_logs = pd.read_csv("parsed_logs.csv")
    root_df = detect_root_logins(df_logs)
    if not root_df.empty:
        print("[!] Root login sessions detected:")
        print(root_df[['timestamp', 'message']])
    else:
        print("[+] No root logins found.")

