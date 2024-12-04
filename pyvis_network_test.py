from pyvis.network import Network
import pandas as pd
from IPython.display import display, HTML
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.physics import Physics
from pyvis.network import Network

df = pd.read_excel(r"full_top_2022_songs.xlsx", sheet_name='pivoted')

net = Network(
    notebook = False,
    directed = False,            # directed graph     
    bgcolor = '#252c34',    # background color of graph 
    font_color = "white",       # use white for node labels
    cdn_resources = 'in_line',  # make sure Jupyter notebook can display correctly
    height = "1000px",          # height of chart
    width = "100%",             # fill the entire width    
    select_menu=False,
    neighborhood_highlight=True,
    )
net.toggle_physics(True)
# net.show_buttons(filter_=['nodes', 'edges', 'physics'])
# net.show_buttons(filter_=['nodes'])
# net.show_buttons(filter_=['physics'])
# net.repulsion(
#     node_distance=180,
#     central_gravity=1.5,
#     spring_length=0,
#     spring_strength=0.05,
#     damping=0.09,
# )
net.barnes_hut(
        gravity=-2000,
        central_gravity=0.15,
        spring_length=0,
        damping=0.34,
        spring_strength=0.165,
        overlap=0
)

# ~~~~~~~~~~~~~~~~~~~ TESTING ~~~~~~~~~~~~~~~~~~~
weight_list = df['weight'] = df['weight'].apply(lambda x: x*1).tolist()
df['weight_for_edges'] = df['weight'].apply(lambda x: x/5)
net.add_nodes(df['target'],
              label=df['target'],
              size=weight_list,
              color=df['color'],
              shape=df['shape']
              ) # weight_for_edges
print(df.index.dtype)
edges = list(zip(df['target'], df['source'], df['weight_for_edges']))
weights = df['weight']
print(edges)


net.add_edges(edges)


html = net.generate_html()
with open("example.html", mode='w', encoding='utf-8') as fp:
        fp.write(html)
display(HTML(html))
