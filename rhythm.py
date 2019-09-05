class Song:
    def __init__(self, title, filepath, song_length, bpm, chart):
        self.title = title
        self.filepath = filepath
        self.song_length = song_length
        self.bpm = bpm
        self.chart = chart

    def songLen(self):
        return str(self.song_length/60) + ":" + str(self.song_length%60)

class Chart:
    def __init__(self, filepath, bpm):
        self.chart = {}
        self.chart_len = 0
        self.notes = 0
        self.load_chart(filepath)
        self.chart_len = self.chart_len - 1
        self.bpm = bpm

    def get_notes(self, pos):
        return self.chart[pos]

    def load_chart(self, filepath):
        pos = 0
        with open(filepath) as f:
            ftext = f.read().splitlines()
            for line in ftext:
                self.chart_len = self.chart_len + 1
                if(line.rstrip('\n') != "-"):
                    self.notes = self.notes + 1
                    fnotes = line.rstrip('\n').split("*")
                    notelist = []
                    for note in fnotes:
                        fvals = note.lstrip("{").rstrip("}").split(",")
                        my_note = Note(fvals[0], int(fvals[1]), int(fvals[2]))
                        notelist.append(my_note)
                    self.chart[pos] = notelist
                else:
                    self.chart[pos] = "-"
                pos = pos+1


class Note:
    def __init__(self, button, pos_x, pos_y, delay=0, hold_type='S'):
        self.button = button
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.status = 0
        self.delay = delay #Currently unused, but in the future can be used for non-quarter notes
        self.hold_type = hold_type #Currently unused, but in the future can be used for hold notes
        self.radius = 0

class Result:
    def __init__(self, result, status, pos_x, pos_y):
        self.result = result
        self.status = status
        self.pos_x = pos_x
        self.pos_y = pos_y
