import tkinter as tk
from tkinter import messagebox
from collections import Counter



def find_result(dictionary):
    rank_values = list(dictionary.values()) # 각 분야에서 나온 점수들을 내림차순으로 정렬할 리스트
    rank_values.sort(reverse = 1)
    rank_keys = [] # 각 분야명을 values의 내림차순으로(점수가 높은 순서대로) 정렬할 리스트
    
    for i in range(len(rank_values)):
        for key in dictionary:
            if dictionary[key] == rank_values[i]:
                rank_keys.append(key)
                del dictionary[key]
                break
    return rank_keys





class Main:
    def __init__(self):
        self.menu = tk.Tk()
        self.menu.title('메뉴')
        self.menu.geometry('300x200')

        self.subtitle = tk.Label(self.menu, text = '작업을 선택하세요.').pack()
        self.btnSurvey = tk.Button(self.menu, text = "프로그램 시작하기", command = self.survey).pack()
        self.btnResult = tk.Button(self.menu, text = "통계", command = self.result).pack()
        
        self.menu.mainloop()

    def survey(self):
        self.menu.destroy()
        app = SurveyApp(self)

    def result(self):
        self.menu.destroy()
        app = result()



class SurveyApp:
    def __init__(self, main):
        self.root = tk.Tk()
        self.root.title("선택지 프로그램")
        self.root.geometry('300x200')
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
        
        self.question_label = tk.Label(self.root, text=self.questions[self.current_question_index]["question"])
        self.question_label.pack(pady=10)
        
        self.option_var = tk.StringVar()
        self.option_var.set(next(iter(self.questions[self.current_question_index]["options"])))
        
        self.option_menu = tk.OptionMenu(self.root, self.option_var, *self.questions[self.current_question_index]["options"].keys())
        self.option_menu.pack(pady=5)
        
        self.submit_button = tk.Button(self.root, text="제출", command=self.submit_answer)
        self.submit_button.pack(pady=5)

        self.root.mainloop()
    
    def submit_answer(self):
        self.user_answers.append(self.option_var.get())
        
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            self.show_next_question()
        else:
            messagebox.showinfo("결과", f"가장 어울리는 전공은 : {self.get_most_common_info()}")
            self.root.destroy()
            main = Main()
    
    def show_next_question(self):
        self.question_label.config(text=self.questions[self.current_question_index]["question"])
        self.option_var.set(next(iter(self.questions[self.current_question_index]["options"])))
    
    def get_most_common_info(self):
        all_info = ["반도체/디스플레이", "통신", "회로", "소프트웨어"]
        default_num = 0
        for answer in self.user_answers:
            all_info.extend(self.questions[default_num]["options"][answer])
            default_num += 1

        info_counter = dict(Counter(all_info))
        finalResult = find_result(info_counter)
        self.dataSave(finalResult)
       
        return finalResult[0]

    def dataSave(self, result):
        save = open('savedata.bin', 'a')
        for i in result:
            save.write(i + ' ')
        save.write('\n')
        save.close()

class result:
    def __init__(self):
        
        savedata = open('savedata.bin', 'r')
        load = savedata.read().split('\n')
        load = load[:-1]
        savedata.close()
    
        rank = [[], [], [], []]

        for i in load:
            temp = i.split(' ')
            for j in range(4):
                rank[j].append(temp[j])
                
#=================================================================#
        self.board = tk.Tk()
    
        sub0 = rank[0].count('반도체/디스플레이')
        sub1 = rank[0].count('통신')
        sub2 = rank[0].count('회로')
        sub3 = rank[0].count('소프트웨어')

        name0 = tk.Label(self.board, text = '반도체/디스플레이').grid(row = 0, column = 0)
        name1 = tk.Label(self.board, text = '통신').grid(row = 0, column = 1)
        name2 = tk.Label(self.board, text = '회로').grid(row = 0, column = 2)
        name3 = tk.Label(self.board, text = '소프트웨어').grid(row = 0, column = 3)

        show0 = tk.Label(self.board, text = str(sub0)).grid(row = 1, column = 0)
        show1 = tk.Label(self.board, text = str(sub1)).grid(row = 1, column = 1)
        show2 = tk.Label(self.board, text = str(sub2)).grid(row = 1, column = 2)
        show3 = tk.Label(self.board, text = str(sub3)).grid(row = 1, column = 3)

        returnbutton = tk.Button(self.board, text = '돌아가기', command=self.back).grid(row = 2, column = 1)

        savedata.close()
#=================================================================#

    def back(self):
        self.board.destroy()
        main = Main()


main = Main()
