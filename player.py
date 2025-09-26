import pygame as pg
import random
import pickle

pg.init()
window = pg.display.set_mode((720, 720))
pg.display.set_caption("Break out")


back_ground = pg.image.load("download.jfif")
back_ground = pg.transform.scale(back_ground, (720, 720))


class player():
     def __init__(self):
          self.width = 10
          self.length = 200
          self.vel = 5
          self.x_loc = (720-200)/2
          self.y_loc = 700

          self.rad = 10
          self.b_xloc = (720)/2 
          self.b_yloc = 700 - self.rad
          self.first_touch = False
          self.y_in = False
          self.len = 18
          self.wid = 20 
          self.col_list = self.col_gen()
          

          self.ball_vel_x = 10   
          self.ball_vel_y = -10  
          self.bricks()

          self.score = 0
          


     def move_left(self):
         self.x_loc -= self.vel
         if (self.b_xloc < 720 and self.b_yloc>0 and self.first_touch == False):
            self.b_xloc -= 10
            self.b_yloc -= 15
            self.first_touch = True
            

     def move_right(self):
          self.x_loc += self.vel
          if (self.b_xloc > 0 and self.b_yloc>0 and self.first_touch == False):
            self.b_xloc += 10
            self.b_yloc -= 15
            self.first_touch = True
            

     '''the new mwthod needed to be found '''
    
     def col_gen(self)->list:
         col_list = []
         for i in range(200):
             col_list.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
         return col_list
         
     def bricks(self)->list:
          self.brick_list = []
          for i in range(5):
            for j in range(40):
                self.brick_list.append(((j*self.len, i*self.wid, self.len, self.wid), random.uniform(0,100)))
          return self.brick_list
                  
    
     def ball_movement(self):
        if self.first_touch:  # only move after launched
            self.b_xloc += self.ball_vel_x
            self.b_yloc += self.ball_vel_y

            # Bounce off left/right walls
            if self.b_xloc - self.rad <= 0 or self.b_xloc + self.rad >= 720:
                self.ball_vel_x *= -1

            # Bounce off top wall
            if (len(self.brick_list)):
                if self.b_yloc - self.rad <= 0:
                    self.ball_vel_y *= -1
                else:
                    for brick in self.brick_list[:]:  
                        bx, by, bl, bw  = brick[0]  

                        if (self.b_xloc + self.rad >= bx and
                            self.b_xloc - self.rad <= bx + bl and
                            self.b_yloc + self.rad >= by and
                            self.b_yloc - self.rad <= by + bw):
                                self.score += brick[1]
                                self.brick_list.remove(brick)  # removes the exact (x, y) pair
                                self.ball_vel_y *= -1
                                print(f"score is {self.score}")
                                break


            # Paddle collision
            if (self.y_loc <= self.b_yloc + self.rad <= self.y_loc + self.width and
                self.x_loc <= self.b_xloc <= self.x_loc + self.length):
                self.ball_vel_y *= -1
                offset = (self.b_xloc - (self.x_loc + self.length/2)) / (self.length/2)
                self.ball_vel_x += offset * 2

     
     def game_over(self):
        with open("score.bin", "rb") as f:  
            saved_score = pickle.load(f)
        if(self.score >= saved_score):
              with open("score.bin", "wb") as f:   
                pickle.dump(self.score, f)
        window.fill((0,0,0))
        font = pg.font.SysFont(None, 48)
        if(self.score >= saved_score):
            game_over_text = font.render(f"GAME OVER!!! \n HIGHSCORE : {round(self.score, 4)}", True, (0, 128, 255))
            with open("score.bin", "wb") as f:   
                pickle.dump(self.score, f)
        else:
            game_over_text = font.render(f"GAME OVER!!! \n SCORE : {round(self.score, 4)}", True, (0, 128, 255))
        text_rect = game_over_text.get_rect(center=(340, 300))
        window.blit(game_over_text, text_rect)
        pg.display.flip()

    


     def bg_update(self):
        if((self.b_yloc > 720 + self.width) or len(self.brick_list)==0):
            self.game_over()
        else:
            window.blit(back_ground, (0,0))
            pg.draw.rect(window, (255, 255, 255), (self.x_loc, self.y_loc, self.length, self.width))
            self.ball_movement()
            
            
            for i in range(len(self.brick_list)):
                pg.draw.rect(window, self.col_list[i], self.brick_list[i][0])
            
            pg.draw.circle(window, (255, 255, 255), (self.b_xloc, self.b_yloc), self.rad)
            pg.display.update()
            # RENDER  GAME HERE
    