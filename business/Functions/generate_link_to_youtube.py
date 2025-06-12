import urllib.parse


def generate_link_to_youtube(search_text):
    try:
        encoded_query = urllib.parse.quote_plus(search_text)
        search_query = f"https://www.youtube.com/results?search_query={encoded_query}"

    except:
        search_query = 'N/A'

    return(search_query)
