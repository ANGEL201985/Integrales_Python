import sympy as sp

# Definir la variable
x = sp.symbols('x')

# Definir la función a integrar
funcion_1 = x * sp.exp(x**2)
funcion_2 = x / sp.sqrt(x**2 + 4)

# Resolver la integral
integral_1 = sp.integrate(funcion_1, x)
integral_2 = sp.integrate(funcion_2, x)

# Mostrar el resultado
print("La integral es:", integral_1)
print("La integral es:", integral_2)
