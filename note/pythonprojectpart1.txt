import tkinter as tk
from tkinter import messagebox
from collections import Counter

def find_max_key(dictionary, priority):
    max_value = float('-inf')
    max_keys = []

    for key, value in dictionary.items():
        if value > max_value:
            max_value = value
            max_keys = [key]
        elif value == max_value:
            max_keys.append(key)

    for key in priority:
        if key in max_keys:
            return key

    return max_keys[0] if max_keys else None

class SurveyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("선택지 프로그램")
        self.questions = [
            {
                "question": "질문 1: 선택지 1",
                "options": {
                    "옵션 1": ["반도체/디스플레이"],
                    "옵션 2": ["통신", "회로"],
                    "옵션 3": ["소프트웨어"],
                }
            },
            {
                "question": "질문 2: 선택지 2",
                "options": {
                    "옵션 1": ["소프트웨어"],
                    "옵션 2": ["반도체/디스플레이", "통신"],
                    "옵션 3": ["회로"],
                }
            }
            # 추가 질문들...
        ]
        
        self.current_question_index = 0
        self.user_answers = []
        
        self.question_label = tk.Label(root, text=self.questions[self.current_question_index]["question"])
        self.question_label.pack(pady=10)
        
        self.option_var = tk.StringVar()
        self.option_var.set(next(iter(self.questions[self.current_question_index]["options"])))
        
        self.option_menu = tk.OptionMenu(root, self.option_var, *self.questions[self.current_question_index]["options"].keys())
        self.option_menu.pack(pady=5)
        
        self.submit_button = tk.Button(root, text="제출", command=self.submit_answer)
        self.submit_button.pack(pady=5)
    
    def submit_answer(self):
        selected_option = self.option_var.get()
        self.user_answers.append(selected_option)
        
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            self.show_next_question()
        else:
            result = self.get_most_common_info()
            messagebox.showinfo("결과", f"가장 어울리는 전공은 : {result}")
            self.root.quit()
    
    def show_next_question(self):
        self.question_label.config(text=self.questions[self.current_question_index]["question"])
        self.option_var.set(next(iter(self.questions[self.current_question_index]["options"])))
    
    def get_most_common_info(self):
        all_info = []
        default_num = 0
        for answer in self.user_answers:
            all_info.extend(self.questions[default_num]["options"][answer])
            default_num += 1
        info_counter = dict(Counter(all_info))
        priority_dict = {'반도체/디스플레이' : 1, '회로' : 2, '통신' : 3, '소프트웨어' : 4}
        most_common_info = find_max_key(info_counter, priority_dict)
       
        return most_common_info

root = tk.Tk()
app = SurveyApp(root)
root.mainloop()
