first_name = "Vicky"
last_name = "Danko"
age = 32
city = "Pittsburgh"
current_job = "IT Compliance Analyst"
reason = "I want to rebrand myself to get into software engineering."
fun_fact = "I used to be an assistant coach for a D3 college volleyball team." # this is always a fun fact that i like to use when introducing myself to new people.

print("=~"* 40) #i wanted to use a different decoration so i added in the ~
print(f"Student Profile")
print("=~"* 40)
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"__"* 40)#just wanted some more separation between the sections of the profile
print(f"\nCurrent Job: {current_job}")
print(f"__"* 40)#separation between the sections of the profile
print(f"\nWhy I'm learning to code: {reason}")
print(f"__"* 40)#separation between the sections of the profile
print(f"\nFun Fact: {fun_fact}")#it took me about 10 mins to figure out that \n was for the escape character instead of \\n
print("=~"* 40)