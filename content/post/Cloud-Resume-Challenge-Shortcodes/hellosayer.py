class hello_sayer:
    def __init__(self, greeting = "Hello"):
        self.greeting = greeting
    def say_hello(self, name):
        print(f"{self.greeting}, {name}!")

if __name__ == "__main__":
    h = hello_sayer("Good morning")
    h.say_hello("Jeff")