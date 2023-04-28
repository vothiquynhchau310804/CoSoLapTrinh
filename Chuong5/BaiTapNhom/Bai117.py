import numpy as np

def main():
    Lx = []
    Ly = []
    while True:
        x = input("Toa do x: ")
        y = input("Toa do y: ")
        if x != "" or y != "":
            Lx.append(float(x))
            Ly.append(float(y))
        elif x=="":
            break
    tb_x = average(Lx)
    tb_y = average(Ly)
    x_array = np.array(Lx)
    y_array = np.array(Ly)
    m = (sum_array(x_array * y_array) - (sum_array(x_array) * sum_array(y_array) / len(x_array))) / (sum_array(x_array * x_array) - ((sum_array(x_array) * sum_array(x_array)) / len(x_array)))
    b = tb_y - m * tb_x
    print("y=", round(m,2),"x+", round(b,2), sep="")
def sum_array(vector):
    sum = 0
    for el in vector:
        sum = sum + el
    return sum
def average(array):
    suma = 0
    for element in array:
        suma = suma + element
    mean = suma / len(array)
    return mean

main()