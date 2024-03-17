import matplotlib.pyplot as plt

def traceB():
    def f(x):
        return - (3 * x + 9)
    fig, ax = plt.subplots()
    xmin, xmax, pas = -10, 10, 0.01
    X = [-10 + pas * i for i in range(2001)]
    Y = [f(x) for x in X]
    print(min(X), max(X))
    ymin, ymax = min(0, min(Y)), max(0, max(Y))
    print(ymin, ymax)
    plt.plot(X, Y)
    plt.arrow(x=xmin-0.5, y=0, dx=(xmax+0.5)-(xmin-0.5), dy=0, width=0.1, color='black',
              head_length=.5, head_width=.6,
              length_includes_head=True)
    plt.text(11.5, -1.5, "x")
    #https://matplotlib.org/stable/gallery/shapes_and_collections/arrow_guide.html
    #https://stackoverflow.com/questions/43378730/how-to-get-an-open-and-scaling-arrow-head-in-matplotlib
    plt.arrow(x=0, y=(ymin-0.5), dx=0, dy=(ymax+0.5)-(ymin-0.5), width=0.05, color='black',
              head_length=1, head_width=.2,
              length_includes_head=True)
    plt.text(11.5, -1.5, "x")
    #https://numerique.ostralo.net/python_matplotlib/2_ElementsGeneraux.htm
    ##plt.xticks([0,3.142,6.283,9.425], [0,'π','2π','3π'], color='r')
    ##plt.yticks([-1,0,1], fontweight='bold')
    plt.xticks([-10+i for i in range(0, 21)], fontsize=8)
    plt.yticks([-20+5*i for i in range(0, 12)], fontsize=8)
    plt.grid(linestyle='--')
    plt.show()

def traceA():
    def f(x):
        return (x - 5) * (3 * x) + 3
    fig, ax = plt.subplots()
    xmin, xmax, pas = -10, 10, 0.01
    X = [-10 + pas * i for i in range(2001)]
    Y = [f(x) for x in X]
    print(min(X), max(X))
    ymin, ymax = min(0, min(Y)), max(0, max(Y))
    print(ymin, ymax)
    plt.plot(X, Y)
    plt.arrow(x=xmin-0.5, y=0, dx=(xmax+0.5)-(xmin-0.5), dy=0, width=0.1, color='black',
              head_length=.5, head_width=.6,
              length_includes_head=True)
    plt.text(11.5, -1.5, "x")
    #https://matplotlib.org/stable/gallery/shapes_and_collections/arrow_guide.html
    #https://stackoverflow.com/questions/43378730/how-to-get-an-open-and-scaling-arrow-head-in-matplotlib
    plt.arrow(x=0, y=(ymin-0.5), dx=0, dy=(ymax+0.5)-(ymin-0.5), width=0.05, color='black',
              head_length=1, head_width=.2,
              length_includes_head=True)
    plt.text(11.5, -1.5, "x")
    #https://numerique.ostralo.net/python_matplotlib/2_ElementsGeneraux.htm
    ##plt.xticks([0,3.142,6.283,9.425], [0,'π','2π','3π'], color='r')
    ##plt.yticks([-1,0,1], fontweight='bold')
    plt.xticks([-10+i for i in range(0, 21)], fontsize=8)
    plt.yticks([0+50*i for i in range(0, 11)], fontsize=8)
    plt.grid(linestyle='--')
    plt.show()

#traceA()
