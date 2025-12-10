with open("artifact.txt", "w") as f:
	for i in range(20_000):
		print(i, file=f)
