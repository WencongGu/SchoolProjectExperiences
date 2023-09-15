import random
import math
import matplotlib.pyplot as plt

CITY_NUM = 30  # 城市数目
GENERATIONS = 100  # 迭代次数
POPULATION_SIZE = 1000  # 种群规模
MUTATION_PROBABILITY = 0.4  # 变异概率
CROSS_PROBABILITY = 0.6  # 交叉概率
FITNESS_RATE_LIMIT = 10.0  # 适应度上限，达到此上限即停止迭代
x=[45, 82, 91, 83, 71, 62, 58, 44, 54, 54, 58, 64, 68, 83, 87,
   74, 71, 37, 41, 2, 7, 25, 22, 18, 4, 13, 18, 24, 25, 41]
y=[7, 38, 46, 44, 32, 35, 35, 62, 67, 69, 60, 58, 69, 76, 78,
   71, 84, 94, 99, 64, 62, 60, 54, 50, 40, 40, 42, 38, 26, 21]

CITY_LIST=[(x[i],y[i]) for i in range(CITY_NUM)]

class TSP(object):
    def __init__(self, city_list, population_size, mutation_probability):
        """
        初始化函数
        :param city_list: 城市坐标列表
        :param population_size: 种群规模
        :param mutation_probability: 变异概率
        """
        self.city_list = city_list
        self.population_size = population_size
        self.mutation_probability = mutation_probability
        self.population = []
        self.fitness = []
        for i in range(self.population_size):
            individual = list(range(CITY_NUM))
            random.shuffle(individual)
            self.population.append(individual)
            self.fitness.append(self.calculate_fitness(individual))

    def calculate_distance(self, city1, city2):
        """
        计算两个城市之间的距离
        :param city1: 城市1的坐标，格式为 (x1, y1)
        :param city2: 城市2的坐标，格式为 (x2, y2)
        :return: 两个城市之间的距离
        """
        x1, y1 = city1
        x2, y2 = city2
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def calculate_fitness(self, individual):
        """
        计算某个个体的适应度
        :param individual: 个体的染色体，格式为一个长度为 CITY_NUM 的列表，列表内元素为 0 到 CITY_NUM-1
        :return: 个体的适应度
        """
        distance = 0.0
        for i in range(CITY_NUM - 1):
            distance += self.calculate_distance(self.city_list[individual[i]], self.city_list[individual[i + 1]])
        distance += self.calculate_distance(self.city_list[individual[CITY_NUM - 1]], self.city_list[individual[0]])
        return 1 / distance

    def crossover(self, parent1, parent2):
        """
        为两个父代个体产生一个后代个体
        :param parent1: 父代1，格式为一个长度为 CITY_NUM 的列表，列表内元素为 0 到 CITY_NUM-1
        :param parent2: 父代2，格式为一个长度为 CITY_NUM 的列表，列表内元素为 0 到 CITY_NUM-1
        :return: 后代个体，格式为一个长度为 CITY_NUM 的列表，列表内元素为 0 到 CITY_NUM-1
        """
        point1 = random.randint(0, CITY_NUM - 1)
        point2 = random.randint(point1, CITY_NUM - 1)
        child = [-1] * CITY_NUM
        for i in range(point1, point2 + 1):
            child[i] = parent1[i]
        idx = 0
        for i in range(CITY_NUM):
            if idx == point1:
                idx = point2 + 1
            if parent2[i] not in child:
                child[idx] = parent2[i]
                idx += 1
                if idx == point1:
                    idx = point2 + 1
        return child

    def mutate(self, individual):
        """
        对一个个体进行变异
        :param individual: 个体的染色体，格式为一个长度为 CITY_NUM 的列表，列表内元素为 0 到 CITY_NUM-1
        :return: 变异后的个体的染色体，格式为一个长度为 CITY_NUM 的列表，列表内元素为 0 到 CITY_NUM-1
        """
        mutate_point1 = random.randint(0, CITY_NUM - 1)
        mutate_point2 = random.randint(0, CITY_NUM - 1)
        individual[mutate_point1], individual[mutate_point2] = individual[mutate_point2], individual[mutate_point1]
        return individual

    def select(self):
        """
        根据适应度选择下一代种群
        :return: 下一代种群
        """
        new_population = []
        fitness_sum = sum(self.fitness)  # 计算适应度总和
        for i in range(self.population_size):
            # 轮盘赌选择
            rand = random.uniform(0, fitness_sum)
            index = 0
            for j in range(self.population_size):
                index = j
                rand -= self.fitness[j]
                if rand <= 0:
                    break
            new_individual = self.population[index]
            if random.random() < CROSS_PROBABILITY:
                parent1 = new_individual
                parent2 = self.population[random.randint(0, self.population_size - 1)]
            else:
                parent2 = new_individual
                parent1 = self.population[random.randint(0, self.population_size - 1)]
            child = self.crossover(parent1, parent2)
            if random.random() < self.mutation_probability:
                child = self.mutate(child)
            new_population.append(child)
        return new_population

    def find_best_individual(self):
        """
        找到适应度最好的个体
        :return: 最好的适应度值和个体
        """
        best_individual = self.population[0]
        best_fitness = self.fitness[0]
        for i in range(1, self.population_size):
            if self.fitness[i] > best_fitness:
                best_individual = self.population[i]
                best_fitness = self.fitness[i]
        return best_fitness, best_individual

    def evolve(self):
        generation = 0
        best_fitness, _ = self.find_best_individual()
        while generation < GENERATIONS and best_fitness < FITNESS_RATE_LIMIT:
            self.population = self.select()
            self.fitness = []
            for individual in self.population:
                fitness = self.calculate_fitness(individual)
                self.fitness.append(fitness)
            best_fitness, best_individual = self.find_best_individual()
            print("Generation {0}: population size = {1}, fitness = {2}".format(
                generation, len(self.population), best_fitness))
            generation += 1
        return best_fitness, best_individual

CITY_LISTs=[(x[i],y[i]) for i in range(CITY_NUM)]
tsp = TSP(CITY_LIST, POPULATION_SIZE, MUTATION_PROBABILITY)
best_fitness, best_individual = tsp.evolve()
print("Total distance of the best route: {0}".format(1 / best_fitness))
print("Best route: ", end="")
for i in best_individual:
    print(i, end=" ")
print("\n")

plt.figure(figsize=(10, 10))
plt.scatter([city[0] for city in CITY_LISTs], [city[1] for city in CITY_LISTs], s=100)
for i in range(CITY_NUM - 1):
    plt.plot([CITY_LISTs[i][0], CITY_LISTs[i+1][0]],
                 [CITY_LISTs[i][1], CITY_LISTs[i+1][1]], c='r')
plt.plot([CITY_LISTs[CITY_NUM-1][0], CITY_LISTs[0][0]],
             [CITY_LISTs[CITY_NUM-1][1], CITY_LISTs[0][1]], c='g')
plt.show()
