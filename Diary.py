 ##Create a program to make a digital diary in a file, which
##store day to day life experience with their time stamps(the
##exact time when the data is written actually).
##You need to change the path explicitly at line no 20 and 47 otherwise it will not work


import sys,os,time
##import py_compile
##py_compile.compile('Q9.py')
print "		WELCOME"
fl=1
while True:
	print "1.Write"
	print "2.Read"
	print "3.Exit"
	n=eval(raw_input("\nEnter your choise:  "))
	
	if n==1:
		try:
			os.chdir("/home/souvik/Diary")
			t=time.localtime()
			dd=t[2]
			mm=t[1]
			yy=t[0]
			h=t[3]
			m=t[4]
			s=t[5]
			filename=str(dd)+str(mm)+str(yy)
			f=open(filename,"a")
			msg=raw_input("Enter the msg: ")
			f.write("\n\n\t")
			f.write(str(h))
			f.write(":")
			f.write(str(m))
			f.write(":")
			f.write(str(s))
			f.write("\n")
			f.write(msg)
			f.write("\n")
			f.close
		except OSError:
			print "\n\n\tDiary has been created and ready for write"
			os.mkdir("Diary")
	elif n==2:
		if fl==1:
			try:
				os.chdir("/home/souvik/Diary")
				fl=2
			except OSError:
				print "\n\n\tThere is no memo."
				continue
		dd=raw_input("Enter the date: ")
		mm=raw_input("Enter the month: ")
		yy=raw_input("Enter  the year: ")
		filename=dd+mm+yy
		
		try:
			f=open(filename,"r")
			msg=f.read()
			print "\n\n",msg,"\n\n"
		except IOError:
			print " Invaild date....Date format is :ddmmyyyy or no data found..."
	elif n==3:
		sys.exit()
	else:
		print "\n\n\tInvalid input...Try again"
