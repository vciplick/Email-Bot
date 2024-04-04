import smtplib
from email.mime.text import MIMEText
import random
import click
import csv

subject = "Christmas Book Exchange 2023 Assignment"
start = "Hello "
body = "For the Christmas 2023 book exchange, you have been assigned: "
end = "Sincerely, \n Tori's email bot"
sender = "tciplickas@gmail.com"
##TODO: move app password to config
## old one deleted because im an idiot and commited it to a public repository for five minutes 
password = "---"

def get_names_emails(file):
    res = []
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            try:
                res.append((row[0].strip(),row[1].strip()))
            except:
                print("Warning: input file not parsing correctly! Exiting program!")
                print("problem line:", row)
                exit()
    return res

def send_email(subject, body, sender, recipient, password):

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipient, msg.as_string())
    print("Message sent!")

@click.command
@click.option('--input-file', '-f', help='file input containing comma separated [name,email]')
def assign_books(input_file): 
    if (input_file == None):
        print("Input file required! use --help for more info.")
        exit()

    people = get_names_emails(input_file)
    random.shuffle(people)
    n = len(people)
    for i in range(n):
        gifter_name, gifter_email = people[i]
        r_i = (i+1) % n
        recipient_name, _ = people[r_i]
        message = start + gifter_name + ",\n\n" + body + recipient_name + "\n\n" + end
        send_email(subject, message, sender, gifter_email, password)


if __name__=="__main__": 
    assign_books()