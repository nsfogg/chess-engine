# Nick Fogg
# 12/14/2023
# Test environment for testing engine

import chess
import chess.svg
from PIL import Image, ImageTk
import tkinter as tk

class Environment(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        

        # <create the rest of your GUI here>
        # Start button
        start_btn = tk.Button(self, text="start game", command=self.startGame)
        start_btn.pack()
    
    def startGame(self):
        self.chessboard = chess.Board()
        self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
        
        self.widgetSvg.load(self.chessboardSvg)

if __name__ == "__main__":
    root = tk.Tk()
    Environment(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

# def startGame(window):
#     lbl = tk.Label(window, "shit")
#     lbl.pack()

# def loadGUI():
#     # Window
#     root = tk.Tk()
    
#     # Start buttton
#     btn = tk.Button(root, text="Start Game", command=lambda: startGame(root))
#     btn.pack()

#     # Open
#     root.mainloop()

# def main():
#     board = chess.Board()

#     # Load engine
#     # [TO-DO]

#     # Start game
#     loadGUI()

    
# if __name__ == '__main__':
#     main()