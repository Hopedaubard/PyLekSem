import re
print(len(set(re.split(' |//.', input('Введите текст -> ').lower()))))