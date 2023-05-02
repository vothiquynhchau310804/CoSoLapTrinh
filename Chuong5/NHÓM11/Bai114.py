import random
VeSo=[]
while len(VeSo)<6:
    n=random.randint(1, 50)
    if n not in VeSo:
        VeSo.append(n)
VeSo.sort()
print(VeSo)