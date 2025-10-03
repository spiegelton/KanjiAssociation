from support_methods import get_jisho, get_reading_from_response, get_kanjis_from_response, is_kanji

if __name__ == '__main__':
   
    starting_kanji = input("enter starting kanji: ")
    data = get_jisho(starting_kanji)
    last_kanji = ""
    winning = True
    while(winning):
        next_kanji_seed = ""
        if last_kanji != "":
            next_kanji_seed = last_kanji[-1]
            print("next kanji seed: " + next_kanji_seed)
            data = get_jisho(next_kanji_seed)
        kanjis = get_kanjis_from_response(data, next_kanji_seed)
        new_kanji = ""
        if len(kanjis) > 0:
            new_kanji = kanjis[0]
        else:
            print("Unable to get more kanjis")
            break
        correct_reading = get_reading_from_response(data, new_kanji)

        reading_input = input("Write " + new_kanji + " in romaji: ")
        if reading_input == correct_reading:
            print("Correct!")
            last_kanji = new_kanji
        else:
            print("Incorrect!")
            winning = False
        print("correct reading: " + correct_reading)

