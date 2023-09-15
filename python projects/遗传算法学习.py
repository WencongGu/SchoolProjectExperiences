import random
import numpy as np
import matplotlib.pyplot as plt

# TSP问题的数据
city_locations = np.array([(60, 200), (180, 200), (80, 180), (140, 180), (20, 160),
                           (100, 160), (200, 160), (140, 140), (40, 120), (100, 120),
                           (180, 100), (60, 80), (120, 80), (180, 60), (20, 40),
                           (100, 40), (200, 40), (20, 20), (60, 20), (160, 20)], dtype=int)

num_cities = len(city_locations)  # 城市数量
num_generations = 2000  # 迭代次数
population_size = 100  # 种群大小
mutation_rate = 0.02  # 变异率
elite_size = 20  # 精英个体数量

# 计算城市之间的距离矩阵
dist_matrix = np.zeros((num_cities, num_cities), dtype=int)
for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i][j] = np.linalg.norm(city_locations[i] - city_locations[j])

# 随机生成初始种群
def create_population(size):
    population = []
    for i in range(size):
        chromosome = np.random.permutation(num_cities)
        population.append(chromosome)
    return population

# 计算染色体的适应度（即总路程）
def calculate_fitness(chromosome):
    fitness = 0
    for i in range(num_cities):
        j = (i + 1) % num_cities
        fitness += dist_matrix[chromosome[i]][chromosome[j]]
    return fitness

# 选择精英个体
def select_elites(population, elite_size):
    elites = []
    sorted_population = sorted(population, key=lambda x: calculate_fitness(x))
    for i in range(elite_size):
        elites.append(sorted_population[i])
    return elites

# 选择遗传算法的父代
def select_parents(population):
    fitnesses = [calculate_fitness(chromosome) for chromosome in population]
    sum_fitness = sum(fitnesses)
    probabilities = [fitness / sum_fitness for fitness in fitnesses]
    parents = np.random.choice(population, size=2, p=probabilities, replace=False)
    return parents

# 进行交叉操作
def crossover(parents):
    offspring = [-1] * num_cities
    start_index = random.randint(0, num_cities - 1)
    end_index = random.randint(0, num_cities - 1)
    if start_index > end_index:
        start_index, end_index = end_index, start_index
    for i in range(start_index, end_index + 1):
        offspring[i] = parents[0][i]
    j = 0
    for i in range(num_cities):
        if offspring[i] == -1:
            while parents[1][j] in offspring:
                j += 1
            offspring[i] = parents[1][j]
    return offspring

# 进行变异操作

def mutate(chromosome):
    for i in range(num_cities):
        if random.random() < mutation_rate:
            j = random.randint(0, num_cities - 1)
            chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome

#绘制路径图
def plot_path(city_locations, path):
    x = [city_locations[path[i]][0] for i in range(num_cities)]
    y = [city_locations[path[i]][1] for i in range(num_cities)]
    x.append(x[0])
    y.append(y[0])
    plt.plot(x, y, 'o-')
    plt.show()

#使用遗传算法求解TSP问题

def solve_tsp(city_locations, num_generations, population_size, mutation_rate, elite_size):
    population = create_population(population_size)
    best_fitness = float('inf')
    best_path = []
    for i in range(num_generations):
        elites = select_elites(population, elite_size)
        new_population = elites
    while len(new_population) < population_size:
            parents = select_parents(population)
            offspring = crossover(parents)
            offspring = mutate(offspring)
            new_population.append(offspring)
            population = new_population
            current_fitness = calculate_fitness(elites[0])
            if current_fitness < best_fitness:
                best_fitness = current_fitness
                best_path = elites[0]
                if i % 100 == 0:
                    print(f'Generation {i}: best fitness = {best_fitness}')
                    print(f'Total distance: {best_fitness}')
                    print(f'Path: {best_path}')
                    plot_path(city_locations, best_path)



#求解并输出
solve_tsp(city_locations, num_generations, population_size, mutation_rate, elite_size)


#这段代码使用遗传算法求解了一个包含20个城市的TSP问题，并输出了总路程、路径和路径图。
# 你可以修改`city_locations`、`num_cities`、`num_generations`、`population_size`、`mutation_rate`和`elite_size`来尝试解决其他TSP问题。

#当然，还有一些可以改进的地方。例如，我们可以尝试使用更复杂的选择算法，如锦标赛选择或轮盘赌选择，来更好地保留种群中的优秀个体。
# 我们还可以尝试使用更复杂的交叉算子或改进变异算子，以产生更多的多样性和更好的解。
# 此外，我们还可以使用并行计算来加速算法的收敛速度，特别是在处理更大规模的问题时。




#我还想输出交叉概率，变异概率，迭代次数，而且每次迭代都输出群体规模和种群规模，怎么修改代码？
#你可以将函数solve_tsp的定义修改为如下形式：
# def solve_tsp(city_locations, num_generations, population_size, mutation_rate, elite_size, crossover_rate):
#     population = create_population(population_size)
#     best_fitness = float('inf')
#     best_path = []
#     for i in range(num_generations):
#         elites = select_elites(population, elite_size)
#         new_population = elites
#         while len(new_population) < population_size:
#             parents = select_parents(population)
#             offspring = crossover(parents, crossover_rate)
#             offspring = mutate(offspring, mutation_rate)
#             new_population.append(offspring)
#         population = new_population
#         current_fitness = calculate_fitness(elites[0])
#         if current_fitness < best_fitness:
#             best_fitness = current_fitness
#             best_path = elites[0]
#         if i % 100 == 0:
#             print(f'Generation {i}: best fitness = {best_fitness}, population size = {len(population)}, mutation rate = {mutation_rate}, crossover rate = {crossover_rate}')
#     print(f'Total distance: {best_fitness}')
#     print(f'Path: {best_path}')
#     plot_path(city_locations, best_path)
# #你可以看到，我们将函数的定义修改为接收额外的两个参数mutation_rate和crossover_rate，并在每次迭代时输出相关信息。现在你可以调用该函数并传递你想要的参数。例如，要运行200代，种群大小为100，交叉概率为0.8，变异概率为0.02，精英个体数为5，请使用以下代码：
# num_generations = 200
# population_size = 100
# crossover_rate = 0.8
# mutation_rate = 0.02
# elite_size = 5
#
# solve_tsp(city_locations, num_generations, population_size, mutation_rate, elite_size, crossover_rate)



#请注意，这里我们增加了crossover_rate参数，并将其传递到crossover函数中。同时，我们将mutation_rate作为参数传递到mutate函数中，以覆盖先前默认的变异概率。


