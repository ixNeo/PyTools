import re

class FilterAndAct:

	def proc(self, block):
		def actEm(match):
			# print("in actEm's subs")
			return ('<em>%s</em>' % match.group(1))

		def filterEm(block):
			# print('in filterEm')
			return re.sub(r'\*(.+?)\*',actEm,block)


		def actDel(match):
			return ('<del>%s</del>' % match.group(1))

		def filterDel(block):
			return re.sub(r'/(.+?)/',actDel,block)


		def actUrl(match):
			return ('<a onclick="alert(\'you clicked me\');"href="%s">%s</a>' % (match.group(1)
				,match.group(1)))

		def filterUrl(block):
			return re.sub(r'(http://[\.a-zA-Z]+)',actUrl,block)

		block = filterEm(block)
		block = filterDel(block)
		block = filterUrl(block)

		return block