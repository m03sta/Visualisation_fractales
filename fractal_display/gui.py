"""gui module.

Classes
    GUI
"""

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from fractal_display.viewport import Viewport
from fractal_display import complex_fractal as cplxf


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        # Window grid configuration
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=1)
        
        self.fractal = cplxf.MandelbrotSet()
        self.viewport = Viewport()
        self.image = []
        
        ### IMAGE [0-5,0] ######################################################################
        frame_image = tk.Frame(self, bg='white')
        frame_image.grid(row=0, column=0, rowspan=6, sticky=tk.NSEW)
        
        # the figure that will contain the plot 
        figure = Figure(figsize = (6, 6))
        self.plot = figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(figure, master=frame_image) 
        
        ### FRACTAL [0,1] #######################################################################
        frame_fractal = tk.Frame(self)
        frame_fractal.grid(row=0, column=1, sticky=tk.NSEW)
        frame_fractal.rowconfigure(0, weight=1)
        frame_fractal.rowconfigure(1, weight=1)
        frame_fractal.rowconfigure(2, weight=1)
        frame_fractal.columnconfigure(0, weight=1)
        frame_fractal.columnconfigure(1, weight=1)
        
        frame_fractal_mandelbrot = tk.Frame(frame_fractal)
        frame_fractal_mandelbrot.grid(row=0, column=0, sticky=tk.NSEW)  
        frame_fractal_julia = tk.Frame(frame_fractal)
        frame_fractal_julia.grid(row=0, column=1, sticky=tk.NSEW)
        frame_fractal_c = tk.Frame(frame_fractal)
        frame_fractal_c.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW)
        frame_fractal_maxIt = tk.Frame(frame_fractal)
        frame_fractal_maxIt.grid(row=2, column=0, columnspan=2, sticky=tk.NSEW)
        
        button_mandelbrot = tk.Button(frame_fractal_mandelbrot, text='Mandelbrot', command=self.mandelbrot)
        button_mandelbrot.pack(fill=tk.X, expand=True)
        button_julia = tk.Button(frame_fractal_julia, text='Julia', command=self.julia)
        button_julia.pack(fill=tk.X, expand=True)
        
        self.label_c = tk.Label(frame_fractal_c, text='c')
        self.entry_c = tk.Entry(frame_fractal_c)
        
        label_maxIt = tk.Label(frame_fractal_maxIt, text='Max iterations')
        label_maxIt.pack(side=tk.LEFT)
        self.entry_maxIt = tk.Entry(frame_fractal_maxIt)
        self.entry_maxIt.insert(0, '30') # max iterations default value
        self.entry_maxIt.pack(side=tk.RIGHT)
        
        ### RESOLUTION [1,1] ##########################################################################
        frame_resolution = tk.Frame(self)
        frame_resolution.grid(row=1, column=1, sticky=tk.NSEW)
        
        self.const_resolutions = [(640,480), (1024,768)]
        self.var_resolution = self.const_resolutions[0]
        self.strvar_resolution = tk.StringVar()
        self.strvar_resolution.set('Resolution:   ' + str(self.var_resolution[0]) + 'x' + str(self.var_resolution[1]))
        label_resolution = tk.Label(frame_resolution, textvariable=self.strvar_resolution)
        label_resolution.pack(side=tk.LEFT)
        
        button_highRes = tk.Button(frame_resolution, text='+', width=2, command=self.highRes)
        button_highRes.pack(side=tk.RIGHT)
        button_lowRes = tk.Button(frame_resolution, text='-', width=2, command=self.lowRes)
        button_lowRes.pack(side=tk.RIGHT)
        
        ### ZOOM [2,1] ##########################################################################
        frame_zoom = tk.Frame(self)
        frame_zoom.grid(row=2, column=1, sticky=tk.NSEW)

        button_zoomIn = tk.Button(frame_zoom, text='+', width=2, command=self.zoomIn)
        button_zoomIn.pack(side=tk.RIGHT)
        button_zoomOut = tk.Button(frame_zoom, text='-', width=2, command=self.zoomOut)
        button_zoomOut.pack(side=tk.RIGHT)
        
        self.var_zoom = 1.0
        self.strvar_zoom = tk.StringVar()
        self.strvar_zoom.set('Zoom:   x' + str(self.var_zoom))
        label_zoom = tk.Label(frame_zoom, textvariable=self.strvar_zoom)
        label_zoom.pack(side=tk.LEFT)
        
        #### OFFSET [3,1] #############################################################################
        frame_offset = tk.Frame(self)
        frame_offset.grid(row=3, column=1, sticky=tk.NSEW)
        frame_offset.columnconfigure(0, weight=1)
        frame_offset.columnconfigure(1, weight=1)
        
        frame_offset_left = tk.Frame(frame_offset)
        frame_offset_left.grid(row=0, column=0, sticky=tk.NSEW)
        frame_offset_left.rowconfigure(0,weight=1)
        frame_offset_left.rowconfigure(1,weight=1)
        frame_offset_left.rowconfigure(2,weight=1)
        frame_offset_left.columnconfigure(0, weight=1)
        frame_offset_left.columnconfigure(1, weight=1)
        frame_offset_left.columnconfigure(2, weight=1)
        frame_offset_right = tk.Frame(frame_offset)
        frame_offset_right.grid(row=0, column=1, sticky=tk.NSEW)

        button_moveRight = tk.Button(frame_offset_right, text='\U00002192', width=4, height=1, command=self.moveRight)
        button_moveRight.grid(row=1, column=2)
        button_moveLeft = tk.Button(frame_offset_right, text='\U00002190', width=4, height=1, command=self.moveLeft)
        button_moveLeft.grid(row=1, column=0)
        button_moveUp = tk.Button(frame_offset_right, text='\U00002191', width=4, height=1, command=self.moveUp)
        button_moveUp.grid(row=0, column=1)
        button_moveDown = tk.Button(frame_offset_right, text='\U00002193', width=4, height=1, command=self.moveDown)
        button_moveDown.grid(row=2, column=1)

        self.var_offsetX = 0
        self.var_offsetY = 0
        self.strvar_offset = tk.StringVar()
        self.strvar_offset.set('Offset:   ' + str((self.var_offsetX,self.var_offsetX)))
        label_offset = tk.Label(frame_offset_left, textvariable=self.strvar_offset, height=1)
        label_offset.pack(side=tk.LEFT)
        
        ### COLOR [4,1] ###############################################################################
        frame_color = tk.Frame(self)
        frame_color.grid(row=4, column=1, sticky=tk.NSEW)

        # Creating the Combobox for colormaps
        label_color = tk.Label(frame_color, text='Colormap')
        label_color.pack(side=tk.LEFT)
        
        const_colormaps = plt.colormaps()
        self.combobox_color = ttk.Combobox(frame_color, text='Colormap', values=const_colormaps)
        self.combobox_color.current(0) # combobox default value
        self.combobox_color.pack(side=tk.RIGHT)     

        ### APPLY / SAVE IMAGE [5,1] #####################################################################
        frame_apply = tk.Frame(self)
        frame_apply.grid(row=5, column=1, sticky=tk.NSEW)

        button_apply = tk.Button(frame_apply, text='Apply modifications', command=self.apply)
        button_apply.pack(side=tk.TOP)
        button_save = tk.Button(frame_apply, text='Save image', command=self.saveImage)
        button_save.pack(side=tk.BOTTOM)
 
    def mandelbrot(self):
        self.label_c.pack_forget()
        self.entry_c.pack_forget()
        self.fractal = cplxf.MandelbrotSet()
    def julia(self):
        self.label_c.pack(side=tk.LEFT)
        self.entry_c.insert(0, '0') # c default value
        self.entry_c.pack(side=tk.RIGHT)
        self.fractal = cplxf.JuliaSet()

    def zoomIn(self):
        self.var_zoom = self.var_zoom + 0.5
        self.strvar_zoom.set('Zoom:   x' + str(self.var_zoom))
    def zoomOut(self):
        self.var_zoom = max(self.var_zoom - 0.5, 0.5) # minimum zoom value : 0.5
        self.strvar_zoom.set('Zoom:   x' + str(self.var_zoom))

    def moveRight(self):
        self.var_offsetX += 0.1 / self.var_zoom
        self.strvar_offset.set('Offset:   ' + str((round(self.var_offsetX, 5), round(self.var_offsetY, 5))))
    def moveLeft(self):
        self.var_offsetX -= 0.1 / self.var_zoom
        self.strvar_offset.set('Offset:   ' + str((round(self.var_offsetX, 5), round(self.var_offsetY, 5))))
    def moveUp(self):
        self.var_offsetY += 0.1 / self.var_zoom
        self.strvar_offset.set('Offset:   ' + str((round(self.var_offsetX, 5), round(self.var_offsetY, 5))))
    def moveDown(self):
        self.var_offsetY -= 0.1 / self.var_zoom
        self.strvar_offset.set('Offset:   ' + str((round(self.var_offsetX, 5), round(self.var_offsetY, 5))))
    
    def highRes(self):
        self.var_resolution = self.const_resolutions[1]
        self.strvar_resolution.set('Resolution:   ' + str(self.var_resolution[0]) + 'x' + str(self.var_resolution[1]))
    def lowRes(self):
        self.var_resolution = self.const_resolutions[0]
        self.strvar_resolution.set('Resolution:   ' + str(self.var_resolution[0]) + 'x' + str(self.var_resolution[1]))
    
    def apply(self):
        self.viewport.fractal = self.fractal
        if isinstance(self.fractal, cplxf.JuliaSet):
            self.viewport.fractal.c = complex(self.entry_c.get())
        if self.entry_maxIt.get():
            self.viewport.fractal.max_iterations = int(self.entry_maxIt.get())
        self.viewport.resolution = self.var_resolution
        self.viewport.offset = (self.var_offsetX, self.var_offsetY)
        self.viewport.zoom = self.var_zoom
        self.viewport.colormap = self.combobox_color.get()
        self.plotViewport()

    def plotViewport(self):
        self.image = self.viewport.img_rgb()
        self.plot.imshow(
            self.image,
            cmap = self.viewport.colormap,
            extent = [
                self.viewport.offset[0] - (self.viewport.size[0] / 2) / self.viewport.zoom,
                self.viewport.offset[0] + (self.viewport.size[0] / 2) / self.viewport.zoom,
                self.viewport.offset[1] - (self.viewport.size[1] / 2) / self.viewport.zoom,
                self.viewport.offset[1] + (self.viewport.size[1] / 2) / self.viewport.zoom
            ]
        )
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def saveImage(self):
        plt.imsave(str(self.viewport.fractal) + '.png', self.image, cmap=self.viewport.colormap)