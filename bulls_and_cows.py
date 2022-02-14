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
from random import sample

class CBGame(tk.Tk):
    def __init__(self, width, heigth, title, bgcolor, ruletext, lang):
        super().__init__()
        self.random_number()
        self.ruletext = ruletext[lang]
        instrule = self.ruletext['instruction']
        self.notifrule = self.ruletext['result']
        self.geometry(str(width) + 'x' + str(heigth))
        self.title(title)
        self.configure(bg=bgcolor)
        msg = tk.Message(width=instrule['wd'], padx=instrule['px'], pady=instrule['py'],
              text=instrule['text'])
        msg.pack(padx=10, pady=5)                      
        msg.config(bg=bgcolor, fg=instrule['textcolor'],
                    font=instrule['font'])
        #Поле ввода чисел пользователем
        self.ent = tk.Entry(width=8)
        self.ent.pack()
        self.ent.focus()
        self.ent.bind( '<Return>', self.play)  

        #Вывод результатов сравнения вводимых пользователем чисел
        self.msg2 = tk.Message(width=self.notifrule['wd'], padx=self.notifrule['px'], pady=self.notifrule['py'], 
                                text=self.notifrule['starttext'])
        self.msg2.pack(padx=10, pady=5)                     
        self.msg2.config(bg=bgcolor,
                font=self.notifrule['font'])


    def random_number(self):
        '''Метод возвращающий случайное число из 4 цифр'''
        self.number = sample(range(0, 10), 4)
        print(self.number)

    def game_play(self):
        '''Метод основной логики игры'''
        bulls = 0
        cows = 0
        user_number = self.ent.get() 
        user_input = str(user_number)[0:4]
        user_map = map(int, user_input)
        user_list = list(user_map)
        if len(self.number) > len(user_list):
            self.msg2.config(text = self.msg2.cget('text') + self.notifrule['eoff'])
            self.ent.delete(0, tk.END)
            return None
        if len(set(user_list)) != len(user_list):
            self.msg2.config(text = self.msg2.cget('text') + self.notifrule['douberror'])
            self.ent.delete(0, tk.END)
            return None
        if self.number == user_list:
            return True
        for index in range(len(self.number)):
            if self.number[index] == user_list[index]:
                bulls += 1
            elif user_list[index] in self.number:
                cows += 1
        self.msg2.config(text = self.msg2.cget('text') + self.notifrule['notify'].format(user_input = user_input, bulls = bulls, cows = cows))
        self.ent.delete(0, tk.END)

    def play(self, event):
        '''Метод запуска обработки вводимых чисел'''
        if self.game_play():
            if not self.continue_game():
                exit()
            self.random_number()
            self.msg2.config(text=self.notifrule['starttext'])
            self.ent.delete(0, tk.END)

    def continue_game(self):
        '''Метод вывода диалогового окна для продолжения игры'''
        cont_dg = self.ruletext['continue']
        gameOwer = dg.Dialog(title = cont_dg['title'],
            text = cont_dg['text'],
            bitmap = cont_dg['bitmap'],
            default = 0,
            strings = cont_dg['strings'])
        if gameOwer.num == 1: 
            return False
        return True

#Локализация игры
text = {'rus': {
        'continue': {'bitmap': 'questhead',
                      'strings': ('Да', 'Нет'),
                      'text': '     Сыграем ещё?           ',
                      'title': 'Вы победили!'},
        'instruction': {'font': ('Arial', 12, 'bold', 'italic'),
                         'px': 10,
                         'py': 5,
                         'text': 'Введите число из 4 цифр. Цифры не должны '
                                 'повторяться. \n'
                                 'Быки - угаданные цифры, находящиеся на '
                                 'нужном месте. \n'
                                 'Коровы - угаданные цифры, находящиеся не на '
                                 'нужном месте',
                         'textcolor': '#3d1515',
                         'wd': 400},
        'result': {'douberror': 'Ввели одинаковые цифры \n',
                    'eoff': 'Ввели недастаточно цифр \n',
                    'font': ('times', 12, 'normal'),
                    'notify': 'Ваше число: {user_input} содержит {bulls} быка '
                              'и {cows} коровы\n',
                    'px': 10,
                    'py': 5,
                    'starttext': '',
                    'textcolor': '#000',
                    'wd': 400}},
        'eng': {
        'continue': {'bitmap': 'questhead',
                      'strings': ('Yes', 'No'),
                      'text': '  Shall we play again?    ',
                      'title': 'You win!'},
        'instruction': {'font': ('Arial', 12, 'bold', 'italic'),
                         'px': 10,
                         'py': 5,
                         'text': 'Enter a 4-digit number. Numbers must not be '
                                 'repeated. \n'
                                 'Bulls - guessed numbers, in the right place\n'
                                 'Cows - guessed numbers, that are not in the '
                                 'right place',
                         'textcolor': '#3d1515',
                         'wd': 400},
        'result': {'douberror': 'Entered the same numbers \n',
                    'eoff': 'Not enough numbers were entered \n',
                    'font': ('times', 12, 'normal'),
                    'notify': 'Your number: {user_input} Includes {bulls} bulls '
                              'and {cows} cows\n',
                    'px': 10,
                    'py': 5,
                    'starttext': '',
                    'textcolor': '#000',
                    'wd': 400}}
        }

#Создание объекта
cows_and_bulls = CBGame(500, 700, 'Быки и Коровы', '#5097ab', text, 'eng')
#Запуск игры
cows_and_bulls.mainloop()