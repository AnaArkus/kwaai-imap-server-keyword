# Importing libraries
import imaplib
import email
import yaml  

with open("credentials.yml") as f:
    content = f.read()
    

credentials = yaml.load(content,Loader=yaml.FullLoader) 

user, password = credentials["user"], credentials["password"]

imap_url = 'imap.gmail.com'

mail = imaplib.IMAP4_SSL(imap_url)

mail.login(user, password)

mail.select('Inbox')

#For other keys (criteria): https://gist.github.com/martinrusev/6121028#file-imap-search
key = 'FROM'
value = 'noreply@medium.com'
_, data = mail.search(None, key, value)

mail_id_list = data[0].split()

msgs = []

#Iterate through messages and extract data into the msgs list
for num in mail_id_list:
    typ, data = mail.fetch(num, '(RFC822)') #RFC822 returns whole message
    msgs.append(data)

# Message object consists of headers and payloads
for msg in msgs[::-1]:
    for response_part in msg:
        if type(response_part) is tuple:
            my_msg=email.message_from_bytes((response_part[1]))
            print("_________________________________________")
            print ("subj:", my_msg['subject'])
            print ("from:", my_msg['from'])
            print ("body:")
            for part in my_msg.walk():  
                if part.get_content_type() == 'text/plain':
                    print (part.get_payload())