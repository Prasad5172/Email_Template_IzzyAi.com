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
email = "prasadpadala2005@gmail.com"


def body_of_send_saleperson_signup_link_email(signup_link):
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

.mb-10 {{
    margin-bottom: 10px;
}}

.mb-5 {{
    margin-bottom: 5px;
}}

.mb-4 {{
    margin-bottom: 4px;
}}

.mb-3 {{
    margin-bottom: 3px;
}}

.mb-6 {{
    margin-bottom: 6px;
}}

.mb-12 {{
    margin-bottom: 12px;
}}

.mb-15 {{
    margin-bottom: 15px;
}}

.link-color {{
    color: #638df8;
}}

.font-bold {{
            font-weight: 600;
            color: black;
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
                        <td style="height: 140px; text-align: center;">
                            <img
                                src="http://drive.google.com/uc?export=view&id=1R3OimiqIpRrTy3j2qsmdhGHsOT2ErpqP"
                                alt="logo"
                                title="IzzyAI Logo"
                                width="50%"
                                height="100px"
                                style="display: inline-block; margin: 0 auto;"
                            >
                        </td>
                    </tr>
                </tbody>
            </table>
        </header>

        <main>
            <div class="main-content">
                <p class="mb-5">Dear User,</p>
                <p class="mb-10">Welcome to IzzyAI! We’re excited to have you on board. To complete your sales prole,
                    please click the link below:</p>
               <p class="mb-10">
    <span class="font-bold">Sign-up Link:</span>
    {signup_link}
</p>


                <p class="mb-15">Follow the instructions on the page to nalize your registration.</p>
                <p class="mb-5">If you weren’t expecting this email or think it was sent by mistake, please contact our
                    support team for assistance.</p>
                <p class="mb-10">Thank you for joining IzzyAI – we’re thrilled to work with you!</p>
                <p class="mb-3">Best regards,</p>
                <p class="mb-10">The IzzyAI Team</p>
                <p>[Please note: This is an automated message. Do not reply directly to this email]</p>
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
# Dashboard Email Templates


def send_saleperson_signup_link_email(recipient_email, signup_link):
    try:
        # Setup email message
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = recipient_email
        msg['Subject'] = "Welcome to IzzyAI - Complete Your Sales Prole on IzzyAI"

        # Email body with the sign-up link
        html_body = body_of_send_saleperson_signup_link_email(signup_link)
        msg.attach(MIMEText(html_body, 'html'))

        # Connect to SMTP server and send email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, recipient_email, msg.as_string())
        server.quit()

        print("Sign-up link email sent successfully.")
    except Exception as e:
        print(f"Failed to send sign-up link email: {e}")
# send_saleperson_signup_link_email("prasadpadala2005@gmail.com","https://www.google.com")


def body_send_slp_signup_link_email(clinic_id, signup_link):
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

.mb-10 {{
    margin-bottom: 10px;
}}

.mb-5 {{
    margin-bottom: 5px;
}}

.mb-4 {{
    margin-bottom: 4px;
}}

.mb-3 {{
    margin-bottom: 3px;
}}

.mb-6 {{
    margin-bottom: 6px;
}}

.mb-12 {{
    margin-bottom: 12px;
}}

.mb-15 {{
    margin-bottom: 15px;
}}

.link-color {{
    color: #638df8;
}}

.font-bold {{
            font-weight: 600;
            color: black;
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
                <p class="mb-5">Dear User,</p>
                <p class="mb-10">We’re excited to welcome you to IzzyAI! You’ve been added to your Clinic’s prole on
                    our platform, giving you access to all the tools and features IzzyAI offers.</p>
                <p class="mb-15">To complete your registration, please click the link below and follow the instructions
                    provided:</p>
                <p class="mb-10">
    <span class="font-bold">Sign-up Link:</span>
    {signup_link}
</p>


                <p class="mb-5">If you weren’t expecting this email or think it was sent by mistake, please reach out to
                    our support team for assistance.</p>
                <p class="mb-10">Thank you for joining IzzyAI. We’re looking forward to supporting your clinic’s success!</p>
                <p class="mb-3">Best regards,</p>
                <p class="mb-10">The IzzyAI Team</p>
                <p>[Please note: This is an automated message. Do not reply directly to this email]</p>
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


def send_slp_signup_link_email(recipient_email, clinic_id, signup_link):
    try:
        # Setup email message
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = recipient_email
        msg['Subject'] = "Welcome to IzzyAI - Complete Your Registration"

        # Email body with the sign-up link
        html_body = body_send_slp_signup_link_email(clinic_id, signup_link)
        msg.attach(MIMEText(html_body, 'html'))

        # Connect to SMTP server and send email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, recipient_email, msg.as_string())
        server.quit()

        print("Sign-up link email sent successfully.")
    except Exception as e:
        print(f"Failed to send sign-up link email: {e}")


def body_of_send_clinic_signup_link_email(sale_person_id, signup_link):
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

.mb-10 {{
    margin-bottom: 10px;
}}

.mb-5 {{
    margin-bottom: 5px;
}}

.mb-4 {{
    margin-bottom: 4px;
}}

.mb-3 {{
    margin-bottom: 3px;
}}

.mb-6 {{
    margin-bottom: 6px;
}}

.mb-12 {{
    margin-bottom: 12px;
}}

.mb-15 {{
    margin-bottom: 15px;
}}

.link-color {{
    color: #638df8;
}}

.font-bold {{
            font-weight: 600;
            color: black;
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
                        <td style="height: 140px; text-align: center;">
                            <img
                                src="http://drive.google.com/uc?export=view&id=1R3OimiqIpRrTy3j2qsmdhGHsOT2ErpqP"
                                alt="logo"
                                title="IzzyAI Logo"
                                width="50%"
                                height="100px"
                                style="display: inline-block; margin: 0 auto;"
                            >
                        </td>

                    </tr>
                </tbody>
            </table>
        </header>

        <main>
            <div class="main-content">
                <p class="mb-5">Dear User,</p>
                <p class="mb-10">Welcome to IzzyAI! You’ve been referred to our platform by one of our sales
                    representatives (ID: {sale_person_id}). We’re excited to have your clinic join our
                    community!</p>
                <p class="mb-15">To complete your registration, simply click the link below and follow the instructions:</p>
                <p class="mb-10">
    <span class="font-bold">Sign-up Link:</span>
    {signup_link}
</p>
                <p class="mb-5">If you weren’t expecting this email or believe it was sent in error, please don’t hesitate
                    to contact our support team for assistance.</p>
                <p class="mb-10">Thank you for choosing IzzyAI. We look forward to supporting your clinic with our
                    innovative platform!</p>
                <p class="mb-3">Best regards,</p>
                <p class="mb-10">The IzzyAI Team</p>
                <p>[Please note: This is an automated message. Do not reply directly to this email]</p>
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


def send_clinic_signup_link_email(recipient_email, sale_person_id, signup_link):
    try:
        # Setup email message
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = recipient_email
        msg['Subject'] = "Welcome to IzzyAI - Complete Your Registration"

        # Email body with the sign-up link
        html_body = body_of_send_clinic_signup_link_email(
            sale_person_id, signup_link)
        msg.attach(MIMEText(html_body, 'html'))

        # Connect to SMTP server and send email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, recipient_email, msg.as_string())
        server.quit()

        print("Sign-up link email sent successfully.")
    except Exception as e:
        print(f"Failed to send sign-up link email: {e}")
# send_clinic_signup_link_email("prasadpadala2005@gmail.com",1,"https://hello.com")


def body_of_send_otp_email_for_signup(otp):
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

.otp {{
    margin-top: 10px;
    font-size: 30px;
    font-weight: 600;
    letter-spacing: 15px;
    color: #ba3d4f;
    margin-bottom: 10px;
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

.mb-10 {{
    margin-bottom: 10px;
}}

.mb-5 {{
    margin-bottom: 5px;
}}

.mb-4 {{
    margin-bottom: 4px;
}}

.mb-3 {{
    margin-bottom: 3px;
}}

.mb-6 {{
    margin-bottom: 6px;
}}

.mb-12 {{
    margin-bottom: 12px;
}}

.mb-15 {{
    margin-bottom: 15px;
}}

.mb-20 {{
    margin-bottom: 20px;
}}

.link-color {{
    color: #638df8;
}}

.font-bold {{
            font-weight: 600;
            color: black;
        }}

.text-center {{
    text-align: center;
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
                        <td style="height: 140px; text-align: center;">
                            <img
                                src="http://drive.google.com/uc?export=view&id=1R3OimiqIpRrTy3j2qsmdhGHsOT2ErpqP"
                                alt="logo"
                                title="IzzyAI Logo"
                                width="50%"
                                height="100px"
                                style="display: inline-block; margin: 0 auto;"
                            >
                        </td>

                    </tr>
                </tbody>
            </table>
        </header>

        <main>
            <div class="main-content">
                <p class="mb-5">Dear User,</p>

                <h1 class="text-center">Your OTP</h1>
                <p class="otp text-center">{otp}</p>
                <p class="mb-10">Use this code to complete your verication process.</p>
                <p class="mb-10">Thank you</p>
                <p class="mb-3">Best regards,</p>
                <p class="mb-10">The IzzyAI Team</p>
                <p>[Please note: This is an automated message. Do not reply directly to this email]</p>
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
# Placeholder function for sending OTP email


def send_otp_email_for_signup(recipient_email, otp):
    try:
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = recipient_email
        msg['Subject'] = "Your OTP for Email Verification for IzzyAI"
        html_body = body_of_send_otp_email_for_signup(otp)
        msg.attach(MIMEText(html_body, 'html'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, recipient_email, msg.as_string())
        server.quit()

        print(f"OTP email sent successfully to {recipient_email}.")
    except Exception as e:
        print(f"Failed to send OTP email: {e}")
# send_otp_email_for_signup("prasadpadala2005@gmail.com",123123)


def body_of_send_otp_email(otp):
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

.otp {{
    margin-top: 10px;
    font-size: 30px;
    font-weight: 600;
    letter-spacing: 15px;
    color: #ba3d4f;
    margin-bottom: 10px;
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

.mb-10 {{
    margin-bottom: 10px;
}}

.mb-5 {{
    margin-bottom: 5px;
}}

.mb-4 {{
    margin-bottom: 4px;
}}

.mb-3 {{
    margin-bottom: 3px;
}}

.mb-6 {{
    margin-bottom: 6px;
}}

.mb-12 {{
    margin-bottom: 12px;
}}

.mb-15 {{
    margin-bottom: 15px;
}}

.mb-20 {{
    margin-bottom: 20px;
}}

.link-color {{
    color: #638df8;
}}

.font-bold {{
            font-weight: 600;
            color: black;
        }}

.text-center {{
    text-align: center;
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
                        <td style="height: 140px; text-align: center;">
                            <img
                                src="http://drive.google.com/uc?export=view&id=1R3OimiqIpRrTy3j2qsmdhGHsOT2ErpqP"
                                alt="logo"
                                title="IzzyAI Logo"
                                width="50%"
                                height="100px"
                                style="display: inline-block; margin: 0 auto;"
                            >
                        </td>

                    </tr>
                </tbody>
            </table>
        </header>

        <main>
            <div class="main-content">
                <p class="mb-5">Dear User,</p>
                <p class="mb-10">You recently requested to reset the password for your IzzyAI account. To proceed,
                    please use the following One-Time Password (OTP):</p>

                        <h1 class="text-center">Your OTP</h1>
                        <p class="otp text-center">{otp}</p>
                <p class="mb-10">If you did not request a password reset, please disregard this email or contact our
                    support team immediately to secure your account.</p>
                <p class="mb-20">To reset your password, simply enter this OTP on the password reset page and follow
                    the instructions.</p>
                <p class="mb-10">Thank you for using IzzyAI. We’re here to help if you need any assistance</p>
                <p class="mb-3">Best regards,</p>
                <p class="mb-10">The IzzyAI Team</p>
                <p>[Please note: This is an automated message. Do not reply directly to this email]</p>
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
# function to create otp and send it


def send_otp_email(recipient_email, otp):
    try:

        # Setup email message
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = recipient_email
        msg['Subject'] = "Your Password Reset Request - One-Time Verification Code"

        # Email body
        html_body = body_of_send_otp_email(otp)
        msg.attach(MIMEText(html_body, 'html'))

        # Connect to SMTP server and send email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, recipient_email, msg.as_string())
        server.quit()

        print("OTP email sent successfully.")
    except Exception as e:
        print(f"Failed to send OTP email: {e}")


def body_of_send_invoice_email(customer_name, invoice_id, total_amount, due_date):
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

.otp {{
    margin-top: 10px;
    font-size: 30px;
    font-weight: 600;
    letter-spacing: 15px;
    color: #ba3d4f;
    margin-bottom: 10px;
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

.mb-10 {{
    margin-bottom: 10px;
}}

.mb-5 {{
    margin-bottom: 5px;
}}

.mb-4 {{
    margin-bottom: 4px;
}}

.mb-3 {{
    margin-bottom: 3px;
}}

.mb-6 {{
    margin-bottom: 6px;
}}

.mb-12 {{
    margin-bottom: 12px;
}}

.mb-15 {{
    margin-bottom: 15px;
}}

.mb-20 {{
    margin-bottom: 20px;
}}

.link-color {{
    color: #638df8;
}}

.font-bold {{
            font-weight: 600;
            color: black;
        }}

.text-center {{
    text-align: center;
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
                        <td style="height: 140px; text-align: center;">
                            <img src="http://drive.google.com/uc?export=view&id=1R3OimiqIpRrTy3j2qsmdhGHsOT2ErpqP"
                                alt="logo" title="IzzyAI Logo" width="50%" height="100px"
                                style="display: inline-block; margin: 0 auto;">
                        </td>

                    </tr>
                </tbody>
            </table>
        </header>

        <main>
            <div class="main-content">
                <p class="mb-5">Dear {customer_name},</p>
                <p class="mb-10">Thank you for your subscription to IzzyAI! Please nd the details of your invoice below:</p>
                <ul>
                    <li>
                        <p class="mb-10"><span class="font-bold">Invoice ID:</span> <span
                            class="link-color">{invoice_id}</span></p>
                    </li>
                    <li>
                        <p class="mb-10"><span class="font-bold">Total Amount:</span> <span
                            class="link-color"> ${total_amount}</span></p>
                    </li>
                    <li>
                        <p class="mb-10"><span class="font-bold">Due Date:</span> <span
                            class="link-color">{due_date}</span></p>
                    </li>
                </ul>

                <p class="mb-10">We kindly request that you complete the payment by the due date to ensure
                    uninterrupted access to your subscription.</p>
                <p class="mb-20">If you have any questions or need assistance, please don’t hesitate to reach out to our
                    support team.</p>
                <p class="mb-10">Thank you for choosing IzzyAI.</p>
                <p class="mb-3">Best regards,</p>
                <p class="mb-10">The IzzyAI Team</p>
                <p>[Please note: This is an automated message. Do not reply directly to this email]</p>
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


def send_invoice_email(recipient_email, customer_name, invoice_id, total_amount, due_date):
    """
    Send an invoice email to the customer with the invoice details.
    """
    try:
        # Setup email message
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = recipient_email
        msg['Subject'] = "Payment Reminder for Your IzzyAI Invoice"

        # Email body with invoice details
        html_body = body_of_send_invoice_email(
            customer_name, invoice_id, total_amount, due_date)
        msg.attach(MIMEText(html_body, 'html'))

        # Connect to SMTP server and send email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, recipient_email, msg.as_string())
        server.quit()

        print(f"Invoice email sent successfully to {recipient_email}.")
    except Exception as e:
        print(f"Failed to send invoice email to {recipient_email}: {e}")
# send_invoice_email(email,"prasad",1,10,123)

# Mobile App and Website Email Templates


def send_email(recipient_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, recipient_email, msg.as_string())
        server.quit()

        print(f"Email sent successfully to {recipient_email}.")
    except Exception as e:
        print(f"Failed to send email: {e}")


def body_of_send_verification_email(otp_code, verification_link):
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

        .otp {{
            margin-top: 10px;
            font-size: 30px;
            font-weight: 600;
            letter-spacing: 15px;
            color: #ba3d4f;
            margin-bottom: 10px;
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

        .mb-10 {{
            margin-bottom: 10px;
        }}

        .mb-5 {{
            margin-bottom: 5px;
        }}

        .mb-4 {{
            margin-bottom: 4px;
        }}

        .mb-3 {{
            margin-bottom: 3px;
        }}

        .mb-6 {{
            margin-bottom: 6px;
        }}

        .mb-12 {{
            margin-bottom: 12px;
        }}

        .mb-15 {{
            margin-bottom: 15px;
        }}

        .mb-20 {{
            margin-bottom: 20px;
        }}

        .link-color {{
            color: #638df8;
        }}

        .font-bold {{
            font-weight: 600;
            color: black;
        }}

        .text-center {{
            text-align: center;
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

        button {{
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }}

        button:hover {{
            background-color: #45a049;
        }}

    </style>
</head>

<body>
    <div class="container">
        <header>
            <table style="width: 100%;">
                <tbody>
                    <tr>
                        <td style="height: 140px; text-align: center;">
                            <img src="http://drive.google.com/uc?export=view&id=1R3OimiqIpRrTy3j2qsmdhGHsOT2ErpqP"
                                alt="logo" title="IzzyAI Logo" width="50%" height="100px"
                                style="display: inline-block; margin: 0 auto;">
                        </td>

                    </tr>
                </tbody>
            </table>
        </header>

        <main>
            <div class="main-content">
                <p class="font-bold mb-10">Welcome to IzzyAI – Your Speech Guardian!</p>
                <p class="mb-10">You’re just one step away from starting your journey with IzzyAI.</p>
                <p class="mb-10">
                    <span class="font-bold">Your OTP Code:</span>
                    <span class="otp ">{otp_code}</span>
                </p>
                <p class="mb-10">Click below to verify your email address and to activate your 7-day Free Trial.</p>
                <p class="mb-20">Your 7-day free trial is your gateway to personalized AI-powered speech therapy with
                    exclusive features and tools. Once your trial ends, your subscription will automatically
                    convert to IzzyAI Unlimited [Monthly] so you can continue your progress without
                    interruption.</p>
                <button class="mb-10" onclick="location.href={verification_link};">Verify</button>
                <p class="font-bold mb-10">Want to Save More?</p>
                <p class="mb-5">You’ll also have the option to switch to our Annual Plan, which oers the best value and
                    signicant savings. If you choose to switch, your annual subscription will begin at the
                    start of your next billing cycle.</p>
                <p class="mb-10">Thank you for choosing IzzyAI to guide your journey to condent speech!</p>
                <p class="font-bold mb-10">The IzzyAI Team</p>
                <p>[Please note: This is an automated message. Do not reply directly to this email]</p>
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
# Specific email functions


def send_verification_email(recipient_email, otp_code, verification_link):
    subject = "Your Journey with IzzyAI Speech Guardian Awaits - Verify Now!"
    body = body_of_send_verification_email(otp_code, verification_link)
    send_email(recipient_email, subject, body)

# send_verification_email(email,11111,"https://google.com")


def body_of_send_welcome_email(first_name):
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

        .otp {{
            margin-top: 10px;
            font-size: 30px;
            font-weight: 600;
            letter-spacing: 15px;
            color: #ba3d4f;
            margin-bottom: 10px;
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

        .mb-10 {{
            margin-bottom: 10px;
        }}

        .mb-5 {{
            margin-bottom: 5px;
        }}

        .mb-4 {{
            margin-bottom: 4px;
        }}

        .mb-3 {{
            margin-bottom: 3px;
        }}

        .mb-6 {{
            margin-bottom: 6px;
        }}

        .mb-12 {{
            margin-bottom: 12px;
        }}

        .mb-15 {{
            margin-bottom: 15px;
        }}

        .mb-20 {{
            margin-bottom: 20px;
        }}

        .link-color {{
            color: #638df8;
        }}

        .font-bold {{
            font-weight: bold;
        }}

        .text-center {{
            text-align: center;
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

        button {{
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }}

        button:hover {{
            background-color: #45a049;
        }}
    </style>
</head>

<body>
    <div class="container">
        <header>
            <table style="width: 100%;">
                <tbody>
                    <tr>
                        <td style="height: 140px; text-align: center;">
                            <img src="http://drive.google.com/uc?export=view&id=1R3OimiqIpRrTy3j2qsmdhGHsOT2ErpqP"
                                alt="logo" title="IzzyAI Logo" width="50%" height="100px"
                                style="display: inline-block; margin: 0 auto;">
                        </td>

                    </tr>
                </tbody>
            </table>
        </header>

        <main>
            <div class="main-content">
                <p class="mb-5 font-bold">Hi {first_name},</p>
                <p class="mb-10">We’re so excited to have you on board! Your 7-day Free Trial has ocially started, and
                    your Speech Guardian is ready to help you shine.</p>

                <ul>
                    <li>
                        <p class="mb-10">Personalized therapy sessions tailored to your needs and goals</p>
                    </li>
                    <li>
                        <p class="mb-10">AI powered exercises to improve your communication skills.</p>
                    </li>
                    <li>
                        <p class="mb-10">Daily access to your Speech Guardian—always there when you need them.</p>
                    </li>
                </ul>
                <p class="mb-20">Ready to get started? Dive in now to start working towards condent speech:</p>

                <p class="font-bold mb-5">Finish Setting Up Your Prole & Start Exploring</p>
                <p>To help you get started, we’ve included a helpful Instructional Guide that explains how
                    to eectively use IzzyAI and make the most of its features. </p>
                <p class="mb-10">Thanks,</p>
                <p class="mb-10">The IzzyAI Team</p>
                <p class="mb-10">P.S. Unlock unlimited access to all IzzyAI features and enjoy 24/7 availability to
                    AI-powered therapy by subscribing to the IzzyAI Unlimited plan today!</p>
                <p>[Please note: This is an automated message. Do not reply directly to this email]</p>
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


def send_welcome_email(recipient_email, first_name):
    subject = "Welcome to IzzyAI - Your Speech Guardian!"
    body = body_of_send_welcome_email(first_name)
    send_email(recipient_email, subject, body)


def body_of_send_mid_week_email(first_name):
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

        .otp {{
            margin-top: 10px;
            font-size: 30px;
            font-weight: 600;
            letter-spacing: 15px;
            color: #ba3d4f;
            margin-bottom: 10px;
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

        .mb-10 {{
            margin-bottom: 10px;
        }}

        .mb-5 {{
            margin-bottom: 5px;
        }}

        .mb-4 {{
            margin-bottom: 4px;
        }}

        .mb-3 {{
            margin-bottom: 3px;
        }}

        .mb-6 {{
            margin-bottom: 6px;
        }}

        .mb-12 {{
            margin-bottom: 12px;
        }}

        .mb-15 {{
            margin-bottom: 15px;
        }}

        .mb-20 {{
            margin-bottom: 20px;
        }}

        .link-color {{
            color: #638df8;
        }}

        .font-bold {{
            font-weight: bold;
        }}

        .text-center {{
            text-align: center;
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

        button {{
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }}

        button:hover {{
            background-color: #45a049;
        }}

    </style>
</head>

<body>
    <div class="container">
        <header>
            <table style="width: 100%;">
                <tbody>
                    <tr>
                        <td style="height: 140px; text-align: center;">
                            <img src="http://drive.google.com/uc?export=view&id=1R3OimiqIpRrTy3j2qsmdhGHsOT2ErpqP"
                                alt="logo" title="IzzyAI Logo" width="50%" height="100px"
                                style="display: inline-block; margin: 0 auto;">
                        </td>

                    </tr>
                </tbody>
            </table>
        </header>

        <main>
            <div class="main-content">
                <p class="mb-5">Hi <span class="font-bold">{first_name}</span>,</p>
                <p class="mb-10">We hope you’re loving your time with IzzyAI! You’re halfway through your 7-day free trial,
                    and there’s still so much to discover.</p>
                <ul>
                    <li>
                        <p class="mb-10">Personalized AI powered therapy sessions to target your speech language needs</p>
                    </li>
                    <li>
                        <p class="mb-10">Interactive Games to enhance your progress</p>
                    </li>
                    <li>
                        <p class="mb-10">Guidance tailored to your goals through real-time conversations with IzzyAI
                            chatbot - available anytime you need it!</p>
                    </li>
                </ul>
                <p class="mb-20">Remember, your Speech Guardian is here to guide you every step of the way. Don’t miss
                    out on these powerful AI tools to elevate your therapy experience.</p>
                <p class="mb-10">Keep up the amazing progress,</p>
                <p class="mb-10 font-bold">The IzzyAI Team</p>
                <p class="font-bold">[Please note: This is an automated message. Do not reply directly to this email]</p>
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


def send_mid_week_email(recipient_email, first_name):
    subject = "How’s Your Journey with IzzyAI, Your Speech Guardian?"
    body = body_of_send_mid_week_email(first_name)
    send_email(recipient_email, subject, body)
# send_mid_week_email(email,"prasad")


def body_of_send_subscription_start_email(first_name):
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

        .otp {{
            margin-top: 10px;
            font-size: 30px;
            font-weight: 600;
            letter-spacing: 15px;
            color: #ba3d4f;
            margin-bottom: 10px;
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

        .mb-10 {{
            margin-bottom: 10px;
        }}

        .mb-5 {{
            margin-bottom: 5px;
        }}

        .mb-4 {{
            margin-bottom: 4px;
        }}

        .mb-3 {{
            margin-bottom: 3px;
        }}

        .mb-6 {{
            margin-bottom: 6px;
        }}

        .mb-12 {{
            margin-bottom: 12px;
        }}

        .mb-15 {{
            margin-bottom: 15px;
        }}

        .mb-20 {{
            margin-bottom: 20px;
        }}

        .link-color {{
            color: #638df8;
        }}

        .font-bold {{
            font-weight: bold;
        }}

        .text-center {{
            text-align: center;
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

        button {{
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }}

        button:hover {{
            background-color: #45a049;
        }}
    </style>
</head>

<body>
    <div class="container">
        <header>
            <table style="width: 100%;">
                <tbody>
                    <tr>
                        <td style="height: 140px; text-align: center;">
                            <img src="http://drive.google.com/uc?export=view&id=1R3OimiqIpRrTy3j2qsmdhGHsOT2ErpqP"
                                alt="logo" title="IzzyAI Logo" width="50%" height="100px"
                                style="display: inline-block; margin: 0 auto;">
                        </td>

                    </tr>
                </tbody>
            </table>
        </header>

        <main>
            <div class="main-content">
                <p class="mb-5">Hi <span class="font-bold">{first_name}</span>,</p>
                <p class="mb-10">Congratulations—your <span class="font-bold">Monthly Unlimited subscription</span> has
                    ocially started! We’re
                    thrilled to have you continue your journey with IzzyAI, with full access to all the tools and
                    support you need to achieve your goals.</p>

                <p class="mb-5 font-bold">Here’s what’s unlocked for you in Unlimited:</p>
                <ul>
                    <li>
                        <p class="mb-10"><span class="font-bold">Unlimited Access to All AI Therapy Features:</span>
                            Your Speech Guardian, available
                            24/7, oering personalized support and guidance.</p>
                    </li>
                    <li>
                        <p class="mb-10"><span class="font-bold">Personalized Insights and Tailored Progress
                                Tracking:</span> Track your growth with
                            advanced insights and tools designed just for you.</p>
                    </li>
                    <li>
                        <p class="mb-10"><span class="font-bold">Interactive Therapy Games: </span> Fun, engaging
                            exercises to help you support your
                            growth and stay motivated.</p>
                    </li>
                    <li>
                        <p class="mb-10"><span class="font-bold">Exclusive Premium Features: </span> Priority support,
                            AI-guided exercises, and more to
                            accelerate your progress.</p>
                    </li>
                </ul>
                <p class="mb-10 font-bold">Want to switch to Annual?</p>
                <p>You can upgrade to an <span class="font-bold">Annual IzzyAI Unlimited subscription</span> and enjoy
                    greater savings
                    (over a massive 50%)! If you switch to annual, your plan will begin at the start of your next
                    billing cycle.</p>

                <a href="https://izzyai.com/account" style="color:  #638df8; text-decoration: underline;" target="_blank">Manage My Subscription</a>.

                <p class="mb-10">We’re excited to keep supporting you on your journey to condent communication. Let’s
                    make amazing progress together!</p>
                <p class="mb-3 font-bold">Warmly,</p>
                <p class="mb-10 font-bold">The IzzyAI Team</p>
                <p class="font-bold">[Please note: This is an automated message. Do not reply directly to this email]
                </p>
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


def send_subscription_start_email(recipient_email, first_name):
    subject = "Welcome to IzzyAI Unlimited! Your Journey with Your Speech Guardian Just Got Better"
    body = body_of_send_subscription_start_email(first_name)
    send_email(recipient_email, subject, body)


def body_send_cancellation_email(first_name):
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

        .otp {{
            margin-top: 10px;
            font-size: 30px;
            font-weight: 600;
            letter-spacing: 15px;
            color: #ba3d4f;
            margin-bottom: 10px;
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

        .mb-10 {{
            margin-bottom: 10px;
        }}

        .mb-5 {{
            margin-bottom: 5px;
        }}

        .mb-4 {{
            margin-bottom: 4px;
        }}

        .mb-3 {{
            margin-bottom: 3px;
        }}

        .mb-6 {{
            margin-bottom: 6px;
        }}

        .mb-12 {{
            margin-bottom: 12px;
        }}

        .mb-15 {{
            margin-bottom: 15px;
        }}

        .mb-20 {{
            margin-bottom: 20px;
        }}

        .link-color {{
            color: #638df8;
        }}

        .font-bold {{
            font-weight: bold;
        }}

        .text-center {{
            text-align: center;
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

        button {{
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }}

        button:hover {{
            background-color: #45a049;
        }}
    </style>
</head>

<body>
    <div class="container">
        <header>
            <table style="width: 100%;">
                <tbody>
                    <tr>
                        <td style="height: 140px; text-align: center;">
                            <img src="http://drive.google.com/uc?export=view&id=1R3OimiqIpRrTy3j2qsmdhGHsOT2ErpqP"
                                alt="logo" title="IzzyAI Logo" width="50%" height="100px"
                                style="display: inline-block; margin: 0 auto;">
                        </td>

                    </tr>
                </tbody>
            </table>
        </header>

        <main>
                        <div class="main-content">
                <p class="mb-5">Hi <span class="font-bold">{first_name}</span>,</p>
                <p class="mb-10">We noticed you decided to cancel your Unlimited subscription, and we’re truly sorry to see
                    you go. Your Speech Guardian has been cheering you on every step of the way, and we’d
                    love the chance to continue supporting you on your journey to condent communication.</p>

                <p class="mb-5 font-bold">Here’s What You’ll Miss in IzzyAI Unlimited:</p>
                <ul>
                    <li>
                        <p class="mb-10"><span class="font-bold">Unlimited Access to All AI Therapy Features:</span> Your Speech Guardian, available
                            24/7, oering personalized support and guidance.</p>
                    </li>
                    <li>
                        <p class="mb-10"><span class="font-bold">Personalized Insights and Tailored Progress Tracking:</span> Track your growth with
                            advanced insights and tools designed just for you.</p>
                    </li>
                    <li>
                        <p class="mb-10"><span class="font-bold">Interactive Therapy Games: </span> Fun, engaging exercises to help you support your
                            growth and stay motivated.</p>
                    </li>
                    <li>
                        <p class="mb-10"><span class="font-bold">Exclusive Premium Features: </span> Priority support, AI-guided exercises, and more to
                            accelerate your progress.</p>
                    </li>
                </ul>
                <p class="mb-10">We don’t want you to lose the progress you’ve already made <a href="https://izzyai.com/pricing" class="color: #638df8; text-decoration: none;">Re-Subscribe Now</a></p>

                <p class="mb-10">Your growth matters to us, and we’d be thrilled to help you achieve your communication
                    goals. Let’s pick up right where you left o—your Speech Guardian is ready to support
                    you.</p>
                <p class="mb-3 font-bold">Warmly,</p>
                <p class="mb-10 font-bold">The IzzyAI Team</p>

                <p class="font-bold">[Please note: This is an automated message. Do not reply directly to this email]</p>
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


def send_cancellation_email(recipient_email, first_name):
    subject = "We’re Sorry to See You Go - Your Journey with IzzyAI Awaits"
    body = body_send_cancellation_email(first_name)
    send_email(recipient_email, subject, body)


def body_of_send_payment_issue_email(first_name):
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

        .otp {{
            margin-top: 10px;
            font-size: 30px;
            font-weight: 600;
            letter-spacing: 15px;
            color: #ba3d4f;
            margin-bottom: 10px;
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

        .mb-10 {{
            margin-bottom: 10px;
        }}

        .mb-5 {{
            margin-bottom: 5px;
        }}

        .mb-4 {{
            margin-bottom: 4px;
        }}

        .mb-3 {{
            margin-bottom: 3px;
        }}

        .mb-6 {{
            margin-bottom: 6px;
        }}

        .mb-12 {{
            margin-bottom: 12px;
        }}

        .mb-15 {{
            margin-bottom: 15px;
        }}

        .mb-20 {{
            margin-bottom: 20px;
        }}

        .link-color {{
            color: #638df8;
        }}

        .font-bold {{
            font-weight: bold;
        }}

        .text-center {{
            text-align: center;
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

        button {{
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }}

        button:hover {{
            background-color: #45a049;
        }}
    </style>
</head>

<body>
    <div class="container">
        <header>
            <table style="width: 100%;">
                <tbody>
                    <tr>
                        <td style="height: 140px; text-align: center;">
                            <img src="http://drive.google.com/uc?export=view&id=1R3OimiqIpRrTy3j2qsmdhGHsOT2ErpqP"
                                alt="logo" title="IzzyAI Logo" width="50%" height="100px"
                                style="display: inline-block; margin: 0 auto;">
                        </td>

                    </tr>
                </tbody>
            </table>
        </header>

        <main>
            <div class="main-content">
                <p class="mb-5">Hi <span class="font-bold">{first_name}</span>,</p>
                <p class="mb-10">We tried to process your payment for your IzzyAI Unlimited subscription, but
                    unfortunately, it didn’t go through. Don’t worry—your Speech Guardian is waiting to
                    support you, and we’re here to help resolve the issue quickly.</p>
                <p class="mb-5">What to Do Next:</p>
                <ul>
                    <li>
                        <p class="mb-10">Check that your payment details are up to date</p>
                    </li>
                    <li>
                        <p class="mb-10">Update your payment method to ensure uninterrupted access to all your Unlimited
                            features.</p>
                    </li>
                </ul>
                <a class="" style="color: #638df8;" href="https://izzyai.com/account/subscription">Update My Payment Details</a>
                <p class="mb-3" style="margin-top: 15px;">What Happens If It’s Not Fixed?</p>
                <p class="mb-10">If we’re unable to process your payment, your subscription will automatically move to
                    IzzyAI Basic on [Insert Date]. You’ll still have access to basic features, but Unlimited
                    benets like 24/7 access to your AI therapist, personalized tools, and progress tracking
                    will no longer be available.</p>
                <p class="mb-10">We’d hate for you to lose all the progress you’ve made so far. Let’s get your subscription
                    back on track today!</p>
                <!-- <p class="mb-10 font-bold">[Fix My Payment Now]</p> -->
                <p class="mb-3 font-bold">Warmly,</p>
                <p class="mb-10 font-bold">The IzzyAI Team</p>
                <p class="font-bold">[Please note: This is an automated message. Do not reply directly to this email]</p>
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


def send_payment_issue_email(recipient_email, first_name):
    subject = "There’s an Issue with Your Payment for IzzyAI"
    body = body_of_send_payment_issue_email(first_name)
    send_email(recipient_email, subject, body)
# send_payment_issue_email(email,"prasad")


def body_of_send_upgrade_reminder_email(first_name):
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

        .otp {{
            margin-top: 10px;
            font-size: 30px;
            font-weight: 600;
            letter-spacing: 15px;
            color: #ba3d4f;
            margin-bottom: 10px;
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

        .mb-10 {{
            margin-bottom: 10px;
        }}

        .mb-5 {{
            margin-bottom: 5px;
        }}

        .mb-4 {{
            margin-bottom: 4px;
        }}

        .mb-3 {{
            margin-bottom: 3px;
        }}

        .mb-6 {{
            margin-bottom: 6px;
        }}

        .mb-12 {{
            margin-bottom: 12px;
        }}

        .mb-15 {{
            margin-bottom: 15px;
        }}

        .mb-20 {{
            margin-bottom: 20px;
        }}

        .link-color {{
            color: #638df8;
        }}

        .font-bold {{
            font-weight: bold;
        }}

        .text-center {{
            text-align: center;
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

        button {{
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }}

        button:hover {{
            background-color: #45a049;
        }}

    </style>
</head>

<body>
    <div class="container">
        <header>
            <table style="width: 100%;">
                <tbody>
                    <tr>
                        <td style="height: 140px; text-align: center;">
                            <img src="http://drive.google.com/uc?export=view&id=1R3OimiqIpRrTy3j2qsmdhGHsOT2ErpqP"
                                alt="logo" title="IzzyAI Logo" width="50%" height="100px"
                                style="display: inline-block; margin: 0 auto;">
                        </td>

                    </tr>
                </tbody>
            </table>
        </header>

        <main>
            <div class="main-content">
                <p class="mb-5">Hi <span class="font-bold">{first_name}</span>,</p>
                <p class="mb-10">We noticed you’ve been using the Basic version of IzzyAI, and while we’re thrilled you’ve
                    explored our Assessment, there’s so much more waiting for you in Unlimited!</p>

                <p class="mb-5 font-bold">Here’s What You’ll Unlock in IzzyAI Unlimited:</p>
                <ul>
                    <li>
                        <p class="mb-10"><span class="font-bold">Unlimited Access to All AI Therapy Features: </span> Your Speech Guardian, available
                            24/7, oering personalized support and guidance.</p>
                    </li>
                    <li>
                        <p class="mb-10"><span class="font-bold">Personalized Insights and Tailored Progress Tracking:</span> Track your growth with
                            advanced insights and tools designed just for you.</p>
                    </li>
                    <li>
                        <p class="mb-10"><span class="font-bold">Interactive Therapy Games: </span> Fun, engaging exercises to help you support your
                            growth and stay motivated.</p>
                    </li>
                    <li>
                        <p class="mb-10"><span class="font-bold">Exclusive Premium Features: </span> Priority support, AI-guided exercises, and more to
                            accelerate your progress.</p>
                    </li>
                </ul>
                <a class="mb-10 font-bold" href="https://izzyai.com/pricing" target="_blank">Upgrade to Unlimited</a>
                <p class="mb-3" style="margin-top: 10px;">What Happens If It’s Not Fixed?</p>
                <p class="mb-10">Your Speech Guardian is ready to pick up right where you left o and help you achieve
                    your speech therapy goals. Don’t wait to unlock the full potential of IzzyAI Unlimited.</p>
                <p class="mb-3 font-bold">Warmly,</p>
                <p class="mb-10 font-bold">The IzzyAI Team</p>

                <p class="font-bold">[Please note: This is an automated message. Do not reply directly to this email]</p>
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


def send_upgrade_reminder_email(recipient_email, first_name):
    subject = "Discover What You’re Missing with IzzyAI Unlimited"
    body = body_of_send_upgrade_reminder_email(first_name)
    send_email(recipient_email, subject, body)
# send_upgrade_reminder_email(email,"prasad")
