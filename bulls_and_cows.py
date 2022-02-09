# Написать игру «Быки и коровы». 
# Программа «загадывает» четырёхзначное число
# играющий должен угадать его. 
# После ввода пользователем числа программа сообщает, 
# сколько цифр числа угадано и стоит на нужном месте (быки) и 
# сколько цифр угадано, но стоит не на нужном месте (коровы). 
# После отгадывания числа на экран необходимо вывести количество сделанных пользователем попыток. 
# В программе необходимо использовать рекурсию.
import tkinter as tk
import tkinter.dialog as dg
from random import randint

def random_number():
    '''Функция возвращающая случайное число из 4 цифр'''
    list_num = []
    step = 0
    list_len = 4
    while step < list_len:
        list_num.append(randint(0, 9))
        step += 1
    if len(set(list_num)) == len(list_num):
        return list_num 
    else:
        return random_number()


def game_play(computer_number):
    '''Функция обработки вводимых пользователем чисел'''
    bulls = 0
    cows = 0
    user_number = ent.get() 
    user_input = str(user_number)[0:4]
    user_map = map(int, user_input)
    user_list = list(user_map)
    if len(computer_number) > len(user_list):
        msg2.config(text = msg2.cget('text') + 'Ввели недастаточно цифр \n')
        ent.delete(0, tk.END)
        return None
    if len(set(user_list)) != len(user_list):
        msg2.config(text = msg2.cget('text') + 'Ввели одинаковые цифры \n')
        ent.delete(0, tk.END)
        return None
    if computer_number == user_list:
        return 'win!'
    for index in range(4):
        if computer_number[index] == user_list[index]:
            bulls += 1
        elif user_list[index] in computer_number:
            cows += 1
    msg2.config(text = msg2.cget('text') + 'Ваше число: ' + user_input + ' содержит ' + str(
                                bulls) + ' быка и ' + str(
                                    cows) + ' коровы\n')
    ent.delete(0, tk.END)

def play(event):
    '''Функция запуска обработки вводимых чисел'''
    global number
    gameplay = game_play(number)
    if gameplay == 'win!':
        gameOwer = dg.Dialog(title = 'Вы победили!',
               text = '     Сыграем ещё?           ',
               bitmap = 'questhead',
               default = 0,
               strings = ('Да', 'Нет'))
        if gameOwer.num == 1: 
            exit()
        else:
            number = random_number()
            #Вывод для отладки. Для самой игры не нужно
            # print(number)
            msg2.config(text='')
            ent.delete(0, tk.END) 
            


number = random_number()

# print(number)                       

#Создание и настройка gui
root = tk.Tk()
root.geometry('500x700')
root.title('Быки и Коровы')
root.configure(bg='#5097ab')

#Текст с правилами игры
msg = tk.Message(width=400, padx=10, pady=5,
              text='Введите число из 4 цифр.'
              'Цифры не должны повторяться. \n'
              'Быки - угаданные цифры, находящиеся на нужном месте. \n'
              'Коровы - угаданные цифры, находящиеся не на нужном месте')
msg.pack(padx=10, pady=5)                      
msg.config(bg='#5097ab', fg='#3d1515',
           font=('Arial', 12, 'bold', 'italic'))

#Поле ввода чисел пользователем
ent = tk.Entry(width=8)
ent.pack()
ent.focus()
ent.bind( '<Return>', play)  

#Вывод результатов сравнения вводимых пользователем чисел
msg2 = tk.Message(width=400, padx=10, pady=5, text='')
msg2.pack(padx=10, pady=5)                     
msg2.config(bg='#5097ab',
        font=('times', 12, 'normal'))  

#Запуск gui
root.mainloop()