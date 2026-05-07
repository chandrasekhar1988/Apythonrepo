import subprocess

def run_command(command):
    try:
        # shell=True ఇస్తే నేరుగా linux కమాండ్ రన్ అవుతుంది
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Success: {command}")
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e.stderr.decode()}")

print("Nginx ఇన్‌స్టాలేషన్ ప్రారంభిస్తున్నాము...")
# Nginx ఇన్‌స్టాల్ చేయడం
run_command("sudo dnf install nginx -y")

# Nginx సర్వీస్ స్టార్ట్ చేయడం
run_command("sudo systemctl start nginx")

# స్టేటస్ చెక్ చేయడం
status = run_command("sudo systemctl is-active nginx")
print(f"Nginx Status: {status}")