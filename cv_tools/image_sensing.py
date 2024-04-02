import math

"""
Noise
"""


# Photon Noise : Poisson Distribution
def photon_noise_probability(k: int, lambda_: float) -> float:
    """
    Approximately Gaussian for lambda_ over 10

    :param k: Signal
    :param lambda_: Expectation
    :return: Probability of Photon Noise (0 ~ 1)
    """
    return (lambda_ ** k) * math.exp(-lambda_) / math.factorial(k)


# Read Noise : Gaussian Distribution
def read_noise_probability(k: float, mu: float, sigma: float) -> float:  # mu: Mean Signal Value, sigma: Standard Deviation
    first = 1. / (sigma * (2. * math.pi) ** 0.5)
    second = math.exp(-0.5 * (((k - mu) / sigma) ** 2))
    return first * second


# Quantization Noise
def quantization_noise(delta: int) -> float:  # delta: Gap between Two Consecutive Discrete Values
    return (delta ** 2) / 12


# Dynamic Range
def dynamic_range_db(b_min: float, b_max: float) -> float:
    """
    :param b_min: The Maximum Possible Photon Energy
    :param b_max: The Minimum Detectable Photon Energy
    :return: Dynamic Range (dB)
    """
    return 20 * math.log10(b_max / b_min)  # Unit: Decibels (dB)


"""
Sensing Color
"""


# Quantum Efficiency
def quantum_efficiency(p: float, i: float) -> float:  # p: Incoming Light (Photon Flux), i: Pixel Intensity (Electron Flux)
    return i / p


# Electron Flux
def electron_flux(q: float, p: float) -> float:  # q: Quantum Efficiency (Monochromatic Light)
    return q * p


"""
Camera Response and High Dynamic Range Imaging
"""


# Exposure
def exposure(d: float, t: float) -> float:  # d: Aperture Diameter, t: Integration Time
    aperture_area = (math.pi * d ** 2) / 4
    return aperture_area * t


# Camera Response Function
def image_brightness(i: float, d: float, t: float) -> float:
    return i * exposure(d, t)

