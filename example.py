def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:  # Intentional issue for demo
        print("Hello, World!")

greet("SonarQube")
greet(None)
