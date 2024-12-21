from sympy import symbols, sympify, Abs, exp
import numpy as np
import matplotlib.pyplot as plt
import os
import uuid
import re

def generate_graph(equation, x_range=(-10, 10), num_points=100):
    x = symbols('x')
    original_equation = equation  # Store the original equation
    try:
        # Remove 'y=' if present
        if equation.startswith('y='):
            equation = equation[2:]
        
        # Replace implicit multiplication (e.g., 2x) with explicit multiplication (e.g., 2*x)
        equation = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', equation)
        
        # Replace absolute value notation |x| with Abs(x)
        equation = re.sub(r'\|([a-zA-Z]+)\|', r'Abs(\1)', equation)
        
        # Replace exponential notation e^x with exp(x)
        equation = re.sub(r'e\^([a-zA-Z]+)', r'exp(\1)', equation)
        
        # Remove any whitespace
        equation = equation.replace(' ', '')
        
        # Parse the equation
        expr = sympify(equation)
        
        # Generate x values
        x_values = np.linspace(x_range[0], x_range[1], num_points)
        
        # Calculate y values
        y_values = [expr.subs(x, val) for val in x_values]
        
        # Create the graph
        plt.figure()
        plt.plot(x_values, y_values, label=original_equation)
        plt.title('Graph of ' + original_equation)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axhline(0, color='black', linewidth=0.5, ls='--')
        plt.axvline(0, color='black', linewidth=0.5, ls='--')
        plt.grid()
        plt.legend()
        
        # Ensure the directory exists
        os.makedirs('static/graphs', exist_ok=True)
        
        # Generate a unique filename
        filename = f'graph_{uuid.uuid4().hex}.png'
        
        # Save the graph to a file
        graph_path = os.path.join('static', 'graphs', filename)
        plt.savefig(graph_path)
        plt.close()
        
        return f'graphs/{filename}'
    except Exception as e:
        return str(e)  # Return the error message for debugging