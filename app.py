from flask import Flask, render_template, request
import matplotlib
matplotlib.use('Agg')  # Use the Agg backend
import matplotlib.pyplot as plt
import os
from graph_generator import generate_graph  # Ensure this is the correct import path

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        equation = request.form['equation']
        graph_path = generate_graph(equation)  # Ensure this returns a relative path like 'graphs/graph.png'
        
        # If graph_path contains an error message, render an error page or show an error in graph.html
        if "Error" in graph_path or "could not parse" in graph_path:
            return render_template('graph.html', graph_path=graph_path, equation=equation, error=True)
        
        return render_template('graph.html', graph_path=graph_path, equation=equation)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
