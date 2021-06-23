
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())	#.strip把換行符號給去掉。
	return lines

def convert(lines):

	person = None				#訂義person 為None 就是沒有值但它存在。
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(' ')		#split 就是字串的切割，（' '）括號內的空格就是遇到空客就切一刀， ＝ s 就是將它存成清單。
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for msg in s[2:]:
					allen_word_count += len(msg)		# += 意思是指 allen_word_count＝allen_word_count ＋ len(msg)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count +=1
			else:
				for msg in s[2:]:
					viki_word_count += len(msg)
	print('Allen說了', allen_word_count)
	print('Allen傳了', allen_sticker_count, '個貼圖')
	print('Allen傳了', allen_image_count, '張圖片' )
	print('Viki說了', viki_word_count)
	print('Viki傳了', viki_sticker_count, '個貼圖')
	print('Viki傳了', viki_image_count, '張圖片')

		

def write_file(filename, lines):
	with open(filename, 'w')as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('[LINE]Viki.txt')
	lines = convert(lines)
	# write_file('output.txt', lines)

main()
