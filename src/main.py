
#Boot Message
print("""SpiralOS Starting...
         SpiralOS v0.01
         Local Mode Enabled
      """)
#User name defined
user_name = input("Enter Name: ")
#User input var defined
user_input = input("You: ")

#Edge case for no input
if user_input == "":
    print("You didn't type anything.")

print(f"""What is your name?
      Name: {user_name}""")


print(f"SpiralOS heard you say: {user_input}")
print(f"Welcome {user_name}")

if user_input == "Hello":
    print("What can I help you with today?")