#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal 
#y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> 
#es el índice de masa corporal calculado redondeado con dos decimales.
#peso en kilogramos dividido por la estatura en metros cuadrados(o altura*altura)

def bmi(altura, peso,edad=28):
    imc = round(float(peso) / (float(altura)*float(altura)))
    print(f"Tu bmi es :{imc}")   
    if imc <18 :
        print("Tienes bajo peso")
    elif imc >=18 and imc<25:
        print("Tienes un peso normal")
    elif imc >=25 and imc <30:
        print("Tienes sobrepeso")
    elif imc >=30 and imc <34:
        print("Tienes Obesidad grado I")
    elif imc >=34 and imc <39:
        print("Tienes obesidad grado II")
    elif imc >=40:
        print("Tienes grado III Obesidad Mórbida")
bmi(1.50,75)
bmi(peso=75, altura=1.50)
