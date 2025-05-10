# Questão 5 - Inversão de string
# Escreva um programa que inverta os caracteres de uma string.
# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

def inverter_string(string):
    string_invertida = ""
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    print(f"String invertida: {string_invertida}")


if __name__ == "__main__":
    texto = input("Informe uma string para inverter: ")
    inverter_string(texto)
