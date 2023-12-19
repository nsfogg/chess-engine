# Nick Fogg
# 12/17/2023
# Chess engine logic

from tree import *
import chess
import chess.engine

class Engine():
    def __init__(self, position):
        self.search_bound = 3
        node = TreeNode(position)
        self.turn = True
        self.best_move = []
        self.eng = chess.engine.SimpleEngine.popen_uci("D:\Projects\Stockfish\stockfish-windows-x86-64-modern")
        self.alpha_beta_minimax(node, float('-inf'), float('inf'))
    
    def alpha_beta_minimax(self, node, alpha, beta):
        # check if at search bound
        if node.get_level() >= self.search_bound:
            return self.static_eval(node)

        # check if at leaf
        if len(node.children) == 0:
            if node.get_level() == 0:
                self.bestMove = []
            return self.static_eval(node)

        # init best moves list
        if node.get_level() == 0:
            self.best_move.append(node.children[0])
            # check if there is only one option
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
                        self.best_move.append(child)
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
                        self.best_move.append(child)
                if beta <= alpha:
                    return beta
            return beta
    
    def static_eval(self, node):
        info = self.eng.analyse(node, chess.engine.Limit(time=0.1))
        score = info['score']
        num = ""
        mate = False
        if score[0:4] == 'Mate':
            Mate = True
            i = score[5]
            while not i == ')':
                num += score[i]
        else:
            i = score[3]
            while not i == ')':
                num += score[i]
        
        if mate:
            if num[0] == '-':
                return int(num) - 100000
            else:
                return int(num) + 100000
        else:
            return int(num)

if __name__ == '__main__':
    board = chess.Board()
    board.push_san("f3")
    board.push_san("e6")
    eng = Engine(board)
    print(eng.best_move)
