from graphics import *
import time
from threading import Thread

grid_side = 50;
# create a graphics window
win = GraphWin ('Testing', 500, 500)
win.setBackground(color_rgb(255, 255, 255))
wallsList = [(9, 1), (10, 1), (2, 2), (4, 2), (5, 2), (7, 2), (7, 3), (9, 3),
             (3, 4), (5, 4), (7, 4), (9, 4), (3, 5), (5, 5), (7, 5), (8, 5), (9, 5), (2, 6),
             (3, 6), (5, 6), (8, 6), (2, 7), (5, 7), (6, 7), (8, 7), (10, 7), (2, 8), (6, 8), (8, 8),
             (10, 8), (4, 9), (5, 9), (6, 9), (1, 10), (2, 10)]

adjencyDict = {} #lưu trữ thông tin cho mỗi ô lưới
nodeVisit = [[False for i in range(11)] for j in range(11)] # gán bằng giá trị false nếu đi qua rồi thì sẽ chuyển thành true
nodeVisit[1][1] = True
for a in wallsList: # duyện tường
    pt1 = Point((a[0] - 1) * grid_side, (a[1] - 1) * grid_side) # xác định thuộc góc phía trên bên trái
    pt2 = Point((a[0]) * grid_side, (a[1]) * grid_side) # góc phía trên bên phải
    rect1 = Rectangle(pt1, pt2) # tạo ra một hình vuông bằng 2 góc trên
    rect1.setFill(color_rgb(0, 102, 248))# đựat mau xanh
    rect1.draw(win)# vẽ nó

global endPoint # là 1 biến toàn cục ( có thể sử dụng mọi nơi trong chương trình )
endPoint = (2,1 ) # gán bằng (1,4)
# tạo đôi tượng  hình tròn
circle = Circle(Point(((endPoint[0] - 1) * grid_side) + 25, ((endPoint[1] - 1) * grid_side) + 25), 25)
circle.setFill('yellow') # set màu
circle.draw(win) # vẽ
global startPoint
startPoint = (1, 1)
circle1 = Circle(Point(((startPoint[0] - 1) * grid_side) + 25, ((startPoint[1] - 1) * grid_side) + 25), 25)
circle1.setFill('red')
circle1.draw(win)

path = [];

def createAdjencyDict():
    for y in range(1, 11):
        for x in range(1, 11):
            point = (y, x) # đặt point ( y , x )
            if point in wallsList: # dích tường
                continue # đi tiếp
            else: # k dích tường
                adjencyDict[point] = [] # tạo ra một mạng point để chứa
                if ((y - 1 != 0)): # tính tình hàng từ 2 -10
                    if (y - 1, x) not in wallsList: # nếu mà k dính tường
                        currList = adjencyDict[point] # thì gọi nó là một currList
                        currList.insert(0, (y - 1, x)) # thêm vào đầu mảng ;
                if ((y + 1 != 11)):
                    if (y + 1, x) not in wallsList:
                        currList = adjencyDict[point]
                        currList.insert(0, (y + 1, x))
                if ((x - 1 != 0)):
                    if (y, x - 1) not in wallsList:
                        currList = adjencyDict[point]
                        currList.insert(0, (y, x - 1))
                if ((x + 1 != 11)):
                    if (y, x + 1) not in wallsList:
                        currList = adjencyDict[point]
                        currList.insert(0, (y, x + 1))

def moving():
    global endPoint
    key = win.checkKey()# kiếm tra nếu phím nào được bấm
    if key == 'Up':
        circle.move (0, -50) # di chuyển lên 1 ô
        print("Up")
        for a in wallsList: # check tường
            pt1 = Point((a[0] - 1) * grid_side, (a[1] - 1) * grid_side) # xét góc th 1 bên trái
            pt2 = Point(a[0] * grid_side, a[1] * grid_side)# xét góc thứ 1 bên pahir
            rect1 = Rectangle(pt1, pt2) # tạo ra hình cn
            # nếu tâm hình tròn trùng với tâm của hình cnx`

            if circle.getCenter().x == rect1.getCenter().x and circle.getCenter().y == rect1.getCenter().y:
                circle.move(0, 50)
    elif key == 'Down':
        circle.move (0, 50)
        print("Down")
        for a in wallsList:
            pt1 = Point((a[0] - 1) * grid_side, (a[1] - 1) * grid_side)
            pt2 = Point(a[0] * grid_side, a[1] * grid_side)
            rect1 = Rectangle(pt1, pt2)
            if circle.getCenter().x == rect1.getCenter().x and circle.getCenter().y == rect1.getCenter().y:
                circle.move(0, 50)
        for a in wallsList:
            pt1 = Point((a[0] - 1) * grid_side, (a[1] - 1) * grid_side)
            pt2 = Point(a[0] * grid_side, a[1] * grid_side)
            rect1 = Rectangle(pt1, pt2)
            if circle.getCenter().x == rect1.getCenter().x and circle.getCenter().y == rect1.getCenter().y:
                circle.move(0, -50)
    elif key == 'Left':
        circle.move (-50, 0)
        print("Left")
        for a in wallsList:
            pt1 = Point((a[0] - 1) * grid_side, (a[1] - 1) * grid_side)
            pt2 = Point(a[0] * grid_side, a[1] * grid_side)
            rect1 = Rectangle(pt1, pt2)
            if circle.getCenter().x == rect1.getCenter().x and circle.getCenter().y == rect1.getCenter().y:
                circle.move(50, 0)
    elif key == 'Right':
        circle.move (50, 0)
        print("Right")
        for a in wallsList:
            pt1 = Point((a[0] - 1) * grid_side, (a[1] - 1) * grid_side)
            pt2 = Point(a[0] * grid_side, a[1] * grid_side)
            rect1 = Rectangle(pt1, pt2)
            if circle.getCenter().x == rect1.getCenter().x and circle.getCenter().y == rect1.getCenter().y:
                circle.move(-50, 0)

    endPoint = ((circle.p1.x / grid_side) + 1, (circle.p1.y / grid_side) + 1) #xác định tọa độ của endpoint khi di chuyển .
    #xác đinh bằng cách (lấy tọa độ điểm x / kích thuốc ô +1 ) làm tròn xuống theo phy thon
    # ví dụ như (2,3) thì circle.p1.x = 75 / 50 +1 thì sẽ bằng 2  múc địch có cái này là để xác định tọa độ của nó
    path.clear() # gọi hàm này để chúng ta làm sạch mảng khi tìm đường đi mới
    dfs(startPoint, endPoint) # gọi hàm dfs thay node = startPoint và target = endPoint

def dfs(node, target):
    endReached = False # biến kiểm tra xem thấy đến đích chưa
    nodeVisit[node[0]][node[1]] = True # đây là mảng 2 chiều đại diện cho y là node[0] x là node[1] . việc đánh dấu true ở vị trị node này có nghĩa là nó đã được đến thăm
    path.append(node) # nút hiện tại đã được thăm và có thể đưa vào mảng
    if node == target: # nếu node hiện tại đang ở đích trả về true (đã tìm thấy đường đi)
        return True
    for point in adjencyDict[node]:# duyệt tất cả các điểm kề với node
        if (endReached == True): # nếu tìm thấy đích thì dừng lại
            break
        if nodeVisit[point[0]][point[1]] == False: # nếu các điểm kề xung quoanh point chưa được thăm
            endReached = dfs(point, target)# thì chúng ta sẽ chạy lại đệ quy các nút kề với nó
            if not endReached: # nếu mà không tìm được đến đích
                path.append(node)# thêm nút hiện tại vào danh sách để biết đường đi này không hoạt động và ta cần tìm theo hướng khác
                # điều này đảm bảo rằng khi mà ta ko tìm thấy đcđường  thì node đó đã được lưu và khi check node khác ta sẽ kp check nút ko có đg đi nx;
    return endReached #nếu tìm đc đường đi rồi thì ta sẽ dừng lại còn nếu chưa thì thấy thì ta lại chạy lại từ đầu cho đênns khi tìm đc đường đi

def moveGhost(): # hàm này có nhiệm vụ di chuyển theo mảng path
    global startPoint
    for i in range(0, len(path) - 1): # duyệt qua đường đi trong mảng path bắt đầu từ index 0
        time.sleep(0.1)  # tốc độ chạy
        # Put a circle in next cell:
        cell = path[i + 1] # gán điểm tiếp theo bằng cell
        cellBefore = path[i] # và điểm trước đó là cellbefore
        changey = ((cell[0] - startPoint[0]) * grid_side) -  ((cellBefore[0] - startPoint[0]) * grid_side) # tính toán di chuyển trục x
        changex = ((cell[1] - startPoint[1] - 0.5) * grid_side) - ((cellBefore[1] - startPoint[1] - 0.5) * grid_side) # tính toán trục y
        circle1.move(changey, changex) ;# cho chi chuyển
        startPoint = cell #gán điểm xuất phát mơi

while True:
    nodeVisit = [[False for i in range(11)] for j in range(11)]
    nodeVisit[1][1] = True
    createAdjencyDict()
    moving()
    moveGhost()
    print(nodeVisit)