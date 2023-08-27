#faça um programa que leia um angulo e mostre o seno, cosseno e tangente desse angulo
import math

# Lê o ângulo em graus
angulo = float(input("Digite o ângulo em graus: "))

# Converte o ângulo para radianos
angulo_radianos = math.radians(angulo)

# Calcula e exibe o seno, cosseno e tangente
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print(f"Seno do ângulo: {seno:.4f}")
print(f"Cosseno do ângulo: {cosseno:.4f}")
print(f"Tangente do ângulo: {tangente:.4f}")
