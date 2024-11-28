T=()
print(T)

T=("Anu","Hema","Vino","Divya")
L=list(T)
L.append("Dharani")
L.remove("Vino")
T=tuple(L)
print(T)


txt="     python program"
print("index=",txt.index("m"))


txt="     I like icecreams"
x=txt.replace("icecreams","chocolates")
print(x)

txt="     python program"#remove the space before the characters
print("strip=",txt.strip())
 
