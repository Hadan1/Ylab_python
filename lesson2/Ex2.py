from tkinter import *
import random


window = Tk()
window.title("Обратные крестики-нолики")

def press(cell_number):
    token = 'X'
    turns[cell_number] = token
    buttons[cell_number].config(text=token, bg='white', state='disabled')
    turns_left.remove(cell_number)
    print(turns)
    print(turns_left)
    losing_check(token)

    computer_turn = random.choice(turns_left)
    token = 'O'
    turns[computer_turn] = token
    buttons[computer_turn].config(text=token, bg='green', state='disabled')
    turns_left.remove(computer_turn)
    # losing_check(token)
    if turns_left == []: #ничья
        pass

def losing_check(token):
    count = 0
    for i in turns:
        if i == token and (turns.index(i) % 10) <= 5:
            # print('asd')
            if turns.index(i) % 10 <= 5 and turns[turns.index(i)] == turns[turns.index(i)+1] == turns[turns.index(i)+2] == turns[turns.index(i)+3] == turns[turns.index(i)+4]:
                end_game()

            # if turns.index(i) < 60 and turns[turns.index(i)] == \
            # turns[turns.index(i)+10] == turns[turns.index(i)+20] == turns[turns.index(i)+30] == turns[turns.index(i)+40]:
            #     end_game()
            
def end_game():
    print('END GAME')


turns = [None] * 100
turns_left = list(range(100))

buttons = [Button(command=lambda cell_number=i: press(cell_number), width=6, height=3, bg='grey') for i in range(100)]
# width=3, height=1 font=('Arial', 28, 'bold')

row = 1; col = 0
for i in range(100):
    buttons[i].grid(row=row, column=col)
    col += 1
    if col == 10:
        row += 1
        col = 0
window.mainloop()