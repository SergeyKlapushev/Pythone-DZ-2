''''Задача 2: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть.'''

print('Введите кол-во монет: ')
n = int(input())
i = 0
orel = 0
reshka = 0

for i in range(i,n):
    print("Что выпало на", i+1, "монете? (Орёл 1, решка 0):")
    side = int(input())
    if side == 0:
        reshka += 1

    if side == 1:
        orel += 1

if reshka > orel:
    print('Мин. кол-во монет которое надо перевернуть:', orel)
else: print('Мин. кол-во монет которое надо перевернуть:', reshka)