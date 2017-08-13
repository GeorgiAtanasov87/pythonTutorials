fmenu = {'spam':1.50, 'ham':1.99, 'eggs':0.99}

corder = input("What will you have today--spam, ham or eggs? ")

if corder == 'spam':
    print("For the spam, that will be", "$", "%.2f" % fmenu.get('spam'), ", please.")
elif corder == 'ham':
    print("Your total for the ham is", "$", "%.2f" % fmenu.get('ham'), ", please.")
else:
    print("Eggs by default! Your total is", "$", "%.2f" % fmenu.get('eggs'), ".") 
