FILE_INPUT = "input.txt"
FILE_OUTPUT = "output.txt"

def addmattrix(A : list, B: list) -> list:
	res = []
	columnA = len(A[0])
	lineA = len(A)
	columnB = len(B[0])
	lineB = len(B)
	if lineA == lineB and (columnA == columnB):
		for i in range(lineA):
			res.append([])
			for j in range(columnA):
				res[i].append(A[i][j]+B[i][j])
	else:
		print("Given matrices cannot be added. Check Dimension!")
		return(None)
	return res

def multnumber(X : list, a : float) -> list:
	res = []
	columnX = len(X[0])
	lineX = len(X)
	for i in range(lineX):
		res.append([])
		for j in range(columnX):
			res[i].append(a*X[i][j])
	return(res)

def multmatrix(A : list, B : list) -> list:
	res = []
	columnA = len(A[0])
	lineA = len(A)
	columnB = len(B[0])
	lineB = len(B)
	print(columnA)
	print(lineB)
	if (columnA == lineB):
		for i in range(lineA):
			res.append([])
			for j in range(columnB):
				res[i].append(0)
				for k in range(columnA):
					res[i][j] += A[i][k]*B[k][j]
	else:
		print("Given matrices cannot be multiplied. Check Dimension!")
		return(None)
	return(res)

def transposition(A : list) -> list:
	res = []
	columnA = len(A[0])
	lineA = len(A)
	for i in range(columnA):
		res.append([])
		for j in range(lineA):
			res[i].append(A[j][i])
	return(res)

def equation_solution(A : list, B : list, C : list, D : list, F : list, a : float, b: float) -> list:
	A = multnumber(A,a)
	B = multnumber(transposition(B),b)
	if A!= None and B!= None:
		K = transposition(addmattrix(A,B))
	else:
		return None
	if K!= None:
		M = multmatrix(C,K)
	else:
		return None
	if M!= None and D!= None:
		N = multmatrix(M,D)
	else:
		return None
	F = multnumber(F,-1)
	if N!= None and F!= None:
		X = addmattrix(N,F)
	else:
		return None
	return(X)

def matrix_creation(l : list, n : int, m : int) -> list:
	res = []
	k = 0
	for i in range(n):
		res.append([])
		for j in range(m):
			res[i].append(0)
			res[i][j] = l[k]
			k += 1
	return(res)

def write_data(X : list):
	if X!= None:
		with open(FILE_OUTPUT, "w+") as f:
			f.write("1\n")
			f.write(str(len(X)) + " " + str(len(X[0])))
			for i in range(len(X)):
				f.write("\n")
				for j in range(len(X[0])):
					if j!= 0:
						f.write(" ")
					f.write(str(X[i][j]))
	else:
		with open(FILE_OUTPUT, "w+") as f:
			f.write("0")

def read_data() -> dict:
	data = []
	with open(FILE_INPUT, "r", encoding="UTF-8") as f:
		for line in f:
			data.append(line.replace(" \n", "").replace("\n", "").split(" "))
	a = float((data[0][0]))
	b = float((data[0][1]))
	na = int(data[1][0])
	ma = int(data[1][1])
	for i in range(2,11,2):
		for j in range(len(data[i])): 
			if data[i][j]!= "": 
				data[i][j] = float((data[i][j]))
	A = matrix_creation(data[2],na,ma)
	nb = int(data[3][0])
	mb = int(data[3][1])
	B = matrix_creation(data[4],nb,mb)
	nc = int(data[5][0])
	mc = int(data[5][1])
	C = matrix_creation(data[6],nc,mc)
	nd = int(data[7][0])
	md = int(data[7][1])
	D = matrix_creation(data[8],nd,md)
	nf = int(data[9][0])
	mf = int(data[9][1])
	F = matrix_creation(data[10],nf,mf)
	out_data = dict()
	out_data["A"] = A
	out_data["B"] = B
	out_data["C"] = C
	out_data["D"] = D
	out_data["F"] = F
	out_data["a"] = a
	out_data["b"] = b
	return out_data

def main():
	data = read_data()
	X = equation_solution(data["A"], data["B"], data["C"], data["D"], data["F"], data["a"], data["b"])
	write_data(X)

if __name__ == "__main__":
	main()
