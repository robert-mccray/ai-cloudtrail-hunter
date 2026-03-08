# 🕵️ CloudTrail AI Hunter (SIEM/SOAR Automation)

A proactive DevSecOps engine designed to combat alert fatigue. Ingests raw AWS CloudTrail logs and uses contextual LLM analysis to instantly differentiate between benign operational noise and critical behavioral anomalies (e.g., unauthorized IAM privilege escalation).

## 🚀 How to Run Locally

### Prerequisites
1. **Ollama:** Must be running locally with the `llama3` model.
2. **Python Environment:** Python 3.10+ installed.

### Execution Steps
1. Clone the repository.
2. Inspect the mock log files in the `/data` directory to see the difference between standard traffic and the simulated attack payload.
3. Install dependencies:
   ```bash
   pip install requests
   ```
Run the hunter script to parse the logs and generate the security alert:

```Bash
python hunter.py
```
---
