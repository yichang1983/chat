
lines = []
with open('3.txt', 'r', encoding= 'utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())		#.strip把換行符號給去掉。

for line in lines:
	s = line.split(' ')		#split 就是字串的切割，（' '）括號內的空格就是遇到空客就切一刀， ＝ s 就是將它存成清單。
	time = s[0][:5]			#[0]意思就是第0個清單， [:5] 從0-4 的字	。
	name = s[0][5:]			#[0]意思就是第0個清單， [5:] 從第5個字的開始。
	print(name)
