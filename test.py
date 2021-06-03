import cvxpy as cp
a = cp.Variable ()
b = cp.Variable ()
c = cp.transforms.indicator([a+b == 5])
o = cp.Minimize (0)
p = cp.Problem(o, [c <= 0])
# p.solve (verbose=True, solver=cp.ECOS)
data = p.get_problem_data(cp.ECOS)
print(data)
print(data[0]["A"])