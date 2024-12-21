import matplotlib
matplotlib.use('Agg')  # Use Agg backend
import matplotlib.pyplot as plt

# Simple plot for testing
plt.plot([1, 2, 3], [4, 5, 6])
plt.savefig('test_graph.png')
