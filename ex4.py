def get_min_cost(jobs, hire, fire, salary, free):
    #Preprocessing
    num_jobs = len(jobs)
    dict = {}
    for j in range(0, num_jobs):
        dict.setdefault(jobs[j], 0)
        dict[jobs[j]] += free[j]

    jobs = list(dict.keys())
    free = list(dict.values())
    num_jobs = len(jobs)

    #Algorithm
    store = []
    for i in range(0, num_jobs):
        store.append([0, 0])

    hire_salary = hire + salary
    hire_salary_fired = hire + salary + fire

    store[0][0] = min(free[0], hire_salary_fired)
    store[0][1] = hire_salary

    for i in range(1, num_jobs):
        store[i][0] = min(store[i-1][0] + free[i], store[i-1][0] + hire_salary_fired, store[i-1][1] + fire + salary*(jobs[i] - jobs[i-1]))
        store[i][1] = min(store[i-1][0] + hire_salary, store[i-1][1] + salary*(jobs[i] - jobs[i-1]))

    return min(store[i][0], store[i][1])

hire_cost = 2
fire_cost = 3
salary = 2
jobs = [1, 1, 2, 5]
free_cost = [3, 2, 6, 1]

opt = get_min_cost(jobs, hire_cost, fire_cost, salary, free_cost)
print("Optimum:")
print(opt)
