import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mt
import scipy.special as ss


def beta(a, b, x):
    gammaConst = np.exp(ss.gammaln(a+b) - (ss.gammaln(a) + ss.gammaln(b)))
    # return (ss.gamma(a+b)/(ss.gamma(a)*ss.gamma(b))) * (x**(a-1)) * ((1-x)**(b-1))
    return gammaConst * (x**(a-1)) * ((1-x)**(b-1))


def plot(a, b, fig_no):
    plt.figure(1)
    ax = plt.gca()
    ax.set_ylim(0, 20)
    ax.xaxis.set_major_locator(mt.FixedLocator([i*0.1 for i in range(11)]))
    x = np.linspace(0, 1, 5000)
    y = np.zeros(x.size)
    for i in range(x.size):
        y[i] = beta(a, b, x[i])
    ax.plot(x, y, linewidth=0, marker='.', markersize=4)
    plt.savefig("Q1A_images/Fig {}.png".format(fig_no))
    plt.close(1)


def main():
    # Creating the dataset
    n = np.random.random([150, 1])
    n = n >= 0.5
    dataset = n.astype(int)

    # Method A: Sequential Learning
    a = 4
    b = 6
    fig_no = 0
    plot(a, b, fig_no)  # Plotting the prior mean distribution
    for x in np.nditer(dataset):
        if x == 1:
            a = a + 1
        else:
            b = b + 1
        fig_no = fig_no + 1
        plot(a, b, fig_no)  # Plotting the posterior mean distribution
        print('Plotted Fig ' + str(fig_no) +
              ' with a = ' + str(a) + ' b = ' + str(b))

    # Method B: At Once Learning
    a = 4
    b = 6
    m = 0
    for x in np.nditer(dataset):
        if x == 1:
            m = m + 1
    l = dataset.size - m
    plot(m+a, l+b, 'Q1B_1000')
    print('Plotted Fig B' + ' with a = ' + str(m+a) + ' b = ' + str(l+b))


if __name__ == '__main__':
    main()
