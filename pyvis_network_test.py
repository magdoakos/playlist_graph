from pyvis.network import Network
import pandas as pd
from IPython.display import display, HTML
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.physics import Physics
from pyvis.network import Network

df = pd.read_excel(r"C:\Users\aki\VSCodeProject\BlenderSandbox\full_top_2022_songs.xlsx", sheet_name='pivoted')

net = Network(
    notebook = False,
    directed = False,            # directed graph
#     bgcolor = "#0d141d",          # background color of graph 
    bgcolor = '#252c34',
    font_color = "white",       # use yellow for node labels
    cdn_resources = 'in_line',  # make sure Jupyter notebook can display correctly
    height = "4000px",          # height of chart
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



# # ~~~~~~~~~~~~~~~~~~~ WORKING ~~~~~~~~~~~~~~~~~~~
# nodes = list(set([*df['source'], 
#                   *df['target']
#                  ]))
# print(type(nodes))

# # extract the size of each airport
# node_sizes = df.groupby('target').weight.agg(sum)

# values = [node_sizes[node] for node in nodes]
# print(node_sizes.dtype)
# node_sizes.astype(int)
# print(node_sizes.dtype)
# node_sizes = node_sizes.tolist()
# print(type(node_sizes))

# # extract the edges
# edges = df.values.tolist()
# print(type(edges))

# net.add_nodes(nodes) #, value = values

# # add the edges
# net.add_edges(edges)
# net.repulsion(
#     node_distance=200,
#     central_gravity=0.1,
#     spring_length=400,
#     spring_strength=0.05,
#     damping=0.09,
# )



# html = net.generate_html()
# with open("example.html", mode='w', encoding='utf-8') as fp:
#         fp.write(html)
# display(HTML(html))