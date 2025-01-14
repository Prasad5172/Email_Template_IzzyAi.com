from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = os.getenv('SMTP_PORT')
SMTP_USERNAME = os.getenv('SMTP_USERNAME')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')

def send_otp_email(recipient_email, otp):
    try:
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = recipient_email
        msg['Subject'] = "Your Password Reset Request - One-Time Verification Code"
        
        # Email body
        message_body = f"""\
        Dear Valued User,

        We have received a request to reset the password for your IzzyAI account. To complete the process, please use the One-Time Password (OTP)               provided below:

        Your OTP: {otp}

        If you did not make this request, please disregard this email or contact our support team immediately to safeguard your account.

        To proceed with resetting your password, please enter this OTP on the password reset page.

        Thank you for choosing IzzyAI. We appreciate your trust in our services.

        Warm regards,
        The IzzyAI Team

        [Note: This is an automated message. Please do not reply directly to this email.]
        """
        msg.attach(MIMEText(message_body, 'plain'))
        
        # Connect to SMTP server and send email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, recipient_email, msg.as_string())
        server.quit()
        
        print("OTP email sent successfully.")
    except Exception as e:
        print(f"Failed to send OTP email: {e}")


# Placeholder function for sending OTP email
def send_otp_email_for_signup(recipient_email, otp):
    try:
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = recipient_email
        msg['Subject'] = "Your OTP for Email Verification for IzzyAI"
        message_body = f"Dear User,\n\nYour OTP is: {otp}\n\nThank you!"
        msg.attach(MIMEText(message_body, 'plain'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, recipient_email, msg.as_string())
        server.quit()

        print(f"OTP email sent successfully to {recipient_email}.")
    except Exception as e:
        print(f"Failed to send OTP email: {e}")


def send_cancellation_email(email, name):
    # Set up the SMTP server
    smtp_server = SMTP_SERVER
    smtp_port = SMTP_PORT
    smtp_user = SMTP_USERNAME
    smtp_password = SMTP_PASSWORD
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = email
    msg['Subject'] = "Your Subscription Has Been Cancelled"
    body = f"""
    Hello {name},
    We are sorry to see you go. Your subscription has been successfully cancelled.
    If you have any questions or concerns, please feel free to contact us.
    Best regards,
    Your Company Name
    """
    msg.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, email, msg.as_string())
        server.quit()
        print(f"Cancellation notification sent to {email}")
    except Exception as e:
        print(f"Failed to send notification: {e}")
