def generate_fibonacci():
    # Get the number of terms from the user
    try:
        n = int(input("Enter the number of terms: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
        
        # Initialize the Fibonacci sequence
        fib_sequence = []
        a, b = 0, 1
        
        # Generate the sequence
        for _ in range(n):
            fib_sequence.append(a)
            a, b = b, a + b
        
        # Display the sequence
        print("Fibonacci sequence:")
        print(fib_sequence)
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Call the function
generate_fibonacci()
