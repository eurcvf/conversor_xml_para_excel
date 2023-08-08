import xmltodict 
import os # manusear arquivos, pastas e etc
import pandas as pd # para criar as tabelas

# Pegar informações dos arquivos
def pegar_infos(nome_arquivo, valores):
  # print(f'Peguei as informações: {nome_arquivo}')
  # Para abrir o arquivo
  with open(f'nfs/{nome_arquivo}', "rb") as arquivo_xml:
    dic_arquivo = xmltodict.parse(arquivo_xml)
    
    if 'NFe' in dic_arquivo:
      infos_nf = dic_arquivo['NFe']['infNFe']
    else:
      infos_nf = dic_arquivo['nfeProc']['NFe']['infNFe']
    numero_nf = infos_nf['@Id']
    emissor_nf = infos_nf['emit']['xNome']
    nome_cliente_nf = infos_nf['dest']['xNome']
    endereco_nf = infos_nf['dest']['enderDest']
    if 'vol' in infos_nf['transp']:
      peso_nf = infos_nf['transp']['vol']['pesoB']
    else:
      peso_nf = 'Não informado'
    valores.append([numero_nf, emissor_nf, nome_cliente_nf, endereco_nf, peso_nf])

lista_arquivos = os.listdir('nfs')

colunas = ['numero_nf', 'emissor_nf', 'nome_cliente_nf', 'endereco_nf', 'peso_nf']
valores = []

for arquivo in lista_arquivos:
  pegar_infos(arquivo, valores)
tabela = pd.DataFrame(columns=colunas, data=valores)
tabela.to_excel('NFesFiscais.xlsx', index=False)
print('Finalizei')