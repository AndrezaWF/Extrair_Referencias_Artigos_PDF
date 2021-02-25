"""
andrezawf@gmail.com
PROGRAMA PARA EXTRAIR REFERÊNCIAS DOS PDFs: O programa lê o arquivo PDF e recorta as suas referências.
É CRIADO UM TXT PARA ARMAZENAR AS REFS DE CADA ARTIGO
É necessário instalar as bibliotecas pdfminer.six e pdfminer.py:  pip install pdfminer.six
                                                                  pip install pdfminer.py
Os artigos devem estar nomeados iniciando em 1. Por exemplo: 1.pdf, 2.pdf, 3.pdf, ...
Os artigos em formato PDF devem estar dentro da mesma pasta deste programa.
"""

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO
from io import StringIO
import codecs
import re


def pdf_to_text(path):  #Função retirada de https://gist.github.com/skhani/c2ceaa8c9ed7c980ac8571a56ac656a4
    manager = PDFResourceManager()
    retstr = BytesIO()
    layout = LAParams(all_texts=True)
    device = TextConverter(manager, retstr, laparams=layout)
    filepath = open(path, 'rb')
    interpreter = PDFPageInterpreter(manager, device)

    for page in PDFPage.get_pages(filepath, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    filepath.close()
    device.close()
    retstr.close()
    return text

def localiza_ref(lista):    

        flag = "Referências \n" in lista

        if flag == True:
             indice_inicio_refs = lista.index("Referências \n")
        else:
            flag = "Referências\n" in lista
            if flag == True:
                indice_inicio_refs = lista.index("Referências\n")
            else:
                flag = "References\n" in lista
                if flag == True:
                    indice_inicio_refs = lista.index("References\n")
                else:
                    flag = "Referˆencias\n" in lista
                    if flag == True:
                        indice_inicio_refs = lista.index("Referˆencias\n")
                    else:
                        flag = "6. Referências \n" in lista
                        if flag == True:
                            indice_inicio_refs = lista.index("6. Referências \n")
                        else:
                            flag = "Referências  \n" in lista
                            if flag == True:
                                indice_inicio_refs = lista.index("Referências  \n")
                            else:
                                flag = "References \n" in lista
                                if flag == True:
                                    indice_inicio_refs = lista.index("References \n")
                                else:
                                    flag = "References\xa0\n" in lista
                                    if flag == True:
                                        indice_inicio_refs = lista.index("References\xa0\n")
                                    else:
                                        flag = "7.  Referências \n" in lista
                                        if flag == True:
                                            indice_inicio_refs = lista.index("7.  Referências \n")
                                        else:
                                            flag = "Referencias \n" in lista
                                            if flag == True:
                                                indice_inicio_refs = lista.index("Referencias \n")
                                            else:
                                                flag = "5. Referências \n" in lista
                                                if flag == True:
                                                    indice_inicio_refs = lista.index("5. Referências \n")
                                                else:
                                                    flag = "7. Referências\n" in lista
                                                    if flag == True:
                                                        indice_inicio_refs = lista.index("7. Referências\n")
                                                    else:
                                                        flag = "Referências \xa0\n" in lista
                                                        if flag == True:
                                                            indice_inicio_refs = lista.index("Referências \xa0\n")
                                                        else:
                                                            flag = "Referências bibliográficas \n" in lista
                                                            if flag == True:
                                                                indice_inicio_refs = lista.index("Referências bibliográficas \n")
                                                            else:
                                                                print("****Referências não encontradas.****\n")
                                                                return False
                                                          
        

        lista_referencias = lista[indice_inicio_refs+1:len(lista)]  #Gera uma nova lista contendo as referências.
        return lista_referencias


def corrige_caracteres(lista_referencias):

        lista_referencias = [l.replace('c¸˜ao','ção') for l in lista_referencias]  
        lista_referencias = [l.replace('´a', 'á') for l in lista_referencias]
        lista_referencias = [l.replace('´e','é') for l in lista_referencias]
        lista_referencias = [l.replace('´ı','í') for l in lista_referencias]
        lista_referencias = [l.replace('´o','ó') for l in lista_referencias]
        lista_referencias = [l.replace('´o','ó') for l in lista_referencias]
        lista_referencias = [l.replace('´u','ú') for l in lista_referencias]  
        lista_referencias = [l.replace(' ´a', 'á') for l in lista_referencias]
        lista_referencias = [l.replace(' ´e','é') for l in lista_referencias]
        lista_referencias = [l.replace('`e','é') for l in lista_referencias]
        lista_referencias = [l.replace(' ´ı','í') for l in lista_referencias]
        lista_referencias = [l.replace(' ´o','ó') for l in lista_referencias]
        lista_referencias = [l.replace(' ´u','ú') for l in lista_referencias]   
        lista_referencias = [l.replace('˜a', 'ã') for l in lista_referencias]
        lista_referencias = [l.replace('˜o','õ') for l in lista_referencias]
        lista_referencias = [l.replace('a´','á') for l in lista_referencias]
        lista_referencias = [l.replace('e´','é') for l in lista_referencias]
        lista_referencias = [l.replace('o´','ó') for l in lista_referencias]
        lista_referencias = [l.replace('u´','ú') for l in lista_referencias]
        lista_referencias = [l.replace('ˆo','ô') for l in lista_referencias]  

        lista_referencias = [l.replace('ˆa','â') for l in lista_referencias]
        lista_referencias = [l.replace('ˆe','ê') for l in lista_referencias]
        lista_referencias = [l.replace('c¸','ç') for l in lista_referencias]
        lista_referencias = [l.replace('`a','à') for l in lista_referencias]
        lista_referencias = [l.replace('´','í') for l in lista_referencias]
        lista_referencias = [l.replace('¨u','ü') for l in lista_referencias]
        lista_referencias = [l.replace('¨o','ö') for l in lista_referencias]
        lista_referencias = [l.replace('¨a','ä') for l in lista_referencias]
        lista_referencias = [l.replace('ç ˜oes','ções') for l in lista_referencias]
        lista_referencias = [l.replace('ç ões','ções') for l in lista_referencias]
        lista_referencias = [l.replace('','') for l in lista_referencias]
        lista_referencias = [l.replace('¸c˜o','çõ;') for l in lista_referencias]
        lista_referencias = [l.replace('c¸ ˜ao','ção') for l in lista_referencias]
        lista_referencias = [l.replace('ç ão','ção') for l in lista_referencias]
        lista_referencias = [l.replace(' ú','ú') for l in lista_referencias]


        lista_referencias = [l.replace('&','&amp;') for l in lista_referencias]
        lista_referencias = [l.replace('"','&quot;') for l in lista_referencias]
        lista_referencias = [l.replace("'",'&apos;') for l in lista_referencias]
        lista_referencias = [l.replace('”','&quot;') for l in lista_referencias]
        lista_referencias = [l.replace('“','&quot;') for l in lista_referencias]
        lista_referencias = [l.replace('’','&apos;') for l in lista_referencias] 
        lista_referencias = [l.replace('‘','&apos;') for l in lista_referencias]
        lista_referencias = [l.replace('>',' &gt;') for l in lista_referencias]
        lista_referencias = [l.replace('<','&lt; ') for l in lista_referencias]
        lista_referencias = [l.replace('\n','') for l in lista_referencias]
        lista_referencias = [l.replace('#','\n') for l in lista_referencias]
        

        lista_referencias =' '.join(lista_referencias)
        return lista_referencias

    

def main():

    cont = 0
    print("==========================================================")
    print("\tPROGRAMA PARA EXTRAÇÃO DE REFERÊNCIAS")
    print("==========================================================")
    print("\nOs artigos devem estar nomeados como 1.pdf, 2.pdf, 3.pdf, ...________")
    print("\n")    
    numero_de_artigos = int(input("Digite o número de artigos PDF presentes na pasta:"))
    print("\n")

    for n in range(1, numero_de_artigos+1):
        nome_artigo = str(n)+".pdf"                             #Gera o nome do artigo a ser lido 1.pdf, 2.pdf, 3.pdf...               
        print("\tLendo artigo "+nome_artigo+".")

        texto_art_bin = pdf_to_text(nome_artigo)                #Função retorna o texto completo do artigo em binário
        
        texto_artigo = texto_art_bin.decode("utf-8", errors='ignore')  
    
        lista_completa = texto_artigo.splitlines(keepends=True) #Transforma o conteúdo do arquivo em uma lista
        #print(lista_completa)

        lista_de_refs = localiza_ref(lista_completa)            #Localiza a palavra referências na lista e retorna uma lista contendo refs
        #print(lista_de_refs)

        if lista_de_refs == False:
            arquivo = open(str(n)+'.txt', 'w', errors = 'ignore') 
            arquivo.write("Referencias não encontradas.")
            arquivo.close()

            lista_completa = ''
            lista_de_refs = ''
            lista_refs_corrigida = ''

        else:
            for elemento in lista_de_refs:
                cont = cont+1
                if elemento == "\n":
                    lista_de_refs[cont-1] = "#" 

            lista_refs_corrigida = corrige_caracteres(lista_de_refs) #Corrige caracteres e faz as substituições de <, >, &, ' e " pelos seus equivalentes em html.
            lista_refs_corrigida_= lista_refs_corrigida.replace("- ", "")

            arquivo = open(str(n)+'.txt', 'w', errors = 'ignore') 
            arquivo.write(lista_refs_corrigida_)
            print("****Criado o .txt contendo as refs do artigo "+nome_artigo+". ****\n")
            arquivo.close()


            lista_completa = ''
            lista_de_refs = ''
            lista_refs_corrigida = ''
            cont = 0

    print("\n\t*****Referências extraídas.*****")

main()
