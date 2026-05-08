print("欢迎你开启大模型开发之旅！")


def greet(name: str) -> str:
    return f"你好，{name}，祝你学习顺利！"


if __name__ == "__main__":
    message = greet("开发者")
    print(message)
