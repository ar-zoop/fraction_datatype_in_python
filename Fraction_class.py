class Fraction:
	
	def gcd(self):
		a = self.num
		b = self.den
		if(b>a):
			a,b=b,a
		while b != 0:
			a, b = b, a % b
		return a        
	
	def simplify(self):
		gcd = self.gcd()
		self.num //= gcd
		self.den //= gcd
		
	def __init__(self, n, d):
		if(d==0):
			raise ValueError("Denominator cannot be 0")
		else:
			self.num=n
			self.den=d
			self.simplify()
		
		
	def __str__(self):
		return "{}/{}".format(self.num, self.den)
	
	def __add__(self,other):
		den=self.den * other.den
		num=(self.den * other.num)+(other.den*self.num)
		return "{}/{}".format(num,den)
	
	def __sub__(self,other):
		den=self.den * other.den
		num=(self.den * other.num)-(other.den*self.num)
		return "{}/{}".format(num,den)
	
	def __mul__(self, other):
		den=self.den * other.den
		num=self.num * other.num
		return "{}/{}".format(num,den)
	
	def __truediv__(self, other):
		den=self.den * other.num
		num=self.num * other.den
		return "{}/{}".format(num,den)   
		
	def __eq__(self, other):
		if(self.den == other.den and self.num == other.num):
			return True
		return False
	
	def __lt__(self, other):
		return self.num * other.den < other.num * self.den
	
	def __gt__(self, other):
		return self.num * other.den > other.num * self.den
	
	def __le__(self, other):
		return self.num * other.den <= other.num * self.den
	
	def __ge__(self, other):
		return self.num * other.den >= other.num * self.den
	
	def __float__(self):
		return float(self.num) / float(self.den)
	
	def __int__(self):
		return self.num // self.den
	
	def __abs__(self):
		return Fraction(abs(self.num), abs(self.den))
	
	def __invert__(self):
		return Fraction(self.den, self.num)
	
	def __round__(self, ndigits=None):
		if ndigits is None:
			return round(float(self))
		else:
			return Fraction(round(self.num * 10**ndigits / self.den),
							10**ndigits)
	
	
