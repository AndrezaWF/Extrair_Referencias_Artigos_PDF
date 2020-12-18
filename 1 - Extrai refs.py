"""
PROGRAMA PARA EXTRAIR REFERÊNCIAS DOS PDFs -  É CRIADO UM TXT PARA ARMAZENAR AS REFS DE CADA ARTIGO - DEPOIS CONCATENO ESSAS REFS NA TAG <citations> DOS XMLs
andrezawf@gmail.com
"""

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO
from io import StringIO
import codecs
import re


def pdf_to_text(path): #Função retirada de https://stackoverflow.com/questions/5725278/how-do-i-use-pdfminer-as-a-library
    manager = PDFResourceManager()
    retstr = BytesIO()
    layout = LAParams(all_texts=True)
    device = TextConverter(manager, retstr, laparams=layout)
    filepath = open(path, 'rb')
    interpreter = PDFPageInterpreter(manager, device)

    for page in PDFPage.get_pages(filepath, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()
    print(text)

    filepath.close()
    device.close()
    retstr.close()
    return text

def localiza_ref(lista):

        flag = "Referências \n" in lista

        if flag == True:
             pos = lista.index("Referências \n")
        else:
            flag = "Referências\n" in lista
            if flag == True:
                pos = lista.index("Referências\n")
            else:
                flag = "References\n" in lista
                if flag == True:
                    pos = lista.index("References\n")
                else:
                    flag = "Referˆencias\n" in lista
                    if flag == True:
                        pos = lista.index("Referˆencias\n")
                    else:
                        flag = "6. Referências \n" in lista
                        if flag == True:
                            pos = lista.index("6. Referências \n")
                        else:
                            flag = "Referências  \n" in lista
                            if flag == True:
                                pos = lista.index("Referências  \n")
                            else:
                                flag = "References \n" in lista
                                if flag == True:
                                    pos = lista.index("References \n")
                                else:
                                    flag = "References\xa0\n" in lista
                                    if flag == True:
                                        pos = lista.index("References\xa0\n")
                                    else:
                                        flag = "7.  Referências \n" in lista
                                        if flag == True:
                                            pos = lista.index("7.  Referências \n")
                                        else:
                                            flag = "Referencias \n" in lista
                                            if flag == True:
                                                pos = lista.index("Referencias \n")
                                            else:
                                                flag = "5. Referências \n" in lista
                                                if flag == True:
                                                    pos = lista.index("5. Referências \n")

        

        return lista[pos+1:len(lista)]
       


def corrige_caracteres(lista2):

        lista2 = [l.replace('c¸˜ao','ção') for l in lista2]  
        lista2 = [l.replace('´a', 'á') for l in lista2]
        lista2 = [l.replace('´e','é') for l in lista2]
        lista2 = [l.replace('´i','í') for l in lista2]
        lista2 = [l.replace('´o','ó') for l in lista2]
        lista2 = [l.replace('´u','ú') for l in lista2]
        lista2 = [l.replace('˜a', 'ã') for l in lista2]
        lista2 = [l.replace('a´','á') for l in lista2]
        lista2 = [l.replace('e´','é') for l in lista2]
        lista2 = [l.replace('o´','ó') for l in lista2]
        lista2 = [l.replace('u´','ú') for l in lista2]
        lista2 = [l.replace('ˆo','ô') for l in lista2]  
        lista2 = [l.replace('- ','') for l in lista2]
        lista2 = [l.replace('ç ão','ção') for l in lista2]
        lista2 = [l.replace('ç ão','ção') for l in lista2]
        lista2 = [l.replace('c¸ ˜ao','ção') for l in lista2]
        lista2 = [l.replace('ˆa','â') for l in lista2]
        lista2 = [l.replace('ˆe','ê') for l in lista2]
        lista2 = [l.replace('c¸','ç') for l in lista2]
        lista2 = [l.replace('`a','à') for l in lista2]
        lista2 = [l.replace('´','í') for l in lista2]
        lista2 = [l.replace('&','&amp;') for l in lista2]
        lista2 = [l.replace('¨u','ü') for l in lista2]
        lista2 = [l.replace('¨o','ö') for l in lista2]
        lista2 = [l.replace('”','&quot;') for l in lista2]
        lista2 = [l.replace('“','&quot;') for l in lista2]
        lista2 = [l.replace('’','&apos;') for l in lista2]
        lista2 = [l.replace('ç ˜oes','ções') for l in lista2]
        lista2 = [l.replace('˜o','õ') for l in lista2]
        lista2 = [l.replace('','') for l in lista2]
        lista2 = [l.replace('>','&gt;') for l in lista2]
        lista2 = [l.replace('<','&lt;') for l in lista2]
        lista2 = [l.replace('¸c˜o','çõ;') for l in lista2]
        lista2 = [l.replace('"','&quot;') for l in lista2]
        lista2 = [l.replace("'",'&apos;') for l in lista2]  
        
        return ' '.join(lista2)


def main():

    n_art = int(input("Digite o número de artigos:"))
    print("\n")

    for n in range(1, n_art+1):
        nome = str(n)+".pdf"
        print("\tLendo artigo "+nome+".")

        text = pdf_to_text(nome)
        #print(text)

        string = text.decode("utf-8", errors='ignore')
        #print(minha_string)

        lista = string.splitlines(keepends=True) #Transforma o arquivo em uma lista
        #print(lista)

        lista2 = localiza_ref(lista) #Localiza a palavra referências na lista e retorna uma lista contendo as refs
        lista3 = corrige_caracteres(lista2) #Corrige caracteres e faz as substituições de <, >, &, ' e " pelos seus equivalentes em html.

        arquivo = open(str(n)+'.txt', 'w', errors = 'ignore') 
        arquivo.write(lista3)
        print("Criado o .txt contendo as refs do artigo "+nome+".\n")
        arquivo.close()

        minha_string = ''
        lista = ''
        lista2 = ''
        lista3 = ''

    print("________Referências extraídas.________")

main()

        

					
