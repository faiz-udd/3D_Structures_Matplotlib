import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence

def plot_fibonacci_3d(n):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    fibonacci_sequence = generate_fibonacci(n)
    x = fibonacci_sequence
    y = range(len(fibonacci_sequence))
    z = [0] * len(fibonacci_sequence)
    
    ax.scatter(x, y, z, c='r', marker='o')
    
    ax.set_xlabel('Fibonacci Number')
    ax.set_ylabel('Index')
    ax.set_zlabel('Z')
    
    plt.title('3D Structure of Fibonacci Numbers')
    
    plt.show()

# Set the number of Fibonacci numbers to generate and plot
num_fibonacci = 1000
plot_fibonacci_3d(num_fibonacci)
