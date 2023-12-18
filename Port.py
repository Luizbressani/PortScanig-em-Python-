import socket
import sys



def Scan(lhost, Aports):
	try:
		for porta in Aports:
			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			client.settimeout(0.5)
			alvo = client.connect_ex((lhost, int(porta)))

			if alvo == 0:
				print("[+] {} open".format(porta))
	except Exception as erro:
		print(erro)
if __name__== "__main__":
	if len(sys.argv)>=2:
		lhost = sys.argv[1]
		if len(sys.argv)>=3:
			try:
				Aports = sys.argv[2].split(",")
			except Exception as error:
				print(error)
		else:
			Aports = range(65000)
		Scan(lhost, Aports)
	else:
		print("Modo de uso: python Port.py Domino/IP 22,23,80,443")
