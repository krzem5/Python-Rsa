import sys



DEFAULT_BLOCK_SIZE=128



def main():
	msg="String"
	enc=encrypt(msg,key("pub.txt"))
	print(msg)
	print(enc)
	print(decrypt(enc,key("prv.txt")))



def key(fn):
	f=open(fn)
	sz,n,ed=f.read().split("g")
	f.close()
	return [int(sz,16),int(n,16),int(ed,16)]


def encrypt(seq,key):
	try:
		sz,n,e=key
		bs=DEFAULT_BLOCK_SIZE
		if (sz<bs*8):
			return None
		enc=""
		seq=seq.encode("ascii")
		for i in range(0,len(seq),bs):
			blk=0
			for j in range(i,min(i+bs,len(seq))):
				blk+=seq[j]*(256**(j%bs))
			enc+=f"g{hex(pow(blk,e,n))[2:]}"
		return f"{enc[1:]}g{hex(len(seq))[2:]}g{hex(bs)[2:]}"
	except:
		return None


def decrypt(seq,key):
	try:
		sz,n,d=key
		ln,bs=seq.split("g")[-2:]
		seq=seq.split("g")[:-2]
		ln=int(ln,16)
		bs=int(bs,16)
		if (sz<bs*8):
			return None
		dec=[]
		for blk in seq:
			blk=pow(int(blk,16),d,n)
			db=[]
			for i in range(bs-1,-1,-1):
				if (len(dec)+i<ln):
					db.insert(0,chr(blk//(256**i)))
					blk=blk%(256**i)
			dec+=db
		return "".join(dec)
	except:
		return None


main()