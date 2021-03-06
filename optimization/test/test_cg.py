import numpy
import unittest
import sys

PyRLA_dir = '../../'
sys.path.append(PyRLA_dir)

from optimization import cg


class TestCG(unittest.TestCase):
    def test_converge1(self):
        w_solved_vec, is_converged_bool = cg.cg(x_mat, y_vec, tol=1e-3)
        dist_vec = numpy.dot(x_mat, w_opt_vec - w_solved_vec.reshape(len(w_solved_vec), 1))
        err = numpy.sum(dist_vec ** 2)
        print('Squared norm error of CG (tolerance=1e-3):' + str(err))
        self.assertTrue(err < 1e-1)
        self.assertTrue(is_converged_bool)
        
    def test_converge2(self):
        w_solved_vec, is_converged_bool = cg.cg(x_mat, y_vec, tol=1e-10, max_iter_int=123)
        dist_vec = numpy.dot(x_mat, w_opt_vec - w_solved_vec.reshape(len(w_solved_vec), 1))
        err = numpy.sum(dist_vec ** 2)
        print('Squared norm error of CG (tolerance=1e-3):' + str(err))
        self.assertTrue(err > 1e-10)
        self.assertTrue(not is_converged_bool)
        
    def test_converge3(self):
        w_solved_vec, is_converged_bool = cg.cg(x_mat, y_vec)
        dist_vec = numpy.dot(x_mat, w_opt_vec - w_solved_vec.reshape(len(w_solved_vec), 1))
        err = numpy.sum(dist_vec ** 2)
        print('Squared norm error of CG (tolerance=1e-3):' + str(err))
        self.assertTrue(err < 1e-10)
        
    def test_margin(self):
        w_solved_vec, is_converged_bool = cg.cg(x_mat, y_vec, tol=1e-10, max_iter_int=0)
        self.assertTrue(not is_converged_bool)
        w_solved_vec, is_converged_bool = cg.cg(x_mat, y_vec, tol=1e-10, max_iter_int=1)
        self.assertTrue(not is_converged_bool)
        w_solved_vec, is_converged_bool = cg.cg(x_mat, y_vec, tol=1e-10, max_iter_int=2)
        self.assertTrue(not is_converged_bool)
        
if __name__ == '__main__':
    rawdata_mat = numpy.load(PyRLA_dir + 'data/YearPredictionMSD.npy', mmap_mode='r')
    rawdata_mat = rawdata_mat[0:50000, :]
    x_mat = rawdata_mat[:, 1:]
    n_int, d_int = x_mat.shape
    y_vec = rawdata_mat[:, 0].reshape((n_int, 1))

    w_opt_vec = numpy.dot(numpy.linalg.pinv(x_mat), y_vec)
    unittest.main()