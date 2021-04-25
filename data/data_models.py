from datetime import datetime

class Note:
    def __init__(self, noteid:str='', title:str='', body:str=''):

        self.noteid = noteid
        self.title = title
        self.body = body
        self.created_at = datetime.today()

    def __str__(self):
        return self.title

    def is_note_in_db(self):
        return True if self.noteid is None else False


