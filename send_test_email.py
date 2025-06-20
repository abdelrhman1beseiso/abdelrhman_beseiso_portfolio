import os
import resend

resend.api_key = "re_T688dGfy_3pEBNwwsSaEobur8HxfRU6xL"

params: resend.Emails.SendParams = {
    "from": "Acme <onboarding@resend.dev>",
    "to": "abdelrhman.f.beseiso@gmail.com",
    "subject": "hello world",
    "html": "<strong>it works!</strong>",
}

email = resend.Emails.send(params)
print(email)