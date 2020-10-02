from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants





class Intro(Page):


        form_model = 'player'
        form_fields = ['breakpoint1']

        def breakpoint1_error_message(self, value):
                if value != 1386:
                    return "Please enter the correct code or wait until you receive the code "




class Q1(Page):
    form_model = 'player'
    form_fields = ['choice1', 'choice1qv','choice1cred']
    def vars_for_template(self):
        return {'credits': self.player.credits}

  #  def after_all_players_arrive(self):
   #     self.subsession.set_sum_groupdes()
    #    for group in self.subsession.get_groups():
      #      for player in group.get_players():
       #         player.set_maxvote()

class Wait1(WaitPage):


 def after_all_players_arrive(self):
        for group in self.subsession.get_groups():
            for player in group.get_players():
                player.set_credits1()
                player.set_voteqv1()
        self.subsession.update_mv1()
        self.subsession.update_qv1()




class Q1R(Page):
    form_model = 'player'
    def vars_for_template(self):
        return {'voteqv1': self.player.voteqv1,
                'qv1': self.subsession.qv1,
                'mv1': self.subsession.mv1}

class Q2(Page):
    form_model = 'player'
    form_fields = ['choice2', 'choice2qv','choice2cred']
    def vars_for_template(self):
        return {'credits': self.player.credits}

class Wait2(WaitPage):

 def after_all_players_arrive(self):
        for group in self.subsession.get_groups():
            for player in group.get_players():
                player.set_credits2()
                player.set_voteqv2()
        self.subsession.update_mv2()
        self.subsession.update_qv2()

class Q2R(Page):
    form_model = 'player'
    def vars_for_template(self):
        return {'voteqv2': self.player.voteqv2,
                'qv2': self.subsession.qv2,
                'mv2': self.subsession.mv2}

class Q3(Page):
    form_model = 'player'
    form_fields = ['choice3', 'choice3qv','choice3cred']
    def vars_for_template(self):
        return {'credits': self.player.credits}

class Wait3(WaitPage):

 def after_all_players_arrive(self):
        for group in self.subsession.get_groups():
            for player in group.get_players():
                player.set_credits3()
                player.set_voteqv3()
        self.subsession.update_mv3()
        self.subsession.update_qv3()

class Q3R(Page):
    form_model = 'player'
    def vars_for_template(self):
        return {'voteqv3': self.player.voteqv3,
                'qv3': self.subsession.qv3,
                'mv3': self.subsession.mv3}


class Q4(Page):
    form_model = 'player'
    form_fields = ['choice4', 'choice4qv', 'choice4cred']

    def vars_for_template(self):
        return {'credits': self.player.credits}


class Wait4(WaitPage):

    def after_all_players_arrive(self):
        for group in self.subsession.get_groups():
            for player in group.get_players():
                player.set_credits4()
                player.set_voteqv4()
        self.subsession.update_mv4()
        self.subsession.update_qv4()


class Q4R(Page):
    form_model = 'player'

    def vars_for_template(self):
        return {'voteqv4': self.player.voteqv4,
                'qv4': self.subsession.qv4,
                'mv4': self.subsession.mv4}


class Q5(Page):
    form_model = 'player'
    form_fields = ['choice5', 'choice5qv', 'choice5cred']

    def vars_for_template(self):
        return {'credits': self.player.credits}


class Wait5(WaitPage):

    def after_all_players_arrive(self):
        for group in self.subsession.get_groups():
            for player in group.get_players():
                player.set_credits5()
                player.set_voteqv5()
        self.subsession.update_mv5()
        self.subsession.update_qv5()


class Q5R(Page):
    form_model = 'player'

    def vars_for_template(self):
        return {'voteqv5': self.player.voteqv5,
                'qv5': self.subsession.qv5,
                'mv5': self.subsession.mv5}

class Q6(Page):
    form_model = 'player'
    form_fields = ['choice6', 'choice6qv','choice6cred']
    def vars_for_template(self):
        return {'credits': self.player.credits}

class Wait6(WaitPage):

 def after_all_players_arrive(self):
        for group in self.subsession.get_groups():
            for player in group.get_players():
                player.set_credits6()
                player.set_voteqv6()
        self.subsession.update_mv6()
        self.subsession.update_qv6()

class Q6R(Page):
    form_model = 'player'
    def vars_for_template(self):
        return {'voteqv6': self.player.voteqv6,
                'qv6': self.subsession.qv6,
                'mv6': self.subsession.mv6}


class Q7(Page):
    form_model = 'player'
    form_fields = ['choice7', 'choice7qv', 'choice7cred']

    def vars_for_template(self):
        return {'credits': self.player.credits}


class Wait7(WaitPage):

    def after_all_players_arrive(self):
        for group in self.subsession.get_groups():
            for player in group.get_players():
                player.set_credits7()
                player.set_voteqv7()
        self.subsession.update_mv7()
        self.subsession.update_qv7()


class Q7R(Page):
    form_model = 'player'

    def vars_for_template(self):
        return {'voteqv7': self.player.voteqv7,
                'qv7': self.subsession.qv7,
                'mv7': self.subsession.mv7}


class Q8(Page):
    form_model = 'player'
    form_fields = ['choice8', 'choice8qv', 'choice8cred']

    def vars_for_template(self):
        return {'credits': self.player.credits}


class Wait8(WaitPage):

    def after_all_players_arrive(self):
        for group in self.subsession.get_groups():
            for player in group.get_players():
                player.set_credits8()
                player.set_voteqv8()
        self.subsession.update_mv8()
        self.subsession.update_qv8()


class Q8R(Page):
    form_model = 'player'

    def vars_for_template(self):
        return {'voteqv8': self.player.voteqv8,
                'qv8': self.subsession.qv8,
                'mv8': self.subsession.mv8}

class Q9(Page):
    form_model = 'player'
    form_fields = ['choice9', 'choice9qv','choice9cred']
    def vars_for_template(self):
        return {'credits': self.player.credits}

class Wait9(WaitPage):

 def after_all_players_arrive(self):
        for group in self.subsession.get_groups():
            for player in group.get_players():
                player.set_credits9()
                player.set_voteqv9()
        self.subsession.update_mv9()
        self.subsession.update_qv9()

class Q9R(Page):
    form_model = 'player'
    def vars_for_template(self):
        return {'voteqv9': self.player.voteqv9,
                'qv9': self.subsession.qv9,
                'mv9': self.subsession.mv9}


class Q10(Page):
    form_model = 'player'
    form_fields = ['choice10', 'choice10qv', 'choice10cred']

    def vars_for_template(self):
        return {'credits': self.player.credits}


class Wait10(WaitPage):

    def after_all_players_arrive(self):
        for group in self.subsession.get_groups():
            for player in group.get_players():
                player.set_credits10()
                player.set_voteqv10()
        self.subsession.update_mv10()
        self.subsession.update_qv10()


class Q10R(Page):
    form_model = 'player'

    def vars_for_template(self):
        return {'voteqv10': self.player.voteqv10,
                'qv10': self.subsession.qv10,
                'mv10': self.subsession.mv10}


class Q11(Page):
    form_model = 'player'
    form_fields = ['choice11', 'choice11qv', 'choice11cred']

    def vars_for_template(self):
        return {'credits': self.player.credits}


class Wait11(WaitPage):

    def after_all_players_arrive(self):
        for group in self.subsession.get_groups():
            for player in group.get_players():
                player.set_credits11()
                player.set_voteqv11()
        self.subsession.update_mv11()
        self.subsession.update_qv11()


class Q11R(Page):
    form_model = 'player'

    def vars_for_template(self):
        return {'voteqv11': self.player.voteqv11,
                'qv11': self.subsession.qv11,
                'mv11': self.subsession.mv11}

class Q12(Page):
    form_model = 'player'
    form_fields = ['choice12', 'choice12qv','choice12cred']
    def vars_for_template(self):
        return {'credits': self.player.credits}

class Wait12(WaitPage):

 def after_all_players_arrive(self):
        for group in self.subsession.get_groups():
            for player in group.get_players():
                player.set_credits12()
                player.set_voteqv12()
        self.subsession.update_mv12()
        self.subsession.update_qv12()

class Q12R(Page):
    form_model = 'player'
    def vars_for_template(self):
        return {'voteqv12': self.player.voteqv12,
                'qv12': self.subsession.qv12,
                'mv12': self.subsession.mv12}


class Q13(Page):
    form_model = 'player'
    form_fields = ['choice13', 'choice13qv', 'choice13cred']

    def vars_for_template(self):
        return {'credits': self.player.credits}


class Wait13(WaitPage):

    def after_all_players_arrive(self):
        for group in self.subsession.get_groups():
            for player in group.get_players():
                player.set_credits13()
                player.set_voteqv13()
        self.subsession.update_mv13()
        self.subsession.update_qv13()


class Q13R(Page):
    form_model = 'player'

    def vars_for_template(self):
        return {'voteqv13': self.player.voteqv13,
                'qv13': self.subsession.qv13,
                'mv13': self.subsession.mv13}


class Q14(Page):
    form_model = 'player'
    form_fields = ['choice14', 'choice14qv', 'choice14cred']

    def vars_for_template(self):
        return {'credits': self.player.credits}


class Wait14(WaitPage):

    def after_all_players_arrive(self):
        for group in self.subsession.get_groups():
            for player in group.get_players():
                player.set_credits14()
                player.set_voteqv14()
        self.subsession.update_mv14()
        self.subsession.update_qv14()


class Q14R(Page):
    form_model = 'player'

    def vars_for_template(self):
        return {'voteqv14': self.player.voteqv14,
                'qv14': self.subsession.qv14,
                'mv14': self.subsession.mv14}
    
class Q15(Page):
    form_model = 'player'
    form_fields = ['choice15', 'choice15qv', 'choice15cred']

    def vars_for_template(self):
        return {'credits': self.player.credits}


class Wait15(WaitPage):

    def after_all_players_arrive(self):
        for group in self.subsession.get_groups():
            for player in group.get_players():
                player.set_credits15()
                player.set_voteqv15()
        self.subsession.update_mv15()
        self.subsession.update_qv15()


class Q15R(Page):
    form_model = 'player'

    def vars_for_template(self):
        return {'voteqv15': self.player.voteqv15,
                'qv15': self.subsession.qv15,
                'mv15': self.subsession.mv15}


class Q16(Page):
    form_model = 'player'
    form_fields = ['choice16', 'choice16qv', 'choice16cred']

    def vars_for_template(self):
        return {'credits': self.player.credits}


class Wait16(WaitPage):

    def after_all_players_arrive(self):
        for group in self.subsession.get_groups():
            for player in group.get_players():
                player.set_credits16()
                player.set_voteqv16()
        self.subsession.update_mv16()
        self.subsession.update_qv16()


class Q16R(Page):
    form_model = 'player'

    def vars_for_template(self):
        return {'voteqv16': self.player.voteqv16,
                'qv16': self.subsession.qv16,
                'mv16': self.subsession.mv16}

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass








page_sequence = [Intro,
                 Q1,
                 Wait1,
                 Q1R,
                 Q2,
                 Wait2,
                 Q2R,
                 Q3,
                 Wait3,
                 Q3R,
                 Q4,
                 Wait4,
                 Q4R,
                 Q5,
                 Wait5,
                 Q5R,
                 Q6,
                 Wait6,
                 Q6R,
                 Q7,
                 Wait7,
                 Q7R,
                 Q8,
                 Wait8,
                 Q8R,
                 Q9,
                 Wait9,
                 Q9R,
                 Q10,
                 Wait10,
                 Q10R,
                 Q11,
                 Wait11,
                 Q11R,
                 Q12,
                 Wait12,
                 Q12R,
                 Q13,
                 Wait13,
                 Q13R,
                 Q14,
                 Wait14,
                 Q14R,
                 Q15,
                 Wait15,
                 Q15R,
                 Q16,
                 Wait16,
                 Q16R,
                 Results,
                 ]
