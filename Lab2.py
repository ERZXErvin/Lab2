
import statistics
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    userinput = get_user_input()
    calc_average_temperature(userinput)
    calc_min_max_temperature(userinput)
    calc_median_temperature(userinput)

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
    print("Average =", average)
    return 2

def calc_min_max_temperature(userinput):
    minnum = min(userinput)
    maxnum = max(userinput)
    print("Min =", minnum)
    print("Max =", maxnum)
    return 0

def calc_median_temperature(userinput):
    sortedinput = sorted(userinput)
    median = statistics.median(sortedinput)
    print("Median =", median)
    return 1

main()