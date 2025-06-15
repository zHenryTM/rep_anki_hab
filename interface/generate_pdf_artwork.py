import string
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def generate_pdf_artwork(dataframe_questions_infos):

  all_items = ' '.join(s for s in dataframe_questions_infos['OCRSearch'].apply(str).values)
  all_items = all_items.replace(';',  ' ').replace('/',  ' ')
  all_letters = list(string.ascii_lowercase + string.ascii_uppercase)


  stop_words = all_letters +  ['a', 'A', 'b', 'B', 'c', 'C', 'd','figura', 'D', 'e', 'E', 'v', 'nan','pela', 'ser', 'de', 'etc', '(s)', 'do', 'da', 'por', 'para', 'entre', 'se', 'um', 'até', 'ele', 'ela', 'qual', 'bem', 'só', 'mesmo', 'uma', 'um', 'mais', 'menos', 'outro', 'porque', 'por que', 'cada', 'muito', 'todo', 'foram', 'tem', 'meio', 'país', 'una', 'for',
                'uma', 'na', 'su', 'with', 'no','estes','mesma', 'lá', 'that', 'vo' 'pela', 'pelo', 'h', 'H', 'CH', 'ao', 'com', 'que', 'em', 'dos', 'das', 'eu', 'lo', 'the', 'me', 'y', 'la', 'en', 'en', 'to', 'quem', 'and', 'sem', 'on', 'at', 'essa', 'sem', 'uso', 'esse', 'las', 'suas', 'el', 'poi', 'pai', 'doi', 'in', 'pois', 'con', 'of',
                'ainda', 'não', 'o', 'a', 'os','mê','próximo', 'apresenta','quando', 'meu', 'acordo', 'grande', 'saída', 'dessa', 'as', 'deve', 'Além', 'cinco', 'nessa', 'conforme', 'contendo', 'interior', 'Disponível', 'disponível', 'ocorre', 'vezes', 'através', 'grupo', 'tipo', 'algumas', 'causa', 'considerando', 'essas', 'formação', 'so', 'SO', 'pessoa', 'utilizada', 'alguns', 'quais', 'fio', 'outras', 'só', 'exemplo', 'está', 'oo','isso', 'fonte', 'durante', 'onde', 'caso', 'será', 'pelos', 'Disponível', 'duas', 'dois', 'onde', 'podem', 'apresentam', 'alguma', 'outra', 'seja', 'menor', 'Após', 'Considere', 'partir' 'aq', 'etapa', 'três', 'vez', 'pelas', 'dia', 'nova', 'Acesso', 'veículo', 'seus', 'têm', 'quadro', 'parte', 'desses', 'alguma', 'alta', 'sendo', 'eles', 'outros', 'respectivamente', 'lhe', 'ficou','desse', 'pode', 'nas', 'nem', 'nos', 'nesse', 'apenas', 'n', 'esses', 'igual', 'estão', 'br', 'L', 'questão', 'e', 'texto', 'são', 'é', 'como', 'à', 'no', 'mai', 'seu', 'sua', 'mais', '.', 'ano', 'ma', 'ou', 'foi', 'sobre', 'às', 'aos', 'mas', 'há', 'seguinte', 'já', 'maior', 'era', 'desde', 'diferente', 'forma', 'também']


  wc = WordCloud(background_color='black',
                  stopwords=stop_words,
                  collocations=False,
                  colormap = 'copper',
                  width=2480, height=3508, contour_width=0)  # Defina a largura e altura desejadas


  wordcloud = wc.generate(all_items)
  
  plt.figure(figsize=(10, 10))  # Plotar a núvem de palavras. Ajuste o tamanho da figura se necessário

  a4_width_inches = 8.27
  a4_height_inches = 11.69
  
  dpi = 300  # Ajuste a resolução conforme necessário

  fig, ax = plt.subplots(figsize=(a4_width_inches, a4_height_inches), dpi=dpi)  # Criar a figura com o tamanho A4
  
  ax.imshow(wordcloud, interpolation='bilinear')  # Plotar a nuvem de palavras
  ax.axis("off")

  plt.savefig("./images/design/wordcloud_a4.png", bbox_inches='tight', pad_inches=0)  # Salvar a figura em tamanho A4
