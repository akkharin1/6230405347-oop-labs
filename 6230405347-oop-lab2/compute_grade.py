def score_check(n):
    if n == 0:
        term = "midterm"
    elif n == 1:
        term = "final"
    score = False
    while not score:
        try:
            while True:
                score = float(input(f"please enter the student's {term} exam mark (0-100): "))
                if score > 100 or score < 0:
                    print(("Please enter a valid %s exam mark (0-100)") % term)
                else:
                    break
        except ValueError:
            print(("Please enter a valid %s exam mark (0-100)") % term)
        else:
            return score / 2

n = 0
name = input("Please enter a student name: ")
midterm_score = score_check(n)
n = 1
final_score = score_check(n)
average_score = midterm_score + final_score
if average_score < 50:
    print("%s has total mark as %.2f and grade as F" % (name, average_score))
if average_score >= 50 and average_score < 60:
    print("%s has total mark as %.2f and grade as D" % (name, average_score))
if average_score >= 60 and average_score < 70:
    print("%s has total mark as %.2f and grade as C" % (name, average_score))
if average_score >= 70 and average_score < 80:
    print("%s has total mark as %.2f and grade as B" % (name, average_score))
if average_score >= 80 and average_score <= 100:
    print("%s has total mark as %.2f and grade as A" % (name, average_score))