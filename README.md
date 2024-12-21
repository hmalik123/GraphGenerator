# Flask Graph App

This project is a Flask web application that allows users to input mathematical equations and generate corresponding graphs. The application utilizes SymPy for parsing equations, NumPy for generating data points, and Matplotlib or Plotly for graphing.

## Project Structure

```
flask-graph-app
├── app.py                # Main entry point of the Flask application
├── templates
│   ├── index.html       # HTML form for user input
│   └── graph.html       # Displays the generated graph
├── static
│   ├── css
│   │   └── styles.css    # CSS styles for the application
│   └── js
│       └── scripts.js     # JavaScript for client-side interactivity
├── graph_generator.py    # Module for parsing equations and generating graphs
├── requirements.txt      # Lists project dependencies
└── README.md             # Project documentation
```

## Setup Instructions

1. **Clone the repository:**

   ```
   git clone <repository-url>
   cd flask-graph-app
   ```

2. **Create a virtual environment:**

   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install dependencies:**

   ```
   pip install -r requirements.txt
   ```

5. **Run the Flask application:**

   ```
   python app.py
   ```

6. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- Navigate to the home page to input your mathematical equation.
- Submit the form to generate and view the graph based on the provided equation.

## Future Enhancements

- Add support for more complex equations.
- Implement user authentication for saving graphs.
- Enhance the UI with additional styling and features.
- Add threejs for 3d interactive graph models where I can manually change the graph and it will return the graph equation
- Allow user to export graph simulations / save them
