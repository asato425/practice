class Subject:
    def __init__(self,name,number_of_units,score,when):
        self.name = name
        self.number_of_units = number_of_units
        self.score = score
        self.when = when
        
    def show(self):
        print(str(self.score)+'点 : '+ self.name+' ('+ str(self.number_of_units) +'単位)')
        
def GPA(list):
        total_num = 0
        count = 0
        for s in list:
            total_num += ((s.score-55)/10) * s.number_of_units
            count += s.number_of_units
        print('GPA : {:.2f}'.format(total_num/count))
        
def GPT(list):
    total_num = 0
    for s in list:
        total_num += ((s.score-55)/10) * s.number_of_units
    print('GPT : {:.2f}'.format(total_num/110))

class Overall_score:
    def __init__(self):
        self.subject_list = []
        self.units = 0
    
    def add_subject(self,subject):
        if isinstance(subject, Subject):
            self.subject_list.append(subject) 
            self.units += subject.number_of_units
        else:
            print("Error: Invalid student object.")
            
    def GPA(self):
        total_num = 0
        for s in self.subject_list:
            total_num += ((s.score-55)/10) * s.number_of_units
        print('通算GPA : {:.2f}'.format(total_num/self.units))
        
    def GPT(self):
        total_num = 0
        for s in self.subject_list:
            total_num += ((s.score-55)/10) * s.number_of_units
        print('通算GPT : {:.2f}'.format((total_num + 7.5)/110)) #7.5は合否科目の分、三単位
    
    def result_all(self):
        sorted_subject_list = sorted(self.subject_list, key=lambda x: x.score,reverse=True)
        print('取得済み単位 : '+ str(self.units) + '単位(合否科目(3)は除く)')
        print()
        total_score = 0
        for s in sorted_subject_list:
            s.show()
            total_score += s.score
        print()
        print('平均点:{:.2f}'.format(total_score/len(sorted_subject_list)))
        self.GPA()
        self.GPT()
        
    def result_quarter(self, inputnum):
        year = inputnum // 10
        quarter = inputnum % 10
        sorted_subject_list = sorted(self.subject_list, key=lambda x: x.score,reverse=True)
        list = []
        unit = 0
        for s in sorted_subject_list:
            if s.when == inputnum:
                list.append(s)
                unit += s.number_of_units
        if unit != 0:
            print(f'{year}年{quarter}Q 取得済み単位 : '+ str(unit) + '単位(合否科目は除く)')
            print()
            total_score = 0
            for s in list:
                total_score += s.score
                s.show()
            print()
            print('平均点 : {:.2f}'.format(total_score/len(list)))
            GPA(list)
            GPT(list)
        else:
            print(f'該当するクオーターはありません:{inputnum}')
        
         
        
overall_score = Overall_score()
overall_score.add_subject(Subject('現代社会論',2,80,21))
overall_score.add_subject(Subject('統計学B',2,90,22))
overall_score.add_subject(Subject('外国語への招待2',1,90,13))
overall_score.add_subject(Subject('スポーツ科学',1,94,14))
overall_score.add_subject(Subject('国際関係論A',1,80,12))

overall_score.add_subject(Subject('TOEIC第1',1,90,11))
overall_score.add_subject(Subject('TOEIC第2',1,87,12))
overall_score.add_subject(Subject('TOEIC第3',1,89,23))
overall_score.add_subject(Subject('TOEIC第4',1,90,24))

overall_score.add_subject(Subject('英語第1',1,87,11))
overall_score.add_subject(Subject('英語第2',1,90,12))
overall_score.add_subject(Subject('英語第3',1,85,13))
overall_score.add_subject(Subject('英語第4',1,85,14))
overall_score.add_subject(Subject('英語第5',1,81,21))
overall_score.add_subject(Subject('英語第6',1,82,22))
overall_score.add_subject(Subject('英語第7',1,89,23))
overall_score.add_subject(Subject('英語第8',1,81,24))

overall_score.add_subject(Subject('スペイン語初級1',1,90,21))
overall_score.add_subject(Subject('スペイン語初級2',1,87,22))
overall_score.add_subject(Subject('スペイン語初級3',1,96,23))
overall_score.add_subject(Subject('スペイン語初級4',1,97,24))

overall_score.add_subject(Subject('健康科学論',1,80,11))

overall_score.add_subject(Subject('線形代数第一',2,85,11))
overall_score.add_subject(Subject('微分積分第一',2,94,12))
overall_score.add_subject(Subject('線形代数第二',2,100,14))
overall_score.add_subject(Subject('線形代数演習第二',1,100,14))
overall_score.add_subject(Subject('微分積分第二',2,99,13))
overall_score.add_subject(Subject('微分積分演習第二',1,84,13))

overall_score.add_subject(Subject('力学基礎1',1,95,11))
overall_score.add_subject(Subject('力学基礎2',1,100,12))
overall_score.add_subject(Subject('電磁気学基礎1',1,100,13))
overall_score.add_subject(Subject('電磁気学基礎2',1,87,14))

overall_score.add_subject(Subject('物理学演習第一',1,88,12))
overall_score.add_subject(Subject('物理学演習第二',1,97,14))
overall_score.add_subject(Subject('物理学実験第一',1,100,13))
overall_score.add_subject(Subject('物理学実験第二',1,92,14))

overall_score.add_subject(Subject('有機化学基礎',1,82,11))
overall_score.add_subject(Subject('無機化学基礎',1,88,12))
overall_score.add_subject(Subject('化学熱力学基礎',1,97,13))
overall_score.add_subject(Subject('量子化学基礎',1,89,14))

overall_score.add_subject(Subject('生命科学基礎第一1',1,71,11))
overall_score.add_subject(Subject('生命科学基礎第一2',1,92,12))

overall_score.add_subject(Subject('情報リテラシー第一',1,98,11))
overall_score.add_subject(Subject('情報リテラシー第一',1,100,12))
overall_score.add_subject(Subject('コンピュータサイエンス第一',1,100,13))
overall_score.add_subject(Subject('コンピュータサイエンス第二',1,96,14))

overall_score.add_subject(Subject('基礎データサイエンスAI',1,88,14))
overall_score.add_subject(Subject('応用基礎データサイエンスAI第一',1,91,21))
overall_score.add_subject(Subject('応用基礎データサイエンスAI第二',1,88,22))

overall_score.add_subject(Subject('科学・技術の創造プロセス【情報理工学院】',1,91,12))
overall_score.add_subject(Subject('情報理工学リテラシー',1,82,11))
overall_score.add_subject(Subject('情報理工学基礎1',1,76,12))
overall_score.add_subject(Subject('情報理工学基礎2',1,91,13))
overall_score.add_subject(Subject('情報理工学基礎3',1,86,14))

overall_score.add_subject(Subject('手続き型プログラミング基礎',3,89,21))
overall_score.add_subject(Subject('手続き型プログラミング発展',3,86,22))
overall_score.add_subject(Subject('関数型プログラミング基礎',2,88,23))
overall_score.add_subject(Subject('オブジェクト指向プログラミング',2,92,24))

overall_score.add_subject(Subject('確率論統計学',2,93,21))
overall_score.add_subject(Subject('経営経済のための統計',2,90,22))
overall_score.add_subject(Subject('確率統計',1,78,24))
overall_score.add_subject(Subject('データ科学基礎',2,96,24))

overall_score.add_subject(Subject('計算基礎論',2,82,21))
overall_score.add_subject(Subject('オートマトンと形式言語',2,95,22))
overall_score.add_subject(Subject('人工知能',2,100,22))
overall_score.add_subject(Subject('論理回路理論',2,93,23))
overall_score.add_subject(Subject('情報論理',2,84,23))
overall_score.add_subject(Subject('アセンブリ言語',2,93,23))
overall_score.add_subject(Subject('機械学習',2,97,24))
overall_score.add_subject(Subject('データ構造とアルゴリズム',2,96,24))


# overall_score.add_subject(Subject('コンピュータ論理設計',3,0,31))
# overall_score.add_subject(Subject('データベース',2,0,31))
# overall_score.add_subject(Subject('コンピュータネットワーク',2,0,31))
# overall_score.add_subject(Subject('数値計算法',2,0,31))
# overall_score.add_subject(Subject('システムプログラミング',2,0,31))
# overall_score.add_subject(Subject('パターン認識',2,0,32))
# overall_score.add_subject(Subject('システム解析',2,0,32))
# overall_score.add_subject(Subject('並列プログラミング',2,0,32))
# overall_score.add_subject(Subject('コンパイラ構成',2,0,32))
# overall_score.add_subject(Subject('生命情報解析',2,0,32))
# overall_score.add_subject(Subject('パターン認識',2,0,32))

            
input = list(input().split(','))
for s in input:
    if s == 'all':  
        overall_score.result_all()
    elif s == 'GPA':
        overall_score.GPA()
    elif s == 'GPT':
        overall_score.GPT()
    elif 11<= int(s) <= 44:
        overall_score.result_quarter(int(s))
