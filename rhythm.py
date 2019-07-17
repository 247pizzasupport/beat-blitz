class Song:
    def __init__(self, title, filepath, song_length, bpm, chart):
        self.title = title
        self.filepath = filepath
        self.song_length = song_length
        self.bpm = bpm
        self.chart = chart

#    def print(self):
#        print(str(self.title) + " - " + str(self.song_length) + ", " + str(self.bpm) + " BPM")
#        self.chart.print()

class Chart:
    def __init__(self, filepath, bpm, chart_len):
        self.chart = {}
        self.load_chart(filepath)
        self.chart[-1] = "-"
        self.bpm = bpm
        self.chart_len = chart_len

    def get_notes(self, pos):
        return self.chart[pos]

#    def print(self):
#        for i in range(0,self.chart_len+1):
#            timing = float(i)/float(self.bpm/60)
#            if(type(self.chart[i]) is not str):
#                notestring = ""
#                for note in self.chart[i]:
#                    notestring = notestring + note.getText() + " "
#                print(str(timing) + "s : " + notestring)
#            else:
#                print(str(timing) + "s : -")

    def load_chart(self, filepath):
        pos = 0
        with open(filepath) as f:
            ftext = f.read().splitlines()
            for line in ftext:
                if(line.rstrip('\n') != "-"):
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
    def __init__(self, button, pos_x, pos_y, delay=0):
        self.button = button
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.status = 0
        self.delay = 0
        self.radius = 0

#    def getText(self):
#        return "{" + str(self.button) + ", " + str(self.hold_type) + ", " + str(self.pos_start) + ", " + str(self.pos_end) + "}"
