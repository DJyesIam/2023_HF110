import datetime



class Hospital_pkg():

    def __init__(self, text):
        self.input_text = text

    def text_analysis(self, srv_type):

        if srv_type == 'location' :
            if '외과' in self.input_text or '내과' in self.input_text or '편의점' in self.input_text :
                if '외과' in self.input_text: return '외과는 2층 입니다.'
                if '내과' in self.input_text: return '내과는 3층 입니다.'
                if '편의점' in self.input_text: return '편의점은 지하 1층 입니다.'
            else: return '원하시는 위치를 찾지 못 하였습니다.'

        if srv_type == 'administration' :
            if '접수' in self.input_text or '수납' in self.input_text :
                if '접수' in self.input_text: return '접수는 1층으로 가셔야 합니다. 번호표를 뽑고 대기하시면 됩니다.'
                if '수납' in self.input_text: return '수납은 1층으로 가셔야 합니다. 무인수납기를 이용해 주세요.'
            else : return '원하시는 서비스를 찾지 못 하였습니다.'

        if srv_type == 'meal' :
            if '양식' in self.input_text or '한식' in self.input_text :

                if '양식' in self.input_text:
                    self.meal_list('양식')
                    return '양식으로 접수 되었습니다.'

                if '한식' in self.input_text:
                    self.meal_list('한식')
                    return '한식으로 접수 되었습니다.'

            else : return '원하시는 메뉴를 찾지 못 하였습니다. 다시 한번 말씀해 주세요'

    def meal_list(self, meal):

        self.now = datetime.datetime.now()

        file_name = "/home/junha/23_HF110/junha_ws/Meal_list/Meal_list_" + self.now.strftime("%Y%m%d") + ".txt"
        # 식사 리스트 저장경로 역시 각자의 컴퓨터에 맞게 지정해야 함.
        # "/home/[이름]/23_HF110/junha_ws/Meal_list/Meal_list_" + self.now.strftime("%Y%m%d") + ".txt"

        with open(file_name, 'a') as file:
            file.write(self.now.strftime("%H시 %M분 %S초") + " : " + meal + "\n")
