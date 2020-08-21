import os
import pyttsx3
"""
1. In 't' we are storing all true vale response.
2. In 'f' we are storing all true vale response.
3. In 'p' we are storing all the program names.
4. In 'c' we stored command respective to each program in 'p'.
5. To search any website write the name/url of the website with 'search' prefix: 
	EX: search facebook or search facebook.com
6. Made by Aditya Raj underguidence of IIEC Community BY Vimal Sir.
"""
user_name = input("Enter Your Name: ")
# TRUE
t = ["run","on","onn","opening","open","exicute","start"]
# FALSE
f = ["close","closing","terminate","off","exit","stop"]
# Response_List
response = ["opening","closing","text not recognized"]
#process name
p = ["chrome","browser","media","songs","video","player","text","editor","notepad","powerpoint","msword","wordpad","excel","msexcel"]
#command name
c = ["chrome","chrome","wmplayer","wmplayer","wmplayer","wmplayer","notepad","notepad","notepad","powerpnt","winword","wordpad","excel","excel"]
# Intro program
# Bot name variable
bot = "Jarvis"
print("{}: Type 'help' !".format(bot))
voice_activ = "false"
while(True):
	temp = "NULL"
	#storing user input
	user_input = input("\t\t\t\t\t{}: ".format(user_name))
	i = 0
	j = 0
	k = 0
# -------------------Special 'HELP' Command Codes-----------
	if(user_input == "help"):
		response = "may this helped you!"
		print("1. Type which program you want to open/close.")
		print("2. \"clear\" to clean the chat")
		print("3. \"exit\" to exit this program")
		print("4. To search any website write the name/url of the website with 'search' prefix->EX: search facebook.com")
		print("5. Type 'voice_set' to change Voice Settings.\n")
		if(voice_activ == "true"):
			pyttsx3.speak("here is the help list")
# clear command
	elif(user_input == "clear"):
		if(voice_activ =="true"):
			pyttsx3.speak("screen cleared")
		response = "screen cleared"
		os.system("cls")
# exit command
	elif(user_input in f):
			response = "ok bye!"
			exit()
# online URL search command
	elif("search" in user_input):
		os.system("start chrome {}".format(user_input[6:]))
		response = "opening: "+user_input[6:]
# Voice Command Setting Program
	elif(user_input == "voice_set"):
		while(True):
			print("1. Voice Change\n2. Voice ONN/OFF\n3. Exit this Menu")
			vset_opt = input("enter 1 or 2 or 3: ")
			if(vset_opt == "1"):
				print("1. Jarvis Voice\n2. Alexa Voice")
				vi = input("enter 1 or 2: ")
				engine = pyttsx3.init()
				voices = engine.getProperty('voices')
				if(vi == "1"):
					engine.setProperty('voice', voices[0].id)
					pyttsx3.speak("hello i am jarvis")
					bot = "Jarvis"
				elif(vi == "2"):
					engine.setProperty('voice', voices[1].id)
					pyttsx3.speak("hello i am alexa")
					bot = "Alexa"
				else:
					print("wrong input")
			elif(vset_opt == "2"):
				print("Type 'true' to ONN and 'false' to OFF: ",end="")
				#check if user have inputed some wrong value
				voice_input_error = input()
				if((voice_input_error == "true") or (voice_input_error == "false")):
					voice_activ = voice_input_error
					if(voice_activ == "true"):
						print("activated");
						pyttsx3.speak("activated")
					else:
						print("deactivated")
				else:
					print("Invalid input\nSetting not changed !!!!")
			elif(vset_opt == "3"):
				response = "Setting Saved"
				break
			else:
				print("Invalid Input !")
#-----------------General Commands Code-------------------
	else:
		while(i < len(p)):
			if(p[i] in user_input):
				response = "NULL"
				#program name stored in temp
				temp = p[i]
				while(j < len(t)):
					if(t[j] in user_input):
						response = "opening";
						break;
					j=j+1
				if(response != "opening"):
					while(k < len(f)):
						if(f[k] in user_input):
							response = "closing"
							break
						k=k+1
				break					
			else:
				response = "no program found !"
			i = i + 1;

# Final Command processing
	print("{}: ".format(bot),end="")
	if((response == "opening") or (response == "NULL")):
		print("opening"+" "+temp+" !")
		os.system("start {}".format(c[i]))
		if(voice_activ == "true"):
			pyttsx3.speak("opening {}".format(temp))
	elif(response == "closing"):
			print("closing"+" "+temp+" !")
# path of cache file in by default on 
			os.system("taskkill/im {}.exe -F > D:\cache_file".format(c[i]))
			if(voice_activ == "true"):
				pyttsx3.speak("closing {}".format(temp))
	else:
		print(response)
