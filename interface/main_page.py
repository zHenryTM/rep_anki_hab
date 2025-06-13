import streamlit as st
import os
import zipfile
import pandas as pd

from business.Functions.get_enem_subjects_acronym import get_enem_subjects_acronym
from business.Functions.questHab import questHab

urlItens = "https://github.com/NiedsonEmanoel/NiedsonEmanoel/raw/main/enem/An%C3%A1lise%20de%20Itens/OrdenarPorTri/gerador/provasOrdernadasPorTri.csv"
dItens = pd.read_csv(urlItens, encoding='utf-8', decimal=',')

def main_page():
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
        mat = get_enem_subjects_acronym(mats)
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