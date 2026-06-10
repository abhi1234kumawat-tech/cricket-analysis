import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

data = {
    'Match': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Runs': [73, 25, 0, 51, 82, 13, 45, 100, 34, 67],
    'Balls': [54, 22, 3, 40, 60, 15, 38, 72, 30, 50]
}

df = pd.DataFrame(data)
df['Strike_Rate'] = (df['Runs'] / df['Balls']) * 100

plt.figure(figsize=(10, 5))
plt.plot(df['Match'], df['Runs'], marker='o', color='red', label='Runs')
plt.title('Virat Kohli - IPL Performance')
plt.xlabel('Match Number')
plt.ylabel('Runs')
plt.legend()
plt.grid(True)
plt.savefig('kohli_graph.png')

print("Graph save ho gaya!")
print(df)
