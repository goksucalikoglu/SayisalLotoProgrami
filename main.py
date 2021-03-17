import random
sayilar=[]
kolon=1
while (True):
    sayi=random.randint(1,49)
    if len(sayilar)==6:
        sayilar.sort()
        print("(). Kolon: ".format(kolon),sayilar)
        kolon+=1
        sayilar=[]
        if kolon==9:
            break

    else:
        if not (sayi in sayilar):
            sayilar.append(sayi)
input("Kapatmak için enter'a basın")



# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
