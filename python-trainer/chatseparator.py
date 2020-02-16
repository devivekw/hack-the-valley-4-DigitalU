filenames = ["whatsapp_chat"]
cwboolean = True
othersboolean = True

for names in filenames:
	file_handle = open(names + "out.txt", encoding='utf-8')
	print(names + "out.txt has been opened")
	fcw = open(names + "CW.txt", 'w',encoding='utf-8')
	fothers = open(names + "sep.txt", 'w',encoding='utf-8')
	for line in file_handle:
		if(line.startswith("vivek")):
			if(cwboolean):
				fcw.write("|\n")
				othersboolean = True
				cwboolean = False
			fcw.write(line)
		else:
			if(othersboolean):
				fothers.write("|\n")
				cwboolean = True
				othersboolean = False
			fothers.write(line)
		#print(line)
file_handle.close()