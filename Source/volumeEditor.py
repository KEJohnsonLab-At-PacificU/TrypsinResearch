#densityA is the volume of the initial temperature
#densityB is the volume of the second temperature

def editVolume(vectors, densityA, densityB):
    density = (densityB / densityA)
    multiplier = pow(density, 1/3)
    vectors[0] = vectors[0] * multiplier
    vectors[1] = vectors[1] * multiplier
    vectors[2] = vectors[2] * multiplier

    return vectors