f = open("成绩表.txt", "w")
f.write("张三 90\n")
f.write("李四 85\n")
f.write("王五 78\n")
f.close()
print("已保存到 成绩表.txt")
f = open("成绩表.txt", "r")
content = f.read()
f.close()
print(content)
lines = content.split("\n")
scores = []
for line in lines:
    if line =="":
        continue
    parts = line.split(" ")
    scores.append(int(parts[1]))
print("所有分数是",scores)
print("平均数是",sum(scores)/len(scores))
