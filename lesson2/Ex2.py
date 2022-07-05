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
    if turns_left == []: #ничья
        pass

def losing_check(token):
    main_count = -1
    for i in turns:
        main_count += 1
        if turns[main_count] == token and (main_count % 10) <= 5:
            if turns[main_count] == turns[main_count+1] == turns[main_count+2] \
                == turns[main_count+3] == turns[main_count+4]:
                ending_color_line = [main_count, main_count+1, main_count+2, main_count+3, main_count+4]
                print('END GAME')

    main_count = -1
    for i in turns:
        main_count += 1
        if turns[main_count] == token and main_count < 60:
            if turns[main_count] == turns[main_count+10] == turns[main_count+20] \
                == turns[main_count+30] == turns[main_count+40]:
                ending_color_line = [main_count, main_count+10, main_count+20, main_count+30, main_count+40]
                print('END GAME2')

    main_count = -1
    for i in turns:
        main_count += 1
        if turns[main_count] == token and main_count > 40 and (main_count % 10) <= 5:
            if turns[main_count] == turns[main_count-9] == turns[main_count-18] \
                == turns[main_count-27] == turns[main_count-36]:
                ending_color_line = [main_count, main_count-9, main_count-18, main_count-27, main_count-36]
                print('END GAME3')

    main_count = -1
    for i in turns:
        main_count += 1
        if turns[main_count] == token and main_count < 60 and (main_count % 10) <= 5:
            if turns[main_count] == turns[main_count+11] == turns[main_count+22] \
                == turns[main_count+33] == turns[main_count+44]:
                print('END GAME4')
        

            # if turns.index(i) < 60 and turns[turns.index(i)] == \
            # turns[turns.index(i)+10] == turns[turns.index(i)+20] == turns[turns.index(i)+30] == turns[turns.index(i)+40]:
            #     end_game()
            
def end_game():
    print('END GAME')

# up_diag_exception = [0, 1, 2, 3, 10, 11, 12, 20, 21, 30, 69, 78, 79, 87, 88, 89, 96, 97, 98, 99]
# down_diag_exception = []
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