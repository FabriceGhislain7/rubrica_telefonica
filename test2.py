try:
    while True:
        number = int(input("Insert number: "))
except ValueError as e:
    print(f"Error: {e}")

print(f"{'-' * 40}")

