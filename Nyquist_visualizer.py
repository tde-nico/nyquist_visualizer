from scipy import signal
import matplotlib.pyplot as plt
import tkinter as tkr

display = tkr.Tk()
display.title('Grafici di Nyquist')
display.geometry('400x225')


def Generate():
    try:
        k = float(entry1.get())
        zeri = [float(b) for b in entry2.get().split()]
        poli = [float(b) for b in entry3.get().split()]
        s1 = signal.ZerosPolesGain(zeri, poli, k)
        
        w, H = signal.freqresp(s1)
        
        plt.figure()
        plt.axes()
        plt.axhline()
        plt.arrow(-1,0, 0,-min(H.imag))
        plt.arrow(-1,0, 0,min(H.imag))

        plt.plot(H.real, H.imag, "b")
        plt.plot(H.real, -H.imag, "r")
        
        text4.config(text = 'Success')
        text4.pack()
        
        plt.show()
        
    except:
        text4.config(text = 'Error')
        text4.pack()


text1 = tkr.Label(display, text = 'Costante')
text1.pack()
canvas1 = tkr.Canvas(display, width = 100, height = 25,  relief = 'raised')
canvas1.pack()
entry1 = tkr.Entry(display) 
canvas1.create_window(50, 10, window=entry1)


text2 = tkr.Label(display, text = 'Zeri')
text2.pack()
canvas2 = tkr.Canvas(display, width = 100, height = 25,  relief = 'raised')
canvas2.pack()
entry2 = tkr.Entry(display) 
canvas2.create_window(50, 10, window=entry2)


text3 = tkr.Label(display, text = 'Poli')
text3.pack()
canvas3 = tkr.Canvas(display, width = 100, height = 25,  relief = 'raised')
canvas3.pack()
entry3 = tkr.Entry(display) 
canvas3.create_window(50, 10, window=entry3)


botton1 = tkr.Button(display, width = 5, height = 3, text = 'Genera Diagramma', command = Generate)
botton1.pack(fill='x')

text4 = tkr.Label(display, text = '')

display.mainloop()
