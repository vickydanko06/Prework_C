def calculate_average(numbers):
    """
    Takes a list of numbers, returns the average. Returns 0 if the list is empty.
    """
    if not numbers:
        return {"Average": 0}
    return {"Average": sum(numbers) / len(numbers)}

def find_max_and_min(numbers):
    """
    Takes a list of numbers, returns a tuple (max_value, min_value).
    """
    if not numbers:
        return {"Max": None, "Min": None}
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
    Takes a list of items and a target item, returns the number of occurrences of the target item in the list.
    """
    counter = 0
    for item in items:
        if item == target:
            counter += 1
    return counter

def is_palindrome(text):
    """
    Takes a string, returns True if it reads the same forward and backward (case-insensitive, ignoring spaces). Examples: "racecar" → True, "hello" → False, "A man a plan a canal Panama" → True.
    """
    return text == text[::-1]

def create_report(title,scores):
    """Takes a report title and a list of scores. Uses calculate_average and find_max_and_min internally"""
    average = calculate_average(scores)
    max_min = find_max_and_min(scores)
    report = (f"{title}\nAverage: {average['Average']:.2f}\nMax: {max_min[0]}\nMin: {max_min[1]}")
    return report

if __name__ == "__main__":
    # Test each function
    test_scores = [85, 92, 78, 95, 88, 70, 93]
    
    print(f"Average: {calculate_average(test_scores)['Average']:.2f}")
    print(f"Max/Min: {find_max_and_min(test_scores)}")
    print(f"Count of 85: {count_occurrences(test_scores, 85)}")
    print(f"'racecar' palindrome: {is_palindrome('racecar')}")
    print(f"'hello' palindrome: {is_palindrome('hello')}")
    print()
    print(create_report("Class Scores", test_scores))