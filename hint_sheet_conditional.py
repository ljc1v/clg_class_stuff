
num_men = 4
num_women = 4


num_people = num_men + num_women
print "debug: num_people is",num_people

if  num_people > 8  or num_people < 8:
    print "you need 8 people to square dance."
    print "this could also have been written num_people != 8"
elif num_men != num_women:
    print "at this point you know you have 8 people"
    print "debug: you have {0} men and {1} women".format(num_men,num_women)
    if num_men > num_women:
        print "you have more men than women"
        print "this is a nested code block 8 spaces in not 4"
    else:
        print "you have more women than men"
        print "this is a nested code block 8 spaces in not 4"
else:
    print "This else block goes with the first if statement, so you know you have 8 people"
    print "Since it didn't stop at the elif, you know the num_men = num_women"
    print "debug: you have {0} men and {1} women".format(num_men,num_women)
    print "time to dance :-)"
