import pandas as pd
import plotly.express as px

# Read file
file_path = "D:/学习/aaaNottingham/reasearch method/CW2/Results_21Mar2022.csv"
df = pd.read_csv(file_path)

# Choose variables
selected_columns = [
    'mean_ghgs',           
    'mean_land',           
    'mean_watscar',        
    'mean_eut',            
    'mean_bio',            
    'mean_watuse'          
]

# Draw scatter matrix
fig = px.scatter_matrix(
    df,
    dimensions=selected_columns,
    color="diet_group",  
    symbol="sex",        
    title="Environmental Impacts by Diet Group",
    labels={col: col.replace('_', ' ').capitalize() for col in selected_columns},
    height=800
)

# Hide diagonal plots
fig.update_traces(diagonal_visible=False)

# Update layout
fig.update_layout(
    dragmode='select',
    plot_bgcolor='white',
    font=dict(size=16), 
    title_font=dict(size=40, family='Arial', color='black'), 
    coloraxis_colorbar=dict(title="Diet Group"),
)

# Force all x/y axes to show grid lines
for i in range(1, len(selected_columns)+1):
    for j in range(1, len(selected_columns)+1):
        fig.update_layout({
            f'xaxis{i*j}': dict(
                showgrid=True,
                gridcolor='lightgrey',
                gridwidth=1,
                zeroline=False,
                showline=True,
                linecolor='lightgrey',
                linewidth=1,
                title_font=dict(size=14), 
                tickfont=dict(size=11),  
            ),
            f'yaxis{i*j}': dict(
                showgrid=True,
                gridcolor='lightgrey',
                gridwidth=1,
                zeroline=False,
                showline=True,
                linecolor='lightgrey',
                linewidth=1,
                title_font=dict(size=14), 
                tickfont=dict(size=11),  
            )
        })

fig.show()