# Nick Fogg
# 12/14/2023
# Test environment for testing engine

import chess
import chess.svg
from PIL import Image, ImageTk
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

import tkinter as tk
from tkinter import messagebox

class Environment(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        # Start button
        self.initial_run = True
        start_btn = tk.Button(self, text="start game", command=self.startGame)
        start_btn.pack()
    
    def startGame(self):
        # Clear GUI
        self.clear_move_handlers()
        self.clear_board()
        
        # Move entry field
        self.move_label = tk.Label(self, text="Enter move using algebraic notation:")
        self.move_label.pack()
        self.move_entry = tk.Entry(self, width=10)
        self.move_entry.pack()
        self.move_btn = tk.Button(self, text="Move", command=self.make_move)
        self.move_btn.pack()
        
        # Generate new board
        self.chessboard = chess.Board()        
        self.paint_board()
    
    def make_move(self):
        try:
            self.chessboard.push_san(self.move_entry.get())
            # Make bot move here #
            self.clear_board()
            self.paint_board()
            self.check_game_status()
        except:
            messagebox.showinfo("Error", "Invalid Chess Move")
        self.move_entry.delete(0, tk.END)
    
    def paint_board(self):
        # Get current board status
        self.chessboardSvg = chess.svg.board(self.chessboard)
        
        # Write SVG to file
        with open("images/board.svg", "w") as file:
            file.write(self.chessboardSvg)

        # Convert SVG to ReportLab graphics
        drawing = svg2rlg("images/board.svg")
        
        # Convert ReportLab graphics to a PNG
        with open("images/board.png", "w") as file:
            renderPM.drawToFile(drawing, 'images/board.png', fmt="PNG")

        # Open PNG board image
        self.start_board = Image.open("images/board.png")
        self.board = ImageTk.PhotoImage(self.start_board)        

        # Display image using Tkinter
        self.board_lbl = tk.Label(self, image=self.board)
        self.board_lbl.pack()
    
    def clear_board(self):
        # Destroy previous board label
        if not self.initial_run:
            self.board_lbl.destroy()
        self.initial_run = False
    
    def clear_move_handlers(self):
        if not self.initial_run:
            self.move_btn.destroy()
            self.move_entry.destroy()
            self.move_label.destroy()
    
    def check_game_status(self):
        if self.chessboard.is_game_over():
            messagebox.showinfo("Game Over", f"{self.chessboard.outcome()}")





if __name__ == "__main__":
    root = tk.Tk()
    Environment(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
