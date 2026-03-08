import json
import urllib.request

def hunt_anomalies():
    # Mocking a suspicious AWS CloudTrail log entry
    suspicious_log = {
        "eventTime": "2026-03-07T03:00:00Z",
        "eventName": "AssumeRole",
        "userIdentity": {"type": "AssumedRole", "principalId": "dev-user-bob"},
        "requestParameters": {"roleArn": "arn:aws:iam::123:role/Production-DB-Admin"},
        "sourceIPAddress": "192.168.1.55" # Example IP
    }

    print(" Hunting CloudTrail Logs with Llama-3...")
    prompt = f"""
    you are a Principal Cybersecurity Analyst. Review this AWS CloudTrail log:
    {json.dumps(suspicious_log)}
    Explain in 2 sentences why a 'dev-user' assuming a 'Production-DB-Admin' role at 3 AM is a critical security anomaly.
    """

    data = {"model": "llama3", "prompt": prompt, "stream": False}
    req = urllib.request.Request("http://localhost:11434/api/generate", data=json.dumps(data).encode("utf-8"))

    with urllib.request.urlopen(req) as response:
        print("\n================ AI SECURITY ALERT ================")
        print(json.loads(response.read().decode("utf-8"))["response"])
        print("===================================================")

i __name__ == "__main__":
hunt_anomalies() 