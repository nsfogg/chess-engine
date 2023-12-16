# Nick Fogg
# 12/14/2023
# Test environment for testing engine

import chess
import chess.svg
from PIL import Image, ImageTk
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF


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
        
        # # Convert SVG to ReportLab graphics
        # drawing = svg2rlg(self.chessboardSvg)
        
        # # Render ReportLab graphics to a PNG string
        # board_string = drawing.asString('PNG')

        # temp image
        self.image = Image.open("images/chess-engine-logo.png")
        # create imagetk obj to display
        self.img = ImageTk.PhotoImage(self.image)
        # create label to display image

        # Display image using Tkinter
        # img = ImageTk.PhotoImage()
        self.board = tk.Label(self, image=self.img)
        self.board.pack()

if __name__ == "__main__":
    root = tk.Tk()
    Environment(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
