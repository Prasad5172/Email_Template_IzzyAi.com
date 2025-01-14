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

print(SMTP_SERVER)
def get_send_otp_email_html(otp):
    return f"""
  <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>IzzyAi</title>

    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet" />
    <style>
        body {{
            margin: 0;
            font-family: 'Poppins', sans-serif;
            background: #ffffff;
            font-size: 14px;
        }}

        .container {{
            max-width: 680px;
            margin: 0 auto;
            padding: 45px 30px 60px;
            background: #111920;
            font-size: 14px;
            color: #434343;
            position: relative;
            overflow: hidden;
        }}

        .container::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-repeat: no-repeat;
            background-size: 800px 300px;
            background-position: top top;
            filter: blur(2px);
            z-index: 0;
        }}

        .main-content {{
            margin: 0;
            margin-top: 40px;
            padding: 50px 20px;
            background: #e1e1e1;
            border-radius: 30px;
            text-align: center;
            position: relative;
            z-index: 1;
        }}

        h1 {{
            margin: 0;
            font-size: 24px;
            font-weight: 500;
            color: #1f1f1f;
        }}

        p {{
            margin: 0;
            margin-top: 17px;
            font-weight: 500;
            letter-spacing: 0.56px;
            color: #434343;
        }}

        .otp {{
            margin-top: 20px;
            font-size: 40px;
            font-weight: 600;
            letter-spacing: 25px;
            color: #ba3d4f;
        }}

        footer {{
            width: 100%;
            max-width: 490px;
            margin: 20px auto 0;
            text-align: center;
            border-top: 1px solid #979797;
        }}

        .footer-links a {{
            font-size: small;
            color: #638df8;
            text-decoration: none;
            margin: 0 5px;
        }}

        .social-icons a {{
            display: inline-block;
            margin: 0 8px;
            scale: 1.5;
        }}

        .social-icons a i {{
            color: #2DEEAA;
        }}

        /* Responsive Design */
        @media only screen and (max-width: 600px) {{
            .container {{
                padding: 30px 20px;
            }}

            .main-content {{
                padding: 40px 20px;
                border-radius: 15px;
            }}

            h1 {{
                font-size: 20px;
            }}

            .otp {{
                font-size: 32px;
                letter-spacing: 15px;
            }}

            footer {{
                max-width: 100%;
                padding: 0 15px;
            }}

            .footer-links a {{
                font-size: smaller;
            }}

            .social-icons a {{
                margin: 0 5px;
            }}
        }}
    </style>
</head>

<body>
    <div class="container">
        <header>
            <table style="width: 100%;">
                <tbody>
                    <tr>
                        <td style="text-align: center; position: relative; height: 140px;display:flex;justify-content:center;">
                            <img src="http://drive.google.com/uc?export=view&id=1R3OimiqIpRrTy3j2qsmdhGHsOT2ErpqP" alt="logo" width="50%" style="display:block" title="IzzyAI Logo" height="100px">
                        </td>
                    </tr>
                </tbody>
            </table>
        </header>

        <main>
            <div class="main-content">
                <h1>Your OTP</h1>
                <p class="otp">123456</p>
                <p>
                    Thank you for choosing IzzyAI, a product of Victoriam Inc. Please use the following OTP to complete your
                    sign-up process. The OTP is valid for <span style="font-weight: 600; color: #1f1f1f;">10 minutes</span>.
                    Do not share this code with others, including IzzyAI team members.
                </p>
                <p>Best Regards,</p>
                <p>Team IzzyAI.</p>
            </div>

            <p style="text-align: center; font-weight: 500; color: #979797; margin-top: 30px;">
                Need help? Ask at
                <a href="mailto:hello@izzyai.com" style="color:  #638df8; text-decoration: none;">hello@izzyai.com</a>.
            </p>
        </main>

        <footer>
            <p style="margin-top: 20px; font-size: 16px; font-weight: 600; color: #979797;">
                Victoriam Inc.
            </p>
            <p style="margin-top: 8px; color: #979797;">
                8 The Green STE A, Dover, Delaware 19901.
            </p>
            <div class="social-icons" style="margin-top: 16px;">
                <a href="" target="_blank"><i class="fa-brands fa-facebook"></i></a>
                <a href="" target="_blank"><i class="fa-brands fa-instagram"></i></a>
                <a href="" target="_blank"><i class="fa-brands fa-twitter"></i></a>
            </div>
            <p style="margin-top: 16px; color: #979797;">
                Copyright © 2025 IzzyAI a product of Victoriam Inc. All rights reserved.
            </p>
            <div class="footer-links" style="margin-top: 20px;">
                <a href="https://vtm.ai">Home</a> |
                <a href="http://localhost:3000/contact">Contact Us</a> |
                <a href="https://izzyai.com/service">User Agreement</a> |
                <a href="https://izzyai.com/privacy">Privacy Policy</a>
            </div>
        </footer>
    </div>
</body>

</html>

    """


def send_otp_email(recipient_email, otp):
    try:
        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = recipient_email
        msg['Subject'] = "Your Password Reset Request - One-Time Verification Code"

        # HTML email body
        html_body = get_send_otp_email_html(otp)

        # Attach the HTML content to the email
        msg.attach(MIMEText(html_body, 'html'))

        # Connect to the SMTP server and send the email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, recipient_email, msg.as_string())
        server.quit()

        print("OTP email sent successfully.")
    except Exception as e:
        print(f"Failed to send OTP email: {e}")


# Send the email
# send_otp_email("prasadpadala2005@gmail.com", 123123)



# Placeholder function for sending OTP email
def send_otp_email_for_signup(recipient_email, otp):
    try:
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = recipient_email
        msg['Subject'] = "Your OTP for Email Verification for IzzyAI"
        html_body = get_send_otp_email_html(otp)
        msg.attach(MIMEText(html_body, 'html'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, recipient_email, msg.as_string())
        server.quit()

        print(f"OTP email sent successfully to {recipient_email}.")
    except Exception as e:
        print(f"Failed to send OTP email: {e}")

def get_cancellation_email(name):
    return f"""
   <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>IzzyAi</title>

    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet" />
    <style>
        body {{
            margin: 0;
            font-family: 'Poppins', sans-serif;
            background: #ffffff;
            font-size: 14px;
        }}

        .container {{
            max-width: 680px;
            margin: 0 auto;
            padding: 45px 30px 60px;
            background: #111920;
            font-size: 14px;
            color: #434343;
            position: relative;
            overflow: hidden;
        }}

        .container::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-repeat: no-repeat;
            background-size: 800px 300px;
            background-position: top top;
            filter: blur(2px);
            z-index: 0;
        }}

        .main-content {{
            margin: 0;
            margin-top: 40px;
            padding: 50px 20px;
            background: #e1e1e1;
            border-radius: 30px;
            position: relative;
            z-index: 1;
        }}

        h1 {{
            margin: 0;
            font-size: 24px;
            font-weight: 500;
            color: #1f1f1f;
        }}

        p {{
            margin: 0;
            font-weight: 500;
            letter-spacing: 0.56px;
            color: #434343;
        }}

        footer {{
            width: 100%;
            max-width: 490px;
            margin: 20px auto 0;
            text-align: center;
            border-top: 1px solid #979797;
        }}

        .footer-links a {{
            font-size: small;
            color: #638df8;
            text-decoration: none;
            margin: 0 5px;
        }}

        .social-icons a {{
            display: inline-block;
            margin: 0 8px;
            scale: 1.5;
        }}

        .social-icons a i {{
            color: #2DEEAA;
        }}

        /* Responsive Design */
        @media only screen and (max-width: 600px) {{
            .container {{
                padding: 30px 20px;
            }}

            .main-content {{
                padding: 40px 20px;
                border-radius: 15px;
            }}

            h1 {{
                font-size: 20px;
            }}


            footer {{
                max-width: 100%;
                padding: 0 15px;
            }}

            .footer-links a {{
                font-size: smaller;
            }}

            .social-icons a {{
                margin: 0 5px;
            }}
        }}
    </style>
</head>

<body>
    <div class="container">
        <header>
            <table style="width: 100%;">
                <tbody>
                    <tr>
                        <td
                            style="text-align: center; position: relative; height: 140px;display:flex;justify-content:center;">
                            <img src="http://drive.google.com/uc?export=view&id=1R3OimiqIpRrTy3j2qsmdhGHsOT2ErpqP"
                                alt="logo" width="50%" style="display:block" title="IzzyAI Logo" height="100px">
                        </td>
                    </tr>
                </tbody>
            </table>
        </header>

        <main>
            <div class="main-content">
                <p style="margin-bottom: 10px;">Hello {name},</p>
                <p style="margin-bottom: 5px;">
                    We are sorry to see you go. Your subscription has been successfully cancelled.
                    If you have any questions or concerns, please feel free to contact us.
                </p>
                <p style="margin-bottom: 4px;">
                    We’re sorry to see you go! Your subscription has been successfully cancelled; but the good news is you’ll still have full access to your plan until the end of your current billing cycle.
                </p>
                <p style="margin-bottom: 4px;">
                    Should you decide to return, you can resubscribe anytime by visiting our plans and pricing page: <a href="www.izzyai.com/plans-pricing" style="text-decoration: underline;">www.izzyai.com/plans-pricing</a>.
                </p>
                <p style="margin-bottom: 15px;">
                    If you have any questions or concerns, please don’t hesitate to contact our support team.
                </p>
                <p style="margin-bottom: 6px;">
                    Thank you for being a part of IzzyAI, and we hope to see you again in the future!
                </p>
                <p style=" margin-bottom: 5px;">Best Regards,</p>
                <p>The IzzyAI Team</p>
            </div>

            <p style="text-align: center; font-weight: 500; color: #979797; margin-top: 30px;">
                Need help? Ask at
                <a href="mailto:hello@izzyai.com" style="color:  #638df8; text-decoration: none;">hello@izzyai.com</a>.
            </p>
        </main>

        <footer>
            <p style="margin-top: 20px; font-size: 16px; font-weight: 600; color: #979797;">
                Victoriam Inc.
            </p>
            <p style="margin-top: 8px; color: #979797;">
                8 The Green STE A, Dover, Delaware 19901.
            </p>
            <div class="social-icons" style="margin-top: 16px;">
                <a href="" target="_blank"><i class="fa-brands fa-facebook"></i></a>
                <a href="" target="_blank"><i class="fa-brands fa-instagram"></i></a>
                <a href="" target="_blank"><i class="fa-brands fa-twitter"></i></a>
            </div>
            <p style="margin-top: 16px; color: #979797;">
                Copyright © 2025 IzzyAI a product of Victoriam Inc. All rights reserved.
            </p>
            <div class="footer-links" style="margin-top: 20px;">
                <a href="https://vtm.ai">Home</a> |
                <a href="http://localhost:3000/contact">Contact Us</a> |
                <a href="https://izzyai.com/service">User Agreement</a> |
                <a href="https://izzyai.com/privacy">Privacy Policy</a>
            </div>
        </footer>
    </div>
</body>

</html>
    """

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
    html_body = get_cancellation_email(name)
    msg.attach(MIMEText(html_body, 'html'))
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, email, msg.as_string())
        server.quit()
        print(f"Cancellation notification sent to {email}")
    except Exception as e:
        print(f"Failed to send notification: {e}")

# send_cancellation_email("prasadpadala2005@gmail.com", "Prasad")