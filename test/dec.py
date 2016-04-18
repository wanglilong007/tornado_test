def dec(fn):
	print('before fn')
	fn()
	print('after fn')
	return fn

def dec_in(fn):
	def _dec_in():
		print('dec1 before fn')
		fn()
		print('dec1 after fn')
	return _dec_in

def dec_in_2(fn):
	def _dec_in():
		print('dec2 before fn')
		fn()
		print('dec 2after fn')
	return _dec_in
'''
#f = dec(f())
@dec
def f():
	print('f')
'''

#e = dec_in_2(dec_in(e()))
@dec_in_2
@dec_in
def e():
	print('e')


#f()
e()
