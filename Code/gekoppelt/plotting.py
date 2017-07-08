import matplotlib.pyplot as plt


# Plotting
def plot(P, Q, labels="", timerange=[0, 1]):

    fig = plt.figure(1, figsize=(12, 8))
    plt.title("Blutdruck P")
    plt.imshow(P, interpolation='nearest', cmap=plt.cm.jet, aspect='auto')
    plt.ylabel("t [s]", fontsize=14)
    plt.xlabel(labels, fontsize=14)
    plt.savefig("out/plotP.png")

    plt.title("Flussrate Q")
    plt.imshow(Q, interpolation='nearest', cmap=plt.cm.bwr, aspect='auto')
    plt.ylabel("t [s]", fontsize=14)
    plt.xlabel(labels, fontsize=14)
    plt.savefig("out/plotQ.png")
