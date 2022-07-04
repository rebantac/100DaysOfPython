import smtplib

my_email = "sendeer email"
password = "your password"
with smtplib.SMTP("smtp.gmail.com") as connection: # smtp info og gmail=> the service provider
    connection.starttls() # makes the connection secure
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="receiver email", msg="Sample text from python")
