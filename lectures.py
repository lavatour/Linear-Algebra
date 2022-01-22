import math
import numpy as np

from matrixMath import MatrixMath
matrix = MatrixMath()

class Lectures():
  def __init__(self):
    pass

  def lecture52(self):
    # generate XY coordinates for a circle
    import matplotlib.pyplot as plt
    angles = []
    XY = []
    for angle in range(0, 360, 3):
        angle = angle * math.pi / 180
        XY.append([math.cos(angle), math.sin(angle)])
    print()
    R = matrix.randomMatrix(2,2, -5, 5, int)
    print(R)
    R = matrix.symetrizeMatrix(R)
    R = matrix.singularizeAMatrix(R)
    print(f"R = {R}")
    for pt in XY:
        plt.plot(pt[0], pt[1], 'o')
        V = np.matrix(pt)

        T = matrix.transpose(V)

        z = matrix.matMult(R, T)
        plt.plot(z[0], z[1], 'o')

    plt.axis('square')
    plt.show()

  def liveEvil(self, A, B):
      res1 = np.transpose(A @ B)
      res2 = MatrixMath.transpose(self, B) @ MatrixMath.transpose(self, A)
      print(res1)
      print(res2)
      print(res1 - res2)

  
    
  def lecture54(self, A):
    S = matrix.symetrizeMatrix(A)