

#Boot Message
print("""
SpiralOS Starting...
SpiralOS v0.01
Local Mode Enabled
      """)


user_name = input(f"""What is your name?
    Name: """)
if user_name == "":
    print("You didn't type anything.")

user_request = input(f"What can I help you with today?: ")

if user_request  == "":
    print("You didn't type anything.")



#Edge case for no input
if user_request or user_name == "":
    print("You didn't type anything.")



#print(f"SpiralOS heard you say: {user_input}")
print(f"Welcome {user_name}")
print(f"Let's get started on {user_request}!")

#if user_input == "Hello":
    #print("What can I help you with today?")