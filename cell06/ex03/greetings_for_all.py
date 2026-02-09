def greetings(name=None):
    if not name:
        print("Hello, noble stranger.")
    elif not isinstance(name, str):
        print(f"Error! It was not a name.")
    else:
        print(f"Hello, {name}!")
greetings('Alexandra')
greetings('Will')
greetings()
greetings(42)