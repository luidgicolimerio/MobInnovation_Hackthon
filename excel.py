import openpyxl
import tinydb
import json


with open("database.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

for cont in dados.items():
    total = len(cont[1])


book = openpyxl.Workbook()
del book['Sheet']

book.create_sheet('HACKATHON')
seg = book['HACKATHON']


n = 0
num = 1
listas = []


# Busca um item de dentro do dicionário que está dentro de um dicionário

seg.append(['USUARIO', 'SENHA', 'CAPACETE', 'PNEUS BONS', 'MOTO EM DIA'])
for x in range(0,total):
    for default in dados.items():
        nome = default[1][f'{num}']['user']
        senha = default[1][f'{num}']['password']
        cap = 'True'
        pneu = 'False'
        moto = 'True'


        # if q1 == 'sim':        q1, q2, q3 são as perguntas que serão feitas no forms
        #     cap = True
        # else:
        #     cap = False
        # if q2 == 'sim':
        #     pneu = True
        # else:
        #     pneu = False
        # if q3 == 'sim':
        #     moto = True
        # else:
        #     moto = False

        lista = []
        lista.append(nome)
        lista.append(senha)
        lista.append(cap)
        lista.append(pneu)
        lista.append(moto)


        seg.append([nome, senha, cap, pneu , moto])
        listas.append(lista)
        
        num +=1

print(listas)

    


book.save('tabela_Excel.xlsx')
