import os
if __name__ == "__main__":
	try:
		__import__("crack").resik()
		__import__("crack").sandi()
	except Exception as e:
		exit(str(e))
