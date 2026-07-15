noinput_error = "You didn't type anything in the input."

#Boot Message
print("""
SpiralOS Starting...
SpiralOS v0.01
Local Mode Enabled
      """)


user_name = input("""What is your name?
    Name: """)
if user_name == "":
    print(noinput_error)

user_request = input("What can I help you with today?: ")

#Edge case for blank 
if user_request  == "":
    print(noinput_error)






#print(f"SpiralOS heard you say: {user_input}")
print(f"Welcome {user_name}")
print(f"Let's get started on {user_request}!")

#if user_input == "Hello":
    #print("What can I help you with today?")