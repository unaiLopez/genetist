import sys
sys.path.append('../')
from genetist.environment import Environment #pip install genetist
from genetist.parameters import Parameters

#defining a 4 variable search space of float values from -100.0 to 100.0
params = {
    'x': Parameters.suggest_float(-100, 100),
    'y': Parameters.suggest_float(-100, 100),
    'z': Parameters.suggest_float(-100, 100),
    'k': Parameters.suggest_float(-100, 100)
}

#defining an objective function
def objective(individual):
    x = individual['x']
    y = individual['y']
    z = individual['z']
    k = individual['k']

    return ((x**2 - 4*y**3 / z**4) * k**3), (k**3 / x)

if __name__ == '__main__':
    #defining our Environment instance with a population of 100 individuals,
    #one-point crossover and a single gene mutation with a 25% probability of mutation
    environment = Environment(
        params=params,
        num_population=100,
        crossover_type='one-point',
        mutation_type='single-gene',
        prob_mutation=0.25,
        verbose=1,
        random_state=42
    )
    #minimizing the first value and maximazing the second value of the objective function
    #and adding 1 stop criterias (timeout)
    results = environment.optimize(
        objective=objective,
        direction=['minimize', 'maximize'],
        weights=[0.5, 0.5],
        timeout=3,
        score_names=['complex_equation_score', 'simple_equation_score'])

    print()
    print(f'EXECUTION TIME={results.execution_time}')
    print(f'BEST SCORE={results.best_score}')
    print(f'BEST INDIVIDUAL={results.best_individual}')
    print('BEST PER GENERATION:')
    print(results.best_per_generation_dataframe)