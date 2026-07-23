def calculate_average(numbers):
    """
    Takes a list of numbers and if there are no numbers returns 0, but if there are numbers finds the average of those numbers by adding them together and dividing by the length of the numbers available.
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_max_and_min(numbers):
    """
    Takes a list of numbers and finds the max and min if numbers are available. returns the max and minimum numbers
    """
    if not numbers:
        return None, None
    my_max = tuple(numbers)[0]
    my_min = tuple(numbers)[0]
    for num in numbers:
        if num > my_max:
            my_max = num
    for num2 in numbers:
        if num2 < my_min:
            my_min = num2

    return my_max , my_min


def count_occurrences(items, target):
    """
    this function takes items and a target and counts how many times an item appears.
    """
    counter = 0
    for item in items:
        if item == target:
            counter += 1
    return counter

def is_palindrome(text):
    """
    Function will check to make sure that the text will ignore any spaces and will also convert all letters to lower before checking if the text is a palindrome.
    Takes a string and will return True if the word is spelled the same forward and backward. Will return false if word is not spelled the same forward and backward.
    """
    text = text.replace(" ","").lower()
    return text == text[::-1]

def create_report(title,scores):
    """This function will create a report with arguments that give the title and the scores and will process the average and maximum/minimum scores."""
    average = calculate_average(scores)
    max_min = find_max_and_min(scores)
    report = (f"{title}\nAverage: {average:.2f}\nMax: {max_min[0]}\nMin: {max_min[1]}")
    return report

if __name__ == "__main__":
    # Test each function
    test_scores = [85, 92, 78, 95, 88, 70, 93]
    
    print(f"Average: {calculate_average(test_scores):.2f}")
    print(f"Max/Min: {find_max_and_min(test_scores)}")
    print(f"Count of 85: {count_occurrences(test_scores, 85)}")
    print(f"'racecar' palindrome: {is_palindrome('racecar')}")
    print(f"'hello' palindrome: {is_palindrome('hello')}")
    print()
    print(create_report("Class Scores", test_scores))

    #these are testcases for my functions
    empty_scores = [] #testing the empty lists
    repeated = [80,80,80,80,80] #checking for repeat values
    print("-" * 40)
    print(f"Average: {calculate_average(empty_scores):.2f}") #this will test the empty list
    print(f"Max/Min: {find_max_and_min(empty_scores)}")#testing the empty list
    print(f"Count of 81: {count_occurrences(repeated, 81)}")#checking for repeat values
    print(f"'A man a plan a canal Panama' palindrome: {is_palindrome('A man a plan a canal Panama')}")# this will check if my spacing and capital letter conversion is working. This should come back true
    
