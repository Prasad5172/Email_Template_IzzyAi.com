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

# Dashboard Email Templates
def send_saleperson_signup_link_email(recipient_email, signup_link):
    try:
        # Setup email message
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = recipient_email
        msg['Subject'] = "Welcome to IzzyAI - Complete Your Registration"

        # Email body with the sign-up link
        message_body = f"""\
        Dear User,

        Welcome to IzzyAI!To complete your registration, please click the following link:

        Sign-up Link: {signup_link}

        Please follow the instructions on the page to complete your registration.

        If you did not expect this email or believe it was sent in error, please contact our support team.

        Thank you for choosing IzzyAI.

        Best regards,
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

        print("Sign-up link email sent successfully.")
    except Exception as e:
        print(f"Failed to send sign-up link email: {e}")


def send_slp_signup_link_email(recipient_email, clinic_id, signup_link):
    try:
        # Setup email message
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = recipient_email
        msg['Subject'] = "Welcome to IzzyAI - Complete Your Registration"

        # Email body with the sign-up link
        message_body = f"""\
        Dear User,

        Welcome to IzzyAI! A sales representative (ID: {clinic_id}) has referred you to our platform. To complete your registration, please click the following link:

        Sign-up Link: {signup_link}

        Please follow the instructions on the page to complete your registration.

        If you did not expect this email or believe it was sent in error, please contact our support team.

        Thank you for choosing IzzyAI.

        Best regards,
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

        print("Sign-up link email sent successfully.")
    except Exception as e:
        print(f"Failed to send sign-up link email: {e}")


def send_clinic_signup_link_email(recipient_email, sale_person_id, signup_link):
    try:
        # Setup email message
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = recipient_email
        msg['Subject'] = "Welcome to IzzyAI - Complete Your Registration"

        # Email body with the sign-up link
        message_body = f"""\
        Dear User,

        Welcome to IzzyAI! A sales representative (ID: {sale_person_id}) has referred you to our platform. To complete your registration, please click the following link:

        Sign-up Link: {signup_link}

        Please follow the instructions on the page to complete your registration.

        If you did not expect this email or believe it was sent in error, please contact our support team.

        Thank you for choosing IzzyAI.

        Best regards,
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

        print("Sign-up link email sent successfully.")
    except Exception as e:
        print(f"Failed to send sign-up link email: {e}")



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

# function to create otp and send it
def send_otp_email(recipient_email, otp):
    try:
        
        # Setup email message
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = recipient_email
        msg['Subject'] = "Your Password Reset Request - One-Time Verification Code"
        
        # Email body
        message_body = f"""\
        Dear User,

        You recently requested to reset your password for your IzzyAI account. To complete the process, please use the following One-Time Password (OTP):

        OTP: {otp}

        If you did not request a password reset, please ignore this email or contact our support team immediately to ensure your account remains secure.

        If you are ready to reset your password, enter this OTP in the password reset page.

        Thank you for using IzzyAI.

        Best regards,
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

def send_invoice_email(recipient_email, customer_name, invoice_id, total_amount, due_date):
    """
    Send an invoice email to the customer with the invoice details.
    """
    try:
        # Setup email message
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = recipient_email
        msg['Subject'] = "Your Invoice from IzzyAI"

        # Email body with invoice details
        message_body = f"""\

        Dear {customer_name},

        Thank you for your subscription with IzzyAI. Please find the details of your invoice below:

        Invoice ID: {invoice_id}
        Total Amount: ${total_amount}
        Due Date: {due_date}

        Please make the payment by the due date to avoid any interruptions to your subscription.

        If you have any questions or need assistance, feel free to contact our support team.

        Thank you for choosing IzzyAI.

        Best regards,
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

        print(f"Invoice email sent successfully to {recipient_email}.")
    except Exception as e:
        print(f"Failed to send invoice email to {recipient_email}: {e}")

        
# Mobile App and Website Email Templates 

def send_email(recipient_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, recipient_email, msg.as_string())
        server.quit()

        print(f"Email sent successfully to {recipient_email}.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Specific email functions
def send_verification_email(recipient_email, otp_code, verification_link):
    subject = "Your Journey with IzzyAI Speech Guardian Awaits - Verify Now!"
    body = (
        "Welcome to IzzyAI – Your Speech Guardian!\n\n"
        "You’re just one step away from starting your journey with IzzyAI.\n\n"
        f"**Your OTP Code: {otp_code}**\n\n"
        "**Click below to verify your email address and to activate your 7-day Free Trial.**\n\n"
        "Your 7-day free trial is your gateway to personalized AI-powered speech therapy with exclusive features and tools. "
        "Once your trial ends, your subscription will automatically convert to **IzzyAI Unlimited [Monthly]** so you can continue your progress without interruption.\n\n"
        f"**[Verify Email Button]({verification_link})**\n\n"
        "**Want to Save More?**\n"
        "You’ll also have the option to switch to our Annual Plan, which offers the best value and significant savings. "
        "If you choose to switch, your annual subscription will begin at the start of your next billing cycle.\n\n"
        "Thank you for choosing IzzyAI to guide your journey to confident speech!\n\n"
        "The IzzyAI Team"
    )
    send_email(recipient_email, subject, body)

def send_welcome_email(recipient_email, first_name):
    subject = "Welcome to IzzyAI - Your Speech Guardian!"
    body = (
        f"Hi {first_name},\n\n"
        "We’re so excited to have you on board! Your 7-day Free Trial has officially started, and your Speech Guardian is ready to help you shine.\n\n"
        "Here’s what you can explore during your trial:\n"
        "● Personalized therapy sessions tailored to your needs and goals.\n"
        "● AI powered exercises to improve your communication skills.\n"
        "● Daily access to your Speech Guardian—always there when you need them.\n\n"
        "Ready to get started? Dive in now to start working towards confident speech:\n"
        "Finish Setting Up Your Profile & Start Exploring\n\n"
        "To help you get started, we’ve included a helpful Instructional Guide that explains how to effectively use IzzyAI and make the most of its features. [Click here to access the guide].\n\n"
        "Thanks,\n"
        "The IzzyAI Team\n\n"
        "P.S. Unlock unlimited access to all IzzyAI features and enjoy 24/7 availability to AI-powered therapy by subscribing to the IzzyAI Unlimited plan today!"
    )
    send_email(recipient_email, subject, body)

def send_mid_week_email(recipient_email, first_name):
    subject = "How’s Your Journey with IzzyAI, Your Speech Guardian?"
    body = (
        f"Hi {first_name},\n\n"
        "We hope you’re loving your time with IzzyAI! You’re halfway through your 7-day free trial, and there’s still so much to discover.\n\n"
        "Keep up the amazing progress,\nThe IzzyAI Team"
    )
    send_email(recipient_email, subject, body)

def send_subscription_start_email(recipient_email, first_name):
    subject = "Welcome to IzzyAI Unlimited! Your Journey Just Got Better"
    body = (
        f"Hi {first_name},\n\n"
        "Congratulations—your Monthly Unlimited subscription has officially started!\n\n"
        "Warmly,\nThe IzzyAI Team"
    )
    send_email(recipient_email, subject, body)

def send_cancellation_email(recipient_email, first_name):
    subject = "We’re Sorry to See You Go – Continue Your Journey with IzzyAI"
    body = (
        f"Hi {first_name},\n\n"
        "We noticed you decided to cancel your Unlimited plan, and we’re truly sorry to see you go.\n\n"
        "Warmly,\nThe IzzyAI Team"
    )
    send_email(recipient_email, subject, body)

def send_payment_issue_email(recipient_email, first_name):
    subject = "There’s an Issue with Your Payment for IzzyAI"
    body = (
        f"Hi {first_name},\n\n"
        "We tried to process your payment for your IzzyAI Unlimited plan, but unfortunately, it didn’t go through.\n\n"
        "Warmly,\nThe IzzyAI Team"
    )
    send_email(recipient_email, subject, body)

def send_upgrade_reminder_email(recipient_email, first_name):
    subject = "Discover What You’re Missing with IzzyAI Unlimited"
    body = (
        f"Hi {first_name},\n\n"
        "We noticed you’ve been using the Basic version of IzzyAI, and there’s so much more waiting for you in Unlimited!\n\n"
        "Warmly,\nThe IzzyAI Team"
    )
    send_email(recipient_email, subject, body)