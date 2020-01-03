#ModBySobyDamn
from bsUI import *
import bsUI
import bsInternal
import ChatFilterConfig as config
from datetime import *
import time
#bs.screenMessage("ChatFilter added")

def chatLogs(msg, clientID):
	date = str(datetime.date(datetime.now()))
	now = datetime.now()
	time = str(now.hour) + ":" + str(now.minute)
	for i in bsInternal._getGameRoster():
		cid = i['clientID']
		if cid == clientID:
			f = open(bs.getEnvironment()['userScriptsDirectory'] + "/Chats " + date + ".txt",'a')
			f.write(i['players'][0]['name'] + "(" + i['displayString'] + ")[" + time + "]: " + msg + "\n")
	
def _chatFilter(msg, clientID):
	chatLogs(msg, clientID)
	if 'yes' in config.blockChats:
		return None
		
	if any(word in msg for word in config.blacklist):
		for i in bsInternal._getGameRoster():
			cid = i['clientID']
			if cid == clientID:
				name = str(i['players'][0]['name'])
				nameID = str(i['displayString'])
				now = str(datetime.now())
		if not 'yes' in config.kickSpammer:
			f = open(bs.getEnvironment()['userScriptsDirectory'] + "/spammerID.txt",'a')
			f.write(nameID + " Used bad word" + "[" + now + "]: " + msg + "\nName Using:-" + name + "\n")
		if 'yes' in config.kickSpammer:
			bsInternal._chatMessage(nameID + " Kicked for using bad word")
			f = open(bs.getEnvironment()['userScriptsDirectory'] + "/spammerID.txt",'a')
			f.write(nameID + " Kicked for using bad word" + "[" + now + "]: " + msg + "\nName Using:-" + name + "\n")
			bsInternal._disconnectClient(clientID)
			if 'yes' in config.credits:
				bsInternal._chatMessage("ChatFilter Made By SobyDamn")
		else:
			return
		return None
		#print 'ChatFilter Working'
	else:
		return msg

bsUI._filterChatMessage = _chatFilter