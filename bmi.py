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

    if (bmiindex >= 18.5 and bmiindex <=25.0):
        print ("Normal Weight")
        return 0

    if (bmiindex > 25.0):
        print ("Overweight")       
        return 1



calculate_bmi(1.8, 100)



