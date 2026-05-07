import os
import sys

# 1. ప్రస్తుత డైరెక్టరీ తెలుసుకోవడం
print("Current Working Directory:", os.getcwd())

#2. కొత్త ఫోల్డర్ క్రియేట్ చేయడం
folder_name = "devops_scripts"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' has been created.")
else:
    print(f"Folder '{folder_name}' already exists.")

# 3. కమాండ్ లైన్ ఆర్గుమెంట్స్ తీసుకోవడం(sys.argv)
if len(sys.argv) > 1:
    user_name = sys.argv[1]
    print(f"Hello {user_name}, the argument you passed is working!")
else:
    print("Please provide your name as an argument (e.g., python3 system_info.py Chandra)")