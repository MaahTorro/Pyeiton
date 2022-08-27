def verificaSeTriangulo(valor1, valor2, valor3):
    if (valor1+valor2) >= valor3 and (valor2+valor3) >= valor1 and (valor3+valor1) >= valor2:
        return 1
    return 0

if verificaSeTriangulo(1,1,1) == 1:
    print("é um triângulo")
else:
    print("Não é um triângulo")