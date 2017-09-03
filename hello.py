import logging

logging.basicConfig(filename="hello.log", format='%(asctime)s-%(levelname)s-%(message)s', level=logging.INFO)

if __name__ == "__main__":
	greeting = "Git World"
	#print "Hello..{}".format(greeting)
	logging.info("Hello..{}".format(greeting))
