# # Открыть на запись файл example.txt
# file = open('example.txt', 'w', encoding='utf-8')
# # Записать в файл строку
# file.write('Зевну, укроюсь с головою,\nбудильник заведу на март.\n')
# # Закрыть файл
# file.close()

# Открыть файл example.txt на чтение (аргумент 'r')
file = open('example.txt', 'r', encoding='utf-8')
# Прочитать первые 12 символов из файла и сохранить их в переменную content
content = file.read(12)
# Вывести на печать содержимое переменной content
print(content)
# Закрыть файл
file.close() 