# Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре различны. Для одного данного слова определите его синоним.
# Формат ввода
#
# Программа получает на вход количество пар синонимов N. Далее следует N строк, каждая строка содержит ровно два слова-синонима. После этого следует одно слово.
# Формат вывода
#
# Программа должна вывести синоним к данному слову. Примечание
#
# Эту задачу можно решить и без словарей (сохранив все входные данные в списке), но решение со словарем будет более простым.

syns = {}

for i in range(int(input())):
    word1, word2 = input().split()
    syns[word1], syns[word2] = word2, word1

print(syns[input()])
