import win32com.client as win32

outlook = win32.Dispatch("Outlook.Application").GetNamespace("MAPI")

#Outbox has ID 5 - check the ID
outbox = outlook.GetDefaultFolder(5) 

#Pay attention to your sys datetime
messages = outbox.Items.restrict("[SentOn] > '05/06/2017 10:00 AM'")

for message in messages:
	# print message - use this to verify if the restrict works before launching the script
	NewMsg = message.Forward()
	NewMsg.Body = message.Body
	NewMsg.Subject = message.Subject
	NewMsg.To = "mail@mail.com"
	NewMsg.Send()
