def remove_invalid_characters(text):
        numAssc = 251

        try:
            invalid_characters = [char for char in text if ord(char) > numAssc]
            replaced_text = ''.join('' if ord(char) > numAssc else char for char in text)

            print(f"Caracteres inválidos substituídos: {invalid_characters}")

            return replaced_text
        
        except:
            print('sorry')

            return(text)
        