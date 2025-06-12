import pandas as pd
import numpy as np
import time
import random
import plotly.express as px
import streamlit as st
import numpy as np
from scipy.optimize import minimize_scalar
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


# Minhas imports
from business.Functions.generate_link_to_youtube import generate_link_to_youtube
from business.Functions.remove_invalid_characters import remove_invalid_characters
from business.Classes.PDF_Generator import PDF_Generator
from business.Classes.Anki_Handler import Anki_Handler
from interface.artwork import artwork


urlItens = "https://github.com/NiedsonEmanoel/NiedsonEmanoel/raw/main/enem/An%C3%A1lise%20de%20Itens/OrdenarPorTri/gerador/provasOrdernadasPorTri.csv"
dItens = pd.read_csv(urlItens, encoding='utf-8', decimal=',')


def flashnamesa(SG):
    if SG == 'Natureza': return 'CN'
    elif SG == 'Matemática': return 'MT'
    elif SG == 'Humanas': return 'CH'
    else: return 'LC'



def questHab(dfResult_CN, prova, Habilidade, idom, flashname):

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
    artwork(dfResult_CN)
    dfResult_CN.sort_values('theta_065', ascending=True, inplace=True)
    dfResult_CN['indexacao'] = dfResult_CN.reset_index().index + 1


    baralho = Anki_Handler.create_deck(deck_id=random.randint(0, 100000), deck_name=str('Questões::Habilidades::'+str(flashname)+'::H'+str(Habilidade)))


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
        flashcard = Anki_Handler.create_flashcard(
            model=Anki_Handler.get_flashcards_model(),
            fields=[inic, '<img src="https://niedsonemanoel.com.br/enem/An%C3%A1lise%20de%20Itens/OrdenarPorTri/1.%20Itens%20BNI_/' + imagem + '"]', resposta,  '<img src="https://niedsonemanoel.com.br/enem/An%C3%A1lise%20de%20Itens/OrdenarPorTri/1.%20Itens%20BNI_/Correcao/' + imagemQ + '"]']
        )

        # Adicionar o flashcard à lista de flashcards
        flashcards.append(flashcard)

    for flashcard in flashcards:
        baralho.add_note(flashcard)

    # Criar um pacote com o baralho e as imagens
    pacote = Anki_Handler.create_package(decks=baralho)
    pacote.write_to_file('H'+str(Habilidade)+'_'+str(flashname)+'.apkg')

    pdf = PDF_Generator()
    pdf.alias_nb_pages()
    pdf.set_title(flashname)

    pdf.add_page()
    pdf.image("images/design/wordcloud_a4.png", x=0, y=0, w=pdf.w, h=pdf.h, type='png')
    pdf.add_page()

    pdf.set_font('Times', 'B', 12)
    img_dir = 'images/questions_images'  # Diretório local para salvar as imagens

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

                link = generate_link_to_youtube(remove_invalid_characters(dfResult_CN.loc[i, "OCRSearch"]))
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
            with st.spinner("Gerando seu material (isso pode demorar um pouco)..."):
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


if __name__ == "__main__":
    main()
