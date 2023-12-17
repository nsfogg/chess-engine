# Nick Fogg
# 12/17/2023
# Chess engine logic

from tree import *

class engine():
    def __init__(self):
        self.search_bound = 3
        node = TreeNode()
        self.turn = True

        self.alpha_beta_minimax(self, node, a, b)
    
    def alpha_beta_minimax(self, node, alpha, beta):
        # check if at search bound
        if node.get_level() >= self.search_bound:
            return self.static_eval(node)

        # check if at leaf
        if len(node.children) == 0:
            if node.get_level() == 0:
                bestMove = []
            return self.static_eval(node)

        # init best moves list
        if node.get_level() == 0:
            best_move = node.children[0]
            # ccheck if there is only one option
            if len(node.children) == 1:
                return None
        
        # Max's turn
        if self.turn:
            self.turn = False
            for child in node.children:
                result = self.alpha_beta_minimax(child, alpha, beta)
                if result > alpha:
                    alpha = result
                    if node.get_level == 0:
                        best_move = child
                if alpha >= beta:
                    return alpha
            return alpha
        # Min's turn
        else:
            self.turn = True
            for child in node.children:
                result = self.alpha_beta_minimax(child, alpha, beta)
                if result < beta:
                    beta = result
                    if node.get_level() == 0:
                        best_move = child
                if beta <= alpha:
                    return beta
            return beta
    
    def static_eval(self, node):
        return 0