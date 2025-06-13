from business.Functions.generate_anki_deck_from_filtered_questions import generate_anki_deck_from_filtered_questions
from business.Functions.generate_list_from_filtered_questions import generate_list_from_filtered_questions
from business.Functions.get_enem_filtered_questions import generate_enem_filtered_questions

from interface.generate_pdf_artwork import generate_pdf_artwork


def questHab(dfResult_CN, prova, Habilidade, idom, flashname):
    dfResult_CN = generate_enem_filtered_questions(dfResult_CN, prova, Habilidade, idom)
    generate_anki_deck_from_filtered_questions(dfResult_CN, Habilidade, flashname)
    generate_list_from_filtered_questions(dfResult_CN, Habilidade, flashname)

    return 'H'+str(Habilidade)+'_'+str(flashname)