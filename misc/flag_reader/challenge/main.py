#!/usr/bin/env python3

def main():
	while True :
		path = input('Enter a path : ')
		try:
			with open(f"/challenge/flag_not_here/{path}/flag.txt",'r', encoding = 'utf-8') as f:
				flag = f.read()
				print(flag)
		except:
			print('hey try again')


if __name__ == '__main__':
	main()
