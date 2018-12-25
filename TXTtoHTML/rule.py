class RuleAndAct:
	istitle = True
	isul = True
	begul = True
	rules = ['Title','Li','P']


	def ruleTitle(self,block):
		if self.istitle:
			self.istitle = False
		# if len(block)<=10:
			return True
		else:
			return False

	def actTitle(self,block):
		return "<h1>"+block+'</h1>'


	# def ruleList(block):
	# 	if self.isul and ruleLi(block):
	# 		self.isul = False
	# 		return True
	# 	elif not self.isul and not ruleLi(block):
	# 		return False
	# def actList(block):
	# 	if self.begul:
	# 		self.begul = False
	# 		return '<ul><li>'+block
	# 	else:
	# 		return block


	def ruleLi(self,block):
		return block[0]=='-'

	def actLi(self,block):
		return '<li style="decoration: none; color: orange;">'+block[1:]+'</li>'

	def ruleP(self,block):
		return True
	def actP(self, block):
		return block

	# * list "rules", easy to extend
	# * function"call", auto call related function
	# note: these function have to belong to the class, especially "call"
	def call(self,functype,ruletype,*args):
		method = getattr(self, functype+ruletype,*args)

		if callable(method):
			return method(*args)

	def proc(self,block):
		for rule in self.rules:
			if self.call('rule',rule,block):
				block = self.call('act',rule,block)
		# if ruleTitle(block):
		# 	block = actTitle(block)
		# elif ruleList(block):
		# 	block = actList(block)
		# elif ruleLi(block):
		# 	block =actLi(block)
		# elif ruleP(block):
		# 	block =actP(block)
		return block