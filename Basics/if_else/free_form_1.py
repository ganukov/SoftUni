import matplotlib.pylab as p

percent = [80, 15, 5, 2, 8]
languages = ["Python", "Java ", "C++ ", "Go ", "JavaScript"]
p.pie(percent, labels=languages)
p.show()
