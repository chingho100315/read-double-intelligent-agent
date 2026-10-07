from time import sleep

print("正在為你換醒記憶中... ")
path = "all/conversations.txt"
with open(path) as file:
    text = file.read()
    load = eval(text)
    print(f"type : {type(load)}\n")

for a in load:
    if not (a["bot_name"] == ""):
        print(a["bot_name"])
    sleep(0.01)

print()

class Content:
    def __init__(self):
        self.number = 0
        self.both = None
        self.ai()

    def ai(self):
        self.bot = input("你想到什麼智能體 : \n")

        for a in load:
            if a["bot_name"] == self.bot:
                return

        print("沒有這個智能體\n")
        self.ai()

    def inputs(self):
        a = input("第幾次？ : \n")

        try:
            self.number = eval(a)

            for z in load:
                if z["bot_name"] == self.bot:
                    if len(z["messages"]) <= eval(a):
                        print(f"數字過大, 只有 : {len(z['messages']) - 1}")
                        self.number = "nope"

        except Exception as e:
            print("數字有誤")
            self.number = "nope"

content = Content()

running = True
while running:
    if content.number == "nope":
        nexts = False
    else:
        nexts = True
    find = False
    cmd = input("\n你有其他事情嗎, ('e' : 退出, 'c' : 換個, 'a' : 聊數, 't' : 時間, 'l' : 調出所有, 'm' : 從到), 's' : 儲存, 'sl' : 儲存描述, 如果什麼都沒有直接回車: \n")

    if cmd == "e":
        break

    if cmd == "c":
        content.ai()
        continue

    if cmd == "sl":
        with open(f"{content.bot}.write.txt", "w") as w:
            with open("all/bots/bot_information.txt", "r") as r:
                for z in eval(r.read()):
                    if z["bot_name"] == content.bot:
                        w.write(str(z))
        print("it's finish")
        nexts = False

    if cmd == "s":
        for z in load:
            if z["bot_name"] == content.bot:
                with open(f"{content.bot}.normal.txt", "w") as file:
                    file.write(str(z))
        print("it's finish")
        nexts = False

    if cmd == "a":
        for z in load:
            if z["bot_name"] == content.bot:
                print(f"\n你們已經聊了足足... {len(z['messages']) - 1}次... ")
                nexts = False

    if cmd == "m":
        many = input("一定要按照格式 : (1, 100)\n")

        try:
            number = eval(many)
            if type(number) == tuple:
                for a in load:
                    if a["bot_name"] == content.bot:
                        for b in a["messages"]:
                            if number[0] <= a["messages"].index(b) <= number[1]:
                                text = b["show_content"]

                                print("\n")

                                if b["user_type"] == "bot":
                                    for z in content.bot + " : " + text:
                                        print(z, end="", flush=True)
                                        sleep(0.01)
                                if b["user_type"] == "user":
                                    for z in "你 : " + text:
                                        print(z, end="", flush=True)
                                        sleep(0.03)

                                sleep(0.2)

        except Exception:
            print("出錯或格式不符")

        nexts = False

    if cmd == "l":
        if input("確定嗎, 要很久才能輸完 (確定 : 'y'): \n") == "y":
            for a in load:
                if a["bot_name"] == content.bot:
                    for b in a["messages"]:
                        text = b["show_content"]

                        if b["user_type"] == "bot":
                            for z in f"{content.bot} : {text}":
                                print(z, end="", flush=True)
                                sleep(0.01)
                        if b["user_type"] == "user":
                            for z in f"你 : {text}":
                                print(z, end="", flush=True)
                                sleep(0.03)

                        print("\n")
                        sleep(0.25)

        nexts = False

    if cmd == "t":
        nexts = False
        time = input("時間 : 要严格按照格式 (2026-01-01)\n")

        for a in load:
            if a["bot_name"] == content.bot:
                for b in a["messages"]:
                    if b["create_time"][:10] == time:
                        text = b["show_content"]

                        if b["user_type"] == "bot":
                            for z in f"{content.bot} : {text}":
                                print(z, end="", flush=True)
                                sleep(0.02)
                        if b["user_type"] == "user":
                            for z in f"你 : {text}":
                                print(z, end="", flush=True)
                                sleep(0.08)

                        print("\n")

                        sleep(0.5)

                        find = True

        if not find:
            print("無法找到, 或者格式有錯, 請檢查")

    if nexts:
        content.inputs()

        try:
            for a in load:
                if a["bot_name"] == content.bot:
                    print()

                    text = a["messages"][content.number]["show_content"]

                    for b in a["messages"]:
                        if a["messages"].index(b) == content.number:
                            if b["user_type"] == "bot":
                                print(content.bot + " : " + text)
                            elif b["user_type"] == "user":
                                print("你 : " + text)

                    print()
        except Exception:
            ...
