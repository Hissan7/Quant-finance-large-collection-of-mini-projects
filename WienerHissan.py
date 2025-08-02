import numpy as np
import matplotlib.pyplot as plt


def wiener_process(mu=0, dt=0.5, n=500):
    # generate n random steps from N(mu, sqrt(dt))
    steps = np.random.normal(mu, np.sqrt(dt), n)

    # create a W array with W[0] = 0, and fill the rest with cumulative steps
    W = np.zeros(n + 1)
    W[1:] = np.cumsum(steps)

    # time array from 0 to n*dt
    t = np.linspace(0, n * dt, n + 1)
    return t, W


def plot(n=500, dt=0.5):
    t, W1 = wiener_process(mu=0, dt=dt, n=n)
    _, W2 = wiener_process(mu=1, dt=dt, n=n)  # using drift = 1 

    plt.plot(t, W1, label='No Drift (μ=0)')
    plt.plot(t, W2, label='Drift (μ=1)')
    plt.legend()
    plt.xlabel("Time")
    plt.ylabel("W(t)")
    plt.title("Wiener Process Comparison")
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    plot()
