# x = "I'm a string"
# print x[1]
# y = x.replace("a","the",1)  #only one time
# print y

# #list
# alist = ["a", "b", "c"]

# #append is for one
# alist.append ("z")
# #extend is for adding another whole list and needs brackets.
# alist.extend(["d","e"])
# print "alist is ", alist
# age = [23,23,24,24,25,25]
# print "age is ", age
# print "zero position is", alist[0]
# print "{0} is {1} years old".format(alist[0],age[0])
# print "length is ",len (alist)
# for i in range(len(alist)):
# 	print alist[i], age[i]



# # pop the list one off the list, you can pop any position
# print "{0} is {1} years old".format(alist.pop(0),age.pop(0))
# print alist, age

# # insert a value anywhere in the list
# alist.insert (2,"y")
# print alist, age

# address = "1133 19th St.  NW Washington DC 20036"
# address_as_list = address.split(" ")
# print address_as_list
# print '19'in address
# print '19'in address_as_list

# name = raw_input('Name: ');
# print name

# q_nw =[]
# q_ne = []
# q_sw = []
# q_se = []

# input1 = raw_input(' Address1: ')
# input1_list = input1.split(" ")

# if 'NW' in input1_list:
# 	q_nw.append (input1)
# elif 'NE' in input1_list:
# 	q_ne.append (input1)
# elif "SW" in input1_list:
# 	q_sw.append (input1)
# elif "SE" in input1_list:
# 	q_se.append (input1)
# else:
# 	print "no quadrant in address1: ", input1, "\n"

# input2 = raw_input(' Address2: ')

# if ' NW ' in input2.upper():
# 	q_nw.append (input2)
# elif ' NE ' in input2 or ' ne ' in input2:
# 	q_ne.append (input2)
# elif "SW" in input2_list:
# 	q_sw.append (input2)
# elif "SE" in input2_list:
# 	q_se.append (input2)
# else:
# 	print "no quadrant in address2: ", input1


# input3 = raw_input(' Address3: ')
# input3_list = input3.split(" ")

# if 'NW' in input3_list:
# 	q_nw.append (input3)
# elif 'NE' in input3_list:
# 	q_ne.append (input3)
# elif "SW" in input3_list:
# 	q_sw.append (input3)
# elif "SE" in input3_list:
# 	q_se.append (input3)
# else:
# 	print "no quadrant in address3: ", input1

# print "\n        "
# print "NW", q_nw
# print "NE", q_ne
# print "SW", q_sw
# print "SE", q_se

#print range(5)

# q_nw =[]
# q_ne = []
# q_sw = []
# q_se = []

# print "\nInput 5 Addresses"
# for i in range(5):
# 	input= raw_input('Address: ')
# 	input_upper = input.upper()
# 	input_list = input_upper.split(" ")

# 	if 'NW' in input_list:
# 		q_nw.append (input)
# 	elif 'NE' in input_list:
# 		q_ne.append (input)
# 	elif "SW" in input_list:
# 		q_sw.append (input)
# 	elif "SE" in input_list:
# 		q_se.append (input)
# 	else:
# 		print "no quadrant in address: ", input, "\n"

# print "\nQuadrants        "
# print "NW", q_nw
# print "NE", q_ne
# print "SW", q_sw
# print "SE", q_se, "\n"


# days_of_week = ["Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun"]
# for day in days_of_week:
# 	print day

# for week in range(1,5):
# 	print "Week {0}".format(week)
# 	for day in days_of_week:
# 		print "	",day

#enumerate provides both position and vaule
# for index, day in enumerate(days_of_week):
# 	print "day {0} is {1}".format(index,day)

#zip is for taking two lists and making a tuple list
# state_names = ['Alabama', 'Alaska', 'Arkansas']
# state_abbrs = ['AL', 'AK', 'AR']
# for name, abbr in zip (state_names, state_abbrs):
# 	print '{0} ({1})'.format(name,abbr)

i=1
while i <10:
	print 'round ',i
	i=i+1

sand = 0
bread = int(raw_input('How much many bread slices do you have? ' ))
while bread >=2:
	sand = sand + 1
	print "make sandwich ", sand, " with two slices."
	bread = bread - 2

print "You have made {0} sandwiches.".format(sand)
print "You have {0} bread slice left over".format(bread)





	








