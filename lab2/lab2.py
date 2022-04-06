from math import acos
from math import pi

FILE_INPUT = "input.txt"
FILE_OUTPUT = "output.txt"
WORD = "robotics"

def comparison_of_tuples(t1,t2):
	if len(t1) != len(t2):
		return False
	for i in range(len(t1)):
		if t1[i] != t2[i]:
			return False
	return True

def mixed_product_of_vectors(a,b,c):
	return a[0]*(b[1]*c[2]-b[2]*c[1])-b[0]*(a[1]*c[2]-a[2]*c[1])+c[0]*(a[1]*b[2]-a[2]*b[1])

def angle_lines(line1, line2):
	if not(comparison_of_tuples(line1, line2)) and (zero_mass(line1)) and (zero_mass(line2)):
		return acos((line1[0]*line2[0]+line1[1]*line2[1]+line1[2]*line2[2])/(((line1[0]**2 + line1[1]**2 + line1[2]**2)**0.5)*(line2[0]**2 + line2[1]**2 + line2[2]**2)**0.5))

def converting_radina_to_degrees(angle):
	return angle/pi*180

def difference_between_vectors(a,b):
	r = []
	for i in range(3):
		r.append(a[i] - b[i])
	return r

def zero_mass(mass):
	t = 0
	for element in mass:
		t += abs(element)
	if t == 0: return False
	else: return True

def determination_of_the_angle_of_rotation_B(keel, r):
	if not(comparison_of_tuples(keel, r)):
		angle = angle_lines(keel,r)
		if angle != None:
			angle = 90 - converting_radina_to_degrees(angle)
		else: return(None)
	else: return 1000
	if abs(angle) > 60.0:
		return None
	else:
		return angle

def determination_of_the_ships_side(keel, r, vn):
	normXoY = (vn[0], vn[1], 1)
	if mixed_product_of_vectors(keel, r, normXoY) > 0:
		return 1
	elif mixed_product_of_vectors(keel, r, normXoY) < 0: 
		return -1

def determination_of_the_angle_of_rotation_J(mast, keel):
	normXoY = [0,0,1]
	if not(comparison_of_tuples(normXoY, mast)):
		angle = converting_radina_to_degrees(angle_lines(normXoY, mast))
	else:
		return 100
	if angle != None:
		if mixed_product_of_vectors(normXoY, mast, keel) > 0:
			return -angle
		else:
			return angle
	else: return None

def str_in_float(mass : list) -> list:
	res = []
	for element in mass:
		res.append(float(element))
	return res

def error():
	with open(FILE_OUTPUT, "w+") as f:
			f.write("0" + "\n")
			f.write(WORD)

def read_data() -> dict:
	data = dict()
	with open(FILE_INPUT, "r") as f:
		line = f.readline()
		data["v"] = str_in_float(line.split())
		data["v"].append(0.0)
		line = f.readline()
		data["a"] = str_in_float(line.split())
		data["a"].append(0.0)
		line = f.readline()
		data["m"] = str_in_float(line.split())
		data["m"].append(1.0)
		line = f.readline()
		data["w"] = str_in_float(line.split())
		data["w"].append(0.0)
	return data

def main():
	data = read_data()
	r = difference_between_vectors(data["w"] , data["v"])
	if not(comparison_of_tuples(data["v"], data["w"])):
		angle = determination_of_the_angle_of_rotation_B(data["a"], r)
		j = determination_of_the_angle_of_rotation_J(data["m"], data["a"])
		if angle == 1000: angle = None
		if comparison_of_tuples(data["v"], data["a"]): error()
		elif angle != None and j:
			side = determination_of_the_ships_side(data["a"], r, data["v"])
			with open(FILE_OUTPUT, "w+") as f:
				f.write(str(side) + "\n")
				if angle == 0.0: f.write("0.0\n")
				else: f.write(str(angle) + "\n")
				if j == 100:
					j = 0
				if j == 0: f.write("0.0\n")
				else: f.write(str(j) + "\n")
				f.write(WORD)
		else: error()
	else: error()


if __name__ == "__main__":
	main()