#read in CVS file,  print out HTML file

with open("states.csv","r") as inputfile:
	states= inputfile.read().split("\n")

#print intput variable
print states

#print tranformation
for index, state in enumerate(states):
	print "states[{0}] is {1}".format(index, states[index])
	states[index] = state.split(",")
	print "states[{0}] is {1} ".format(index, states[index])

#print nested loops
print states

#print select list

print "<select name='state'>"
for index, state in enumerate(states):
	print '<option value ="{0}"">{1}</option>'.format(state[0],state[1])
print '</select>'


# now print to a file

with open ("states.html", "w") as new_file:
	new_file.write("<select name='state'>\n")
	for index, state in enumerate(states):
		new_file.write ('<option value ="{0}"">{1}</option>\n'.format(state[0],state[1]))
	new_file.write('</select>')



	








