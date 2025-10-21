import numpy as np 
import matplotlib.pyplot as plt 
import math 
 
def binomial_pmf(k, n, p): 
    if k < 0 or k > n: 
        return 0 
    combination = math.factorial(n) / (math.factorial(k) * math.factorial(n - k)) 
    return combination * (p**k) * ((1-p)**(n-k)) 
 
def normal_pdf(x, mu, sigma): 
    coefficient = 1 / (sigma * math.sqrt(2 * math.pi)) 
    exponent = -0.5 * ((x - mu) / sigma)**2 
    return coefficient * math.exp(exponent) 
 
def poisson_pmf(k, lam): 
    if k < 0: 
        return 0 
    return (lam**k * math.exp(-lam)) / math.factorial(k) 
 
def uniform_pdf(x, a, b): 
    if a <= x <= b: 
        return 1 / (b - a) 
    else: 
        return 0 
 
def plot_binomial(n=10, p=0.5): 
    x = np.arange(0, n + 1) 
    y = [binomial_pmf(val, n, p) for val in x] 
    plt.bar(x, y, color='skyblue', edgecolor='black') 
    plt.title(f'Binomial Distribution (n={n}, p={p})') 
    plt.xlabel('Number of Successes') 
    plt.ylabel('Probability') 
    plt.grid(True) 
    plt.show() 
 
def plot_normal(mu=0, sigma=1): 
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000) 
    y = [normal_pdf(val, mu, sigma) for val in x] 
    plt.plot(x, y, color='green') 
    plt.title(f'Normal Distribution (μ={mu}, σ={sigma})') 
    plt.xlabel('x') 
    plt.ylabel('Probability Density') 
    plt.grid(True) 
    plt.show() 
 
def plot_poisson(lam=5): 
    x = np.arange(0, 20) 
    y = [poisson_pmf(val, lam) for val in x] 
    plt.bar(x, y, color='salmon', edgecolor='black') 
    plt.title(f'Poisson Distribution (λ={lam})') 
    plt.xlabel('Number of Events') 
    plt.ylabel('Probability') 
    plt.grid(True) 
    plt.show() 
 
def plot_uniform(a=0, b=1): 
    x = np.linspace(a - 1, b + 1, 1000) 
    y = [uniform_pdf(val, a, b) for val in x] 
    plt.plot(x, y, color='purple') 
    plt.title(f'Uniform Distribution (a={a}, b={b})') 
    plt.xlabel('x') 
    plt.ylabel('Probability Density') 
    plt.grid(True) 
    plt.show() 
 
def main(): 
    print("Choose a distribution to plot:") 
    print("1. Binomial") 
    print("2. Normal") 
    print("3. Poisson") 
    print("4. Uniform") 
     
    choice = input("Enter choice (1-4): ") 
     
    if choice == '1': 
        n = int(input("Enter number of trials (n): ")) 
        p = float(input("Enter probability of success (p): ")) 
        plot_binomial(n, p) 
    elif choice == '2': 
        mu = float(input("Enter mean (μ): ")) 
        sigma = float(input("Enter standard deviation (σ): ")) 
        plot_normal(mu, sigma) 
    elif choice == '3': 
        lam = float(input("Enter rate parameter (λ): ")) 
        plot_poisson(lam) 
    elif choice == '4': 
        a = float(input("Enter lower bound (a): ")) 
        b = float(input("Enter upper bound (b): ")) 
        plot_uniform(a, b) 
    else: 
        print("Invalid choice!") 
 
import numpy as np 
import matplotlib.pyplot as plt 
import math 
 
def binomial_pmf(k, n, p): 
    if k < 0 or k > n: 
        return 0 
    combination = math.factorial(n) / (math.factorial(k) * math.factorial(n - k)) 
    return combination * (p**k) * ((1-p)**(n-k)) 
 
def normal_pdf(x, mu, sigma): 
    coefficient = 1 / (sigma * math.sqrt(2 * math.pi)) 
    exponent = -0.5 * ((x - mu) / sigma)**2 
    return coefficient * math.exp(exponent) 
 
def poisson_pmf(k, lam): 
    if k < 0: 
        return 0 
    return (lam**k * math.exp(-lam)) / math.factorial(k) 
 
def uniform_pdf(x, a, b): 
    if a <= x <= b: 
        return 1 / (b - a) 
    else: 
        return 0 
 
def plot_binomial(n=10, p=0.5): 
    x = np.arange(0, n + 1) 
    y = [binomial_pmf(val, n, p) for val in x] 
    plt.bar(x, y, color='skyblue', edgecolor='black') 
    plt.title(f'Binomial Distribution (n={n}, p={p})') 
    plt.xlabel('Number of Successes') 
    plt.ylabel('Probability') 
    plt.grid(True) 
    plt.show() 
 
def plot_normal(mu=0, sigma=1): 
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000) 
    y = [normal_pdf(val, mu, sigma) for val in x] 
    plt.plot(x, y, color='green') 
    plt.title(f'Normal Distribution (μ={mu}, σ={sigma})') 
    plt.xlabel('x') 
    plt.ylabel('Probability Density') 
    plt.grid(True) 
    plt.show() 
 
def plot_poisson(lam=5): 
    x = np.arange(0, 20) 
    y = [poisson_pmf(val, lam) for val in x] 
    plt.bar(x, y, color='salmon', edgecolor='black') 
    plt.title(f'Poisson Distribution (λ={lam})') 
    plt.xlabel('Number of Events') 
    plt.ylabel('Probability') 
    plt.grid(True) 
    plt.show() 
 
def plot_uniform(a=0, b=1): 
    x = np.linspace(a - 1, b + 1, 1000) 
    y = [uniform_pdf(val, a, b) for val in x] 
    plt.plot(x, y, color='purple') 
    plt.title(f'Uniform Distribution (a={a}, b={b})') 
    plt.xlabel('x') 
    plt.ylabel('Probability Density') 
    plt.grid(True) 
    plt.show() 
 
def main(): 
    print("Choose a distribution to plot:") 
    print("1. Binomial") 
    print("2. Normal") 
    print("3. Poisson") 
    print("4. Uniform") 
     
    choice = input("Enter choice (1-4): ") 
     
    if choice == '1': 
        n = int(input("Enter number of trials (n): ")) 
        p = float(input("Enter probability of success (p): ")) 
        plot_binomial(n, p) 
    elif choice == '2': 
        mu = float(input("Enter mean (μ): ")) 
        sigma = float(input("Enter standard deviation (σ): ")) 
        plot_normal(mu, sigma) 
    elif choice == '3': 
        lam = float(input("Enter rate parameter (λ): ")) 
        plot_poisson(lam) 
    elif choice == '4': 
        a = float(input("Enter lower bound (a): ")) 
        b = float(input("Enter upper bound (b): ")) 
        plot_uniform(a, b) 
    else: 
        print("Invalid choice!") 
 
if __name__ == "__main__": 
    main() 
 
 
 
 
 
 
 
 
 
