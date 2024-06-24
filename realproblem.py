import time
import smtplib
from email.mime.text import MIMEText

# Initialize system
SAFE_RANGE_LOW = 60  # Lower bound of safe heart rate range
SAFE_RANGE_HIGH = 100  # Upper bound of safe heart rate range
CHECK_INTERVAL = 5  # Check heart rate every 5 seconds

def read_heart_rate():
    # This function should interface with your heart rate sensor.
    # For this example, we will simulate it.
    import random
    return random.randint(50, 110)  # Simulated heart rate reading

def send_alert(current_hr):
    # Replace with your email details
    sender_email = "youremail@example.com"
    receiver_email = "alert@example.com"
    password = "yourpassword"

    # Create the email content
    subject = "Heart Rate Alert!"
    body = f"The patient's heart rate is out of the safe range! Current heart rate: {current_hr} bpm"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send the email
    try:
        with smtplib.SMTP_SSL('smtp.example.com', 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print(f"Alert sent: {body}")
    except Exception as e:
        print(f"Failed to send alert: {e}")

def log_heart_rate(current_hr):
    with open("heart_rate_log.txt", "a") as log_file:
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {current_hr} bpm\n")
    print(f"Heart rate logged: {current_hr} bpm")

def main():
    while True:
        # Read heart rate
        current_hr = read_heart_rate()
        
        # Check heart rate
        if current_hr < SAFE_RANGE_LOW or current_hr > SAFE_RANGE_HIGH:
            send_alert(current_hr)
        
        # Log heart rate
        log_heart_rate(current_hr)
        
        # Wait for the next check
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
