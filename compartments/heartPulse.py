from numpy import exp


pulseDuration = 0.65   # length of the pulse
pulseInterval = 1.0   # one pulse every second
steepness = 12.0


# simulates a hearts pulse (change in volume), t in seconds
def pulse(t, vMax=120, vMin=80):
    t = t % pulseInterval
    if t < pulseDuration / 2.0:
        return vMax + (vMax - vMin) * (exp(-t * steepness / pulseDuration) - 1)
    elif t < pulseDuration:
        return vMax - (vMax - vMin) * exp(-(t - (pulseDuration / 2)) * steepness / pulseDuration)
    else:
        return vMax


def dPulse_dt(t, vMax=120, vMin=80):
    t = t % pulseInterval
    if t < pulseDuration / 2.0:
        return -1 * (steepness / pulseDuration) * (vMax - vMin) * exp(-t * steepness / pulseDuration)
    elif t < pulseDuration:
        return (steepness / pulseDuration) * (vMax - vMin) * exp(-(t - (pulseDuration / 2)) * steepness / pulseDuration)
    else:
        return 0


# if not imported but executed itself: plot the pulse
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np
    t0 = -0.2
    t = np.linspace(t0, t0 + pulseInterval, 500)
    vals = [pulse(tStep) for tStep in t]
    plt.plot(t, vals)
    plt.xlabel("t [s]")
    plt.ylabel("Herzvolumen V []")
    plt.margins(0, 0.1)
    plt.savefig("heartPulse.png")
    plt.show()
