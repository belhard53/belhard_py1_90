# https://regex101.com/r/aGn8QC/1410
#  https://regex101.com/r/AwjqgR/1


# re.match(pattern, string)	совпадение патерна в НАЧАЛЕ строки	re.match(r'\d+', '123abc') → 123
# re.fullmatch(pattern, string)	совпадение патерна во ВСЕЙ строке	re.fullmatch(r'^[а-яА-ЯёЁ]+$', "Вася123") → None
# re.search(pattern, string)	ищет Первое совпадение	re.search(r'\d+', 'abc123def') → 123
# re.findall(pattern, string)	ВСЕ совпадения → список	re.findall(r'\d+', 'a1b2c3') → ['1','2','3']
# re.sub(pattern, repl, string)	Замена	re.sub(r'\d+', 'X', 'a1b2') → 'aXbX'
# re.split(pattern, string)	Разделение	re.split(r'[,\s]', 'a,b c') → ['a','b','c']
# re.compile(pattern)	Компиляция шаблона	pat = re.compile(r'\d+'); pat.findall(text)


# {} - сколько
# [] - какие символы [a-zA-Z,.!@]
# [^] - исключение [^abc]
# + - 1 или больше
# * - 0 или больше
# ? - одно повторение
# () одно из обязательных условий
# . - любой символ
# ^ - начало
# $ - окончание строки
 
# \b - границы слова
# \d — соответствует любой одной цифре и заменяет собой выражение [0-9];
# \D — исключает все цифры и заменяет [^0-9];
# \w — заменяет любую цифру, букву, а также знак нижнего подчёркивания;
# \W — любой символ кроме латиницы, цифр или нижнего подчёркивания;
# \s — соответствует любому пробельному символу;
# \S — описывает любой непробельный символ.


# '^\w+' - первое слово	
# \d+\.\d{2} - дробные числа с 2 знаками после запятой(.)
# ^[a-zA-Z][a-zA-Z0-9-_\.]{1,20}$ - логин
# ^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{8,}$ - пароль
# (?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$ - пароль более 8 символов
# (\+375)(29|33|44)[0-9]{7} - номер телефона РБ
# \d\d\/\d\d\/\d{4} - дата
# [-+]?\d+ = +12121 -6546 - числа с минусом и плюсом




 
import re
s = '3754412345678'

res = re.search(r'\+*375(29|33|44)[0-9]{7}', s)
res2 = re.findall('[0-9]{7}$', s)
print(res2)
if res:
	print(res[0])
	print(res.group(0))


# # 1. Найти все email
# emails = r'[\w\.-]+@[\w\.-]+\w+'
# print(re.findall(emails, text))

# # 2. Извлечь телефоны +7...
# phones = r'\+7[\s\(\)]?\d{3}[\s\(\)-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}'
# print(re.findall(phones, text))

# # 3. Выделить даты YYYY-MM-DD
# dates = r'\d{4}-\d{2}-\d{2}'
# print(re.findall(dates, text))

# # 4. Найти цены с ₽/$/€
# prices = r'[€$₽]\s*[\d\s]+,?\d{2}'
# print(re.findall(prices, text))

# # 5. Извлечь URL
# urls = r'https?://[\w\.-]+(?:/[\w\.-]*)*[\w\.-]*\??[\w\.-=&]*'
# print(re.findall(urls, text))

# # 6. Получить ID заказов (20251234)
# order_ids = r'заказ\s*[№#]?\s*(\d{8})'
# print(re.findall(order_ids, text))

# # 7. Найти HTML теги с class/id
# html_tags = r'<[\w\s]+class="[^"]*"[^>]*>|<\w+\sid="[^"]*"[^>]*>'
# print(re.findall(html_tags, text))

# # 8. Заменить все цифры на X
# no_digits = re.sub(r'\d', 'X', text)

# # 9. Разделить по пробелам/запятым
# words = re.split(r'[\s,]+', text)

# # 10. Найти слова длиной 5+ символов
# long_words = r'\b\w{5,}\b'
# print(re.findall(long_words, text))


# -------------------------------

# s='175/65R14 Кама Euro 129, 82H 175/65/R14 Кама Euro 129, 82H'
# res = re.findall(r'\d{3}\/\d{2}\/*R\d{2}', s)
# print(res[0] if res else None)