x = ('masala chai','lemon','ginger')
y=enumerate(x)
print(y)
z= list(y)
print(z)
file =open('yt.txt','w')
try:
    file.write('chai aur code')
finally:
    file.close()
with open('youtube.txt','w') as file:#better 
    file.write('chai aur python')
    