import pythainlp
from pythainlp.corpus.common import thai_words, thai_syllables, thai_negations, thai_stopwords, thai_family_names, thai_female_names, thai_male_names, countries, provinces
from ssg import syllable_tokenize
import re


tu = str.maketrans("มวกขฃคฅฆงยญณนฎฏดตศษสบปพภผฝฟหอฮจฉชซฌฐฑฒถทธรฤลฦ"
                   ,"mw111111g233344444445555666666777778888889999")

tu2 = str.maketrans("ะัาิีึืุูเแโอยำใไว็"
                   ,"abcdefghijklmnopqrs")


def rhyme(s):
    global y, x

    s = re.sub('รร([เ-ไ])', 'ัน\\1', s)  # 4. รร แล้วตามด้วยสระ เ แ โ ไ เปลี่ยน รร เป็น ั น
    s = re.sub('รร([ก-ฮ])', 'ั\\1', s) # 5. ถ้า รร แล้วต่อด้วยพยัญชนะ เปลี่ยน รร เป็นสระ ั
    s = re.sub('รร([ก-ฮ][ะ-ู่-์])','ัน\\1', s)  # รร แล้วตามด้วยสระ เปลี่ยน รร เป็น ั น
    s = re.sub('รร', 'ัน', s)   #รร เฉยๆ เปลี่ยนเป็น ั น
    #print(s)

    if "ไ" in s or "ใ" in s : #ถ้าเป็นสระ ไ หรือ ใ ให้เปลี่ยนคําเป็นอัย
        s = "อัย"
    #print(s)

    if "ำ" in s: #ถ้าเป็นสระอําให้เปลี่ยนเป็นอัม
        s = "อัม"
    #print(s)

    s = re.sub("่", "", s) #ลบวรรณยุกต์
    s = re.sub("้", "", s)
    s = re.sub("๊", "", s)
    s = re.sub("๋", "", s)

    s = re.sub('จน์|มณ์|ณฑ์|ทร์|ตร์|[ก-ฮ]์|[ก-ฮ][ะ-ู]์', "", s) # 6.ลบการันต์
    #print(s)
    x = s


    s = re.sub('[ะ-์]', '', s) # 7. ตัดสระทั้งหมดที่เหลือ
    #print(s)
    y = s

    """if len(s) >= 3 and (s[1] == "ร" or s[1] == "ล"):  #ลบตัวควบกลํ้า
        s = s.replace("ร", "")
        s = s.replace("ล", "")
    """
    if len(s) >= 3 and s[0] in "มวกขฃคฅฆงยญณนฎฏดตศษสบปพภผฝฟหอฮจฉชซฌฐฑฒถทธรฤลฦ" and s[1] in "มวกขฃคฅฆงยญณนฎฏดตศษสบปพภผฝฟหอฮจฉชซฌฐฑฒถทธรฤลฦ":
        s = list(s)
        del s[0]
        s = "".join(s)


    #print(s)

    first = set(x)
    second = set(y)
    d = list(first.symmetric_difference(second))#เอาค่าก่อนลบสระ กับหลังลบ สระมาลบกันเพื่อให้เหลือแต่สระ
    #print(d)


    sd = s[1:].translate(tu)#9 เอาsไปถอดรหัสเพื่อหามาตราตัวสะกด
    #print(sd)

    vw = ""
    for x in d:   #เอาdไปถอดรหัสเพื่อหาสระ
        wy = x.translate(tu2)
        vw = vw + wy

    #print(vw)

    return sd+vw