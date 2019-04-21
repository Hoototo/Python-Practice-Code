"""
    作者：Nick
    功能：五角星的绘制
    版本：2.0
    日期：4/8/2019
    新增功能：加入循环操作绘制重复不同大小的图形
"""
import turtle


def draw_pentagram(size):
    """
        绘制五角星
    """
    # 计数器
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count = count + 1

def main():
    """
        主函数
    """
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize()
    turtle.pencolor('red')

    size = 50  # pentagram的长度

    while size <= 100:
        draw_pentagram(size)
        size = size + 10

    turtle.exitonclick()

if __name__ == '__main__':
    main()