import random
from business.Classes.Anki_Handler import Anki_Handler


def generate_anki_deck_from_filtered_questions(dfResult_CN, Habilidade, flashname):

    deck = Anki_Handler.create_deck(deck_id=random.randint(0, 100000), deck_name=str('Questões::Habilidades::'+str(flashname)+'::H'+str(Habilidade)))

    flashcards = []

    question_number = 0

    # Percorrer as linhas do dataframe dfResult_CN
    for i in dfResult_CN.index:

        question_number += 1

        question_image_path = str(dfResult_CN.loc[i, "CO_ITEM"]) + '.png'

        imagemQ = str(dfResult_CN.loc[i, "CO_ITEM"]) + '.gif'

        question_answer = str('Gabarito: ')+ str(dfResult_CN.loc[i, 'TX_GABARITO'])
        
        question_informations = f"N{question_number} - Q{str(dfResult_CN.loc[i, "CO_POSICAO"])}:{str(dfResult_CN.loc[i, "ANO"])} - H{str(dfResult_CN.loc[i, "CO_HABILIDADE"].astype(int))} - Proficiência: {str(dfResult_CN.loc[i, "theta_065"].round(2))}"

        flashcard = Anki_Handler.create_flashcard(
            model=Anki_Handler.get_flashcards_model(),
            fields=[question_informations, '<img src="https://niedsonemanoel.com.br/enem/An%C3%A1lise%20de%20Itens/OrdenarPorTri/1.%20Itens%20wadBNI_/' + question_image_path + '"]', question_answer,  '<img src="https://niedsonemanoel.com.br/enem/An%C3%A1lise%20de%20Itens/OrdenarPorTri/1.%20Itens%20BNI_/Correcao/' + imagemQ + '"]']
        )

        # Adicionar o flashcard à lista de flashcards
        flashcards.append(flashcard)

    for flashcard in flashcards:
        deck.add_note(flashcard)

    package = Anki_Handler.create_package(decks=deck)
    package.write_to_file('H'+str(Habilidade)+'_'+str(flashname)+'.apkg')
