from tkinter import *
import tkinter.messagebox
import random

window = Tk()
window.title("Обратные крестики-нолики")


def press(cell_number):  # нажатие на клетку
    token = 'X'
    turns[cell_number] = token
    buttons[cell_number].config(text=token, bg='white', state='disabled')
    turns_left.remove(cell_number)
    losing_check(token)

    computer_turn = random.choice(turns_left)  # ход компьютера
    token = 'O'
    turns[computer_turn] = token
    buttons[computer_turn].config(text=token, bg='white', state='disabled')
    turns_left.remove(computer_turn)
    if not turns_left:  # ничья
        tkinter.messagebox.showinfo('End game', 'Конец игры, ничья')
    losing_check(token)


def losing_check(token):  # функция проверки конца игры
    main_count = -1
    for i in turns:  # конец игры через горизонтальную линию слева-направо
        main_count += 1
        if turns[main_count] == token and (main_count % 10) <= 5:
            if turns[main_count] == turns[main_count + 1] == turns[main_count + 2] \
                    == turns[main_count + 3] == turns[main_count + 4]:
                ending_color_line = [buttons[main_count], buttons[main_count + 1], buttons[main_count + 2],
                                     buttons[main_count + 3], buttons[main_count + 4]]
                end_game(ending_color_line, token)

    main_count = -1
    for i in turns:  # конец игры через вертикальную линию сверху-вниз
        main_count += 1
        if turns[main_count] == token and main_count < 60:
            if turns[main_count] == turns[main_count + 10] == turns[main_count + 20] \
                    == turns[main_count + 30] == turns[main_count + 40]:
                ending_color_line = [buttons[main_count], buttons[main_count + 10], buttons[main_count + 20],
                                     buttons[main_count + 30], buttons[main_count + 40]]
                end_game(ending_color_line, token)

    main_count = -1
    for i in turns:  # конец игры через диагональную снизу-вверх, слева-направо
        main_count += 1
        if turns[main_count] == token and main_count > 40 and (main_count % 10) <= 5:
            if turns[main_count] == turns[main_count - 9] == turns[main_count - 18] \
                    == turns[main_count - 27] == turns[main_count - 36]:
                ending_color_line = [buttons[main_count], buttons[main_count - 9], buttons[main_count - 18],
                                     buttons[main_count - 27], buttons[main_count - 36]]
                end_game(ending_color_line, token)

    main_count = -1
    for i in turns:  # конец игры через диагональную сверху-вниз, слева-направо
        main_count += 1
        if turns[main_count] == token and main_count < 60 and (main_count % 10) <= 5:
            if turns[main_count] == turns[main_count + 11] == turns[main_count + 22] \
                    == turns[main_count + 33] == turns[main_count + 44]:
                ending_color_line = [buttons[main_count], buttons[main_count + 11], buttons[main_count + 22],
                                     buttons[main_count + 33], buttons[main_count + 44]]
                end_game(ending_color_line, token)


def end_game(ending_color_line, token):
    for i in buttons:
        i.config(state='disabled')
        if i in ending_color_line:
            i.config(bg='red')
    tkinter.messagebox.showinfo('Конец игры', 'Конец игры, ' + token + ' проиграли!')


turns = [None] * 100
turns_left = list(range(100))
buttons = [
    Button(command=lambda cell_number=i: press(cell_number), width=3, height=1, font=('Arial', 28, 'bold'), bg='grey')
    for i in range(100)]

row = 1;
col = 0
for i in range(100):
    buttons[i].grid(row=row, column=col)
    col += 1
    if col == 10:
        row += 1
        col = 0

window.mainloop()
