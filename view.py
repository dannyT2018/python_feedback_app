import smtplib
import subprocess
from email.mime.text import MIMEText

from django.http import HttpRequest, HttpResponse


def operate_on_twos(request: HttpRequest) -> HttpResponse:
    operator = request.GET["operator"]

    result = eval(f"2 {operator} 2")  # noqa: P204

    return result

    
def operate_on_threes(request: HttpRequest) -> HttpResponse:
    operator = request.GET["operator"]

    exec(f"result = 3 {operator} 3")

    return result  # noqa: F821


def operate_on_fours(request: HttpRequest) -> HttpResponse:
    operator = request.GET["operator"]

    result = subprocess.getoutput(f"expr 4 {operator} 4")

    return result


def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = ''
    password = ''
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
