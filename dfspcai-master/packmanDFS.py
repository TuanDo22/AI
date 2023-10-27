from graphics import *
import time

grid_side = 50;
win = GraphWin("ProjectPacman", grid_side*10, grid_side*10);
#NOTE: In this list and other places, first point is y axis and second is x!!

wallsList = [(1,9), (1,10), (2,2), (2,4), (2,5), (2,7), (3,7), (3,9),
            (4,3), (4,5), (4,7), (4,9), (5,3), (5,5), (5,7),(5,8),(5,9), (6,2),
            (6,3),(6,5),(6,8),(7,2),(7,5),(7,6),(7,8),(7,10),(8,2),(8,6),(8,8),
            (8,10),(9,4),(9,5),(9,6),(10,1),(10,2)];

startPoint = (1,1);
endPoint = (4,6);

adjencyDict = {};

# nó sẽ gán cho map bằng giá trị (F) false nếu mà đã ghé thăm rồi thì giá trị sẽ chuyển thành True ;
nodeVisit = [[False for i in range(11)] for j in range(11)]
nodeVisit[1][1] = True;

path = [];


######################################################################
######################################################################
#hàm create tạo các điểm không bị chặn bởi tường 
def createAdjencyDict():
   # chạy hàng  từ 1-10
   for y in range(1, 11):
      # chạy cột từ 1-10
      for x in range(1, 11):
         point = (y, x);
         if point in wallsList:  # nếu như ô này vướng tường thì tiếp tục
            continue;
         else:  # còn không vướng tường
            adjencyDict[point] = [];  # thì ta sẽ tạo ra một list trống tại thời điểm đó
            if ((y - 1 != 0)):  # nếu như hàng hiện tại không phải hàng đầu tiên nghĩa là tính từ hàng thứ 2 trở đi ( từ hàng tứ  2 đến hàng thứ 10 )
               if (y - 1, x) not in wallsList:  # nêu ô này không có nằm trong wallList(danh sách bị chặn )
                  currList = adjencyDict[point];  # lây ra danh sách các ô mà không nằm trong wallList
                  currList.insert(0, (y - 1, x));  # sau đó thêm các phần tử có trong điểu kiện vào đầu danh sách
            # các ô sau cũng như thế mục tiêu l để xây dụng các ô kề với điểm point
            if ((y + 1 != 11)):
               if (y + 1, x) not in wallsList:
                  currList = adjencyDict[point];
                  currList.insert(0, (y + 1, x));
            if ((x - 1 != 0)):
               if (y, x - 1) not in wallsList:
                  currList = adjencyDict[point];
                  currList.insert(0, (y, x - 1));
            if ((x + 1 != 11)):
               if (y, x + 1) not in wallsList:
                  currList = adjencyDict[point];
                  currList.insert(0, (y, x + 1));


def initializeGame():
   """
   This function initializes the board with walls and place the pacman at start and
   marks the end position.

   """
   #Coloring the background black
   win.setBackground(color_rgb(0,0,0));

   for i in range(1, 11):
      for j in range(1, 11):
         # dòng này để tính toán cho điểm tại vị trí ở giữa 1 ô
         center = Point((i - 0.5) * grid_side, (j - 0.5) * grid_side);  # grid_slide là kích thước của 1 ô
         cir = Circle(center, 1);  # tạo ra ô tròn
         cir.setFill(color_rgb(255, 255, 255))  # có màu trắng
         cir.draw(win)  # vẽ
   #Drawing the walls;
   for a in wallsList:
      pt1 = Point((a[1]-1)*grid_side, (a[0]-1)*grid_side)
      pt2 = Point((a[1])*grid_side, (a[0])*grid_side)
      rect1 = Rectangle(pt1, pt2)
      rect1.setFill(color_rgb(0,102,248))
      rect1.draw(win)



   center = Point((startPoint[1]-0.5)*grid_side,(startPoint[0]-0.5)*grid_side);
   cir = Circle(center, 25);
   cir.setFill(color_rgb(255,255,0))
   cir.draw(win)
   
   
   rect1 = Rectangle(Point((endPoint[1]-1)*grid_side, (endPoint[0]-1)*grid_side),
                     Point((endPoint[1])*grid_side, (endPoint[0])*grid_side))
   rect1.setFill(color_rgb(255,0,0))
   rect1.draw(win)

######################################################################
######################################################################
# DFS algorithm:
#node is coordinate in (y,x) way.
def explore(node):
   
   endReached = False;
   nodeVisit[node[0]][node[1]] = True;
   path.insert(len(path), node);
   
   if node ==  endPoint:
      return True;

   if node != startPoint:
      colorNode(node,0,175,0); # Green
   
   for neighbour in adjencyDict[node]:
      if(endReached == True):
         break;
      if (nodeVisit[neighbour[0]][neighbour[1]] == False):
         endReached = explore(neighbour);
         if(not endReached):
            path.insert(len(path), node);
            if node != startPoint:
               colorNode(node,0,175,0);
         
   return endReached;

def colorNode(node,r,g,b):
   pt1 = Point((node[1]-1)*grid_side, (node[0]-1)*grid_side)
   pt2 = Point((node[1])*grid_side, (node[0])*grid_side)
   rect1 = Rectangle(pt1, pt2)
   rect1.setFill(color_rgb(r,g,b))
   rect1.draw(win)

def colorPathBlack():
   for node in path:
      pt1 = Point((node[1]-1)*grid_side, (node[0]-1)*grid_side)
      pt2 = Point((node[1])*grid_side, (node[0])*grid_side)
      rect1 = Rectangle(pt1, pt2)
      rect1.setFill(color_rgb(0,0,0))
      rect1.draw(win)
      
      rect1 = Rectangle(Point((endPoint[1]-1)*grid_side, (endPoint[0]-1)*grid_side),
                     Point((endPoint[1])*grid_side, (endPoint[0])*grid_side))
      rect1.setFill(color_rgb(255,0,0))
      rect1.draw(win)

def moveGhost():
   for i in range(0, len(path) - 1):
      time.sleep(0.1);
      #Put a circle in next cell:
      cell = path[i+1];
      center = Point((cell[1]-0.5)*grid_side,(cell[0]-0.5)*grid_side);
      cir = Circle(center, 25);
      cir.setFill(color_rgb(255,255,0))
      cir.draw(win)

      #Turn current circle green
      colorNode(path[i],255,20,147);
      

def main():
   initializeGame();
   createAdjencyDict();
   explore(startPoint);
   #scolorPathBlack()
   moveGhost();
   
   #getMounse() + close(): It wait untilsomeone clicks and doing so closes it
   win.getMouse();
   win.close();


   
main();


