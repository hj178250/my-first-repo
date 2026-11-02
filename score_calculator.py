scores = []                      # 先准备一个空盒子（空列表）
scores.append(int(input("第1个分数：")))
scores.append(int(input("第2个分数：")))
scores.append(int(input("第3个分数：")))
scores.append(int(input("第4个分数：")))
scores.append(int(input("第5个分数：")))

total = 0
for s in scores:
    total = total + s
print("平均数是",total/len(scores))
biggest = scores[0]
for s in scores:
    if s >biggest:
        biggest = s
print("最大数",biggest)
smallest = scores[0]
for s in scores:
    if s < smallest:
        smallest = s
print("最小数：", smallest)

