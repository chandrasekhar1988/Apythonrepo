def safe_divide(a, b):
    try:
        # మనం చేయాలనుకున్న పని
        result = a / b
        print(f"Results: {result}")
    
    except ZeroDivisionError:
        # సున్నా తో భాగిస్తే వచ్చే ఎర్రర్ ని పట్టుకోవడం
        print("Error: Cannot divide by zero (0)!")
        
    except TypeError:
        # నంబర్ కాకుండా టెక్స్ట్ ఇస్తే వచ్చే ఎర్రర్
        print("Error: Please provide numbers only!")
        
    finally:
        # ఇది ఎర్రర్ వచ్చినా, రాకపోయినా రన్ అవుతుంది
        print("Task completed.\n\n")

# ప్రోగ్రామ్ రన్ చేసి చూడండి:
safe_divide(10, 2)  # ఇది సరిగ్గా పనిచేస్తుంది
safe_divide(10, 0)  # ఇది ఎర్రర్ ని పట్టుకుంటుంది
safe_divide(10, "a") # ఇది టైప్ ఎర్రర్ ని పట్టుకుంటుంది