import os
import argparse
import configparser
from revChatGPT.V3 import Chatbot
from rich.console import Console
from colorama import init as colorama_init
from modules.settings import *

console = Console()

colorama_init()
config = configparser.ConfigParser()
config.read("config.ini")


auth = {
    "api_key": config["ChatGPT"]["api_key"],
    "proxy": config["ChatGPT"]["proxy"],
}



# 定义文件路径
filename = os.path.join('models', 'md.txt')
# 打开文件并读取内容
with open(filename, 'r', encoding='utf-8') as f:
    promptStr = f.read()


# print(f"[{BLUE}0{RESET}] {BOLD}读取解析文档的prompt{RESET}")
# 打印读取的字符串
# print(str)
readnum = 0
# 读取代码文件
def read_file(file_path):
    global readnum, prompt
    readnum = readnum + 1
    print('file_path---------------',file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()
        
    file_name, ext = os.path.splitext(file_path)
    file_name = os.path.basename(file_path)
    
    
    print(f"[{BLUE}{readnum}{RESET}] {BOLD}完成{file_name}代码文档读取{RESET}")
    with console.status("[bold green] 正在解析写入中，请等待...") as status:
        print(auth["proxy"])
        # print(code)
        chatbox = Chatbot(api_key=auth["api_key"],proxy=auth["proxy"])
        print(args["frame"])
        prompt = promptStr
        prompt = prompt.replace("framefile",f"{args['frame']}的{file_name}" if args['frame'] else "" )
        prompt = prompt.replace("CODE", code)
        # print(prompt)
        result = chatbox.ask(prompt)
        # 根据回答的内容，生成md文档写入到当前项目的outputs目录下
        with open('outputs/' + file_name + '.md', 'w', encoding='utf-8') as f:
            f.write(result)
    print(f"[{BLUE}{readnum}{RESET}] {BOLD}完成{file_name}代码文档写入{RESET}")
    return result

print(f"[{BLUE}info{RESET}] {BOLD}自动解析代码生成代码解释文档{RESET}")

# print(f"[{BLUE}input{RESET}] {BOLD}请输入要解析的代码地址{RESET}")
path = input('请输入要解析的代码地址:')
frame = input('请输入框架名称:')
# 如果frame有输入内容，则将frame的内容赋值给args.frame，否则赋值None


args = {
    "frame": None,
    "file": None,
    "dir": None
}
args["frame"] = frame if frame else None

if os.path.isfile(path):
    print(f"[{BLUE}0{RESET}] {BOLD}读取代码{RESET}")
    args["file"] = path
elif os.path.isdir(path):
    print(f"[{BLUE}0{RESET}] {BOLD}读取代码目录{RESET}")
    args["dir"] = path
else:
    exit(f"[{RED}Error{RESET}] 代码文件路径不存在")
    
if args["file"]:    
    if not os.path.exists(args["file"]):
        exit(f"[{RED}Error{RESET}] Code file does not exist. Please check the path {args['file']}")
    else:
        code = read_file(args["file"])
    

# 读取代码目录
# 判断args.dir参数是否存在
if args["dir"]:
    if not os.path.exists(args["dir"]):
        exit(f"[{RED}Error{RESET}] Code dir does not exist")
    else:
        # 获取目录下的文件列表
        file_list = os.listdir(args["dir"])
        # 逐个读取文件内容
        for file_name in file_list:
            # 获取文件路径
            file_path = os.path.join(args["dir"], file_name)
            code = read_file(file_path)




