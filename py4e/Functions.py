# this program calculates the overtime pay based on the hours worked and hourly rate entered

# def computepay(hours, rate):
#     try:
#         hours  = int(hours)
#         rate = float(rate)
#         try:
#             hours = float(rate)
#             if hours > 40:
#                 overtimeWorked = hours - 40
#                 overtimerate = rate * 1.5
#                 pay = hours * rate + overtimerate * overtimeWorked
#                 print(f"your pay check is going to be: {pay}")
#             else:
#                 pay = hours * rate
#         except: 
#             print("please enter a dollar amount")
#     except:
#         print("please enter a whole number")
#     return(f"your pay check is going to be: ${pay}")

# print(computepay(20,10))


# this program calculates the grade based on the score entered
def computergrade(score):
    try:
        score = float(score)
        if(score >1):
            print("please enter a numeric value between 0 and 1")
        elif(score >= 0.9):
            grade = ("your grade is 'A'")
            return grade
        elif(score <0.9 and score >= 0.8):
            grade = ("your grade is 'B'")
            return grade
        elif(score < 0.8 and score >= 0.7):
            grade = ("your grade is 'C'")
            return grade
        elif(score < 0.7 and score >= 0.6):
            grade = ("your grade is 'D'")
            return grade
        elif(score < 0):
            print("please enter a numeric value between 0 and 1")
        else:
            grade = ("your grade is 'F'")
            return grade

    except:
        print("please enter a numeric value between 0 and 1")

print(computergrade(0.91))
print(computergrade(10))
print(computergrade("perfect"))
print(computergrade(0.75))
print(computergrade(0.5))
