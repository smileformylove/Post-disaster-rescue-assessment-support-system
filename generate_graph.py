import json
import numpy as np
import os
import PIL.Image
import PIL.ImageDraw
import torch
import networkx as nx
import matplotlib.pyplot as plt


json_path = 'road.json'
device = 'cuda' if torch.cuda.is_available() else 'cpu'


def shape_to_mask(img_shape, points):
    mask = np.zeros(img_shape[:2], dtype=np.uint8)
    mask = PIL.Image.fromarray(mask)
    draw = PIL.ImageDraw.Draw(mask)
    xy = [tuple(point) for point in points]
    assert len(xy) > 2, 'Polygon must have points more than 2'
    draw.polygon(xy=xy, outline=1, fill=1)
    mask = np.array(mask, dtype=bool)
    return mask


def is_neighbor(plg1, plg2):
    plg1 = torch.Tensor(plg1).to(device)
    plg2 = torch.Tensor(plg2).to(device)
    plg1 = plg1.unsqueeze_(1)
    plg2 = plg2.unsqueeze_(0)
    distance = torch.sqrt(torch.pow(plg1 - plg2, 2).sum(2))
    min_dist = torch.min(distance)
    if min_dist < 10:
        return True
    else:
        return False


if __name__ == '__main__':

    with open(json_path, encoding='utf-8') as f:
        diction = json.load(f)
        height = diction['imageHeight']
        width = diction['imageWidth']
        shapes = diction['shapes']

    img_shape = (width, height)
    matrix = np.zeros(img_shape, dtype=np.int8)
    for shape in shapes:
        points = shape['points']
        mask = shape_to_mask(img_shape, points)
        matrix[mask] = int(shape['label'])
    length = len(shapes)
    relation_matrix = np.zeros((length, length), dtype=np.int8)

    G = nx.Graph()
    G.add_nodes_from(list(range(length)))
    color_map = []
    for i in range(length):
        label = shapes[i]['label']
        if label == '1':
            color_map.append('blue')
        elif label == '2':
            color_map.append('green')
        else:
            color_map.append('yellow')
        for j in range(length):
            if i != j:
                neighbor = is_neighbor(
                    shapes[i]['points'], shapes[j]['points'])
                if neighbor:
                    relation_matrix[i, j] = 1
                    G.add_edge(i, j)
                    print(
                        '%d label:%s is neighbor to %d label:%s' %
                        (i, label, j, shapes[j]['label']))
    nx.draw(G, node_color=color_map, with_labels=True)
    plt.savefig('fig.png', bbox_inches='tight')
    plt.show()

    # roads = [i for i in range(length) if shapes[i]['label'] != '3']
    # build = list(range(length))
    # for road in roads:
    #     for i in range(length):
    #         if relation_matrix[road, i] == 1 and

