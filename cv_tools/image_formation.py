"""
Pinhole and Perspective Projection
"""


# Perspective Imaging with Pinhole
def pinhole_image_xy(xo: flaot, yo: float, zo: float, f: float):  # f : Effective Focal Length
    return f * xo / zo, f * yo / zo


# Image Magnification
def pinhole_magnification(zo: float, f: float) -> float:
    return f / zo


# Vanishing Point
def pinhole_vanishing_point(lx: float, ly: float, lz: float, f: float):
    return f * lx / lz, f * ly / lz


# Ideal Pinhole Diameter
def pinhole_ideal_diameter(f: float, wavelength: float) -> float:
    return 2. * (f * wavelength) ** 0.5


"""
Lenses
"""


# Gaussian Lens Law
def lens_image_i(o: float, f: float) -> float:  # i: image distance, o: object distance, f: focal length
    return f * o / (o - f)


# Image Magnification
def lens_magnification(i: float, o: float) -> float:
    return i / o


# Two Lens System
def two_lens_magnification(i1: float, o1: float, i2: float, o2: float) -> float:
    return i1 * i2 / (o1 * o2)


# f-number of Lens
def lens_aperture(f: float, n: float) -> float:  # n: f-number
    return f / n


def lens_f_number(f: float, d: float) -> float:  # d: aperture
    return f / d


# Lens Defocus
def lens_blur_circle_diameter(o: float, o_prime: float, f: float, n: float) -> float:
    return (f ** 2 / n) * abs((o - o_prime) / (o_prime * (o - f)))


# Depth of Field
def lens_dof(o: float, f: float, n: float, c: float) -> float:  # c: pixel size
    numerator = 2. * o * (f ** 2) * c * n * (o - f)
    denominator = (f ** 4) - ((c ** 2) * (n ** 2) * ((o - f) ** 2))
    return numerator / denominator


# Hyperfocal Distance (the closest distance o)
def lens_hyperfocal_distance(f: float, n: float, c: float):
    return ((f**2) / (n * c)) + f
