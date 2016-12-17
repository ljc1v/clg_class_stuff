

#build one list from all_employees & surbey

with open ("all_employees.csv", "r") as input_file:
	contact_lines = input_file.read().split("\n")

with open ("survey.csv", "r") as input_file:
	survey_lines = input_file.read().split("\n")

employees = {}
for index, contact in enumerate(contact_lines):
	#print "contact_lines[{0}] is {1}".format(index, contact_lines[index])
	contact_list = contact.split(",")
	if (index == 0):
		labels = contact_list
	else :
		details={}
		for label, contact in zip (labels,contact_list):
			label = label.strip()
			details[label] = contact.strip()
		#print details
		if details.has_key('email'):
			employees[details.get('email')] = details
		else:
			print "employee {0} is missing email data".format(details.get('name'))

for index, survey_data in enumerate(survey_lines):
	#print "survey_lines[{0}] is {1}".format(index, survey_lines[index])
	contact_list = survey_data.split(",")
	if (index == 0):
		labels = contact_list
	else :
		details={}
		for label, contact in zip (labels,contact_list):
			label = label.strip()
			details[label] = contact.strip()
		#print details
		if details.has_key('email'):
			email = details.get('email')
			if employees.has_key(email):
				employees[email].update(details)
			else:
				print "No employee matches survey email {0}".format(email)
		else:
			print "Missing email data in survey entry: {0}".format(survey_lines[index])


#print employees

list_order=['name', 'email', 'phone', 'department', 'position', 'twitter', 'github']
with open ("new_employee_list.csv", "w") as new_file:
	new_line = ""
	#print the label line
	for label in list_order:
		new_line = new_line + label
		if list_order.index(label) != len(list_order)-1:
				new_line = new_line + ", "
	new_line = new_line + "\n"

	#print the employee lines
	for email in sorted(employees.keys()):
		#print email
		for label in list_order:
			if employees[email].has_key(label):
				new_line = new_line + employees[email].get(label)
			if list_order.index(label) != len(list_order)-1:
				new_line = new_line + ", "
		new_line = new_line + "\n"
	new_file.write(new_line)
		
	







