import math

"""
Noise
"""


# Photon Noise : Poisson Distribution
def photon_noise_probability(k: int, lambda_: float):  # k: Signal, lambda_: Expectation
    return (lambda_ ** k) * math.exp(-lambda_) / math.factorial(k)


# Read Noise : Gaussian Distribution
def read_noise_probability(k: float, mu: float, sigma: float):  # mu: Mean Signal Value, sigma: Standard Deviation
    first = 1. / (sigma * (2. * math.pi) ** 0.5)
    second = math.exp(-0.5 * (((k - mu) / sigma) ** 2))
    return first * second


# Quantization Noise
def quantization_noise(delta: int):  # delta: Gap between Two Consecutive Discrete Values
    return (delta ** 2) / 12


# Dynamic Range
def dynamic_range_db(b_min: float, b_max: float):  # b_min: The Maximum Possible Photon Energy, b_max: The Minimum Detectable Photon Energy
    return 20 * math.log(b_max / b_min)  # Unit: Decibels (dB)


"""
Sensing Color
"""


# Quantum Efficiency
def quantum_efficiency(p: float, i: float):  # p: Incoming Light (Photon Flux), i: Pixel Intensity (Electron Flux)
    return i / p


# Electron Flux
def electron_flux(q: float, p: float):  # q: Quantum Efficiency (Monochromatic Light)
    return q * p
