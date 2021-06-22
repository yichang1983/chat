
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())	#.strip把換行符號給去掉。
	return lines

def convert(lines):
	new = []
	person = None				#訂義person 為None 就是沒有值但它存在。
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:				#如果person 有值，就執行下一行。	
			new.append(person + ': ' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w')as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()
