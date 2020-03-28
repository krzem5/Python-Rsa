import base64
import random



def rand_key(sz):
	return "".join([chr(random.randint(0,256)) for i in range(0,sz,1)])



def encode(key,seq):
	seq=key[:len(key)//3]+seq+key[len(key)//3:]
	enc=[]
	for i in range(len(seq)):
		key_c=key[(i*3)%len(key)]
		enc_c=chr((ord(seq[i])+ord(key_c))%256)
		enc.append(enc_c)
	return str(base64.urlsafe_b64encode(bytes("".join(enc),"utf-8")))[2:-1]



def decode(key,enc):
	dec=[]
	enc=str(base64.urlsafe_b64decode(enc),"utf-8")
	for i in range(len(enc)):
		key_c=key[(i*3)%len(key)]
		dec_c=chr((256+ord(enc[i])-ord(key_c))%256)
		dec.append(dec_c)
	return "".join(dec[len(key)//3:-len(key)*2//3])



msg="String"
key=rand_key(1024)
enc=encode(key,msg)
print(msg)
print(enc)
print(decode(key,enc))