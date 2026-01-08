import smtplib, ssl
from email.message import EmailMessage
def saada_email(saaja_email):
    kiri="""Tere see on test https://github.com/kirillfedulin/Oleinik-Python-lesandeid/blob/master/email.py"""
    teema="Test e-kiri Pythonist"
    saatja_email="kirill.fedulin22@gmail.com"
    parool=input("Sisesta rakenduse parool: ") #mbec buaz lxco hkpk
    smtp_server="smtp.gmail.com"
    port=587 
    context=ssl.create_default_context()
    msg=EmailMessage()
    msg.set_content(kiri)
    msg["Subject"]=teema
    msg["From"]=saatja_email
    msg["To"]=saaja_email
    with open("image.png", "rb") as f:
        image_data = f.read()
    msg.add_attachment(image_data, maintype="image", subtype="png")
    try:
        with smtplib.SMTP(smtp_server,port) as server:
            server.starttls(context=context)
            server.login(saatja_email,parool)
            server.send_message(msg) 
    except Exception as e:
        print(f"Midagi läks valesti... {e}")

kellele=input("Sisesta saaja e-posti aadress: ")
saada_email(kellele)
