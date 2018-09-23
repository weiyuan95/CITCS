import random
import numpy as np
import tensorflow as tf
from keras.models import load_model

class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def addEdge(self, node):
        self.edges.append(node)


def skill_puzzle(data):
    offensive = data["boss"]["offense"]

    attack_list = []
    offense_list = []
    points_list = []
    attack_offense_dict = {}
    attack_point_dict = {}
    nodes = []
    final_attack_list = []

    for skill in data["skills"]:
        attack_list.append(skill["name"])
        offense_list.append(skill["offense"])
        points_list.append(skill["points"])
        attack_point_dict.update({skill["name"]: skill["points"]})
        attack_offense_dict.update({skill["name"]: skill["offense"]})

        curr_node = Node(skill["name"])
        nodes.append(curr_node)

        if skill["require"] in attack_list:
            nodes[attack_list.index(skill["require"])].addEdge(curr_node)

    # print(attack_point_dict)
    # sorted_attack_point_dict = [{k: attack_point_dict[k]} for k in sorted(attack_point_dict, key=attack_point_dict.get)]
    # print(sorted_attack_point_dict)

    resolved = []
    seen = []

    def dep_resolve(node, resolved, seen):
        resolved.append(node)
        seen.append(node)
        if node not in seen:
            for edge in node.edges:
                if edge not in seen:
                    dep_resolve(edge, resolved, seen)
                else:
                    continue

    for node in nodes:
        dep_resolve(node, resolved, seen)

    # for node in resolved:
    #     print(node.name)

    current_offense = 0

    for attack in resolved:
        if current_offense < offensive:
            # print(attack.name)
            current_offense += attack_offense_dict[attack.name]
            # print("current offense: ", current_offense)
            final_attack_list.append(attack.name)
        else:
            break

    return final_attack_list


def machine_learning_q1(data):
    input = data["input"]
    output = data["output"]
    question = data["question"]

    from ortools.linear_solver import pywraplp

    # Instantiate a Glop solver, naming it LinearExample.
    solver = pywraplp.Solver('LinearExample',
                             pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    # Create the two variables and let them take on any value.
    x = solver.NumVar(-solver.infinity(), solver.infinity(), 'x')
    y = solver.NumVar(-solver.infinity(), solver.infinity(), 'y')
    z = solver.NumVar(-solver.infinity(), solver.infinity(), 'z')

    for i in range(0, len(data["input"])):
        # Constraint : x + y + z == output.
        constraint = solver.Constraint(output[i], output[i])
        constraint.SetCoefficient(x, input[i][0])
        constraint.SetCoefficient(y, input[i][1])
        constraint.SetCoefficient(z, input[i][2])

    solver.Solve()

    print('Solution:')
    print('x = ', x.solution_value())
    print('y = ', y.solution_value())
    print('z = ', z.solution_value())

    answer = x.solution_value() * question[0] + y.solution_value() * question[1] + z.solution_value() * question[2]

    return {"answer": answer}


def machine_learning_q2():
    import tensorflow as tf
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

def dino_problem(data):
    # print("Types of food", data["number_of_types_of_food"])
    food_size = data["number_of_types_of_food"]

    raphael_list = data["calories_for_each_type_for_raphael"]

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    model.fit(x=x_train, y=y_train, epochs=10)

    model.evaluate(x_test, y_test)
machine_learning_q2()