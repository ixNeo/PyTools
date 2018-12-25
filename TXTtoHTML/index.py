import sys, re
from filter import *
from rule import *
# read file, get input list
# *requirement: last statement followed by one space line
# 			in input file *
def getfile(file):
	block = []
	for line in file:
		# print("getfile: "+ line)
		if line.strip():
			block.append(line)
		else:
			block = ''.join(block).strip()
			yield block
			block = []
	# print("getfile done")


# loop, condition(subtitition or add start/end)
# type to process: h1, ul, li, url, del, emphasis \
#	paragraph
def parser(file):
	blocks = getfile(file)
	filterAndAct = FilterAndAct()
	ruleAndAct = RuleAndAct()
	print("<html><head><title>yutian</title> \
		</head><body>")
	# PROBLEM: there is no static var in python 
	# SOLUTION: create a class. function slope is so important
	for block in blocks:
		# filters
		block = filterAndAct.proc(block)
		# rules
		block = ruleAndAct.proc(block)
		print(block)
		
	# output
	print("</body></html>")

if __name__=="__main__":
	parser(sys.stdin)