import numpy as np
import matplotlib.pyplot as plt

def flux_surface(A, kappa, delta, R0):
    """Claculate flux surface

    Arguments
    ---------
    A:
        Aspect ratio
    kappa:
        Elongation
    delta:
        Triangularity
    R0:
        Major radius
    """
    
    theta = np.linspace(0, 2 * np.pi)
    r = R0 / A
    R_s = R0 + r * np.cos(theta + (np.arcsin(delta) * np.sin(theta)))
    Z_s = kappa * r * np.sin(theta)
    
    return R_s, Z_s

def plot_surface(R_s, Z_s, ax):
    """Plot flux surface

    Arguments
    ---------
    R_s:
        Major radius coordinates
    Z_s:
        Vertical coordinates
    ax:
        Plot axis
    """
    
    if ax is not None:
        ax.plot(R_s, Z_s)
    else:
        fig, ax = plt.subplots()
        ax.plot(R_s, Z_s)
        ax.axis("equal")
    
    plt.xlabel("R [m]")
    plt.ylabel("Z [m]")     
    plt.savefig("./miller.png")
    
    return ax

def main():
    
    A = 2.2
    kappa = 1.5
    delta = 0.3
    R0 = 2.5
    
    ax = None 
    
    R_s, Z_s = flux_surface(A, kappa, delta, R0)
    ax = plot_surface(R_s, Z_s, ax)
    
if __name__ == "__main__":
    main()