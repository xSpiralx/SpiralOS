

# Boot Message
boot_message = """
SpiralOS Starting...
SpiralOS v0.01
Local Mode Enabled
      """
      

running = True
if running:
    print("...running...")
    
print(boot_message)

# User info/request
user_name = input("""
What is your name?
Name: """).strip()
if user_name == "":
    print("A name is required.")
    running == False
else:
    print(f"""
Welcome, {user_name}!
Type "help" to see available commands.
""")
    
while running:
    user_request = input("What can I help you with today?: ").strip().lower()
    if user_request  == "":
        print("A request is required.")
    elif user_request == "hello":
        print(f"Hello, {user_name}")
    elif user_request == "help":
        print("Current Commands: hello, help, about and exit.\n")
    elif user_request == "about":
        print("SpiralOS is a local-first assistant project")
    elif user_request == "exit":
        running = False
        print("System is shutting down.")
    else: 
        user_request != ("help", "exit", "", "about")
        print("Invalid Command.")