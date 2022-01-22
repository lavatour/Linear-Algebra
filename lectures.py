import math
import numpy as np

from matrixMath import MatrixMath
matrix = MatrixMath()

class Lectures():
  def __init__(self):
    pass

  def lecture44(self):
    # generate XY coordinates for a circle
    import matplotlib.pyplot as plt
    angles = []
    XY = []
    for angle in range(0, 360, 3):
        angle = angle * math.pi / 180
        XY.append([math.cos(angle), math.sin(angle)])
    print()
    R = matrix.randomMatrix(2,2, 0, 3, int)
    print(f"R = {R}")
    for pt in XY:
        plt.plot(pt[0], pt[1], 'o')
        V = np.matrix(pt)

        #V = numpy.transpose(V)

        T = matrix.transpose(V)

        z = matrix.matMult(R, T)
        plt.plot(z[0], z[1], 'o')




    plt.axis('square')
    plt.show()




    # plot the new coordinates

    # try various matrices...

    # try with a singular matrix


  def liveEvil(self, A, B):
      res1 = np.transpose(A @ B)
      res2 = MatrixMath.transpose(self, B) @ MatrixMath.transpose(self, A)
      print(res1)
      print(res2)
      print(res1 - res2)

  def lect52(self):
    """Geometrtic trnasformation via matrix multiplication."""
    points = []
    for angle in range(0, 360, 1):
      theta = angle / 180 * math.pi
      x = math.cos(theta)
      y = math.sin(theta)
      points.append([x, y])
    matrix.singularMatrix(2, 1, 10)
    
  def lecture54(self, A):
    S = matrix.symmetrizeMatrix(A)