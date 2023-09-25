class Score:
    def __init__(self, score, score_widget, best_score_widget):
        self.score = score
        self.score_widget = score_widget
        self.best_score_widget = best_score_widget
    
    def get_score(self):
        self.score_widget.configure(text = str(self.score))

        if int(self.score_widget['text']) > int(self.best_score_widget['text']):
            self.best_score_widget.configure(text = str(self.score))