import random
import numpy as np

def simulate_crossing_bridge(num_monkeys):
    total_steps_array = []

    for _ in range(num_monkeys):
        steps = 0
        while True:
            step = random.randint(1, 201)
            steps += 1
            if step == 201:
                break
        total_steps_array.append(steps)

    return total_steps_array

def calculate_average_steps(total_steps_array):
    return np.mean(total_steps_array)

def main():
    monkeys_list = [100, 500, 1000, 3000, 5000]
    for num_monkeys in monkeys_list:
        total_steps_array = simulate_crossing_bridge(num_monkeys)
        avg_steps = calculate_average_steps(total_steps_array)
        print(f"For {num_monkeys} monkeys, average number of steps: {avg_steps}")

if __name__ == "__main__":
    main()
