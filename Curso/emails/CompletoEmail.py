#! /usr/bin/env python3
import imaplib
import email

EMAIL_ACCOUNT="jimvillarene@gmail.com"
EMAIL_KEY="zhxeuvmgjfevhpsp"

################ IMAP SSL ##############################

with imaplib.IMAP4_SSL(host="imap.gmail.com", port=imaplib.IMAP4_SSL_PORT) as imap_ssl:
    print("Connection Object : {}".format(imap_ssl))

    ############### Login to Mailbox ######################
    print("Logging into mailbox...")
    resp_code, response = imap_ssl.login(EMAIL_ACCOUNT, EMAIL_KEY)

    print("Response Code : {}".format(resp_code))
    print("Response      : {}\n".format(response[0].decode()))

    ############### Set Mailbox #############
    resp_code, mail_count = imap_ssl.select(mailbox="INBOX", readonly=True)

    ############### Retrieve Mail IDs for given Directory #############   
    resp_code, mail_ids = imap_ssl.search(None, "SINCE 01-AUG-2023")

    print("Mail IDs : {}\n".format(mail_ids[0].decode().split()))

    ############### Display Few Messages for given Directory #############
    for mail_id in mail_ids[0].decode().split()[-2:]:
        print("================== Start of Mail [{}] ====================".format(mail_id))

        resp_code, mail_data = imap_ssl.fetch(mail_id, '(RFC822)') ## Fetch mail data.

        message = email.message_from_bytes(mail_data[0][1]) ## Construct Message from mail data
        print("From       : {}".format(message.get("From")))
        print("To         : {}".format(message.get("To")))
        print("Bcc        : {}".format(message.get("Bcc")))
        print("Date       : {}".format(message.get("Date")))
        print("Subject    : {}".format(message.get("Subject")))

        print("Body : ")
        for part in message.walk():
            if part.get_content_type() == "text/plain":
                body_lines = part.as_string().split("\n")
                print("\n".join(body_lines[:12])) ### Print first 12 lines of message

        print("================== End of Mail [{}] ====================\n".format(mail_id))

    ############# Close Selected Mailbox #######################
    imap_ssl.close()