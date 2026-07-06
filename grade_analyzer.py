#Variables needed for the Grade Analyzer
scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71] #Given list of scores from Practice Exercise
count_a = 0
count_b = 0
count_c = 0
count_d = 0
count_f = 0

#For loop to count and store the grade
for score in scores:
    if score >= 90 and score <=100:
        count_a += 1
    if score >= 80 and score <= 89:
        count_b += 1
    if score >= 70 and score <= 79:
        count_c += 1
    if score >= 60 and score <= 69:
        count_d += 1
    if score < 60:
        count_f += 1

#Math Section for the Grade Analyzer
total_scores = len(scores) #Gives the total number of scores in the list
average_score = sum(scores) / total_scores #Calculates the average score
highest_score = max(scores) #Finds the highest score in the list
lowest_score = min(scores) #Finds the lowest score in the list
passing_scores = count_a + count_b + count_c + count_d #Calculates the total number of passing scores
passing_average = passing_scores / total_scores * 100 #Calculates the percentage of passing scores
failing_scores = count_f #Calculates the total number of failing scores
failing_average = failing_scores / total_scores * 100 #Calculates the percentage of failing scores
    

#Fomat of the grade analyzer
print("=== Grade Analyzer ===")
print(f"Total Scores: {total_scores}")
print(f"Average: {average_score:.1f}")
print(f"Highest: {highest_score}")
print(f"Lowest: {lowest_score}")
print(f"Passing: {passing_scores} ({passing_average:.1f}%)")
print(f"Failing: {failing_scores} ({failing_average:.1f}%)")
print("\nGrade Distribution: ")
print(f"A: {count_a}")
print(f"B: {count_b}")
print(f"C: {count_c}")
print(f"D: {count_d}")
print(f"F: {count_f}")
print("\n")
print("\n=== Add More Scores ===")
#Input Section for the Grade Analyzer
update_scores = input("Enter a score (or done to finish):")

while update_scores != "done":
    try:
        score = int(update_scores)
        if score < 0 or score > 100:
            print("Invalid score. Please enter a score between 0 and 100.")
        else:
            scores.append(score) #adds the new score to the list
            average_score = sum(scores) / len(scores) #Calculates the average score
            print(f"Updated Average: {average_score:.1f}") #prints the new average score

    except ValueError:
        print("Invalid input. Please enter a valid integer score or 'done' to finish.")
    update_scores = input("Enter a score (or done to finish):")
print(f"Final Average: {average_score:.1f}") #prints the final average score

