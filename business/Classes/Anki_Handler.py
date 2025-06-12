import genanki


class Anki_Handler:

    @staticmethod
    def get_flashcards_model():
        return genanki.Model(
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
        

    @staticmethod
    def create_deck(deck_id, deck_name):
        try:
            return genanki.Deck(deck_id, deck_name)
        except:
            print("Erro ao criar deck.")
    

    @staticmethod
    def create_flashcard(model, fields):
        try:
            return genanki.Note(
                model=model,
                fields=fields
            )

        except:
            print("Erro ao criar flashcard.")
            
    
    @staticmethod
    def create_package(decks):
        try:
            return genanki.Package(decks)
        except:
            print("Erro ao criar pacote.")