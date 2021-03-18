#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:20:23 2020

@author: kaydee
"""
import argparse
from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM
import time
from os import system,name





def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

BOARDS = ['debug', 'n00b', 'l33t', 'error','on']  # Available sudoku boards
MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board

class SudokuError(Exception):
    pass


class SudokuBoard(object):
    def __init__(self,board_file):
        self.board = self.__create_board(board_file)
        
    def __create_board(self,board_file):
        board = []
        
        for line in board_file:
            #print(line)
            line = line.strip()
            if len(line) != 9:
                board = []
                raise SudokuError("Line should be 9 chars long.")
                
            board.append([])
            
            for char in line:
                if not char.isdigit():
                    raise SudokuError("Sudoku must only contain digits(0-9).")
                board[-1].append(int(char))
                
        if len(board)!=9:
            raise SudokuError("There must be 9 rows in sudoku.",board)
                
        
        return board
    
    
class SudokuGame(object):
    def __init__(self,board_file):
        self.board_file = board_file
        self.start_puzzle = SudokuBoard(board_file).board
        self.puzzle = []
        
    def start(self):
        self.game_over = False
        self.puzzle = []
        
        
        for i in range(9):
            self.puzzle.append([])
            for j in range(9):
                self.puzzle[i].append(self.start_puzzle[i][j])
        #print(self.puzzle,self.start_puzzle)
                
    def check(self):
        checks = 0
        win = True
        for row in range(9):
            r = self.__check_row(row)
            if r == -1:
                self.game_over = True
                return -1
            elif r == 0:
                win = False
            
        for column in range(9):
            c = self.__check_column(column)
            if c == -1:
                self.game_over = True
                return -1
            elif c == 0:
                win = False
            
        for row in range(3):
            for column in range(3):
                b = self.__check_square(row, column)
                if b == -1:
                    self.game_over = True
                    return -1
                elif b == 0:
                    win = False
                
        if win:
            self.game_over = True
            return 1
        else:
            return 0
    
                
        
 
    
    
    def __check_block(self, block,t):
        h= {}
        for i in list(block):
            if i in h and i != 0:
                #print(list(block),t)
                return -1
            h[i] = 1
        
        if set(block) == set(range(1, 10)):
            return 1
        return 0
        

    def __check_row(self, row):
        return self.__check_block(self.puzzle[row],'r')

    def __check_column(self, column):
        return self.__check_block(
            [self.puzzle[row][column] for row in range(9)],'c'
        )

    def __check_square(self, row, column):
        return self.__check_block(
            [
                self.puzzle[r][c]
                for r in range(row * 3, (row + 1) * 3)
                for c in range(column * 3, (column + 1) * 3)
            ],'b'
        )
    def checkg(self):
        for r in range(9):
            for c in range(9):
                if self.puzzle[r][c] == 0:
                    return False
        return True
    
    
    
class SudokuUI(Frame):
    def __init__(self,parent,game):
        self.game = game
        self.parent = parent
        Frame.__init__(self,parent)
        
        self.row,self.col = 0,0
        
        self.__initUI()
        
        
    def __initUI(self):
        self.parent.title('Sudoku')
        self.pack(fill=BOTH,expand=1)
        self.canvas = Canvas(self,width=WIDTH,height=HEIGHT)
        self.canvas.pack(fill=BOTH,side=TOP)
        clear_button = Button(self,text='Start backtracking!(Solve)',command = self.__clear_answers)
        clear_button.pack(fill=BOTH, side = BOTTOM)
        
        self.__draw_grid()
        self.__draw_puzzle()
        
        self.canvas.bind('<Button-1>',self.__cell_clicked)
        self.canvas.bind('<Key>',self.__key_pressed)
        
        
        
    def __draw_grid(self):
        for i in range(10):
            color = 'blue' if i % 3 ==0 else 'gray'
            
            x0 = MARGIN + i*SIDE
            y0 = MARGIN
            x1 = MARGIN + i*SIDE
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0,y0,x1,y1,fill=color)
            
            x0 = MARGIN
            y0 = MARGIN + i*SIDE
            x1 = WIDTH - MARGIN
            y1 = MARGIN + i*SIDE
            self.canvas.create_line(x0,y0,x1,y1,fill=color)
            
            
    def __draw_puzzle(self):
        self.canvas.delete('numbers')
        for i in range(9):
            for j in range(9):
                answer = self.game.puzzle[i][j]
                if answer != 0:
                    x = MARGIN + j *SIDE + SIDE/2
                    y = MARGIN + i *SIDE + SIDE/2
                    orignal = self.game.start_puzzle[i][j]
                    color = 'black' if answer == orignal else 'sea green'
                    self.canvas.create_text(x,y,text=answer,tags='numbers',fill=color)
                    
            
        
    def __clear_answers(self):
        self.game.start()
        self.canvas.delete('victory')
        self.__draw_puzzle()
        self.backtrack()
        
    def __cell_clicked(self,event):
        if self.game.game_over:
            return
        x,y = event.x,event.y
        if (MARGIN < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN):
            self.canvas.focus_set()
            row,col = (y-MARGIN)//SIDE,(x-MARGIN)//SIDE
        
            if (row,col) == (self.row,self.col):
                self.row,self.col = -1,-1
            elif self.game.puzzle[row][col] == 0:
                self.row,self.col = row,col
            
        else:
            self.row,self.col = -1,-1
        #print(self.row,self.col)
        self.__draw_cursor()
        
    def __draw_cursor(self):
        self.canvas.delete("cursor")
        if self.row >= 0 and self.col >= 0:
            x0 = MARGIN + self.col * SIDE + 1
            y0 = MARGIN + self.row * SIDE + 1
            x1 = MARGIN + (self.col + 1) * SIDE - 1
            y1 = MARGIN + (self.row + 1) * SIDE - 1
            self.canvas.create_rectangle(
                x0, y0, x1, y1,
                outline="red", tags="cursor"
            )
            
    def __key_pressed(self,event):
        if self.game.game_over:
            return
        if self.row>=0 and self.col>= 0 and event.char in '1234567890':
            self.game.puzzle[self.row][self.col] = int(event.char)
            self.col,self.row = -1,-1
            self.__draw_puzzle()
            self.__draw_cursor()
            #print(self.game.check())
            if self.game.check() == 1:
                self.__draw_victory()
            elif self.game.check() == -1:
                print("lose")
            else:
                print('runnin')
                
            
                
                
    def __draw_victory(self):
        # create a oval (which will be a circle)
        x0 = y0 = MARGIN + SIDE * 2
        x1 = y1 = MARGIN + SIDE * 7
        self.canvas.create_oval(
            x0, y0, x1, y1,
            tags="victory", fill="dark orange", outline="orange"
        )
        # create text
        x = y = MARGIN + 4 * SIDE + SIDE / 2
        self.canvas.create_text(
            x, y,
            text="You win!", tags="winner",
            fill="white", font=("Arial", 32)
        )
        
        
    def backtrack(self):
        
        for m in range(81):
           
            r = m//9
            c = m%9
           
            if self.game.puzzle[r][c] == 0:
                
                for val in range(1,10):
                    if not val in self.game.puzzle[r]:
                        if not val in  [self.game.puzzle[row][c] for row in range(9)]:
                            if not val in [
                                self.game.puzzle[row][col]
                                for row in range((r//3) * 3, (r//3 + 1) * 3)
                                for col in range((c//3) * 3, (c//3 + 1) * 3)]:
                                    self.row,self.col = r,c
                                    self.game.puzzle[r][c] = val
                                    #self.__draw_cursor()
                                    
                                    clear()
                                    prin = [[self.game.puzzle[b][a] if self.game.puzzle[b][a] != 0 else " " for a in range(9)] for b in range(9)]
                                    prin = [["\033[1m\033[92m"+str(prin[b][a])+"\033[0m" if self.game.start_puzzle[b][a] != 0 else str(prin[b][a]) for a in range(9)] for b in range(9)]
                                    for o in range(9):
                                        if o%3 == 0:
                                            print("+-----+-----+-----+")
                                        print("",*prin[o][:3],*prin[o][3:6],*prin[o][6:],"",sep="|")
                                    print("+-----+-----+-----+")
                                    time.sleep(0.02)
                                    if self.game.checkg():
                                         self.__draw_puzzle()
                                         return True
                                    else:
                                        
                                        
                                        if self.backtrack():
                                            return True
                break                            
        self.game.puzzle[r][c]=0                           
                                
                            
                    
                    
                    
                    
                    
                    
                    
                    
        
def parse_arguments():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--board',help='Desired board name',type=str,choices=BOARDS,required=True)
    
    args = vars(arg_parser.parse_args())
    return args['board']


if __name__ == '__main__':
    board_name = parse_arguments()
    
    with open('%s.sudoku'%board_name,'r') as boards_file:
        game = SudokuGame(boards_file)
        game.start()
        
        root = Tk()
        ui = SudokuUI(root,game)
        root.geometry('%dx%d'%(WIDTH,HEIGHT+40))
        
        root.mainloop()
        