#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import random
import smtplib
import xlsxwriter
from easygui import *
from datetime import datetime

from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

msg_s ="Doğruları mı daha iyi hatırlayacağınızı düşünüyorsunuz yalanları mı?"
title_s = " "
choices = ["Doğruları", "Yalanları"]

workbook = None
row = 0
column = 0

start_time = 0

SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = '587'
SMTP_USER = 'tugcegurbuzodevhesabi@gmail.com'
SMTP_PASSWORD = 'Yc3YZPNPXD2G'


#------------------ENCODING QUESTIONS----------------------------------------------------------------------
qDict = {"Suçlular yürüy___rek içeri girdiler.": "Yalan: ",
		"Suç bank___da işlendi": "Doğru: ",
                "Suçlu bilgis___rı devirdi.": "Doğru: ",
                "Suçlular hayv___n kostümü giyinmişlerdi.": "Yalan: ",
                "Suç bir müz___de işlendi.": "Yalan: ",
                "Suçlular çalışanlara vu___du.": "Doğru: ",
                "Suçlular sil___h taşıyordu.": "Doğru",
                "Suçlular girince banka çalışanları sand___lye oturdu.": "Yalan: ",
                "Suçlular banka çalışanlarının cep te___unu topladı.": "Doğru",
                "Suçlular banka çalışanlarının cep telefonunu bir çuv__a koydu.": "Yalan: ",
                "Suç sabah erk___n saatte işlendi.": "Doğru: ",
                "Suçlular yaşlı ad__mı kasayı açması için zorladı.": "Yalan: ",
                "Suç saat  ____  civarında işlendi.": "Yalan: ",
                "Kasayı açması için zorlanan kadın kasayı il___ deneyişinde açamadı.": "Doğru: ",
                "Suçluların kasayı açması için zorladıkları kadın saç rengi sar___ydı.": "Yalan: ",
                "Suçlular güven___k kamerası kayıtlarını aldılar.": "Doğru: ",
                "Suçlular güvenlik kamerası kayıtlarını çakm___ ile yaktılar.": "Yalan: ",
                "Suçlular bıç___k taşıyordu.": "Yalan: ",
                "Suçlular si___ah kapişonlu bir kıyafet giyiyordu.": "Doğru: ",
                "Suçlular kurukafalı mas___e takıyordu.": "Doğru: ",
                "Suçlular bankadan ayrılırken etrafa ben___in döktüler.": "Doğru: ",
                "Suçlu yaşlı kadının kafa___a silah ile vurdu.": "Yalan: ",
                "Suçlulardan birinin boyn___a dövme vardı.": "Doğru: ",
                "Suçlular bir ada__ı rehin aldı.": "Yalan: ",
                "Suçluların cinsiyeti erk___.": "Doğru: ",
                "Suçlular bey___z bir arabayla kaçtı.": "Yalan: ",
                "Suçlular büy__k bir arabaya bindiler.": "Doğru: ",
                "Suçlular esir aldıkları kadını serbe___t bıraktılar.": "Yalan: ",
                "Suçlular esir aldıkları kadının ell___i bağladı.": "Doğru: ",
                "Suçlular benzin döktükten sonra bankayı y___ktı.": "Yalan: "}
#----------------------------------------------------------------------------------------------------

#---------------------------DISTRACTION TASK QUESTIONS-----------------------------------------------
questionList = ["1 + 5 + 7 = ",
                "8 + 4 + 3 = ",
                "2 + 5 + 9 = ",
                "1 x 5 + 2 = ",
                "2 + 5 x 4 = ",
                "1 + 25 x 6 = ",
                "8 - 5 + 7 = ",
                "12 + 5 + 27 = ",
                "12 x 7 + 7 = ",
                "11 x 12 + 10 = ",
                "111 + 28 + 46 = ",
                "144 / 12 + 10 = ",
                "13 + 85 +79 = ",
                "168 / 2 x 2 = ",
                "134 + 63 / 7 = ",
                "123 + 856 + 17 = ",
                "10 x 5 x 7 = ",
                "12 x 13 + 21 = ",
                "341 + 235 + 70 = ",
                "44 + 55 + 33 = ",
                "67 - 5 - 34 = ",
                "14 x 15 + 205 - 107 = ",
                "231 + 5675 + 457 = ",
                "778 - 655 + 34 = ",
                "23 x 6 + 250 / 2 = ",
                "166 + 585 - 87 + 5 x 9 = ",
                "123 - 65 + 85 + 345 = ",
                "33 x 8 - 29 = ",
                "177 - 69 / 3 = ",
                "199 + 235 + 105 = ",
                "166 + 435 + 6 x 7 = ",
                "274 - 575 + 50 = ",
                "143 / 11 + 34 = ",
                "114 - 57 x 3 = ",
                "1889 + 4345 + 1110 = ",
                "456 x 5 + 56 = ",
                "12 + 53 x 7 = ",
                "166 + 5888 + 799 = ",
                "145 - 345 + 77 = ",
                "13432 - 235 + 67 = ",
                "145 / 5 + 47 = ",
                "123 + 455 - 577 = "]
#------------------------------------------------------------------------------------------------------

#-----------------------------------FUNCTIONS----------------------------------------------------------
def create_survey():
        global msg_s
        global title_s
        global choices
        global choice
        random.shuffle(choices)
        choice = choicebox(msg_s, title_s, choices)


def open_output_file(name):
	global workbook

	workbook = xlsxwriter.Workbook(name)
	worksheet = workbook.add_worksheet("result")
	worksheet.write(row, column, 'Survey Answer')
	next_column()
	worksheet.write(row, column, 'Questions')
	worksheet.set_column(row, column, 50)
	next_column()
	worksheet.write(row, column, 'Answers')
	next_column()
	worksheet.write(row, column, 'JoL Rates')
	next_column()
	worksheet.write(row, column, 'Test Answers')

	next_row()
	return worksheet


def next_row():
	global column
	global row

	column = 0
	row += 1


def next_column():
	global column
	column += 1


def close_output_file():
	global workbook
	workbook.close()

	
def time_delta():
        delta = datetime.now() - start_time
        return delta.total_seconds()


def create_ccbox(title, msg):
        if ccbox(msg, title, ("Devam et", "İptal")):
            pass
        else:
            sys.exit(0)

def prepareAttachment(fpath):
    '''
        The function helps to prepare any file for the email attachment.
        It encodes the file to base64 as an email attachment required.
    '''
    fname = os.path.basename(fpath)
    attachment = open(fpath, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % fname)

    return part

def sendFileByEmail(toaddr, title, body, filepath):
    '''
        The file helps to send a file to any address using email.
        Title will be the title of the email.
        Body will be the main text of the email.
        FilePath will be attached to the email.
        Then function returns the result if the email sent properly or not.
    '''
    msg = MIMEMultipart()

    msg['From'] = SMTP_USER
    msg['To'] = toaddr
    msg['Subject'] = title

    msg.attach(MIMEText(body, 'plain'))
    msg.attach(prepareAttachment(filepath))

    server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
    res = server.starttls()
    if res[0] != 220:
        return False

    res = server.login(SMTP_USER, SMTP_PASSWORD)
    if res[0] != 235:
        return False

    res = server.sendmail(SMTP_USER, toaddr, msg.as_string())
    if res != {}:
        return False

    res = server.quit()
    if res[0] != 221:
        return False

    return True

def play_video(path):
        try:
                os.startfile(path)
                time.sleep(288)
                return True
        except:
                return False


#---------------------------------------------------------------------------------------------------

if __name__ == '__main__':
	#get information of the participant
	ID = input("Lutfen size verilen katilimci numarasini giriniz: ") #kutu

	#save this ID to excel
	worksheet = open_output_file(ID + '.xlsx')

	create_survey()
	worksheet.write(row, column, choice)

	items = list(qDict.items())
	random.shuffle(items)

	play_video("video.mp4")

	for q, value in items:
			msgbox(value)
			question = (value, q)

			answer = enterbox(question, " ")
			next_column()
			worksheet.write(row, column, "{} : {}".format(value, q))
			next_column()
			worksheet.write(row, column, answer)

			JoL = 0
			while JoL not in range(1,6):
					try:
							JoL = int(enterbox('''Bunu ne kadar iyi hatırlayacağınızı düşünüyorsunuz?
							         (1:hiç hatırlayamam, 
							2:biraz hatırlayabilirim,
							3:hatırlayabilirim, 
							4:kolayca hatırlayabilirim, 5:çok kolayca hatırlayabilirim): ''', " "))
							break
					except:
							pass
							

			next_column()
			worksheet.write(row, column, JoL)
			next_row()
	

	

	msg = "Tebrikler, çalışmanın ilk kısmını tamamladınız! İkinci kısıma geçmek için lütfen 'Devam et' seçeneğine tıklayınız."
	title = "Tebrikler"
	create_ccbox(title, msg)

	msg = '''Çalışmanın bu kısmında, 3 dakika boyunca ekranda gösterilen matematik problemlerinin cevaplarını
doğru bir şekilde yazmanız beklenmektedir. Devam etmek için 'Devam et' seçeneğine tıklayınız.'''
	title = "İkinci Bölüm"
	create_ccbox(title, msg)

	start_time = datetime.now()

	while time_delta() < 180:
			enterbox(random.choice(questionList), " ", "Cevap: ")

	

	msg = "Tebrikler, çalışmanın ikinci kısmını tamamladınız! Son kısıma geçmek için lütfen 'Devam et' seçeneğine tıklayınız."
	title = "Tebrikler"
	create_ccbox(title, msg)

	msg = '''Çalışmanın bu kısmında lütfen ekranda çıkan boş kutucuklara, 3 dakika içerisinde doldurduğunuz kelime boşlukları olan cümlelerden hatırlayabildiğiniz kelime boşluklarını ya da cümleleri yazınız.
Yazdığınız her cümleden/kelimeden sonra lütfen 'OK' tuşuna basıp diğer boşluğa geçiniz.'''
	title = "Son bölüm"
	create_ccbox(title, msg)

	start_time = datetime.now()
	row = 1
	

	while time_delta() < 180:
			test_answer = enterbox("Lütfen hatırladığınız cümleyi yazın. Hatırladıklarınızın bu kadar olduğunu düşünüyorsanız lütfen 0 (sıfır) a basınız.", " ")
			column = 4
			worksheet.write(row, column, test_answer)
			next_row()
			if test_answer == "0":
					break
			

	close_output_file()
	msg = "Tebrikler! Deneyi tamamladınız! Katkılarınız için çok teşekkür ederiz."
	title ="Tebrikler"
	create_ccbox(title, msg)


	d = sendFileByEmail('tugcegurbuz97@gmail.com', "ödev"," ", ID + '.xlsx')

if not d:
                msg = "Datanız bize mail olarak gelmedi, lütfen deneyi yürüten kişi ile iletişime geçin"
                create_ccbox("bir problem oluştu", msg)

