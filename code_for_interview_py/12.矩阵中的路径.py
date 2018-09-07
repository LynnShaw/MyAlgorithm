# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        for i, s in enumerate(matrix):
            if s == path[0] and self.visit([(i//cols, i % cols)], matrix, rows, cols, path):
                return True
        return False

    def visit(self, result, matrix, rows, cols, path):
        if len(result) == len(path):
            return True
        i, j = result[-1]
        for ii, jj in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]:
            #             print(ii,jj,result)
            if 0 <= ii and ii < rows and jj < cols and 0 <= jj and (ii, jj) not in result and matrix[ii*cols+jj] == path[len(result)]:
                if self.visit(result+[(ii, jj)], matrix, rows, cols, path):
                    #                     print(result)
                    return True
        return False
