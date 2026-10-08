def create_greeting(name, job):
    sentence = "hi" + " dear" + " " + name + " " + "i hope you are successful as an" + " " + job
    return sentence


name = input("your name: ")
job = input("your job: ")

print(create_greeting(name, job))