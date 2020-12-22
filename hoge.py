import csv
import matplotlib.pyplot as plt
import networkx as nx

data = []
piyo = []

for i in range(3):
    for j in range(10):
        if(j != 9):
            index = "0"+str(i+1)+"0"+str(j+1)
        else:
            index = "0"+str(i+1)+str(j+1)

        with open(index+".csv") as f:
            reader = csv.reader(f)
            data.append([row for row in reader])

ans = 0
for i in range(30):
    for j in range(30):
        if i < j:
            ab_2 = []
            aabb = []
            time, ans, delay1, delay2 = 0, 0, 0, 0
            if len(data[i]) != 21601:
                delay1 = 2880
            if len(data[j]) != 21601:
                delay2 = 2880
            for k in range(1,21601):
                hoge = int(data[i][k+delay1][2])
                fuga = int(data[j][k+delay2][2])
                ab_2.append((hoge - fuga) ** 2)
                aabb.append(hoge**2 + fuga**2)

            for k in range(len(ab_2)):
                sum_ab_2 = sum(ab_2[k:k+60])
                sum_aabb = sum(aabb[k:k+60])
                if sum_aabb != 0:
                    if sum_ab_2/sum_aabb <= 0.05 and sum_aabb >= 5500:
                        time += 1
                        if time >= 15:
                            ans += 1
                    else:
                        time = 0

            print("{}, {}, {}".format(i+1,j+1,ans))
            if ans != 0:
                piyo.append([i+1,j+1,ans])

G = nx.Graph()
G.add_nodes_from(list(range(1,31)))
G.add_weighted_edges_from(piyo)
edge_width = [d["weight"] * 0.02 for (u, v, d) in G.edges(data=True)]
pos = nx.spring_layout(G, k=0.3)
nx.draw(G,pos, with_labels=True, width=edge_width)
plt.show()