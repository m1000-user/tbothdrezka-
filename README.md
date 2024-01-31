# Telegram Bot MIRROR HDREZKA 

This my second project ; Telegram bot to get HDREZKA mirror

# What this can do? :3
Send new message to email hdrezka every 15 minutes

scrap the latest message on callback query and find hdrezka mirror

# Requirements
If u have gmail account , follow this steps:

-Go to settings and toggle 2FA
-Next go to https://myaccount.google.com/apppasswords and create the app
-Save and use APP PASSWORD in smtp and imap libs connection

-At 43 and 46 lines index are positions in message, and may to change.Follow next steps to found your:
-delete from 43 to 46 line , and write print(body.index('hdrezka'). Execute this and check print
-Your print may have two result. Use latest result and from this result plus 17. For example we have latest result are 599 , we write this code --> if 'hdrezka' not in body[599:616]: ...

- Before start download the requirements . Follow next steps:

- Open cmd or IDE with your project dir
- Type this command: 'pip install -r requirements.txt'
- Done!
- Thank for read this :3 If you have some corrections in code , type me
