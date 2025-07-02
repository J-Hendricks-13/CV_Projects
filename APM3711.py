import numpy as np

def f(x, y):
    return -3 * x**2 * y**2

def analytical_solution(x):
    return 2 / (2 * x**3 + 1)

def modified_euler(x0, y0, x_end, h, num_corrections=2):
    x_values = [x0]
    y_values = [y0]
    errors = [0]  # Error at the initial point is 0

    x = x0
    y = y0

    while x < x_end:
        h = min(h, x_end - x)  # Adjust step size for the last interval
        x_next = x + h

        # Predictor step (Euler)
        y_predict = y + h * f(x, y)

        # Corrector steps
        y_correct = y_predict
        for _ in range(num_corrections):
            y_correct = y + (h / 2) * (f(x, y) + f(x_next, y_correct))

        y_next = y_correct
        y_analytical = analytical_solution(x_next)
        error = abs(y_analytical - y_next)

        x_values.append(x_next)
        y_values.append(y_next)
        errors.append(error)

        x = x_next
        y = y_next

    return np.array(x_values), np.array(y_values), np.array(errors)

# Solve with h = 0.2
x0_1 = 0
y0_1 = 2
x_end = 1
h1 = 0.2
x_values_1, y_values_1, errors_1 = modified_euler(x0_1, y0_1, x_end, h1)

print("Results for h = 0.2:")
print("--------------------")
print("x\t\ty_approx\t\ty_analytical\t\tError")
for i in range(len(x_values_1)):
    analytical_val = analytical_solution(x_values_1[i])
    print(f"{x_values_1[i]:.4f}\t\t{y_values_1[i]:.8f}\t\t{analytical_val:.8f}\t\t{errors_1[i]:.8f}")

print("\n")

# Solve with h = 0.1
x0_2 = 0
y0_2 = 2
h2 = 0.1
x_values_2, y_values_2, errors_2 = modified_euler(x0_2, y0_2, x_end, h2)

print("Results for h = 0.1:")
print("--------------------")
print("x\t\ty_approx\t\ty_analytical\t\tError")
for i in range(len(x_values_2)):
    analytical_val = analytical_solution(x_values_2[i])
    print(f"{x_values_2[i]:.4f}\t\t{y_values_2[i]:.8f}\t\t{analytical_val:.8f}\t\t{errors_2[i]:.8f}")