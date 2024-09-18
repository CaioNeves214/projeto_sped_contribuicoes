from os import system
from time import sleep
from tkinter import filedialog as fd
from tkinter import messagebox as msg

arquivo = fd.askopenfilename(defaultextension=".txt")
novo_sped = []
pular_linha = False
cont_registros = 0
cont_registros_0 = 0
cont_registros_150 = 0
cont_registros_190 = 0
cont_registros_200 = 0
cont_registros_500 = 0
cont_registros_1000 = 0
cont_registros_1100 = 0
cont_registros_1500 = 0
cont_registros_c = 0
cont_registros_f = 0
cont_registros_f010 = 0
cont_registros_f100 = 0
cont_registros_f130 = 0
cont_registros_totalizadores = 0

system('cls')
try:
    with open(arquivo, 'r', encoding='ASCII', errors='ignore') as sped:
        ler = sped.readlines()

    for linha in ler:
        is_c170 = False
        pular_linha = False
        
        # REGISTRO DE CLIENTES
        if linha.startswith("|0150|"):
            cont_registros_150 += 1
            # cont_registros_0 = cont_registros_0+1
        #     conteudo_linha = linha.split("|")
        #     insc_estadual = conteudo_linha[7].split()
        #     if len(insc_estadual) != 13:
        #         conteudo_linha[7] = ''
        #         nova_linha = '|'.join(conteudo_linha)
        #         novo_sped.append(nova_linha)
        #         cont_registros_c = cont_registros_c+1
        #         pular_linha = True
        
        if linha.startswith("|0190|"):
            cont_registros_190 += 1
            
        if linha.startswith("|0200|"):
            cont_registros_200 += 1
        
        if linha.startswith("|0500|"):
            cont_registros_500 += 1
        
        if linha.startswith("|1100|"):
            cont_registros_1100 += 1
        
        if linha.startswith("|1500|"):
            cont_registros_1500 += 1
        
        if linha.startswith("|0990|"):
            cont_registros += 1
            pular_linha = True
            nova_linha = linha.replace(linha, f'|0990|{cont_registros_0+1}|\n')
            novo_sped.append(nova_linha)
                
        if linha.startswith("|C100|0|"):
            pular_linha = True
            continue
        
        if linha.startswith("|C100|1|"):
            pular_linha = False
            
        if linha.startswith("|C170|"):
            conteudo_linha = linha.split("|")
            if (conteudo_linha[25] == '01' or conteudo_linha[25] == '05') and (conteudo_linha[31] == '01' or conteudo_linha[31] == '05'):
                is_c170 = True
                conteudo_linha[27] = '0,65'
                conteudo_linha[33] = '3' 
                nova_linha = '|'.join(conteudo_linha)
                novo_sped.append(nova_linha)
                cont_registros_c += 1
                cont_registros += 1
        
        if linha.startswith("|C990|"):
            cont_registros += 1
            pular_linha = True
            nova_linha = linha.replace(linha, f'|C990|{cont_registros_c+1}|\n')
            novo_sped.append(nova_linha)
            
        if linha.startswith("|D"):
            pular_linha = False
            
        # BLOCO F
        if linha.startswith("|F001|"):
            cont_registros_f = cont_registros_f+1
            conteudo_linha = linha.split("|")
            if conteudo_linha[2] == '1':
                conteudo_linha[2] = '0'
                nova_linha = '|'.join(conteudo_linha)
                novo_sped.append(nova_linha)
                cont_registros += 1
                pular_linha = True
        
        if linha.startswith("|F100|"):
            cont_registros_f100 = cont_registros_f100 + 1
        
        if linha.startswith("|F130|"):
            cont_registros_f130 = cont_registros_f130 + 1
            
        if linha.startswith("|F990|"):
            nova_linha = linha.replace(linha, f'|F990|{cont_registros_f+1}|\n')
            novo_sped.append(nova_linha)
            cont_registros += 1
            pular_linha = True      
            
        if linha.startswith("|1001|"):
            cont_registros_1000 = cont_registros_1000+1
            conteudo_linha = linha.split("|")
            if conteudo_linha[2] == '1':
                conteudo_linha[2] = '0'
                nova_linha = '|'.join(conteudo_linha)
                novo_sped.append(nova_linha)
                pular_linha = True
                cont_registros += 1
        
        if linha.startswith("|1990|"):
            nova_linha = linha.replace(linha, f'|1990|{cont_registros_1000+1}|\n')
            novo_sped.append(nova_linha)
            cont_registros += 1
            pular_linha = True
            
        if linha.startswith("|9900|0140|"):
            novo_sped.append(linha)
            novo_sped.append(f"|9900|0150|{cont_registros_150+1}|\n")
            novo_sped.append(f"|9900|0190|{cont_registros_190+1}|\n")
            novo_sped.append(f"|9900|0200|{cont_registros_200+1}|\n")
            novo_sped.append(f"|9900|0500|{cont_registros_500+1}|\n")
            cont_registros_totalizadores += 5
            cont_registros += 5
            pular_linha = True
            
        if linha.startswith("|9900|0150|"):
            pular_linha = True
        
        if linha.startswith("|9900|0190|"):
            pular_linha = True
            
        if linha.startswith("|9900|0200|"):
            pular_linha = True
            
        if linha.startswith("|9900|0500|"):
            pular_linha = True
            
        if linha.startswith("|9900|1001|"):
            novo_sped.append(linha)
            novo_sped.append(f"|9900|1100|{cont_registros_1100+1}|\n")
            novo_sped.append(f"|9900|1500|{cont_registros_1500+1}|\n")
            cont_registros_totalizadores += 3
            cont_registros += 3
            pular_linha = True
            
        if linha.startswith("|9900|1100|"):
            pular_linha = True
            
        if linha.startswith("|9900|1500|"):
            pular_linha = True
            
        if linha.startswith("|9900|F001|"):
            novo_sped.append(linha)
            novo_sped.append(f"|9900|F010|{cont_registros_f010+1}|\n")
            novo_sped.append(f"|9900|F100|{cont_registros_f100+1}|\n")
            novo_sped.append(f"|9900|F130|{cont_registros_f130+1}|\n")
            cont_registros_totalizadores += 4
            cont_registros += 4
            pular_linha = True
        
        if linha.startswith("|9990|"):
            nova_linha = linha.replace(linha, f"|9990|{cont_registros_totalizadores+2}|\n")
            novo_sped.append(nova_linha)
            pular_linha = True
            
        if linha.startswith("|9999|"):
            nova_linha = linha.replace(linha, f'|9999|{cont_registros+2}|\n')
            novo_sped.append(nova_linha)
            pular_linha = True

        if not pular_linha and not is_c170:
            novo_sped.append(linha)  
            cont_registros += 1
            if linha.startswith("|C"):
                cont_registros_c += 1
            if linha.startswith("|F"):
                cont_registros_f += 1
            if linha.startswith("|0"):
                cont_registros_0 += 1
            if linha.startswith("|1"):
                cont_registros_1000 += 1
            if linha.startswith("|9"):
                cont_registros_totalizadores += 1
                

    files = [('Escrituração Fiscal', '*.txt')]
    sped_novo = fd.asksaveasfile(defaultextension='.txt', mode="w", filetypes=files)
    sped_novo.writelines(novo_sped)
    sped.close()

except Exception as e:
    msg.showerror("erro", "Não foi possivel abrir o arquivo:\n{}".format(str(e)))
    print(e)
    