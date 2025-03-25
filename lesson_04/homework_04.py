adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# task 01

adwentures_of_tom_sawer: str = adwentures_of_tom_sawer.replace("\n", " ")

print(adwentures_of_tom_sawer)

# task 02
adwentures_of_tom_sawer: str = adwentures_of_tom_sawer.replace("....", "")

print(adwentures_of_tom_sawer)

# task 03
adwentures_of_tom_sawer = adwentures_of_tom_sawer.split()
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer)
print(adwentures_of_tom_sawer)

# task 04
h_qty = adwentures_of_tom_sawer.count("h")
print(h_qty)

# task 05
text_split = adwentures_of_tom_sawer.split()
capitalaze_words = []

for word in text_split:
    if word.istitle():
        capitalaze_words.append(word)

print(len(capitalaze_words))

# task 06
word_finder = adwentures_of_tom_sawer.find("Tom", 1, -1)
print(word_finder)

# task 07
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(". ")
print(adwentures_of_tom_sawer_sentences)

# task 08
print(adwentures_of_tom_sawer_sentences[3].lower())

# task 09
for sent in adwentures_of_tom_sawer_sentences:
    if sent.startswith("By the time"):
        print('Sentence with "By the time" is present.'),

# task 10
last_sent = adwentures_of_tom_sawer_sentences[-2]
print(last_sent)
print(len(last_sent))
