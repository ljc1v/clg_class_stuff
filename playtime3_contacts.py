



# Dictionary within Dictionary
contacts = {
'Shannon': {'phone': '555-1234', 'twitter' : '@adsfd', 'github' : 'asdfdsaf'},
'Bridgit': {'phone': '555-1222', 'twitter' : '@adf', 'github' :'asdfadsf'},
'Alison' : {'phone' : '555-111', 'twitter' : '@adsfa', 'github' : 'afdad'}
}

print "Alison is ", contacts.get('Alison')
print "Alison's phone is", contacts.get('Alison').get('phone')

for contact in contacts.keys():
	# contact is list of keys
	print contact," has twitter ", contacts.get(contact).get('twitter')

for contact in sorted(contacts.keys()):
	print "\nContact: {0}".format(contact)
	for value in sorted (contacts.get(contact).keys()):
		print "\t{0}: {1}".format(value,contacts.get(contact).get(value))


# playtime goal #1
for key,info in contacts.items():
	print "\n{0}'s info:".format(key)
	for key2 in info.keys():
		print "\t{0}: {1}".format(key2,info.get(key2))

	
# playtime goal #2
print '<table border="1">'
for key,info in contacts.items():
	print "\n<tr><td colspan='3'> {0} </td></tr>".format(key)
	print "<tr>"
	for key2 in info.keys():
		print "<td> {0}: {1} </td>".format(key2,info.get(key2))
	print '</tr>'

print '</table>'

#playtime goal #3 

with open ("contacts.html", "w") as new_file:
	new_file.write('<table border="1">')
	for key,info in contacts.items():
		new_file.write("<tr><td colspan='3'> {0} </td></tr>".format(key))
		new_file.write("<tr>")
		for key2 in info.keys():
			new_file.write("<td> {0}: {1} </td>".format(key2,info.get(key2)))
		new_file.write('</tr>')

	new_file.write('</table>')

#playtime goal #4
with open ("contacts.csv", "r") as input_file:
	contact_lines = input_file.read().split("\n")

contacts = {}
for index, contact in enumerate(contact_lines):
	print "contact_lines[{0}] is {1}".format(index, contact_lines[index])
	contact_list = contact.split(",") 
	name = contact_list.pop(0)
	if (index == 0):
		labels = contact_list
	else :
		details={}
		for label, contact in zip (labels,contact_list):
			details[label] = contact
		contacts[name] = details

print contacts

with open ("contacts2.html", "w") as new_file:
	new_file.write('<table border="1">')
	for name,details in contacts.items():
		new_file.write("<tr><td colspan='3'> {0} </td></tr>".format(name))
		new_file.write("<tr>")
		for key in details.keys():
			new_file.write("<td> {0}: {1} </td>".format(key,details.get(key)))
		new_file.write('</tr>')

	new_file.write('</table>')

# compress goal #4
with open ("contacts.csv", "r") as input_file:
	contact_lines = input_file.read().split("\n")

with open ("contacts2.html", "w") as new_file:
	new_file.write('<table border="1">')
	
	#for each line
	for index, contact in enumerate(contact_lines):
		print "contact_lines[{0}] is {1}".format(index, contact_lines[index])
		contact_list = contact.split(",") 
		name = contact_list.pop(0)
		
		if (index == 0):
			labels = contact_list
		else :
			new_file.write("<tr><td colspan='3'> {0} </td></tr>".format(name))	
			new_file.write("<tr>")
			for label, contact in zip (labels,contact_list):
				new_file.write("<td> {0}: {1} </td>".format(label, contact))
			new_file.write('</tr>')

	new_file.write('</table>')

