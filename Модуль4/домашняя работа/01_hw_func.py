# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    # TODO: your code here
    a = int(input('Введите номер билета: '))
sum_left = 0
sum_right = 0
for i in range(6):
    if i < 3:
        sum_right += a // 10**i % 10
    else:
        sum_left  += a // 10**i % 10
if sum_left == sum_right:
    print('lucky')
else:
    print('unlucky')


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
