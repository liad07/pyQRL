from downloads import download
basic="https://api.qrserver.com/v1/create-qr-code/?data="

def wifi():
    wifiname=input("enter name of wifi\n")
    wifipassword=input("enter password of wifi\n")
    download(f"{basic}WIFI:S:{wifiname};T:WPA;P:{wifipassword};;", out_path="qr.png")
    all=f"{basic}WIFI::S:{wifiname};T:WPA;P:{wifipassword};;"
    print(all)
def  mail():
    to=input('To who to send an email\n')
    subject=input('What is the subject of the email\n')
    body=input('What to write in the email\n')
    bl=f"{basic}mailto:{to}?subject={subject}&body={body}"
    download(bl, out_path="qr.png")
def tel():
    number=input('what the phone\n')
    download(f"{basic}tel:{number}", out_path="qr.png")
def whatsapp():
    number=input('what the phone\n')
    msg=input('what the message\n')
    download(f"{basic}https://wa.me/972{number}?text{msg}", out_path="qr.png")
def link():
    link=input('enter a link\n')
    download(f"{basic}{link}", out_path="qr.png")
def text():
    text=input('enter a text\n')
    download(f"{basic}{text}", out_path="qr.png")
def pyQRL(name):
    if name=="wifi":
        wifi()
    if name=="mail":
        mail()
    if name=="tel":
        tel()
    if name=="whatsapp":
        whatsapp()
    if name=="link":
        link()
    if name=="text":
        text()
