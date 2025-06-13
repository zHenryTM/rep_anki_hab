import os
import zipfile
import pandas as pd
import streamlit as st


from business.Functions.questHab import questHab
from business.Functions.get_enem_subjects_acronym import get_enem_subjects_acronym
from business.Functions.get_enem_filtered_questions import get_enem_filtered_questions
from business.Functions.generate_list_from_filtered_questions import generate_list_from_filtered_questions
from business.Functions.generate_anki_deck_from_filtered_questions import generate_anki_deck_from_filtered_questions



#urlItens = "https://github.com/NiedsonEmanoel/NiedsonEmanoel/raw/main/enem/An%C3%A1lise%20de%20Itens/OrdenarPorTri/gerador/provasOrdernadasPorTri.csv"
#dfResult_CN = pd.read_csv(urlItens, encoding='utf-8', decimal=',')


def main_page():
    urlItens = "https://github.com/NiedsonEmanoel/NiedsonEmanoel/raw/main/enem/An%C3%A1lise%20de%20Itens/OrdenarPorTri/gerador/provasOrdernadasPorTri.csv"
    dfResult_CN = pd.read_csv(urlItens, encoding='utf-8', decimal=',')

    idom = -1

    st.header('Gerador de Listas por Habilidades')

    st.divider()  # Linha, tipo <hr>

    materia = st.selectbox('Matéria', ('Linguagens', 'Humanas', 'Natureza', 'Matemática'), placeholder="Selecione uma Matéria")

    # PARA ADICIONAR LISTAS DE LÍNGUA ESTRANGEIRA NO FUTURO
    #    if (mats == 'Linguagens'):
    #        idi = st.selectbox(
    #        'Idioma',
    #        ('INGLÊS', 'ESPANHOL'), placeholder="Selecione uma Matéria")
    #        if idi == 'INGLÊS': idom = 0
    #        else: idom = 1

    habilidades = st.multiselect(
        'Selecione as Habilidades',

        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],

        placeholder="Selecione as Habilidades"
    )

    st.divider()

    st.info('• H31 é reservada para questões sem Habilidade definida.')
    st.info('• Por enquanto não estão sendo geradas listas de idiomas.')

    st.divider()

    
    if st.button("Gerar!", type="primary"):

        materia_acronym = get_enem_subjects_acronym(materia)

        to_zip = []
        

        if(len(habilidades) > 0):

            with st.spinner("Gerando seu material (isso pode demorar um pouco)..."):

                for Habilidade in habilidades:
                    if ((materia_acronym == 'LC' and Habilidade >= 5) and (materia_acronym == 'LC' and Habilidade <= 8)):
                        continue
                    else:
                        #lt = questHab(dfResult_CN, materia_acronym, Habilidade, idom, materia)

                        dfResult_CN = get_enem_filtered_questions(dfResult_CN, materia_acronym, Habilidade, idom)
                        generate_anki_deck_from_filtered_questions(dfResult_CN, Habilidade, materia)
                        generate_list_from_filtered_questions(dfResult_CN, Habilidade, materia)

                        filename = 'H'+str(Habilidade)+'_'+str(materia)                        

                        to_zip.append(filename +'.pdf')
                        to_zip.append(filename +'.apkg')


            zip_filename = 'materialestudo.zip'


            # Cria um objeto ZipFile em modo de escrita
            with zipfile.ZipFile(zip_filename, 'w') as zipf:

                # Adicione cada arquivo à archive
                for file in to_zip:
                    if os.path.exists(file):
                        zipf.write(file, os.path.basename(file))


            # Apaga os arquivos originais após zipar
            for file in to_zip:
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