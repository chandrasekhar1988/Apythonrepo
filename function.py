import subprocess

def restart_nginx():
    """
    Restarts the Nginx service using systemctl.
    Note: Requires sudo privileges to execute successfully.
    """
    print("Restarting Nginx...")
      # ఇక్కడ అసలైన కమాండ్ ఉంటుంది
    try:
        # It is recommended to test the config before restarting
        subprocess.run(["sudo", "nginx", "-t"], check=True)
        # Restart the Nginx service
        subprocess.run(["sudo", "systemctl", "restart", "nginx"], check=True)
        print("Nginx restarted successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while restarting Nginx: {e}")

# Call the function
restart_nginx() # ఎప్పుడు కావాలంటే అప్పుడు పిలుచుకోవచ్చు

# Example of a function with arguments
def greet(name):
    print("Hello", name)

greet("Python")