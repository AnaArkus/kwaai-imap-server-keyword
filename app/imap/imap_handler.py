"""IMAP Handler"""

import imaplib
import email
from email.header import decode_header

class IMAPHandler:
    @classmethod
    def get_emails(cls, email_address, password, imap_server):
        """Get emails from IMAP server"""
        try:
            mail = imaplib.IMAP4_SSL(imap_server)
            mail.login(email_address, password)
            mail.select('inbox')

            status, messages = mail.search(None, 'ALL')
            email_ids = messages[0].split()

            emails = []
            for email_id in email_ids:
                status, msg_data = mail.fetch(email_id, '(RFC822)')
                raw_email = msg_data[0][1]
                msg = email.message_from_bytes(raw_email)

                subject, encoding = decode_header(msg['Subject'])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding or 'utf-8')

                emails.append({
                    'subject': subject,
                    'from': msg.get("From"),
                    'date': msg.get("Date")
                })

            mail.logout()

            return emails

        except Exception as e:
            raise Exception(f"Error en la conexión IMAP: {str(e)}")
