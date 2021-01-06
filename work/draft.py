from googletrans import Translator
translator = Translator()


input = './data/{}.txt'.format('li ziqi')

with open(input, 'r', encoding='utf-8') as f:
        lines = f.readlines() 
for line in lines:
    print(translator.translate(line, dest='en').text)