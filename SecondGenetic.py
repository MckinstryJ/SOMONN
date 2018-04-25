import random
import os
from GANEAT import evolvefeedforwardparallel as effp
from GANEAT import DataManipulation as dM

generations = 5
initial_population = 10
top_percent_of_agents = 4
prob_of_mutation = .02
pop = [100, 150, 200, 250, 300, 350, 400, 450, 500]
hidden = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
act = ['sigmoid', 'tanh', 'sin', 'gauss', 'relu', 'softplus',
       'identity', 'clamped', 'inv', 'log', 'exp', 'abs', 'hat',
       'square', 'cube']


def run(config_file, _inputs, _outputs):
    agents = init_agents(config_file)

    for generation in range(generations):
        print('\nGeneration: {!r}'.format(generation))

        agents = fitness(agents, _inputs, _outputs)
        agents = selection(agents)
        agents = crossover(agents)
        agents = mutation(agents, prob_of_mutation)
        agents = random_init_on_duplicates(config_file, agents)

    top_settings = max_agent(agents)
    print("Best set:\n Population Size: {!r}\n Hidden Layers: {!r}\n Activation: {!r}"
          .format(top_settings[2], top_settings[3], top_settings[4]))


def init_agents(config_file):
    agents = []
    for ID in range(initial_population):
        popu, hid, activate, prevRun = random_init_agents(config_file, ID)

        agents.append([0.0, "config_{!r}".format(ID), popu, hid, activate, prevRun, ID])
    return agents


def random_init_agents(config, ID):
    popu = pop[random.randint(0, len(pop)-1)]
    hid = hidden[random.randint(0, len(hidden)-1)]
    activate = act[random.randint(0, len(act)-1)]
    dM.changeConfig(config,
                    "pop_size              = 200",
                    "pop_size              = " + str(popu),
                    ID)
    dM.changeConfig(os.path.join(local_dir, "config_" + str(ID)),
                    "num_hidden              = 9",
                    "num_hidden              = " + str(hid),
                    ID)

    dM.changeConfig(os.path.join(local_dir, "config_" + str(ID)),
                    "activation_default      = sigmoid",
                    "activation_default      = " + activate,
                    ID)
    dM.changeConfig(os.path.join(local_dir, "config_{!r}".format(ID)),
                    "activation_options      = sigmoid",
                    "activation_options      = " + activate,
                    ID)
    return popu, hid, activate, False


def max_agent(agents):
    agents.sort(key=lambda x: float(x[0]), reverse=True)
    return agents[0]


def fitness(agents, inputs, outputs):
    for agent in agents:
        if not agent[5]:
            agent[0] = effp.run(os.path.join(local_dir, agent[1]), inputs, outputs)
            agent[5] = True
        print("Highest Fitness of ({!r}) for: \n"
              "     Population Size: {!r}\n"
              "     Number of Hidden Layers: {!r}\n"
              "     Activation Type: {!r}".format(agent[0], agent[2], agent[3], agent[4]))

    return agents


def selection(agents):
    agents.sort(key=lambda x: float(x[0]), reverse=True)
    print("Top Fitness Scores: ", end="")
    for agent in agents[:top_percent_of_agents]:
        print(agent[0], end=" ")
    return agents[:top_percent_of_agents]


def crossover(agents):
    for parent_1 in range(0, 3):
        for parent_2 in range(parent_1+1, 4):
            for child in range(0, 3):
                child_agent = [0.0, config_path, None, None, None, newID(agents)]
                for z in range(0, 3):
                    parent = random.randint(parent_1, parent_2)
                    if z == 0:
                        dM.changeConfig(child_agent[1],
                                        dM.get_current(child_agent[1], "pop_size"),
                                        "pop_size              = " + str(agents[parent][2]) + "\n",
                                        child_agent[-1])
                        child_agent[1] = "config_" + str(child_agent[-1])
                        child_agent[2] = agents[parent][2]
                    elif z == 1:
                        dM.changeConfig(child_agent[1],
                                        dM.get_current(child_agent[1], "num_hidden"),
                                        "num_hidden              = " + str(agents[parent][3]) + "\n",
                                        child_agent[-1])
                        child_agent[3] = agents[parent][3]
                    else:
                        dM.changeConfig(child_agent[1],
                                        dM.get_current(child_agent[1], "activation_default"),
                                        "activation_default      = " + agents[parent][4] + "\n",
                                        child_agent[-1])
                        dM.changeConfig(child_agent[1],
                                        dM.get_current(child_agent[1], "activation_options"),
                                        "activation_options = " + agents[parent][4] + "\n",
                                        child_agent[-1])
                        child_agent[4] = agents[parent][4]
                child_agent[5] = False
                agents.append(child_agent)

    return agents


def newID(agents):
    id_numbers = []
    for agent in agents:
        id_numbers.append(agent[-1])
    id_numbers.sort()
    for x in range(len(id_numbers)):
        if x not in id_numbers:
            return x
        else:
            return len(id_numbers)


def mutation(agents, prob):
    if random.random() < prob:
        random_agent = random.randint(0, len(agents)-1)
        random_trait = random.randint(0, 3)
        if random_trait == 0:
            random_element = random.randint(0, len(pop)-1)
            dM.changeConfig(agents[random_agent][1],
                            dM.get_current(agents[random_agent][1], "pop_size"),
                            "pop_size              = " + str(pop[random_element]),
                            agents[random_agent][-1])
            agents[random_agent][2] = pop[random_element]
        elif random_trait == 1:
            random_element = random.randint(0, len(hidden)-1)
            dM.changeConfig(agents[random_agent][1],
                            dM.get_current(agents[random_agent][1], "num_hidden"),
                            "num_hidden              = " + str(hidden[random_element]),
                            agents[random_agent][-1])
            agents[random_agent][3] = hidden[random_element]
        else:
            random_element = random.randint(0, len(act)-1)
            dM.changeConfig(agents[random_agent][1],
                            dM.get_current(agents[random_agent][1], "activation_default"),
                            "activation_default              = " + act[random_element],
                            agents[random_agent][-1])
            dM.changeConfig(agents[random_agent][1],
                            dM.get_current(agents[random_agent][1], "activation_default"),
                            "activation_options = " + act[random_element],
                            agents[random_agent][-1])
            agents[random_agent][4] = act[random_element]
        agents[random_agent][5] = False

    return agents


def random_init_on_duplicates(config, agents):
    index_element = []
    for x in range(len(agents)):
        for y in range(x+1, len(agents)):
            matches = []
            for z in range(2, 5):
                matches.append(agents[x][z] == agents[y][z])
            if matches.count(True) == 3:
                index_element.append(y)
    for x in index_element:
        agents[x][2], agents[x][3], agents[x][4], agents[x][5] = random_init_agents(config, x)

    return agents

'''
    STARTING POINT OF PROGRAM
'''
if __name__ == '__main__':
    dM.fill("GOOGL")
    _inputs = dM.trainingInputData()
    _outputs = dM.trainingOutputData()

    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward')
    run(config_path, _inputs, _outputs)
