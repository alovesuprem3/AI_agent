import time

def get_current_time():
    """获取当前系统时间"""
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def write_todo_to_file(task):
    """将待办事项写入本地备忘录文件"""
    with open("todo_list.txt", "a", encoding="utf-8") as f:
        f.write(f"- {task}\n")
    return "已成功写入备忘录！"

def run_simulation(user_input):
    print(f"\n[用户]: {user_input}")
    print("[Agent思考中...]")
    time.sleep(1) # 假装在思考
    
    if "时间" in user_input or "几点" in user_input:
        current_time = get_current_time()
        print(f"[Agent回复]: 现在的时间是 {current_time}。")
        
    elif "待办" in user_input or "记录" in user_input:
        task_content = user_input.replace("记录待办", "").replace("帮我", "").replace("记录", "").replace("待办", "").strip()
        if task_content:
            result = write_todo_to_file(task_content)
            print(f"[Agent回复]: 执行操作 `write_todo_to_file`。{result} 内容是：{task_content}")
        else:
            print("[Agent回复]: 请告诉我具体要记录什么待办事项哦。")
            
    else:
         print("[Agent回复]: 抱歉，我目前只能帮你查询时间或记录待办事项。")

# --- 自动演示开始 ---
print("=== 欢迎使用本地极简办公智能助手 ===")
print("Agent: 你好，我是你的本地助手。你可以问我时间，或者让我帮你记录待办。")

# 模拟用户询问时间
run_simulation("现在几点了？")

# 模拟用户记录待办
run_simulation("帮我记录待办：今晚1点前提交软件工程大作业。")

print("\n--- 演示结束 ---")
