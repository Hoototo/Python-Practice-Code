"""
    作者：Nick
    功能：五角星的绘制
    版本：1.0
    日期：4/5/2019
"""
import turtle


def main():
    """
        主函数
    :return:
    """
    # 计数器
    count = 1

    while count <= 5:

        turtle.forward(100)
        turtle.right(144)
        count = count + 1

    turtle.exitonclick()

if __name__ == '__main__':
    main()