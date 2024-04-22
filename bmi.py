bmi = 0
weight = 0
height = 0
def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
  
 #Add code here to calculate BMI
    bmi = weight/(height*height)
 
 #Add code here to display calculate BMI
    print("BMI = " + str(bmi))
 
    if (bmi < 18.5):
        print ("Underweight")

    if (bmi >= 18.5, bmi <= 25.0):
        print ("Normal Weight")

    if (bmi > 25.0):
        print ("Overweight")
    
calculate_bmi(weight=57, height=1.73)



