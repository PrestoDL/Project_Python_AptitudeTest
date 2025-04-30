import tkinter as tk
import time
import matplotlib.pyplot as plt
from tkinter import messagebox
from collections import Counter
from tkinter import font



def find_result(dictionary): #이함수를 쓰면 높은 점수의 분야순서대로 딕셔너리 리턴
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

        self.subtitle = tk.Label(self.menu, text = '작업을 선택하세요.').pack(pady=10)
        self.btnSurvey = tk.Button(self.menu, text = "프로그램 시작하기", command = self.survey).pack()
        self.btnResult = tk.Button(self.menu, text = "통계", command = self.result).pack()
        self.btnMajor = tk.Button(self.menu, text = "전공 정보", command = self.major).pack()
        self.menu.mainloop()

    def survey(self):
        self.menu.destroy()
        app = SurveyApp(self,questions_list)

    def result(self):
        app = result()

    def major(self):
        self.menu.destroy()
        app = ShowMajor()


class SurveyApp:
    def __init__(self, main,questions_list):

        self.user_answers = []                          #선택지식 답변들
        self.user_subj_game = []                        #과목 및 게임으로 얻은 답변들
        self.questions = questions_list                 #선택지식 질문들은 외부로 빼서 가독성 좋게 만듦
        
        self.Circuit_Design = 0
        self.Semiconduct_Display = 0
        self.Communication = 0
        self.Software = 0

        self.Question_subject()


    # =================================================Question(과목,게임,선택지) ==================================================== #        

    def Question_subject(self):                         #과목 질문
        self.subj = tk.Tk()
        self.subj.title("선호과목 선택")
        self.subj.geometry('450x400')
        self.font = tk.font.Font(family="맑은 고딕", size=13)
        self.prefer_sub = tk.Label(text = "선호하는 과목들을 모두 고르시오.",font = self.font)
        self.prefer_sub.place(x=80)

        self.a = tk.IntVar(); self.b = tk.IntVar(); self.c = tk.IntVar()
        self.d = tk.IntVar(); self.e = tk.IntVar(); self.f = tk.IntVar()
        self.g = tk.IntVar(); self.h = tk.IntVar(); self.i = tk.IntVar()


        self.circuit=tk.Checkbutton(self.subj, text="회로이론,전자회로",variable = self.a)      #회로과목 (회설)
        self.circuit.place(x=10, y = 50)
        
        self.se_physics=tk.Checkbutton(self.subj, text="물리전자,전자소자",variable = self.b)   #반도체 물성 (회설,반/디)
        self.se_physics.place(x=250, y = 50 )

        self.sys_com=tk.Checkbutton(self.subj, text="신호 및 시스템, 컴퓨터 구조",variable = self.c)   #시스템 및 통신  (회설,통신)
        self.sys_com.place(x=10, y = 100 )

        self.quantum =tk.Checkbutton(self.subj, text="현대물리학,양자역학",variable = self.d)   #양자역학 (반/디)
        self.quantum.place(x=250, y = 100)

        self.process=tk.Checkbutton(self.subj, text="집적회로 공정설계",variable = self.e)   #공정 및 설계  (반/디)
        self.process.place(x=10, y = 150)

        self.math =tk.Checkbutton(self.subj, text="선형대수,이산수학",variable = self.f)   #수학  (통신)
        self.math.place(x=250, y = 150)

        self.programming=tk.Checkbutton(self.subj, text="C언어,Python,Java",variable = self.g)   #프로그래밍  (통신,소프트웨어)
        self.programming.place(x=10, y = 200)

        self.logic=tk.Checkbutton(self.subj, text="논리회로",variable = self.h)   #논리회로  (소프트웨어)
        self.logic.place(x=250, y = 200)

        self.English=tk.Checkbutton(self.subj, text="영어",variable = self.i)   #영어  (소프트웨어)
        self.English.place(x=10, y = 250)

        self.submit_button = tk.Button(self.subj, text="제출", command=self.submit_subject)
        self.submit_button.place(x=170,y=300)
    
        self.subj.mainloop()

    def Questions_game1(self):
        self.start_time = time.time()

        text1 =  """ 
        ==============================================================================
        0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        0000000000000000000000000000000000000000000000000000008000000000000000000000000000000000
        0000000000000000008000000000000000000000000000000000000000000000000000000000008000000000
        0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        0000000000000000000000000000000000000000000000000030000000000000000000000000000000000000
        0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        0000000000000008000000000000000000000000000000000000000000000000000000000000000000000000
        0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        0000000000000000000000000000000000000000000000800000000000000000000000000000000000000000
        0000000000800000000000000000000000000000000000000000000000000000000000000000000000000000
        0000000300000000000000000000000000000000000000000000000080000000000000000000000000000000
        0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        =============================================================================="""
    
        self.game1 = tk.Tk()
        self.game1.title("Game1")
        self.game1.geometry('1000x500')

        self.font = tk.font.Font(family="맑은 고딕", size=12)
        self.game1_question = tk.Label(self.game1,text = "다음 숫자들 중 0이 아닌 숫자의 갯수를 입력하시오 (45초)",font = self.font)
        self.game1_question.pack()

        self.game1_text = tk.Label(self.game1,text = text1)
        self.game1_text.pack(pady = 10)

        self.game1_sol = tk.Entry(self.game1,width = 3)
        self.game1_sol.pack(pady = 10)
        
        self.submit_button = tk.Button(self.game1, text="제출", command = self.submit_game1)
        self.submit_button.pack()

        self.game1.mainloop()

    def Questions_game2(self):

        text2 = """ 
                ______ random
                random_number = random._______(1,100)
                game_count = 1
                while True:
                    try:
                        my_number = int(input('1부터 100까지의 숫자를 입력하시오: '))
                        if my_number > random_number:
                            print('down')
                        elif my_number < random_number:
                            print('up')
                        elif my_number == random_number:
                            print('정답입니다.({}회 도전)'.format(game_count)
                            _____
                    except:
                        print('범위 안의 수를 입력하시오.')
               """

        self.game2 = tk.Tk()
        self.game2.title("Game2")
        self.game2.geometry('1000x500')

        self.font = tk.font.Font(family="맑은 고딕", size=12)
        self.game2_question = tk.Label(self.game2, text="숫자 맞추는 게임의 코드를 작성하시오.(빈칸 채우기) ", font=self.font)
        self.game2_question.pack()

        self.game2_text = tk.Label(self.game2, text=text2, justify='left')
        self.game2_text.pack()

        self.game2_sol1 = tk.Entry(self.game2, width=15)
        self.game2_sol1.pack()

        self.game2_sol2 = tk.Entry(self.game2, width=15)
        self.game2_sol2.pack()

        self.game2_sol3 = tk.Entry(self.game2, width=15)
        self.game2_sol3.pack()

        self.submit_button = tk.Button(self.game2, text="제출", command=self.submit_game2)
        self.submit_button.pack()

        self.game2.mainloop()

    def Questions_survey(self):                                        #선택지식 질문
        self.root = tk.Tk()
        self.root.title("선택지 프로그램")
        self.root.geometry('600x200')

        self.current_question_index = 0

        self.font = tk.font.Font(family="맑은 고딕", size=11)
        self.question_label = tk.Label(self.root, text=self.questions[self.current_question_index]["question"],font=self.font)
        self.question_label.pack(pady=13)
        
        self.option_var = tk.StringVar()                                                                        
        self.option_var.set(next(iter(self.questions[self.current_question_index]["options"])))


        self.sel1 = tk.Radiobutton(self.root,text = "그렇다" , value = "그렇다",variable = self.option_var)     
        self.sel1.pack()

        self.sel2 = tk.Radiobutton(self.root,text = "보통이다" , value = "보통이다",variable = self.option_var)
        self.sel2.pack()

        self.sel3 = tk.Radiobutton(self.root,text = "아니다" , value = "아니다",variable = self.option_var)    
        self.sel3.pack()            
            
        
        self.submit_button = tk.Button(self.root, text="제출", command=self.submit_answer)
        self.submit_button.pack(pady=5)

        self.root.mainloop()


    # =================================================Submit (과목,게임,선택지) ==================================================== #
    
    def submit_subject(self):                                       #과목
        
        self.Circuit_Design += self.a.get()*2 + self.b.get()*2 + self.c.get()*2          #과목별로 최대 6점씩 흭득가능
        self.Semiconduct_Display += self.b.get()*2 + self.d.get()*2 + self.e.get()*2
        self.Communication += self.c.get()*2 + self.f.get()*2 + self.g.get()*2
        self.Software += self.g.get()*2 + self.h.get()*2 + self.i.get()*2
        
        self.subj.destroy()
        self.Questions_game1()


    def submit_game1(self):                                         #game1(꼼꼼함 역량) -> 회로설계, 반/디 +

        self.end_time = time.time()
        self.gap = self.end_time - self.start_time
    
        if float(self.game1_sol.get()) == 9:         
            if self.gap < 30:
                self.Circuit_Design += 4
                self.Semiconduct_Display += 4
            elif self.gap < 35:
                self.Circuit_Design += 3
                self.Semiconduct_Display += 3
            elif self.gap <40:
                self.Circuit_Design += 2
                self.Semiconduct_Display += 2
            elif self.gap <45:
                self.Circuit_Design += 1
                self.Semiconduct_Display += 1
        self.game1.destroy()
        self.Questions_game2()

    def submit_game2(self):  # game2 프로그래밍

        if str(self.game2_sol1.get()) == 'import':
            self.Communication += 1
            self.Software += 1
            if str(self.game2_sol2.get()) == 'randint':
                self.Communication += 1
                self.Software += 1
                if str(self.game2_sol3.get()) == 'break':
                    self.Communication += 1
                    self.Software += 1
        else :
            self.Communication += 0
            self.Software += 0
        self.user_subj_game.extend(
            ["회로설계"] * self.Circuit_Design + ["반도체/디스플레이"] * self.Semiconduct_Display + ["통신"] * self.Communication + [
                "소프트웨어"] * self.Software)
        self.game2.destroy()
        self.Questions_survey()

    def submit_answer(self):                                         #선택지
        
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
        all_info = ["반도체/디스플레이", "통신", "회로설계", "소프트웨어"]
        default_num = 0

        all_info.extend(self.user_subj_game)   #게임 및 과목 선택으로 받기
        
        for answer in self.user_answers:       #선택지로 받기
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
        try:
            savedata = open('savedata.bin', 'r')
            load = savedata.read().split('\n')
            load = load[:-1]
            savedata.close()
    
            rank = [[], [], [], []]

            for i in load:
                temp = i.split(' ')
                for j in range(4):
                    rank[j].append(temp[j])

            subName = ['반도체/디스플레이', '통신', '회로설계', '소프트웨어']; maxName = []
            subScore = []; maxScore = []

            for i in subName:
                subScore.append(rank[0].count(i) * 10 + 
                                rank[1].count(i) * 6 + 
                                rank[2].count(i) * 3 + 
                                rank[3].count(i) * 1)

            while(max(subScore) != 0):
                for i in range(4):
                    if subScore[i] == max(subScore):
                        maxScore.append(subScore[i])
                        maxName.append(subName[i])
                        subScore[i] = 0
                        break
        
            plt.rcParams['font.family'] = 'Malgun Gothic'
            plt.rcParams['axes.unicode_minus'] = False
            plt.rcParams["font.size"] = 12
            wedgeprops = {'linewidth': 1, 'edgecolor': 'white', 'width':0.4}
            text_props = {'fontsize': 14, 'color': 'white','fontweight':"bold"}

            plt.pie(maxScore,
                    labels = maxName,
                    autopct='%1.1f%%',
                    radius = 1.2,
                    wedgeprops = wedgeprops,
                    pctdistance=0.8,
                    labeldistance=0.95,
                    explode = [0.1, 0, 0, 0])
            plt.text(0,0,'가장 적합한 전공은...\n' + maxName[0], ha='center', va='center', fontsize=16, fontweight='bold', color="blue")
        
            plt.show()

        except:
            self.alart = tk.Tk()
            self.alart.title('알림')
            self.alart.geometry('150x100')

            self.noresult = tk.Label(self.alart, text = '검사 결과가 없습니다.').pack(pady=12)
            self.checkBtn = tk.Button(self.alart, text = "확인", command = self.check).pack()
            self.alart.mainloop()

    def check(self):
        self.alart.destroy()

class ShowMajor:
    def __init__(self):
        self.major_sel = tk.Tk()
        self.major_sel.title("전공 세부 정보")

        self.subtitle = tk.Label(self.major_sel, text =  '전공을 선택하세요.').pack()
        self.btnCir = tk.Button(self.major_sel, text = '회로설계', command = self.Cir).pack()
        self.btnSemi = tk.Button(self.major_sel, text='반도체/디스플레이', command = self.Semi).pack()
        self.btnCommu = tk.Button(self.major_sel, text='통신', command = self.Commu).pack()
        self.btnSW = tk.Button(self.major_sel, text='소프트웨어', command = self.SW).pack()
        self.btnback = tk.Button(self.major_sel, text='돌아가기', command = self.back).pack()


        self.major_sel.mainloop()

    def Cir(self):
        self.cir = tk.Tk()
        cir = '아날로그회로와 디지털집적회로의 설계에 관한 연구를 수행\n연구 분야 : Processing in Memory (PIM)\n\t  System on Chip (SoC)' \
               '\n\t  Computer-aided Design (CAD)\n\t  3-dimensional Integrated Circuits (3D IC)'

        self.cir.title('회로설계')
        self.cir_text = tk.Label(self.cir, text = cir, justify = 'left').pack()

    def Semi(self):
        self.semi = tk.Tk()
        semi = '반도체 재료, 소자 및 집적회로에 관련된 분야를 연구를 수행\n연구 분야 : MEMS/NEMS 기반 센서\n\t  반도체 소자 및 메모리' \
               '\n\t  DRAM\n\t  고성능 화합물 반도체 소자\n\t  초 저전력 TFET\n\t  Flexible (Printed ) Electronics'

        self.semi.title('반도체/디스플레이')
        self.semi_text = tk.Label(self.semi, text = semi, justify = 'left').pack()

    def Commu(self):
        self.commu = tk.Tk()
        commu = '음성 및 영상 신호의 처리 및 부호화 기술 그리고, 정보의 안전한 전달을 위한 정보보호 기술들을 연구 ' \
                '\n연구 분야 : 이동통신 소프트웨어(OMA)\n\t  클라우드 컴퓨팅\n\t  정보보호 \n\t  광대역 유무선통합망(BcN)' \
                '\n\t  인공지능 엣지 컴퓨팅'

        self.commu.title('통신')
        self.commu_text = tk.Label(self.commu, text = commu, justify = 'left').pack()

    def SW(self):
        self.sw = tk.Tk()
        sw = '소프트웨어를 이용한 전반적인 프로그램 개발 연구 ' \
                '\n연구 분야 : 인공지능\n\t  차량용 소프트웨어\n\t  Soft Computing'

        self.sw.title('소프트웨어')
        self.sw_text = tk.Label(self.sw, text = sw, justify = 'left').pack()

    def back(self):
        self.major_sel.destroy()
        Main()

questions_list = [
            {
                "question": "질문 1: 취업 후에도 관련 지식들을 계속해서 배울 것이다.",
                "options": {
                    "그렇다": ["회로설계","소프트웨어"]*2,
                    "보통이다": ["회로설계","소프트웨어"],
                    "아니다": [],
                }
            },
            {
                "question": "질문 2: 돈을 많이 받을 수 있다면 교대근무도 가능하다.",
                "options": {
                    "그렇다": ["반도체/디스플레이"]*2,
                    "보통이다": ["반도체/디스플레이"],
                    "아니다": [],
                }
            },
                        {
                "question": "질문 3: 타인의 의도을 잘 이해하고, 나의 의도 또한 잘 전달한다.",
                "options": {
                    "그렇다": ["회로설계","소프트웨어"]*2,
                    "보통이다": ["회로설계","소프트웨어"],
                    "아니다": [],
                }
            },
            {
                "question": "질문 4: 복잡한 문제를 만나고, 이를 해결하는데 즐거움을 느낀다.",
                "options": {
                    "그렇다": ["회로설계","통신"]*2,
                    "보통이다": ["회로설계","통신"],
                    "아니다": [],
                }
            },
                        {
                "question": "질문 5: 최신기술들을 쉽게 받아들이고, 사용하는 편이다.",
                "options": {
                    "그렇다": ["통신","소프트웨어"]*2,
                    "보통이다": ["통신","소프트웨어"],
                    "아니다": [],
                }
            },
            {
                "question": "질문 6: 현장업무에서사람들을 잘 조율할 수 있다.",
                "options": {
                    "그렇다": ["반도체/디스플레이"]*2,
                    "보통이다": ["반도체/디스플레이"],
                    "아니다": [],
                }
            },
                        {
                "question": "질문 7: 필요하다면 대학원에 진학할 마음이 있다.",
                "options": {
                    "그렇다": ["회로설계","통신"]*2,
                    "보통이다": [],
                    "아니다": ["반도체/디스플레이","소프트웨어"]*2,
                }
            },
            {
                "question": "질문 8: 새로운 일보다는 루틴이 있는 일을 선호한다.",
                "options": {
                    "그렇다": ["반도체/디스플레이"]*2,
                    "보통이다": ["반도체/디스플레이"],
                    "아니다": [],
                }
            },
            {
                "question": "질문 9: TCP/IP, 이더넷, 라우팅, 스위칭등과 같은 네트워크 용어들에대해 알고 있다.",
                "options": {
                    "그렇다": ["통신"]*2,
                    "보통이다": ["통신"],
                    "아니다": [],
                }
            },
            {
                "question": "질문 10: 채널 코딩, 다중화, 복조, 등과 같은 용어들을 알고 있다.",
                "options": {
                    "그렇다": ["통신"]*2,
                    "보통이다": ["통신"],
                    "아니다": [],
                }
            },
            {
                "question": "질문 11: 한번에 해결하지 못한 일들도 끝까지 고민해 해결하는 편이다.",
                "options": {
                    "그렇다": ["소프트웨어"]*2,
                    "보통이다": ["소프트웨어"],
                    "아니다": [],
                }
            },
            {
                "question": "질문 12: 반도체/디스플레이 공정에 관심이 있다.",
                "options": {
                    "그렇다": ["반도체/디스플레이"]*2,
                    "보통이다": ["반도체/디스플레이"],
                    "아니다": [],
                }
            },
            {
                "question": "질문 13: PSPICE,Verilog 같은 회로설계 Tool을 다룰 수 있다.",
                "options": {
                    "그렇다": ["회로설계"]*2,
                    "보통이다": ["회로설계"],
                    "아니다": [],
                }
            }
            # 추가 질문들...
        ]


main = Main()
