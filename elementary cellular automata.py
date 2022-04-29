import copy
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import numpy as np 

def rule(num): #takes the input number and changes it into a binary list to make rules easier
    binary = np.binary_repr(num, 8)
    bin_list = []
    for i in range(len(binary)):
        bin_list.append(binary[i])
    return bin_list

def rulegen(list_i, given_rule): #generates the rules
    list_j = copy.copy(list_i)
    for i in range(len(list_i)-1):
        if list_i[i-1] == 1 and list_i[i] == 1 and list_i[i+1] == 1:
            x = int(given_rule[0])
            list_j[i] = x
        if list_i[i-1] == 1 and list_i[i] == 1 and list_i[i+1] == 0:
            x = int(given_rule[1])
            list_j[i] = x
        if list_i[i-1] == 1 and list_i[i] == 0 and list_i[i+1] == 1:
            x = int(given_rule[2])
            list_j[i] = x
        if list_i[i-1] == 1 and list_i[i] == 0 and list_i[i+1] == 0:
            x = int(given_rule[3])
            list_j[i] = x
        if list_i[i-1] == 0 and list_i[i] == 1 and list_i[i+1] == 1:
            x = int(given_rule[4])
            list_j[i] = x
        if list_i[i-1] == 0 and list_i[i] == 1 and list_i[i+1] == 0:
            x = int(given_rule[5])
            list_j[i] = x
        if list_i[i-1] == 0 and list_i[i] == 0 and list_i[i+1] == 1:
            x = int(given_rule[6])
            list_j[i] = x
        if list_i[i-1] == 0 and list_i[i] == 0 and list_i[i+1] == 0:
            x = int(given_rule[7])
            list_j[i] = x
    return list_j

def gen(given_rule): #generates the automata
    list_a = [0 for x in range(501)]
    list_a[251] = 1 #middle cell in first list is alive
    listy = []
    given_rule = int(given_rule)
    given_rule_list = rule(given_rule)
    print(given_rule, given_rule_list)
    for x in range(400):
        listy.append(list_a)
        list_a = rulegen(list_a, given_rule_list)
    return listy
        

if __name__ == "__main__":
    given_rule = input('Input rule number (0-255): ')
    given_rule = int(given_rule)
    listy = gen(given_rule)

    plt.rcParams['image.cmap'] = 'binary'
    fig, ax = plt.subplots(figsize=(16, 9))

    plt.subplots_adjust(left=0, bottom=0.25)
    axrule = plt.axes([0.25, 0.1, 0.65, 0.03])
    rule_slider = Slider(
    ax=axrule,
    label='Rule number',
    valmin=1,
    valmax=255,
    valinit=given_rule,
    valstep = 1
    )  
    resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
    button = Button(resetax, 'Reset', hovercolor='0.975')

    def reset(event):
        given_rule = int(rule_slider.val)
        listy = gen(given_rule)
        ax.matshow(listy)
        ax.axis(False)
        plt.show()
    button.on_clicked(reset)
    
    ax.matshow(listy)
    ax.axis(False)
    plt.show()