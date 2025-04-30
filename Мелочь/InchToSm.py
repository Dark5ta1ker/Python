import math

def perevod(inch, weight, hidht):

    hidhtTransformed = (inch/math.sqrt(weight*weight + hidht*hidht))*hidht
    weightTransformed = (inch/math.sqrt(weight*weight + hidht*hidht))*weight
    
    hidhtSm = hidhtTransformed*2.54
    weightSM = weightTransformed*2.54
    
    return "При диагонали " + str(inch) + " дюймов и соотношении сторон " + str(weight) + "/" + str(hidht) + "\n Длина будет равна: " + str(weightSM) + " сантиметров\n Ширина будет равна: " + str(hidhtSm) + " сантиметров"

print (perevod(float(input("Введите диагональ в дюймах\n")), int(input("Ведите ширину монитора (из соотношения, например 16 из 16/9)\n")), int(input("Ведите высоту монитора (из соотношения, например 9 из 16/9)\n"))))