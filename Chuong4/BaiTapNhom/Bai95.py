bienso=input("Nhap vao bien so xe: ")
if len(bienso)==6 and \
   bienso[0]>="A" and bienso[0]<="Z" and\
   bienso[1]>="A" and bienso[1]<="Z" and\
   bienso[2]>="A" and bienso[2]<="Z" and\
   bienso[3]>="0" and bienso[3]<="9" and\
   bienso[4]>="0" and bienso[4]<="9" and\
   bienso[5]>="0" and bienso[5]<="9":
      print("Day la bien so xe cu.")
elif(len(bienso)==7) and\
   bienso[0]>="0" and bienso[0]<="9" and\
   bienso[1]>="0" and bienso[1]<="9" and\
   bienso[2]>="0" and bienso[2]<="9" and\
   bienso[3]>="0" and bienso[3]<="9" and\
   bienso[4]>="A" and bienso[4]<="Z" and\
   bienso[5]>="A" and bienso[5]<="Z" and\
   bienso[6]>="A" and bienso[6]<="Z":
      print("Day la bien so xe moi.")
else:
   print("Bien so xe khong ton tai.")