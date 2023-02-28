text_1 = list(input("Enter: ").split())


def rhyme(text):
    vowels = list("АОУЫЭЕЁИЮЯаоэеиыуёюя".split())
    vowel_counter = []
    for i in text:
        count = 0
        for world in i:
            if i in vowels:
                count += 1
        vowel_counter.append(count)
    return vowel_counter


print("Парам пам-пам" if len(set(r := rhyme(text_1))) == 1 and r[0] != 0 else "Пам парам")
