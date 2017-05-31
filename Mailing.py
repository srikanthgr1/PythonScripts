import win32com.client as win32

outlook = win32.Dispatch("Outlook.Application").GetNamespace("MAPI")

#outbox ha ID 5
outbox = outlook.GetDefaultFolder(5) 

messages = outbox.Items.restrict("[SentOn] > '5/30/2017 08:00 AM'")

for message in messages:
	# print message
	NewMsg = message.Forward()
	NewMsg.Body = message.Body
	NewMsg.Subject = message.Subject
	NewMsg.To = "mail@mail.com"
	NewMsg.Send()
