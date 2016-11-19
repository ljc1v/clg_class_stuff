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



	








