import random



def gen_key(sz):
	def gcd(a,b):
		while (a!=0):
			a,b=b%a,a
		return b
	def modinv(a,m):
		if (gcd(a,m)!=1):
			return None
		a1,a2,a3=1,0,a
		b1,b2,b3=0,1,m
		while (b3!=0):
			q=a3//b3
			b1,b2,b3,a1,a2,a3=(a1-q*b1),(a2-q*b2),(a3-q*b3),b1,b2,b3
		return (a1%m)
	def prime(n):
		if (n<2):
			return False
		lp=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]
		if (n in lp):
			return True
		for p in lp:
			if (n%p==0):
				return False
		s=n-1
		t=0
		while (s%2==0):
			s=s//2
			t+=1
		for _ in range(5):
			a=random.randrange(2,n-1)
			v=pow(a,s,n)
			if (v!=1):
				i=0
				while (v!=(n-1)):
					if (i==t-1):
						return False
					else:
						i+=1
						v=(v**2)%n
		return True
	def lp(sz):
		while (True):
			n=random.randrange(2**(sz-1),2**(sz))
			if (prime(n)):
				return n
	p=lp(sz)
	q=lp(sz)
	n=p*q
	while (True):
		e=random.randrange(2**(sz-1),2**(sz))
		if (gcd(e,(p-1)*(q-1))==1):
			break
	d=modinv(e,(p-1)*(q-1))
	pub=f"{hex(sz)[2:]}g{hex(n)[2:]}g{hex(e)[2:]}"
	prv=f"{hex(sz)[2:]}g{hex(n)[2:]}g{hex(d)[2:]}"
	return [pub,prv]



print(gen_key(2048))
