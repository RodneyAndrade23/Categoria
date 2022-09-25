n1 = int(input('Digite o ano que você nasceu: '))
i = 2022 - n1

if i > 0 and i <= 9:
    print('Sua categoria é a MIRIM!')

elif (i > 9 and i < 15):
    print('Sua categoria é a INFANTIL!')

if (i >= 15 and i <= 19):
    print('Sua categoria é a JUNIOR!')

elif i > 19:
    print('Sua categoria é a Sênior!')

