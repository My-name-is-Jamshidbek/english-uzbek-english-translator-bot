from googletrans import Translator


def translator(text):
    trans = Translator()
    holat = trans.detect(text).lang
    if holat == 'uz':
        holat = 'uz_en'
        rt = trans.translate(text=text,dest='en',src='uz').text
    elif holat == 'en':
        holat = 'en_uz'
        rt = trans.translate(text=text,dest='uz',src='en').text
    else:
        rt1 = trans.translate(text=text,dest='en',src='uz').text
        rt2 = trans.translate(text=text,dest='uz',src='en').text
        if rt1==rt2:
            holat = 'uz_en'
            rt = trans.translate(text=text, dest='en', src='uz').text
        elif rt1 == text:
            holat = 'en_uz'
            rt = trans.translate(text=text, dest='uz', src='en').text
        elif rt2 == text:
            holat = 'uz_en'
            rt = trans.translate(text=text, dest='en', src='uz').text
        else:
            holat = 'uz_en'
            rt = trans.translate(text=text, dest='en', src='uz').text
    return [rt,holat]
