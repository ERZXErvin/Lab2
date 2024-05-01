bmi = 0
weight = 0
height = 0
def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
  
 #Add code here to calculate BMI
    bmiindex = weight/(height*height)
 
 #Add code here to display calculate BMI
    print("BMI INDEX = " + str(bmiindex))
 
    if (bmiindex < 18.5):
        print ("Underweight")
        return -1

<<<<<<< HEAD:bmi2.py
    if (bmi >= 18.5 and bmi <= 25.0):
        print ("Normal Weight")
        return 0

    if (bmi > 25.0):
=======
    if (bmiindex >= 18.5 and bmiindex <=25.0):
        print ("Normal Weight")
        return 0

    if (bmiindex > 25.0):
>>>>>>> 58e1a0c9e1de8f27cd31b16fae1162ae90dae858:bmi.py
        print ("Overweight")       
        return 1



<<<<<<< HEAD:bmi2.py
calculate_bmi(weight=197, height=1.73)
=======
calculate_bmi(1.8, 100)
>>>>>>> 58e1a0c9e1de8f27cd31b16fae1162ae90dae858:bmi.py



