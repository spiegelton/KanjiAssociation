from jisho_api.word import Word
import jaconv
def get_jisho(request_kanji: str):
    response = Word.request(request_kanji)
    return(response.data)


def get_reading_from_response(data: any, request_kanji: str):
    for word_config in data:
        kanji = word_config.slug
        if kanji == request_kanji:
            kana = word_config.japanese[0].reading
            return jaconv.kana2alphabet(kana)
        

def get_kanjis_from_response(data: any, original_kanji: str):
    kanji_list = []
    for word_config in data:
        word = word_config.slug
        if len(word) == 2:
            if is_kanji(word[0]) and is_kanji(word[1]) and original_kanji in word:
                kanji_list.append(word)
    return kanji_list

def is_kanji(character):
    # Check if the character falls in the kanji ranges
    return (
        '\u4E00' <= character <= '\u9FFF' or  # Basic Kanji range
        '\u3400' <= character <= '\u4DBF' or  # Kanji Extension A
        '\U00020000' <= character <= '\U0002A6DF'  # Kanji Extension B
    )