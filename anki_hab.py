import pandas as pd
import numpy as np
import time
import random
import plotly.express as px
import streamlit as st
import numpy as np
from scipy.optimize import minimize_scalar
import genanki
from fpdf import FPDF
import requests
from io import BytesIO
import streamlit.components.v1 as components
from PIL import Image
import string
import os
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import barcode
import zipfile
from barcode.writer import ImageWriter
<<<<<<< HEAD
import urllib.parse
=======
>>>>>>> 4d8c41f4356afa3da882388a684e9fdfea15187c

urlItens = "https://github.com/NiedsonEmanoel/NiedsonEmanoel/raw/main/enem/An%C3%A1lise%20de%20Itens/OrdenarPorTri/gerador/provasOrdernadasPorTri.csv"
dItens = pd.read_csv(urlItens, encoding='utf-8', decimal=',')

def flashnamesa(SG):
    if SG == 'Natureza': return 'CN'
    elif SG == 'Matemática': return 'MT'
    elif SG == 'Humanas': return 'CH'
    else: return 'LC'

#Definindo Classe do PDF de Saída
class PDF(FPDF):
    def header(self):
       self.image('fundo.png', x=0, y=0, w=self.w, h=self.h, type='png')

    def add_my_link(self, x, y, txt, link):
        self.set_xy(x, y)
        self.set_text_color(0, 0, 0)
        self.set_font('Times', 'BI', 12)
        self.add_link()

        # obter a largura do texto
        w = self.get_string_width(txt) + 6  # adicione uma margem de 3 em cada lado

        # desenhar o retângulo em torno do texto
        self.set_fill_color(255, 112, 79)
        self.cell(w, 10, '', border=0, ln=0, fill=True, align='C', link=link)

        # adicionar o texto com o link
        self.set_xy(x, y)
        self.cell(w, 10, txt, border=0, ln=1, align='C', link=link)

    # Page footer
    def footer(self):
      if self.page_no() != 1:
        self.image("fundo2.png", x=90, y=283, h=10,type='png')
        self.set_y(0)
        self.set_font('Arial', 'BI', 8)
        self.cell(0, 8, '     '+str(self.page_no()) + '/{nb}', 0, 0, 'C')

def toYoutube(textPrompt):
    try:
<<<<<<< HEAD
      # TEST STUFF (NÃO DELETAR ATÉ TER CERTEZA QUE FUNCIONARÁ CORRETAMENTE)
      encoded_query = urllib.parse.quote_plus(textPrompt)
      search_query = f"https://www.youtube.com/results?search_query={encoded_query}"
      print(f"MUITA CALMA NESSA HORA JÃO CLEBER: {search_query}")
      # END TEST STUFF
=======
      search_query = "https://www.youtube.com/results?search_query=" + "+".join(textPrompt.split())
>>>>>>> 4d8c41f4356afa3da882388a684e9fdfea15187c
    except:
      search_query = 'N/A'
    return(search_query)

def remover_caracteres_invalidos(texto):
        numAssc = 251
        try:
<<<<<<< HEAD
            caracteres_invalidos = [char for char in texto if ord(char) > numAssc]
            texto_substituido = ''.join('' if ord(char) > numAssc else char for char in texto)
            print(f"Caracteres inválidos substituídos: {caracteres_invalidos}")

            return texto_substituido
        except:
            print('sorry')

            return(texto)
        
=======
          caracteres_invalidos = [char for char in texto if ord(char) > numAssc]
          texto_substituido = ''.join('' if ord(char) > numAssc else char for char in texto)
          print(f"Caracteres inválidos substituídos: {caracteres_invalidos}")
          return texto_substituido
        except:
          print('sorry')
          return(texto)
>>>>>>> 4d8c41f4356afa3da882388a684e9fdfea15187c

def Capa(dItens):
  todos_itens = ' '.join(s for s in dItens['OCRSearch'].apply(str).values)
  todos_itens = todos_itens.replace(';',  ' ').replace('/',  ' ')

  all_letters = list(string.ascii_lowercase + string.ascii_uppercase)

  stop_words = all_letters +  ['a', 'A', 'b', 'B', 'c', 'C', 'd','figura', 'D', 'e', 'E', 'v', 'nan','pela', 'ser', 'de', 'etc', '(s)', 'do', 'da', 'por', 'para', 'entre', 'se', 'um', 'até', 'ele', 'ela', 'qual', 'bem', 'só', 'mesmo', 'uma', 'um', 'mais', 'menos', 'outro', 'porque', 'por que', 'cada', 'muito', 'todo', 'foram', 'tem', 'meio', 'país', 'una', 'for',
                'uma', 'na', 'su', 'with', 'no','estes','mesma', 'lá', 'that', 'vo' 'pela', 'pelo', 'h', 'H', 'CH', 'ao', 'com', 'que', 'em', 'dos', 'das', 'eu', 'lo', 'the', 'me', 'y', 'la', 'en', 'en', 'to', 'quem', 'and', 'sem', 'on', 'at', 'essa', 'sem', 'uso', 'esse', 'las', 'suas', 'el', 'poi', 'pai', 'doi', 'in', 'pois', 'con', 'of',
                'ainda', 'não', 'o', 'a', 'os','mê','próximo', 'apresenta','quando', 'meu', 'acordo', 'grande', 'saída', 'dessa', 'as', 'deve', 'Além', 'cinco', 'nessa', 'conforme', 'contendo', 'interior', 'Disponível', 'disponível', 'ocorre', 'vezes', 'através', 'grupo', 'tipo', 'algumas', 'causa', 'considerando', 'essas', 'formação', 'so', 'SO', 'pessoa', 'utilizada', 'alguns', 'quais', 'fio', 'outras', 'só', 'exemplo', 'está', 'oo','isso', 'fonte', 'durante', 'onde', 'caso', 'será', 'pelos', 'Disponível', 'duas', 'dois', 'onde', 'podem', 'apresentam', 'alguma', 'outra', 'seja', 'menor', 'Após', 'Considere', 'partir' 'aq', 'etapa', 'três', 'vez', 'pelas', 'dia', 'nova', 'Acesso', 'veículo', 'seus', 'têm', 'quadro', 'parte', 'desses', 'alguma', 'alta', 'sendo', 'eles', 'outros', 'respectivamente', 'lhe', 'ficou','desse', 'pode', 'nas', 'nem', 'nos', 'nesse', 'apenas', 'n', 'esses', 'igual', 'estão', 'br', 'L', 'questão', 'e', 'texto', 'são', 'é', 'como', 'à', 'no', 'mai', 'seu', 'sua', 'mais', '.', 'ano', 'ma', 'ou', 'foi', 'sobre', 'às', 'aos', 'mas', 'há', 'seguinte', 'já', 'maior', 'era', 'desde', 'diferente', 'forma', 'também']

  wc = WordCloud(background_color='black',
                stopwords=stop_words,
                collocations=False,
                colormap = 'copper',
                width=2480, height=3508, contour_width=0)  # Defina a largura e altura desejadas

  wordcloud = wc.generate(todos_itens)

  # Plotar a nuvem de palavras
  plt.figure(figsize=(10, 10))  # Ajuste o tamanho da figura conforme necessário

  a4_width_inches = 8.27
  a4_height_inches = 11.69
  dpi = 300  # Ajuste a resolução conforme necessário

  # Criar a figura com o tamanho A4
  fig, ax = plt.subplots(figsize=(a4_width_inches, a4_height_inches), dpi=dpi)

  # Plotar a nuvem de palavras
  ax.imshow(wordcloud, interpolation='bilinear')
  ax.axis("off")

  # Salvar a figura em tamanho A4
  plt.savefig("wordcloud_a4.png", bbox_inches='tight', pad_inches=0)

def generate_random_number():
    # Gerar um número inteiro aleatório entre 0 e 100000
    return random.randint(0, 100000)


def questHab(dfResult_CN, prova, Habilidade, idom, flashname):
<<<<<<< HEAD

=======
>>>>>>> 4d8c41f4356afa3da882388a684e9fdfea15187c
    dfResult_CN = dfResult_CN[dfResult_CN['OCRSearch']!='N/A']
    if (prova !='LC'):
        dfResult_CN = dfResult_CN.query("IN_ITEM_ABAN == 0 and TP_LINGUA not in [0, 1]")
    else: 
        dfResult_CN = dfResult_CN.query("IN_ITEM_ABAN == 0")
        if idom==-1: dfResult_CN = dfResult_CN.query("TP_LINGUA not in [0, 1]")
        else:
            alidom = 2 
            if idom == 0: alidom = 1
            else: alidom == 1
            dfResult_CN = dfResult_CN.query("TP_LINGUA not in ["+str(alidom)+']')
    cols_to_drop = ['TP_LINGUA', 'TX_MOTIVO_ABAN', 'IN_ITEM_ADAPTADO', 'NU_PARAM_A', 'NU_PARAM_B', 'NU_PARAM_C']
    dfResult_CN.drop(cols_to_drop, axis=1, inplace=True)

    dfResult_CN = dfResult_CN[dfResult_CN['SG_AREA'] == prova]
    dfResult_CN = dfResult_CN[dfResult_CN['IN_ITEM_ABAN'] == 0]
    dfResult_CN = dfResult_CN[dfResult_CN['CO_HABILIDADE'] == Habilidade]
    Capa(dfResult_CN)
    dfResult_CN.sort_values('theta_065', ascending=True, inplace=True)
    dfResult_CN['indexacao'] = dfResult_CN.reset_index().index + 1

    # Criar um baralho para armazenar os flashcards
    baralho = genanki.Deck(
        generate_random_number(), # Um número aleatório que identifica o baralho
        str('Questões::Habilidades::'+str(flashname)+'::H'+str(Habilidade)) # O nome do baralho
    )

    # Criar uma lista para armazenar as informações dos flashcards
    flashcards = []

    # Percorrer as linhas do dataframe dfResult_CN
    for i in dfResult_CN.index:
        # Obter o nome do arquivo de imagem da questão
        imagem = str(dfResult_CN.loc[i, "CO_ITEM"]) + '.png'
        imagemQ = str(dfResult_CN.loc[i, "CO_ITEM"]) + '.gif'

        # Obter a resposta da questão
        resposta =str('Gabarito: ')+ str(dfResult_CN.loc[i, 'TX_GABARITO'])
        inic = "Q" + str(dfResult_CN.loc[i, "CO_POSICAO"]) + ':' + str(dfResult_CN.loc[i, "ANO"]) + ' - H' + str(dfResult_CN.loc[i, "CO_HABILIDADE"].astype(int)) + " - Proficiência: " + str(dfResult_CN.loc[i, "theta_065"].round(2))

        # Criar um flashcard com a imagem e a resposta
        flashcard = genanki.Note(
            model=modelo,
            fields=[inic, '<img src="https://niedsonemanoel.com.br/enem/An%C3%A1lise%20de%20Itens/OrdenarPorTri/1.%20Itens%20BNI_/' + imagem + '"]', resposta,  '<img src="https://niedsonemanoel.com.br/enem/An%C3%A1lise%20de%20Itens/OrdenarPorTri/1.%20Itens%20BNI_/Correcao/' + imagemQ + '"]']
        )

        # Adicionar o flashcard à lista de flashcards
        flashcards.append(flashcard)

    for flashcard in flashcards:
        baralho.add_note(flashcard)

    # Criar um pacote com o baralho e as imagens
    pacote = genanki.Package(baralho)

    pacote.write_to_file('H'+str(Habilidade)+'_'+str(flashname)+'.apkg')

    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.set_title(flashname)

    pdf.add_page()
    pdf.image("wordcloud_a4.png", x=0, y=0, w=pdf.w, h=pdf.h, type='png')
    pdf.add_page()

    pdf.set_font('Times', 'B', 12)
    img_dir = 'images/'  # Diretório local para salvar as imagens

    # Criar diretório se não existir
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)


    for i in dfResult_CN.index:
        print("N"+str(dfResult_CN.loc[i, 'indexacao'])+"/"+str(len(dfResult_CN)))
        strCN ="N"+str(dfResult_CN.loc[i, 'indexacao'])+" - Q" + str(dfResult_CN.loc[i, "CO_POSICAO"])+':'+str(dfResult_CN.loc[i, "ANO"]) + ' - H'+str(dfResult_CN.loc[i, "CO_HABILIDADE"].astype(int))+ " - Proficiência: " + str(dfResult_CN.loc[i, "theta_065"].round(2))
        if 'dtype:' in strCN:
            print("...")
        else:
            try:
                pdf.ln(15)  # adicionar espaço entre o texto e a imagem
                img_filename = f"{dfResult_CN.loc[i, 'CO_ITEM']}.png"
                img_path = os.path.join(img_dir, img_filename)

                codestr = f"{dfResult_CN.loc[i, 'CO_ITEM']}"

                img_pathax = os.path.join(img_dir, str('xa'+codestr))

                code128 = barcode.get("code128", codestr, writer=ImageWriter())
                filename = code128.save(img_pathax)
                img_pathax = img_pathax+'.png'

                # Verificar se a imagem já foi baixada
                if not os.path.exists(img_path):
                    url = 'https://niedsonemanoel.com.br/enem/An%C3%A1lise%20de%20Itens/OrdenarPorTri/1.%20Itens%20BNI_/'+ str(dfResult_CN.loc[i, "CO_ITEM"]) + '.png'
                    response = requests.get(url)

                    with open(img_path, 'wb') as img_file:
                        img_file.write(response.content)
                        print(img_path)

                # Abrir a imagem do diretório local
                with Image.open(img_path) as img:
                    img.thumbnail((160, 160))
                    width, height = img.size

                pdf.set_fill_color(255, 112, 79)
             #   pdf.ln(15)
                pdf.cell(0, 10, strCN, 0, 1, 'C', 1)
                pdf.ln(10)   # adicionar espaço entre o texto e a imagem

                # caCNular a posição y para centralizar a imagem
                y = pdf.get_y()

                # ajustar as coordenadas de posição e o tamanho da imagem
                pdf.image(img_path, x=pdf.w / 2 - width / 2, y=y, w=width, h=height)
                pdf.image(img_pathax, x=3, y=-3,  h=25) #w=45,
                pdf.ln(10)

                link = toYoutube(remover_caracteres_invalidos(dfResult_CN.loc[i, "OCRSearch"]))
                pdf.add_my_link(170, 25, "RESOLUÇÃO", link)
                pdf.set_text_color(0, 0, 0)
                pdf.set_font('Times', 'B', 12)

                # adicionar quebra de página
                pdf.add_page()
            except FileNotFoundError:
                print(strCN)
                continue

    #GAB
    page_width = 190
    cell_width = 19
    max_cols = int(page_width / cell_width)

    # Junta as colunas do dataframe
    dfResult_CN['merged'] = dfResult_CN['indexacao'].astype(str) + ' - ' + dfResult_CN['TX_GABARITO']

    # Divide os dados em grupos de até max_cols colunas
    data = [dfResult_CN['merged'][i:i+max_cols].tolist() for i in range(0, len(dfResult_CN), max_cols)]

    # CaCNula a largura das células de acordo com o número de colunas
    cell_width = page_width / max_cols

    # Cria a tabela
    pdf.set_fill_color(89, 162, 165)
    # Title
    pdf.ln(15)
    pdf.cell(0, 10, str('GABARITO '+flashname.upper()), 0, 1, 'C', 1)
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 12)

    for row in data:
        for col in row:
            pdf.cell(cell_width, 10, col, 1, 0, 'C')
        pdf.ln() # quebra de linha para a próxima linha da tabela

    pdf.ln(5)
    pdf.set_font('Arial', 'BI', 8)

    strOut = 'H'+str(Habilidade)+'_'+str(flashname)+ '.pdf'

    pdf.output(strOut, 'F')

    return 'H'+str(Habilidade)+'_'+str(flashname)

<<<<<<< HEAD
=======

>>>>>>> 4d8c41f4356afa3da882388a684e9fdfea15187c
modelo = genanki.Model(
    187333333,
    'enemaster',
    fields=[
        {'name': 'MyMedia'},
        {'name': 'Questão'},
        {'name': 'Resposta'},
        {'name': 'Image'}
    ],
    templates=[
        {
            'name': 'Cartão 1',
            'qfmt': '<b>{{Questão}}</b><hr>{{MyMedia}}',
            'afmt': '{{FrontSide}}<br><hr><b>{{Resposta}}<hr></b></b>{{Image}}',
        },
    ])


st.set_page_config(layout='wide', page_title='Enemaster.app', initial_sidebar_state="expanded", page_icon="🧊",    menu_items={
        'About': "# Feito por *enemaster.app*"
    })

def main():
    idom = -1
    st.header('Gerador de Listas por Habilidades')
    st.divider()
    mats = st.selectbox(
    'Matéria',
    ('Linguagens', 'Humanas', 'Natureza', 'Matemática'), placeholder="Selecione uma Matéria")
#    if (mats == 'Linguagens'):
#        idi = st.selectbox(
#        'Idioma',
#        ('INGLÊS', 'ESPANHOL'), placeholder="Selecione uma Matéria")
#        if idi == 'INGLÊS': idom = 0
#        else: idom = 1
    habs = st.multiselect(
    'Selecione as Habilidades',
    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31], placeholder="Selecione as Habilidades")
    st.divider()
    st.info('• H31 é reservada para questões sem Habilidade definida.')
    st.info('• Por enquanto não estão sendo geradas listas de idiomas.')
    st.divider()
    if st.button("Gerar!", type="primary"):
        mat = flashnamesa(mats)
        toZip = []
        if(len(habs) > 0):
            with st.spinner("Gerando seu material..."):
                for i in habs:
                    if ((mat == 'LC' and i >= 5) and (mat == 'LC' and i <= 8)):
                        continue
                    else:
                        lt = questHab(dItens, mat, i, idom, mats)
                        toZip.append(lt+'.pdf')
                        toZip.append(lt+'.apkg')
            zip_filename = 'materialestudo.zip'
            # Crie um objeto ZipFile em modo de escrita
            with zipfile.ZipFile(zip_filename, 'w') as zipf:
                # Adicione cada arquivo à archive
                for file in toZip:
                    # Certifique-se de que o arquivo exista antes de adicioná-lo ao zip
                    if os.path.exists(file):
                        zipf.write(file, os.path.basename(file))

            # Apague os arquivos originais após zipar
            for file in toZip:
                if os.path.exists(file):
                    os.remove(file)
                    print(f'O arquivo {file} foi removido com sucesso.')

            print(f'Arquivos foram zipados para {zip_filename} e os originais foram removidos.')
<<<<<<< HEAD



=======
>>>>>>> 4d8c41f4356afa3da882388a684e9fdfea15187c
            with open(zip_filename, "rb") as fp:
                st.markdown(f"<hr>",unsafe_allow_html=True)
                st.info('Baixe seu material.', icon="ℹ️")
                st.balloons()
                st.download_button(
                    label="Download Material de Estudo",
                    type='primary',
                    data=fp,
                    file_name=zip_filename,
                    mime='application/zip',
                )
<<<<<<< HEAD


if __name__ == "__main__":
    main()
=======
if __name__ == "__main__":
    main()
            
>>>>>>> 4d8c41f4356afa3da882388a684e9fdfea15187c
