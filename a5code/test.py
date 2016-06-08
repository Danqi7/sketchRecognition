import StrokeHmm

if __name__ == '__main__':
    sl = StrokeHmm.StrokeLabeler()
    fname = "../trainingFiles/0128_1.7.1.labeled.xml"
    st = sl.loadStrokeFile(fname)
    sl.trainHMMDir("../trainingFiles/")
    st = sl.loadLabeledFile(fname)
    sl.labelStrokes(st[0])
