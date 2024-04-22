
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    userinput = get_user_input()
    calc_average_temperature(userinput)
    calc_min_max_temperature(userinput)

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    userinput = input()
    num_list = userinput.split(", ")
    new_list = [float(x) for x in num_list]
    print(new_list)
    return(new_list)

def calc_average_temperature(userinput):
    average = sum(userinput)/len(userinput)
    print("average =", average)
    return average

def calc_min_max_temperature(userinput):
    minnum = min(userinput)
    maxnum = max(userinput)
    print("Min =", minnum)
    print("Max =", maxnum)



main()