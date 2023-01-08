import sys
print("coming throuh student")

save_stdout=sys.stdout

fh=open(r"D:\pythonpractice59\day17\axd.txt","w")
sys.stdout=fh
print("this line goes to text .txt")
print(input())
sys.stdout=save_stdout
fh.close()
