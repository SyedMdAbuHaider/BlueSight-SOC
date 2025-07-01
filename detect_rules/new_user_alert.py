import pandas as pd

def detect_new_users(df):
    user_df = df[df['message'].str.contains("new user")]
    return user_df

if __name__ == "__main__":
    df_logs = pd.read_csv("parsed_logs.csv")
    new_users_df = detect_new_users(df_logs)
    if not new_users_df.empty:
        print("[!] New user accounts detected:")
        print(new_users_df[['timestamp', 'message']])
    else:
        print("[+] No new user creation events found.")

