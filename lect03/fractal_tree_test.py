"""
    作者：Nick
    功能：利用递归函数绘制分形树
    版本：1.0
    日期：4/13/2019
"""
import turtle

def draw_branch(branch_length):
    """
    绘制分形树

    """
    if branch_length > 30:
        # 绘制右侧树枝
        turtle.forward(branch_length)
        print('向前 ', branch_length)

        turtle.right(45)
        print('右转 45')
        draw_branch(branch_length - 15)

        # 绘制左侧树枝
        turtle.left(90)
        print('左转 90')
        draw_branch(branch_length - 15)

        # 返回之前的树枝
        turtle.right(45)
        print('右转 45')
        turtle.backward(branch_length)

def main():
    """
        主函数
    """
    turtle.left(90)
    draw_branch(60)
    turtle.exitonclick()

if __name__ == '__main__':
    main()