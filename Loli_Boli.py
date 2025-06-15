import re

common_words = {'это', 'так', 'слово', 'текст', 'быть', 'весна', 'лето', 'осень', 'зима',
    'день', 'ночь', 'вечер', 'утро',
    'человек', 'город', 'дерево', 'цветок',
    'любовь', 'мир', 'радость', 'счастье', 'весной', 'природа', 'оживает'}

def is_real_text(text):
    # Проверяем наличие русских букв и знаков препинания
    cyrillic_pattern = r'[а-яёА-ЯЁ]'
    
    if not text.strip():
        return False
    
    # Подсчет числа символов, соответствующих кириллице
    count_cyrillic = len(re.findall(cyrillic_pattern, text))
    
    # Простейшая проверка наличия некоторых распространённых слов
    words_in_text = set(re.findall(r'\b\w+\b', text.lower()))
    common_word_count = len(words_in_text & common_words)
    
    # Процент соответствия по количеству общих слов
    word_match_percentage = common_word_count / max(len(words_in_text), 1)
    
    # Доля русских букв должна быть значительной,
    # плюс должно присутствовать некоторое количество общеупотребительных слов
    threshold = 0.7  
    if count_cyrillic / len(text) >= threshold and word_match_percentage > 0.1:
        return True
    else:
        return False

# Тестирование функции
print(is_real_text("Ищ чфбоця зотм ювдйфёёкп еттрфь ж цфяъыжша, пхзжрзхха якаучь цзефь."))  # Должно вернуть False
print(is_real_text("Это предложение написано на русском языке."))  # Должно вернуть True