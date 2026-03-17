import RPi.GPIO as GPIO
import time
import math

print("To sent a custom message type it now, there is also a 'O'\(remember captial!\) that flashes the light really fast. Enjoy!")

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
	
dot_time = 0.05
dashtime = dot_time * 3





def dot():
	GPIO.output(24, True)
	time.sleep(dot_time)
	GPIO.output(24, False)
	time.sleep(dot_time)


def dash():
	GPIO.output(24, True)
	time.sleep(dashtime)
	GPIO.output(24, False)
	time.sleep(dot_time)
	
	
def new_word():
	GPIO.output(24, False)
	time.sleep(dot_time * 7)
	
	
def space():
	GPIO.output(24, False)
	time.sleep(dashtime)

def O():
	GPIO.output(24, True)
	time.sleep(0.05)
	GPIO.output(24, False)
	time.sleep(0.05)







def a():
	dot()
	dash()
	space()

def b():
	dash()
	dot()
	dot()
	dot()
	space()
	
def c():
	dash()
	dot()
	dash()
	dot()
	space()
	
def d():
	dash()
	dot()
	dot()
	space()
	
def e():
	dot()
	space()
	
def f():
	dot()
	dot()
	dash()
	dot()
	space()
	
def g():
	dash()
	dash()
	dot()
	
def h():
	dot()
	dot()
	dot()
	dot()

def i():
	dot()
	dot()

def j():
	dot()
	dash()
	dash()
	dash()

def k():
	dash()
	dot()
	dash()

def l():
	dot()
	dash()
	dot()
	dot()

def m():
	dash()
	dash()

def n():
	dash()
	dot() 

def o():
	dash()
	dash()
	dash()

def p():
	dot()
	dash()
	dash()
	dot()

def q():
	dash()
	dash()
	dot()
	dash()

def r():
	dot()
	dash()
	dot()

def s():
	dot()
	dot()
	dot()

def t():
	dash()

def u():
	dot()
	dot()
	dash()

def v():
	dot()
	dot()
	dot()
	dash()

def w():
	dot()
	dash()
	dash()

def x():
	dash()
	dot()
	dot()
	dash()

def y():
	dash()
	dot()
	dash()
	dash()

def z():
	dash()
	dash()
	dot()
	dot()



while True:
	encryption = input()
	for letter in encryption:
		print(f"{letter}")
		if letter == 'a':
			a()
		if letter == 'b':
			b()
		if letter == 'c':
			c()
		if letter == 'd':
			d()
		if letter == 'e':
			e()
		if letter == 'f':
			f()
		if letter == 'g':
			g()
		if letter == 'h':
			h()
		if letter == 'i':
			i()
		if letter == 'j':
			j()
		if letter == 'k':
			k()
		if letter == 'l':
			l()
		if letter == 'm':
			m()
		if letter == 'n':
			n()
		if letter == 'o':
			o()
		if letter == 'p':
			p()
		if letter == 'q':
			q()
		if letter == 'r':
			r()
		if letter == 's':
			s()
		if letter == 't':
			t()
		if letter == 'u':
			u()
		if letter == 'v':
			v()
		if letter == 'w':
			w()
		if letter == 'x':
			x()
		if letter == 'y':
			y()
		if letter == 'z':
			z()
		if letter == ' ':
			new_word()
		if letter == 'O':
			O()
