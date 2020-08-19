import os

"""
1. In 't' we are storing all true vale response.
2. In 'f' we are storing all true vale response.
3. In 'p' we are storing all the program names.
4. In 'c' we stored command respective to each program in 'p'.
5. To search any website write the name/url of the website with 'search' prefix: 
		EX: search facebook or search facebook.com
6. Made by Aditya Raj underguidence of IIEC Community BY Vimal Sir.
"""

# TRUE
t = ["run","on","onn","opening","open","exicute"]
# FALSE
f = ["close","closing","terminate","off","exit"]
# Response_List
response = ["opening","closing","text not recognized"]
#process name
p = ["chrome","browser","media","songs","video","player","text","editor","notepad","powerpoint","msword","wordpad","excel","msexcel"]
#command name
c = ["chrome","chrome","wmplayer","wmplayer","wmplayer","wmplayer","notepad","notepad","notepad","powerpnt","winword","wordpad","excel","excel"]
# Intro program
print("Jarvis: Type 'help' !")
while(True):
	temp = "NULL"
	#storing user input
	user_input = input("\t\t\t\t\tYou: ")
	i = 0
	j = 0
	k = 0
	if(user_input == "clear"):
		response = "screen cleared"
		os.system("cls")
	elif("search" in user_input):
		os.system("start chrome {}".format(user_input[6:]))
		response = "opening: "+user_input[6:]
	elif(user_input in f):
			response = "ok bye!"
			exit()
	elif(user_input == "help"):
		response = "may this helped you!"
		print("1. Type which program you want to open/close.\n2. \"clear\" to clear the screen\n3. \"exit\" to exit this program\n4. To search any website write the name/url of the website with 'search' prefix:\n\tEX: search facebook.com")
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
	print("Jarvis: ",end="")
	if((response == "opening") or (response == "NULL")):
		print("opening"+" "+temp+" !")
		os.system("start {}".format(c[i]))
	elif(response == "closing"):
			print("closing"+" "+temp+" !")
			os.system("taskkill/im {}.exe".format(c[i]))
	else:
		print(response)
#taskkill/im notepad.exe