def romanToInt(texto):
    # diccionario para mapear numeros romanos
    table = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
}
    # inicializacion de variables
    resultado = 0
    texto = texto[::-1]

    for letra in texto:
        numero = table[letra] 
        print('Numero actual: ', numero)
        print('Resultado: ', resultado)

        if numero * 3 > resultado:
            resultado += numero
        else:
            resultado -= numero       

    return resultado

print(romanToInt("LIX"))