import yagmail
from datetime import datetime

def main():
    receiver = "test135634@gmail.com"
    body = "Attached to this email is a file some webscrapped content."
    now = datetime.today().date()
    filename = "Attachment 2021-01-13.txt"
    password = input("Enter your password: \n")

    yagmail.register(receiver, password)
    yag = yagmail.SMTP("test135634@gmail.com")
    yag.send(
        to=receiver,
        subject="WebScrape",
        contents=body, 
        attachments=filename,
    )

    yagmail.close


main()