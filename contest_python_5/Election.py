# В выборах Президента Российской Федерации побеждает кандидат, набравший свыше половины числа голосов избирателей. Если такого кандидата нет, то во второй тур выборов выходят два кандидата, набравших наибольшее число голосов.
#
# Формат ввода
#
# Каждая строка входного файла содержит имя кандидата, за которого отдал голос один избиратель. Известно, что общее число кандидатов не превосходит 20, но в отличии от предыдущих задач список кандидатов явно не задан.
#
# Формат вывода
#
# Если есть кандидат, набравший более 50% голосов, программа должна вывести его имя. Если такого кандидата нет, программа должна вывести имя кандидата, занявшего первое место, затем имя кандидата, занявшего второе место.

votes = {}

with open("input.txt", "r", encoding="utf8") as file:
    for line in file:
        candidate = line.strip()
        if candidate in votes:
            votes[candidate] += 1
        else:
            votes[candidate] = 1

total_votes = sum(votes.values())
winner = None

for candidate, votes_count in votes.items():
    if votes_count > total_votes / 2:
        winner = candidate
        break

if winner:
    print(winner)
else:
    sorted_candidates = sorted(votes.items(), key=lambda x: x[1], reverse=True)
    print(sorted_candidates[0][0])
    print(sorted_candidates[1][0])
