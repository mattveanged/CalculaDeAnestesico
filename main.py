nomeanestesico = input('Anestésico: ')
concentracao = float(input('Concentração do Anestésico (%) : '))
dosemax = float(input('Dosagem máxima por peso: '))
peso = float(input('Peso do paciente (KG): '))

if concentracao <= 0:
    print('Dado Incorreto')


concentracaoml = concentracao * 10
tubete = concentracaoml * 1.8
pacientemax = dosemax * peso
print('{:.2f}mg' .format(pacientemax))

quantidadetubete = pacientemax / tubete
print('{:.2f} tubetes' .format(quantidadetubete))

