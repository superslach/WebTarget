import os
import bs4 as BeautifulSoup
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def read_file(fichier):
    file = open(fichier, "r")
    lecture = file.read()
    file.close()
    return lecture


def write_file(fichier, ecrit):
    file = open(fichier, "a")
    file.write(ecrit)
    file.close()


def verif_email(mail):
    try:
        split = mail.split("@")
        split2 = split[1].split(".")
        split3 = split2[1]
    except:
        return False
    else:
        if "." and "@" in mail and len(split3) <= 3:
            return True
        else:
            return False


def verif_url(url):
    if url.startswith("http://") or url.startswith("https://"):
        return True
    else:
        return False


def domaine_email(mail):
    if verif_email(mail):
        domaine = mail.split("@")
        return domaine[1]
    return None


def supp_doublon(liste):
    return list(set(liste))


def supp_elmt(liste,element):
    liste.remove(element)
    return liste


def ping(lien):
    response = os.system("ping " + lien)
    if response == 0:
        return True
    else:
        return False


def crawl(lien):
    response = requests.get(lien)
    soup = BeautifulSoup.BeautifulSoup(response.content, 'html.parser')
    links = [a["href"] for a in soup.select("a[href^=mailto:]")]
    mails = []
    for link in links:
        mails.append(link.split(':')[1])
    return mails


def envoi_mail(exp,dest, obj, message, pwd):
    msg = MIMEMultipart()
    msg['From'] = exp
    msg['To'] = dest
    msg['Subject'] = obj
    messag = message
    msg.attach(MIMEText(messag))
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login(exp, '..Ch@ritha0308..')
    mailserver.sendmail(exp, dest, msg.as_string())
    mailserver.quit()