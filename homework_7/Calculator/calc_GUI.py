from tkinter import Button, Tk, Label
from calc_core import Calculator

expression = ''


def update_expression_and_screen(data):
    global expression
    if expression:
        if expression[-1] not in ['+', '-', '*', '/']:
            expression += data
            calc_screen.config(text=expression)
        elif data not in ['+', '-', '*', '/']:
            expression += data
            calc_screen.config(text=expression)
        else:
            return
    else:
        if data not in ['+', '-', '*', '/']:
            expression += data
            calc_screen.config(text=expression)
        else:
            return


def convert_to_e_format(e):
    remain_screen = 12 - len(str(e)) - 2
    return expression[0] + '.' + expression[1:remain_screen - 2] + 'e+' + str(e)


def button_1_click(message):
    update_expression_and_screen('1')


def button_2_click(message):
    update_expression_and_screen('2')


def button_3_click(message):
    update_expression_and_screen('3')


def button_4_click(message):
    update_expression_and_screen('4')


def button_5_click(message):
    update_expression_and_screen('5')


def button_6_click(message):
    update_expression_and_screen('6')


def button_7_click(message):
    update_expression_and_screen('7')


def button_8_click(message):
    update_expression_and_screen('8')


def button_9_click(message):
    update_expression_and_screen('9')


def button_0_click(message):
    update_expression_and_screen('0')


def button_divide_click(message):
    update_expression_and_screen('/')


def button_multiply_click(message):
    update_expression_and_screen('*')


def button_subtract_click(message):
    update_expression_and_screen('-')


def button_add_click(message):
    update_expression_and_screen('+')


def button_dot_click(message):
    update_expression_and_screen('.')


def button_equal_click(message):
    global expression
    expression = Calculator.run_calculation(expression)
    if expression[-2:] == '.0':
        expression = expression[:-2]
    if len(expression) > 12:
        if expression.find('.') <= 9 and 'e' not in expression:
            expression = expression[:12]
        elif expression.find('.') <= 9 and 'e' in expression:
            calc_screen.config(
                text=expression[:12 - len(expression[expression.find('e'):])] + expression[expression.find('e'):])
            return
        elif expression.find('.') > 9:
            calc_screen.config(text=convert_to_e_format(expression.find('.') - 1))
            return
        else:
            calc_screen.config(text=convert_to_e_format(len(expression) - 1))
            return

    calc_screen.config(text=expression)
    if expression == 'Error':
        expression = ''


def button_clear_click(message):
    global expression
    expression = ''
    calc_screen.config(text='0')


def button_backspace_click(message):
    global expression
    if expression:
        expression = expression[:-1]
        if not expression:
            calc_screen.config(text='0')
        else:
            calc_screen.config(text=expression)


root = Tk()
root.title('Calculator')
root.geometry('266x378')
root.resizable(0, 0)

calc_screen = Label(root, text='0', bg='white', anchor='e', font='Courier 25', borderwidth=1, relief='solid')
calc_screen.place(x=10, y=10, width=246, height=40)

btn_clear = Button(root, text='C', font='Courier 25')
btn_clear.place(x=196, y=60, width=60, height=60)
btn_clear.bind('<Button-1>', button_clear_click)

btn_backspace = Button(root, text='<-', font='Courier 25')
btn_backspace.place(x=134, y=60, width=60, height=60)
btn_backspace.bind('<Button-1>', button_backspace_click)

btn_7 = Button(root, text='7', font='Courier 25')
btn_7.place(x=10, y=122, width=60, height=60)
btn_7.bind('<Button-1>', button_7_click)
btn_8 = Button(root, text='8', font='Courier 25')
btn_8.place(x=72, y=122, width=60, height=60)
btn_8.bind('<Button-1>', button_8_click)
btn_9 = Button(root, text='9', font='Courier 25')
btn_9.place(x=134, y=122, width=60, height=60)
btn_9.bind('<Button-1>', button_9_click)
btn_divide = Button(root, text='/', font='Courier 25')
btn_divide.place(x=196, y=122, width=60, height=60)
btn_divide.bind('<Button-1>', button_divide_click)

btn_4 = Button(root, text='4', font='Courier 25')
btn_4.place(x=10, y=184, width=60, height=60)
btn_4.bind('<Button-1>', button_4_click)
btn_5 = Button(root, text='5', font='Courier 25')
btn_5.place(x=72, y=184, width=60, height=60)
btn_5.bind('<Button-1>', button_5_click)
btn_6 = Button(root, text='6', font='Courier 25')
btn_6.place(x=134, y=184, width=60, height=60)
btn_6.bind('<Button-1>', button_6_click)
btn_multiply = Button(root, text='*', font='Courier 25')
btn_multiply.place(x=196, y=184, width=60, height=60)
btn_multiply.bind('<Button-1>', button_multiply_click)

btn_1 = Button(root, text='1', font='Courier 25')
btn_1.place(x=10, y=246, width=60, height=60)
btn_1.bind('<Button-1>', button_1_click)
btn_2 = Button(root, text='2', font='Courier 25')
btn_2.place(x=72, y=246, width=60, height=60)
btn_2.bind('<Button-1>', button_2_click)
btn_3 = Button(root, text='3', font='Courier 25')
btn_3.place(x=134, y=246, width=60, height=60)
btn_3.bind('<Button-1>', button_3_click)
btn_subtract = Button(root, text='-', font='Courier 25')
btn_subtract.place(x=196, y=246, width=60, height=60)
btn_subtract.bind('<Button-1>', button_subtract_click)

btn_dot = Button(root, text='.', font='Courier 25')
btn_dot.place(x=10, y=308, width=60, height=60)
btn_dot.bind('<Button-1>', button_dot_click)
btn_0 = Button(root, text='0', font='Courier 25')
btn_0.place(x=72, y=308, width=60, height=60)
btn_0.bind('<Button-1>', button_0_click)
btn_equal = Button(root, text='=', font='Courier 25')
btn_equal.place(x=134, y=308, width=60, height=60)
btn_equal.bind('<Button-1>', button_equal_click)
btn_add = Button(root, text='+', font='Courier 25')
btn_add.place(x=196, y=308, width=60, height=60)
btn_add.bind('<Button-1>', button_add_click)

root.mainloop()
