import os

def infect():
	os.system("echo 'I am a virus! HAHA!' > virus.txt")

if __name__ == '__main__':
	infect()
