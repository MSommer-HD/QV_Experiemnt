from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import math
from django.core.validators import MaxValueValidator, MinValueValidator
author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'qv'
    players_per_group = None
    num_rounds = 1



class Subsession(BaseSubsession):
    mv1 = models.IntegerField()
    qv1 = models.IntegerField()
    mv2 = models.IntegerField()
    qv2 = models.IntegerField()
    mv3 = models.IntegerField()
    qv3 = models.IntegerField()
    mv4 = models.IntegerField()
    qv4 = models.IntegerField()
    mv5 = models.IntegerField()
    qv5 = models.IntegerField()
    mv6 = models.IntegerField()
    qv6 = models.IntegerField()
    mv7 = models.IntegerField()
    qv7 = models.IntegerField()
    mv8 = models.IntegerField()
    qv8 = models.IntegerField()
    mv9 = models.IntegerField()
    qv9 = models.IntegerField()
    mv10 = models.IntegerField()
    qv10 = models.IntegerField()
    mv11 = models.IntegerField()
    qv11 = models.IntegerField()
    mv12 = models.IntegerField()
    qv12 = models.IntegerField()
    mv13 = models.IntegerField()
    qv13 = models.IntegerField()
    mv14 = models.IntegerField()
    qv14 = models.IntegerField()
    mv15 = models.IntegerField()
    qv15 = models.IntegerField()
    mv16 = models.IntegerField()
    qv16 = models.IntegerField()

    def update_mv1(self):
        if sum([p.choice1 for p in self.get_players() if p.choice1 == 1]) > sum(
                [p.choice1 for p in self.get_players() if p.choice1 == 2]) / 2:
            mv1 = 1
        elif sum([p.choice1 for p in self.get_players() if p.choice1 == 1]) < sum(
                [p.choice1 for p in self.get_players() if p.choice1 == 2]) / 2:
            mv1 = 2
        else:
            mv1 = 0
        self.mv1 = mv1

    def update_qv1(self):
        if sum([p.voteqv1 for p in self.get_players() if p.choice1qv == 1]) > sum(
                [p.voteqv1 for p in self.get_players() if p.choice1qv == 2]) / 2:
            qv1 = 1
        elif sum([p.voteqv1 for p in self.get_players() if p.choice1qv == 1]) < sum(
                [p.voteqv1 for p in self.get_players() if p.choice1qv == 2]) / 2:
            qv1 = 2
        else:
            qv1 = 0
        self.qv1 = qv1

    def update_mv2(self):
        if sum([p.choice2 for p in self.get_players() if p.choice2 == 1]) > sum(
                [p.choice2 for p in self.get_players() if p.choice2 == 2]) / 2:
            mv2 = 1
        elif sum([p.choice2 for p in self.get_players() if p.choice2 == 1]) < sum(
                [p.choice2 for p in self.get_players() if p.choice2 == 2]) / 2:
            mv2 = 2
        else:
            mv2 = 0
        self.mv2 = mv2

    def update_qv2(self):
        if sum([p.voteqv2 for p in self.get_players() if p.choice2qv == 1]) > sum(
                [p.voteqv2 for p in self.get_players() if p.choice2qv == 2]) / 2:
            qv2 = 1
        elif sum([p.voteqv2 for p in self.get_players() if p.choice2qv == 1]) < sum(
                [p.voteqv2 for p in self.get_players() if p.choice2qv == 2]) / 2:
            qv2 = 2
        else:
            qv2 = 0
        self.qv2 = qv2
        
    def update_mv3(self):
        if sum([p.choice3 for p in self.get_players() if p.choice3 == 1]) > sum(
                [p.choice3 for p in self.get_players() if p.choice3 == 2]) / 2:
            mv3 = 1
        elif sum([p.choice3 for p in self.get_players() if p.choice3 == 1]) < sum(
                [p.choice3 for p in self.get_players() if p.choice3 == 2]) / 2:
            mv3 = 2
        else:
            mv3 = 0
        self.mv3 = mv3
        
    def update_qv3(self):
        if sum([p.voteqv3 for p in self.get_players() if p.choice3qv == 1]) > sum(
                [p.voteqv3 for p in self.get_players() if p.choice3qv == 2]) / 2:
            qv3 = 1
        elif sum([p.voteqv3 for p in self.get_players() if p.choice3qv == 1]) < sum(
                [p.voteqv3 for p in self.get_players() if p.choice3qv == 2]) / 2:
            qv3 = 2
        else:
            qv3 = 0
        self.qv3 = qv3
        
    def update_qv4(self):
        if sum([p.voteqv4 for p in self.get_players() if p.choice4qv == 1]) > sum(
                [p.voteqv4 for p in self.get_players() if p.choice4qv == 2]) / 2:
            qv4 = 1
        elif sum([p.voteqv4 for p in self.get_players() if p.choice4qv == 1]) < sum(
                [p.voteqv4 for p in self.get_players() if p.choice4qv == 2]) / 2:
            qv4 = 2
        else:
            qv4 = 0
        self.qv4 = qv4

    def update_mv4(self):
        if sum([p.choice4 for p in self.get_players() if p.choice4 == 1]) > sum(
                [p.choice4 for p in self.get_players() if p.choice4 == 2]) / 2:
            mv4 = 1
        elif sum([p.choice4 for p in self.get_players() if p.choice4 == 1]) < sum(
                [p.choice4 for p in self.get_players() if p.choice4 == 2]) / 2:
            mv4 = 2
        else:
            mv4 = 0
        self.mv4 = mv4

    def update_qv5(self):
        if sum([p.voteqv5 for p in self.get_players() if p.choice5qv == 1]) > sum(
                [p.voteqv5 for p in self.get_players() if p.choice5qv == 2]) / 2:
            qv5 = 1
        elif sum([p.voteqv5 for p in self.get_players() if p.choice5qv == 1]) < sum(
                [p.voteqv5 for p in self.get_players() if p.choice5qv == 2]) / 2:
            qv5 = 2
        else:
            qv5 = 0
        self.qv5 = qv5

    def update_mv5(self):
        if sum([p.choice5 for p in self.get_players() if p.choice5 == 1]) > sum(
                [p.choice5 for p in self.get_players() if p.choice5 == 2]) / 2:
            mv5 = 1
        elif sum([p.choice5 for p in self.get_players() if p.choice5 == 1]) < sum(
                [p.choice5 for p in self.get_players() if p.choice5 == 2]) / 2:
            mv5 = 2
        else:
            mv5 = 0
        self.mv5 = mv5

    def update_qv6(self):
        if sum([p.voteqv6 for p in self.get_players() if p.choice6qv == 1]) > sum(
                [p.voteqv6 for p in self.get_players() if p.choice6qv == 2]) / 2:
            qv6 = 1
        elif sum([p.voteqv6 for p in self.get_players() if p.choice6qv == 1]) < sum(
                [p.voteqv6 for p in self.get_players() if p.choice6qv == 2]) / 2:
            qv6 = 2
        else:
            qv6 = 0
        self.qv6 = qv6

    def update_mv6(self):
        if sum([p.choice6 for p in self.get_players() if p.choice6 == 1]) > sum(
                [p.choice6 for p in self.get_players() if p.choice6 == 2]) / 2:
            mv6 = 1
        elif sum([p.choice6 for p in self.get_players() if p.choice6 == 1]) < sum(
                [p.choice6 for p in self.get_players() if p.choice6 == 2]) / 2:
            mv6 = 2
        else:
            mv6 = 0
        self.mv6 = mv6

    def update_mv7(self):
        if sum([p.choice7 for p in self.get_players() if p.choice7 == 1]) > sum(
                [p.choice7 for p in self.get_players() if p.choice7 == 2]) / 2:
            mv7 = 1
        elif sum([p.choice7 for p in self.get_players() if p.choice7 == 1]) < sum(
                [p.choice7 for p in self.get_players() if p.choice7 == 2]) / 2:
            mv7 = 2
        else:
            mv7 = 0
        self.mv7 = mv7

    def update_qv7(self):
        if sum([p.voteqv7 for p in self.get_players() if p.choice7qv == 1]) > sum(
                [p.voteqv7 for p in self.get_players() if p.choice7qv == 2]) / 2:
            qv7 = 1
        elif sum([p.voteqv7 for p in self.get_players() if p.choice7qv == 1]) < sum(
                [p.voteqv7 for p in self.get_players() if p.choice7qv == 2]) / 2:
            qv7 = 2
        else:
            qv7 = 0
        self.qv7 = qv7

    def update_qv8(self):
        if sum([p.voteqv8 for p in self.get_players() if p.choice8qv == 1]) > sum(
                [p.voteqv8 for p in self.get_players() if p.choice8qv == 2]) / 2:
            qv8 = 1
        elif sum([p.voteqv8 for p in self.get_players() if p.choice8qv == 1]) < sum(
                [p.voteqv8 for p in self.get_players() if p.choice8qv == 2]) / 2:
            qv8 = 2
        else:
            qv8 = 0
        self.qv8 = qv8

    def update_mv8(self):
        if sum([p.choice8 for p in self.get_players() if p.choice8 == 1]) > sum(
                [p.choice8 for p in self.get_players() if p.choice8 == 2]) / 2:
            mv8 = 1
        elif sum([p.choice8 for p in self.get_players() if p.choice8 == 1]) < sum(
                [p.choice8 for p in self.get_players() if p.choice8 == 2]) / 2:
            mv8 = 2
        else:
            mv8 = 0
        self.mv8 = mv8

    def update_qv9(self):
        if sum([p.voteqv9 for p in self.get_players() if p.choice9qv == 1]) > sum(
                [p.voteqv9 for p in self.get_players() if p.choice9qv == 2]) / 2:
            qv9 = 1
        elif sum([p.voteqv9 for p in self.get_players() if p.choice9qv == 1]) < sum(
                [p.voteqv9 for p in self.get_players() if p.choice9qv == 2]) / 2:
            qv9 = 2
        else:
            qv9 = 0
        self.qv9 = qv9

    def update_mv9(self):
        if sum([p.choice9 for p in self.get_players() if p.choice9 == 1]) > sum(
                [p.choice9 for p in self.get_players() if p.choice9 == 2]) / 2:
            mv9 = 1
        elif sum([p.choice9 for p in self.get_players() if p.choice9 == 1]) < sum(
                [p.choice9 for p in self.get_players() if p.choice9 == 2]) / 2:
            mv9 = 2
        else:
            mv9 = 0
        self.mv9 = mv9

    def update_qv10(self):
        if sum([p.voteqv10 for p in self.get_players() if p.choice10qv == 1]) > sum(
                [p.voteqv10 for p in self.get_players() if p.choice10qv == 2]) / 2:
            qv10 = 1
        elif sum([p.voteqv10 for p in self.get_players() if p.choice10qv == 1]) < sum(
                [p.voteqv10 for p in self.get_players() if p.choice10qv == 2]) / 2:
            qv10 = 2
        else:
            qv10 = 0
        self.qv10 = qv10

    def update_mv10(self):
        if sum([p.choice10 for p in self.get_players() if p.choice10 == 1]) > sum(
                [p.choice10 for p in self.get_players() if p.choice10 == 2]) / 2:
            mv10 = 1
        elif sum([p.choice10 for p in self.get_players() if p.choice10 == 1]) < sum(
                [p.choice10 for p in self.get_players() if p.choice10 == 2]) / 2:
            mv10 = 2
        else:
            mv10 = 0
        self.mv10 = mv10
   
    def update_mv11(self):
        if sum([p.choice11 for p in self.get_players() if p.choice11 == 1]) > sum(
                [p.choice11 for p in self.get_players() if p.choice11 == 2]) / 2:
            mv11 = 1
        elif sum([p.choice11 for p in self.get_players() if p.choice11 == 1]) < sum(
                [p.choice11 for p in self.get_players() if p.choice11 == 2]) / 2:
            mv11 = 2
        else:
            mv11 = 0
        self.mv11 = mv11

    def update_qv11(self):
        if sum([p.voteqv11 for p in self.get_players() if p.choice11qv == 1]) > sum(
                [p.voteqv11 for p in self.get_players() if p.choice11qv == 2]) / 2:
            qv11 = 1
        elif sum([p.voteqv11 for p in self.get_players() if p.choice11qv == 1]) < sum(
                [p.voteqv11 for p in self.get_players() if p.choice11qv == 2]) / 2:
            qv11 = 2
        else:
            qv11 = 0
        self.qv11 = qv11

    def update_qv12(self):
        if sum([p.voteqv12 for p in self.get_players() if p.choice12qv == 1]) > sum(
                [p.voteqv12 for p in self.get_players() if p.choice12qv == 2]) / 2:
            qv12 = 1
        elif sum([p.voteqv12 for p in self.get_players() if p.choice12qv == 1]) < sum(
                [p.voteqv12 for p in self.get_players() if p.choice12qv == 2]) / 2:
            qv12 = 2
        else:
            qv12 = 0
        self.qv12 = qv12

    def update_mv12(self):
        if sum([p.choice12 for p in self.get_players() if p.choice12 == 1]) > sum(
                [p.choice12 for p in self.get_players() if p.choice12 == 2]) / 2:
            mv12 = 1
        elif sum([p.choice12 for p in self.get_players() if p.choice12 == 1]) < sum(
                [p.choice12 for p in self.get_players() if p.choice12 == 2]) / 2:
            mv12 = 2
        else:
            mv12 = 0
        self.mv12 = mv12

    def update_qv13(self):
        if sum([p.voteqv13 for p in self.get_players() if p.choice13qv == 1]) > sum(
                [p.voteqv13 for p in self.get_players() if p.choice13qv == 2]) / 2:
            qv13 = 1
        elif sum([p.voteqv13 for p in self.get_players() if p.choice13qv == 1]) < sum(
                [p.voteqv13 for p in self.get_players() if p.choice13qv == 2]) / 2:
            qv13 = 2
        else:
            qv13 = 0
        self.qv13 = qv13

    def update_mv13(self):
        if sum([p.choice13 for p in self.get_players() if p.choice13 == 1]) > sum(
                [p.choice13 for p in self.get_players() if p.choice13 == 2]) / 2:
            mv13 = 1
        elif sum([p.choice13 for p in self.get_players() if p.choice13 == 1]) < sum(
                [p.choice13 for p in self.get_players() if p.choice13 == 2]) / 2:
            mv13 = 2
        else:
            mv13 = 0
        self.mv13 = mv13

    def update_qv14(self):
        if sum([p.voteqv14 for p in self.get_players() if p.choice14qv == 1]) > sum(
                [p.voteqv14 for p in self.get_players() if p.choice14qv == 2]) / 2:
            qv14 = 1
        elif sum([p.voteqv14 for p in self.get_players() if p.choice14qv == 1]) < sum(
                [p.voteqv14 for p in self.get_players() if p.choice14qv == 2]) / 2:
            qv14 = 2
        else:
            qv14 = 0
        self.qv14 = qv14

    def update_mv14(self):
        if sum([p.choice14 for p in self.get_players() if p.choice14 == 1]) > sum(
                [p.choice14 for p in self.get_players() if p.choice14 == 2]) / 2:
            mv14 = 1
        elif sum([p.choice14 for p in self.get_players() if p.choice14 == 1]) < sum(
                [p.choice14 for p in self.get_players() if p.choice14 == 2]) / 2:
            mv14 = 2
        else:
            mv14 = 0
        self.mv14 = mv14

    def update_qv15(self):
        if sum([p.voteqv15 for p in self.get_players() if p.choice15qv == 1]) > sum(
                [p.voteqv15 for p in self.get_players() if p.choice15qv == 2]) / 2:
            qv15 = 1
        elif sum([p.voteqv15 for p in self.get_players() if p.choice15qv == 1]) < sum(
                [p.voteqv15 for p in self.get_players() if p.choice15qv == 2]) / 2:
            qv15 = 2
        else:
            qv15 = 0
        self.qv15 = qv15

    def update_mv15(self):
        if sum([p.choice15 for p in self.get_players() if p.choice15 == 1]) > sum(
                [p.choice15 for p in self.get_players() if p.choice15 == 2]) / 2:
            mv15 = 1
        elif sum([p.choice15 for p in self.get_players() if p.choice15 == 1]) < sum(
                [p.choice15 for p in self.get_players() if p.choice15 == 2]) / 2:
            mv15 = 2
        else:
            mv15 = 0
        self.mv15 = mv15

    def update_qv16(self):
        if sum([p.voteqv16 for p in self.get_players() if p.choice16qv == 1]) > sum(
                [p.voteqv16 for p in self.get_players() if p.choice16qv == 2]) / 2:
            qv16 = 1
        elif sum([p.voteqv16 for p in self.get_players() if p.choice16qv == 1]) < sum(
                [p.voteqv16 for p in self.get_players() if p.choice16qv == 2]) / 2:
            qv16 = 2
        else:
            qv16 = 0
        self.qv16 = qv16

    def update_mv16(self):
        if sum([p.choice16 for p in self.get_players() if p.choice16 == 1]) > sum(
                [p.choice16 for p in self.get_players() if p.choice16 == 2]) / 2:
            mv16 = 1
        elif sum([p.choice16 for p in self.get_players() if p.choice16 == 1]) < sum(
                [p.choice16 for p in self.get_players() if p.choice16 == 2]) / 2:
            mv16 = 2
        else:
            mv16 = 0
        self.mv16 = mv16


class Group(BaseGroup):
    pass
    
class Player(BasePlayer):


    breakpoint1 = models.IntegerField(label='Code:')

    credits = models.IntegerField(initial=20)
           
    voteqv1 = models.IntegerField()

    def set_credits1(self):
        credits = self.credits - (self.choice1cred * self.choice1cred)
        self.credits = credits

    choice1 = models.IntegerField(widget=widgets.RadioSelect(), label='Do you agree or disagree with this statement ?',
                                  choices=[[0, 'Neutral.'],[1, 'Agree.'], [2, 'Disagree.']])

    choice1qv = models.IntegerField(widget=widgets.RadioSelect(), label='Do you agree or disagree with this statement ?',
                                  choices=[[0, 'Neutral.'],[1, 'Agree.'], [2, 'Disagree.']])


    choice1cred = models.IntegerField(min=0, label="How often do you want to vote ?")

    def choice1cred_max(self):
         return math.floor(math.sqrt(self.credits))

    def set_voteqv1(self):
        voteqv1 = self.choice1qv * self.choice1cred
        self.voteqv1 = voteqv1

    voteqv2 = models.IntegerField()

    def set_credits2(self):
        credits = self.credits - (self.choice2cred * self.choice2cred)
        self.credits = credits

    choice2 = models.IntegerField(widget=widgets.RadioSelect(), label='Do you agree or disagree with this statement ?',
                                  choices=[[0, 'Neutral.'],[1, 'Agree.'], [2, 'Disagree.']])

    choice2qv = models.IntegerField(widget=widgets.RadioSelect(), label='Do you agree or disagree with this statement ?',
                                  choices=[[0, 'Neutral.'],[1, 'Agree.'], [2, 'Disagree.']])


    choice2cred = models.IntegerField(min=0, label="How often do you want to vote ?")

    def choice2cred_max(self):
         return math.floor(math.sqrt(self.credits))

    def set_voteqv2(self):
        voteqv2 = self.choice2qv * self.choice2cred
        self.voteqv2 = voteqv2

    voteqv3 = models.IntegerField()

    def set_credits3(self):
        credits = self.credits - (self.choice3cred * self.choice3cred)
        self.credits = credits

    choice3 = models.IntegerField(widget=widgets.RadioSelect(), label='Do you agree or disagree with this statement ?',
                                  choices=[[0, 'Neutral.'],[1, 'Agree.'], [2, 'Disagree.']])

    choice3qv = models.IntegerField(widget=widgets.RadioSelect(), label='Do you agree or disagree with this statement ?',
                                  choices=[[0, 'Neutral.'],[1, 'Agree.'], [2, 'Disagree.']])


    choice3cred = models.IntegerField(min=0, label="How often do you want to vote ?")

    def choice3cred_max(self):
         return math.floor(math.sqrt(self.credits))

    def set_voteqv3(self):
        voteqv3 = self.choice3qv * self.choice3cred
        self.voteqv3 = voteqv3

    voteqv4 = models.IntegerField()

    def set_credits4(self):
        credits = self.credits - (self.choice4cred * self.choice4cred)
        self.credits = credits

    choice4 = models.IntegerField(widget=widgets.RadioSelect(), label='Do you agree or disagree with this statement ?',
                                  choices=[[0, 'Neutral.'],[1, 'Agree.'], [2, 'Disagree.']])

    choice4qv = models.IntegerField(widget=widgets.RadioSelect(), label='Do you agree or disagree with this statement ?',
                                  choices=[[0, 'Neutral.'],[1, 'Agree.'], [2, 'Disagree.']])


    choice4cred = models.IntegerField(min=0, label="How often do you want to vote ?")

    def choice4cred_max(self):
         return math.floor(math.sqrt(self.credits))

    def set_voteqv4(self):
        voteqv4 = self.choice4qv * self.choice4cred
        self.voteqv4 = voteqv4
        
    voteqv5 = models.IntegerField()

    def set_credits5(self):
        credits = self.credits - (self.choice5cred * self.choice5cred)
        self.credits = credits

    choice5 = models.IntegerField(widget=widgets.RadioSelect(), label='Do you agree or disagree with this statement ?',
                                  choices=[[0, 'Neutral.'],[1, 'Agree.'], [2, 'Disagree.']])

    choice5qv = models.IntegerField(widget=widgets.RadioSelect(), label='Do you agree or disagree with this statement ?',
                                  choices=[[0, 'Neutral.'],[1, 'Agree.'], [2, 'Disagree.']])


    choice5cred = models.IntegerField(min=0, label="How often do you want to vote ?")

    def choice5cred_max(self):
         return math.floor(math.sqrt(self.credits))

    def set_voteqv5(self):
        voteqv5 = self.choice5qv * self.choice5cred
        self.voteqv5 = voteqv5

    voteqv6 = models.IntegerField()

    def set_credits6(self):
        credits = self.credits - (self.choice6cred * self.choice6cred)
        self.credits = credits

    choice6 = models.IntegerField(widget=widgets.RadioSelect(), label='Do you agree or disagree with this statement ?',
                                  choices=[[0, 'Neutral.'], [1, 'Agree.'], [2, 'Disagree.']])

    choice6qv = models.IntegerField(widget=widgets.RadioSelect(),
                                    label='Do you agree or disagree with this statement ?',
                                    choices=[[0, 'Neutral.'], [1, 'Agree.'], [2, 'Disagree.']])

    choice6cred = models.IntegerField(min=0, label="How often do you want to vote ?")

    def choice6cred_max(self):
        return math.floor(math.sqrt(self.credits))

    def set_voteqv6(self):
        voteqv6 = self.choice6qv * self.choice6cred
        self.voteqv6 = voteqv6

    voteqv7 = models.IntegerField()

    def set_credits7(self):
        credits = self.credits - (self.choice7cred * self.choice7cred)
        self.credits = credits

    choice7 = models.IntegerField(widget=widgets.RadioSelect(), label='Do you agree or disagree with this statement ?',
                                  choices=[[0, 'Neutral.'], [1, 'Agree.'], [2, 'Disagree.']])

    choice7qv = models.IntegerField(widget=widgets.RadioSelect(),
                                    label='Do you agree or disagree with this statement ?',
                                    choices=[[0, 'Neutral.'], [1, 'Agree.'], [2, 'Disagree.']])

    choice7cred = models.IntegerField(min=0, label="How often do you want to vote ?")

    def choice7cred_max(self):
        return math.floor(math.sqrt(self.credits))

    def set_voteqv7(self):
        voteqv7 = self.choice7qv * self.choice7cred
        self.voteqv7 = voteqv7

    voteqv8 = models.IntegerField()

    def set_credits8(self):
        credits = self.credits - (self.choice8cred * self.choice8cred)
        self.credits = credits

    choice8 = models.IntegerField(widget=widgets.RadioSelect(), label='Do you agree or disagree with this statement ?',
                                  choices=[[0, 'Neutral.'], [1, 'Agree.'], [2, 'Disagree.']])

    choice8qv = models.IntegerField(widget=widgets.RadioSelect(),
                                    label='Do you agree or disagree with this statement ?',
                                    choices=[[0, 'Neutral.'], [1, 'Agree.'], [2, 'Disagree.']])

    choice8cred = models.IntegerField(min=0, label="How often do you want to vote ?")

    def choice8cred_max(self):
        return math.floor(math.sqrt(self.credits))

    def set_voteqv8(self):
        voteqv8 = self.choice8qv * self.choice8cred
        self.voteqv8 = voteqv8
        
    voteqv9 = models.IntegerField()

    def set_credits9(self):
        credits = self.credits - (self.choice9cred * self.choice9cred)
        self.credits = credits

    choice9 = models.IntegerField(widget=widgets.RadioSelect(), label='Do you agree or disagree with this statement ?',
                                  choices=[[0, 'Neutral.'],[1, 'Agree.'], [2, 'Disagree.']])

    choice9qv = models.IntegerField(widget=widgets.RadioSelect(), label='Do you agree or disagree with this statement ?',
                                  choices=[[0, 'Neutral.'],[1, 'Agree.'], [2, 'Disagree.']])


    choice9cred = models.IntegerField(min=0, label="How often do you want to vote ?")

    def choice9cred_max(self):
         return math.floor(math.sqrt(self.credits))

    def set_voteqv9(self):
        voteqv9 = self.choice9qv * self.choice9cred
        self.voteqv9 = voteqv9

    voteqv10 = models.IntegerField()

    def set_credits10(self):
        credits = self.credits - (self.choice10cred * self.choice10cred)
        self.credits = credits

    choice10 = models.IntegerField(widget=widgets.RadioSelect(), label='Do you agree or disagree with this statement ?',
                                  choices=[[0, 'Neutral.'], [1, 'Agree.'], [2, 'Disagree.']])

    choice10qv = models.IntegerField(widget=widgets.RadioSelect(),
                                    label='Do you agree or disagree with this statement ?',
                                    choices=[[0, 'Neutral.'], [1, 'Agree.'], [2, 'Disagree.']])

    choice10cred = models.IntegerField(min=0, label="How often do you want to vote ?")

    def choice10cred_max(self):
        return math.floor(math.sqrt(self.credits))

    def set_voteqv10(self):
        voteqv10 = self.choice10qv * self.choice10cred
        self.voteqv10 = voteqv10

    voteqv11 = models.IntegerField()

    def set_credits11(self):
        credits = self.credits - (self.choice11cred * self.choice11cred)
        self.credits = credits

    choice11 = models.IntegerField(widget=widgets.RadioSelect(), label='Do you agree or disagree with this statement ?',
                                  choices=[[0, 'Neutral.'], [1, 'Agree.'], [2, 'Disagree.']])

    choice11qv = models.IntegerField(widget=widgets.RadioSelect(),
                                    label='Do you agree or disagree with this statement ?',
                                    choices=[[0, 'Neutral.'], [1, 'Agree.'], [2, 'Disagree.']])

    choice11cred = models.IntegerField(min=0, label="How often do you want to vote ?")

    def choice11cred_max(self):
        return math.floor(math.sqrt(self.credits))

    def set_voteqv11(self):
        voteqv11 = self.choice11qv * self.choice11cred
        self.voteqv11 = voteqv11

    voteqv12 = models.IntegerField()

    def set_credits12(self):
        credits = self.credits - (self.choice12cred * self.choice12cred)
        self.credits = credits

    choice12 = models.IntegerField(widget=widgets.RadioSelect(), label='Do you agree or disagree with this statement ?',
                                  choices=[[0, 'Neutral.'], [1, 'Agree.'], [2, 'Disagree.']])

    choice12qv = models.IntegerField(widget=widgets.RadioSelect(),
                                    label='Do you agree or disagree with this statement ?',
                                    choices=[[0, 'Neutral.'], [1, 'Agree.'], [2, 'Disagree.']])

    choice12cred = models.IntegerField(min=0, label="How often do you want to vote ?")

    def choice12cred_max(self):
        return math.floor(math.sqrt(self.credits))

    def set_voteqv12(self):
        voteqv12 = self.choice12qv * self.choice12cred
        self.voteqv12 = voteqv12
        
        
    voteqv13 = models.IntegerField()

    def set_credits13(self):
        credits = self.credits - (self.choice13cred * self.choice13cred)
        self.credits = credits

    choice13 = models.IntegerField(widget=widgets.RadioSelect(), label='Do you agree or disagree with this statement ?',
                                  choices=[[0, 'Neutral.'],[1, 'Agree.'], [2, 'Disagree.']])

    choice13qv = models.IntegerField(widget=widgets.RadioSelect(), label='Do you agree or disagree with this statement ?',
                                  choices=[[0, 'Neutral.'],[1, 'Agree.'], [2, 'Disagree.']])


    choice13cred = models.IntegerField(min=0, label="How often do you want to vote ?")

    def choice13cred_max(self):
         return math.floor(math.sqrt(self.credits))

    def set_voteqv13(self):
        voteqv13 = self.choice13qv * self.choice13cred
        self.voteqv13 = voteqv13

    voteqv14 = models.IntegerField()

    def set_credits14(self):
        credits = self.credits - (self.choice14cred * self.choice14cred)
        self.credits = credits

    choice14 = models.IntegerField(widget=widgets.RadioSelect(), label='Do you agree or disagree with this statement ?',
                                  choices=[[0, 'Neutral.'], [1, 'Agree.'], [2, 'Disagree.']])

    choice14qv = models.IntegerField(widget=widgets.RadioSelect(),
                                    label='Do you agree or disagree with this statement ?',
                                    choices=[[0, 'Neutral.'], [1, 'Agree.'], [2, 'Disagree.']])

    choice14cred = models.IntegerField(min=0, label="How often do you want to vote ?")

    def choice14cred_max(self):
        return math.floor(math.sqrt(self.credits))

    def set_voteqv14(self):
        voteqv14 = self.choice14qv * self.choice14cred
        self.voteqv14 = voteqv14

    voteqv15 = models.IntegerField()

    def set_credits15(self):
        credits = self.credits - (self.choice15cred * self.choice15cred)
        self.credits = credits

    choice15 = models.IntegerField(widget=widgets.RadioSelect(), label='Do you agree or disagree with this statement ?',
                                  choices=[[0, 'Neutral.'], [1, 'Agree.'], [2, 'Disagree.']])

    choice15qv = models.IntegerField(widget=widgets.RadioSelect(),
                                    label='Do you agree or disagree with this statement ?',
                                    choices=[[0, 'Neutral.'], [1, 'Agree.'], [2, 'Disagree.']])

    choice15cred = models.IntegerField(min=0, label="How often do you want to vote ?")

    def choice15cred_max(self):
        return math.floor(math.sqrt(self.credits))

    def set_voteqv15(self):
        voteqv15 = self.choice15qv * self.choice15cred
        self.voteqv15 = voteqv15

    voteqv16 = models.IntegerField()

    def set_credits16(self):
        credits = self.credits - (self.choice16cred * self.choice16cred)
        self.credits = credits

    choice16 = models.IntegerField(widget=widgets.RadioSelect(), label='Do you agree or disagree with this statement ?',
                                  choices=[[0, 'Neutral.'], [1, 'Agree.'], [2, 'Disagree.']])

    choice16qv = models.IntegerField(widget=widgets.RadioSelect(),
                                    label='Do you agree or disagree with this statement ?',
                                    choices=[[0, 'Neutral.'], [1, 'Agree.'], [2, 'Disagree.']])

    choice16cred = models.IntegerField(min=0, label="How often do you want to vote ?")

    def choice16cred_max(self):
        return math.floor(math.sqrt(self.credits))

    def set_voteqv16(self):
        voteqv16 = self.choice16qv * self.choice16cred
        self.voteqv16 = voteqv16