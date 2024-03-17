"""gui module.

Classes
    GUI
"""

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from .viewport import Viewport
from . import complex_fractal as cplxf


class GUI(tk.Tk):
    """GUI class.
    
    Provides a TKinter window yo display complex fractals.
    
    Objects declared as attributes (name preceded by 'self.') are used as global variables:
    they are both declared in constructor and used inside methods.
    """
    def __init__(self):
        super().__init__()
        # Window grid configuration
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)
        self.columnconfigure(0, weight=5)
        self.columnconfigure(1, weight=1)
        
        self.fractal = cplxf.MandelbrotSet()
        self.viewport = Viewport()
        self.image = [] # image of fractal
        
        ### IMAGE [0-7,0] ######################################################################
        frame_image = tk.Frame(self, bg='white')
        frame_image.grid(row=0, column=0, rowspan=8, sticky=tk.NSEW)
        
        # figure that will contain the plot 
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
        
        self.label_c = tk.Label(frame_fractal_c, text='c') # pack managed by Mandelbrot/Julia methods
        
        self.entry_c = tk.Entry(frame_fractal_c) # pack managed by Mandelbrot/Julia methods
        
        label_maxIt = tk.Label(frame_fractal_maxIt, text='Max iterations')
        label_maxIt.pack(side=tk.LEFT)
        
        self.entry_maxIt = tk.Entry(frame_fractal_maxIt)
        self.entry_maxIt.insert(0, '30') # max iterations default value
        self.entry_maxIt.pack(side=tk.RIGHT)
        
        ### RESOLUTION [1,1] ##########################################################################
        frame_resolution = tk.Frame(self)
        frame_resolution.grid(row=1, column=1, sticky=tk.NSEW)
        frame_resolution.columnconfigure(0, weight=1)
        frame_resolution.columnconfigure(1, weight=1)
        frame_resolution.columnconfigure(2, weight=1)
        frame_resolution.rowconfigure(0, weight=1)
        
        frame_resolution_left = tk.Frame(frame_resolution)
        frame_resolution_left.grid(row=0, column=0, sticky=tk.NSEW)
        frame_resolution_center = tk.Frame(frame_resolution)
        frame_resolution_center.grid(row=0, column=1, sticky=tk.NSEW)
        frame_resolution_right = tk.Frame(frame_resolution)
        frame_resolution_right.grid(row=0, column=2, sticky=tk.NSEW)
        
        self.const_resolutions = [(640,480), (1024,768), (2048,1536)]
        self.var_resolution = self.const_resolutions[0]
        self.strvar_resolution = tk.StringVar()
        self.strvar_resolution.set(str(self.var_resolution[0]) + 'x' + str(self.var_resolution[1]))
        
        label_resolution = tk.Label(frame_resolution_left, text='Resolution')
        label_resolution.pack(side=tk.LEFT)
        label_resolution_value = tk.Label(frame_resolution_center, textvariable=self.strvar_resolution)
        label_resolution_value.pack(expand=True)
        
        button_highRes = tk.Button(frame_resolution_right, text='+', width=2, command=self.higherRes)
        button_highRes.pack(side=tk.RIGHT)
        button_lowRes = tk.Button(frame_resolution_right, text='-', width=2, command=self.lowerRes)
        button_lowRes.pack(side=tk.RIGHT)
        
        ### COLOR [2,1] ###############################################################################
        frame_color = tk.Frame(self)
        frame_color.grid(row=2, column=1, sticky=tk.NSEW)

        # Creating the Combobox for colormaps
        label_color = tk.Label(frame_color, text='Colormap')
        label_color.pack(side=tk.LEFT)
        
        const_colormaps = plt.colormaps()
        self.combobox_color = ttk.Combobox(frame_color, text='Colormap', values=const_colormaps)
        self.combobox_color.current(0) # combobox default value
        self.combobox_color.pack(side=tk.RIGHT)     

        ### ZOOM [3,1] ##########################################################################
        frame_zoom = tk.Frame(self)
        frame_zoom.grid(row=3, column=1, sticky=tk.NSEW)

        button_zoomIn = tk.Button(frame_zoom, text='+', width=2, command=self.zoomIn)
        button_zoomIn.pack(side=tk.RIGHT)
        button_zoomOut = tk.Button(frame_zoom, text='-', width=2, command=self.zoomOut)
        button_zoomOut.pack(side=tk.RIGHT)

        self.strvar_zoom = tk.StringVar()
        self.strvar_zoom.set(str(1.0)) # zoom default value: 1.0

        self.entry_zoom = tk.Entry(frame_zoom, textvariable=self.strvar_zoom)
        self.entry_zoom.pack(side=tk.RIGHT)
        
        label_zoom = tk.Label(frame_zoom, text='Zoom')
        label_zoom.pack(side=tk.LEFT)
        label_zoom_cross = tk.Label(frame_zoom, text='x')
        label_zoom_cross.pack(side=tk.RIGHT)
        
        #### OFFSET [4,1] #############################################################################
        frame_offset = tk.Frame(self)
        frame_offset.grid(row=4, column=1, sticky=tk.NSEW)
        frame_offset.columnconfigure(0, weight=1)
        frame_offset.columnconfigure(1, weight=1)
        frame_offset.columnconfigure(2, weight=1)
        frame_offset.rowconfigure(0, weight=1)
        
        frame_offset_left = tk.Frame(frame_offset)
        frame_offset_left.grid(row=0, column=0, sticky=tk.NSEW)
        frame_offset_center = tk.Frame(frame_offset)
        frame_offset_center.grid(row=0, column=1, sticky=tk.NSEW)
        frame_offset_right = tk.Frame(frame_offset)
        frame_offset_right.grid(row=0, column=2, sticky=tk.NSEW)
        frame_offset_right.rowconfigure(0,weight=1)
        frame_offset_right.rowconfigure(1,weight=1)
        frame_offset_right.rowconfigure(2,weight=1)
        frame_offset_right.columnconfigure(0, weight=1)
        frame_offset_right.columnconfigure(1, weight=1)
        frame_offset_right.columnconfigure(2, weight=1)
        
        button_moveRight = tk.Button(frame_offset_right, text='\U00002192', width=3, height=1, command=self.moveRight)
        button_moveRight.grid(row=1, column=2)
        button_moveLeft = tk.Button(frame_offset_right, text='\U00002190', width=3, height=1, command=self.moveLeft)
        button_moveLeft.grid(row=1, column=0)
        button_moveUp = tk.Button(frame_offset_right, text='\U00002191', width=3, height=1, command=self.moveUp)
        button_moveUp.grid(row=0, column=1)
        button_moveDown = tk.Button(frame_offset_right, text='\U00002193', width=3, height=1, command=self.moveDown)
        button_moveDown.grid(row=2, column=1)

        self.strvar_offsetX = tk.StringVar()
        self.strvar_offsetY = tk.StringVar()
        self.strvar_offsetX.set(str(0)) # x offset dfault value: 0
        self.strvar_offsetY.set(str(0)) # y offset dfault value: 0
        
        label_offset = tk.Label(frame_offset_left, text='Offset')
        label_offset.pack(side=tk.LEFT)
        
        label_offset_leftpar = tk.Label(frame_offset_center, text='(')
        label_offset_leftpar.pack(side=tk.LEFT)
        self.entry_offsetX = tk.Entry(frame_offset_center, width=7, textvariable=self.strvar_offsetX)
        self.entry_offsetX.pack(side=tk.LEFT)
        label_offset_comma = tk.Label(frame_offset_center, text=',')
        label_offset_comma.pack(side=tk.LEFT)
        self.entry_offsetY = tk.Entry(frame_offset_center, width=7, textvariable=self.strvar_offsetY)
        self.entry_offsetY.pack(side=tk.LEFT)
        label_offset_rightpar = tk.Label(frame_offset_center, text=')')
        label_offset_rightpar.pack(side=tk.LEFT)
        
        ### APPLY CHANGES [5,1] #####################################################################
        frame_apply = tk.Frame(self)
        frame_apply.grid(row=5, column=1, sticky=tk.NSEW)

        button_apply = tk.Button(frame_apply, text='Apply changes', width=12, command=self.apply)
        button_apply.pack(expand=True)
        
        ### SAVE IMAGES [6,1] #####################################################################
        frame_save = tk.Frame(self)
        frame_save.grid(row=6, column=1, sticky=tk.NSEW)
        
        button_save = tk.Button(frame_save, text='Save image', width=12, command=self.saveImage)
        button_save.pack(expand=True)
        
        ### QUIT [7,1] #####################################################################
        frame_quit = tk.Frame(self)
        frame_quit.grid(row=7, column=1, sticky=tk.NSEW)
        
        button_quit = tk.Button(frame_quit, text='QUIT', width=12, command=self.destroy)
        button_quit.pack(expand=True)
 
    def mandelbrot(self):
        self.label_c.pack_forget()
        self.entry_c.pack_forget()
        self.fractal = cplxf.MandelbrotSet()
    def julia(self):
        self.label_c.pack(side=tk.LEFT)
        self.entry_c.delete(0, tk.END)
        self.entry_c.insert(0, '0') # c default value: 0
        self.entry_c.pack(side=tk.RIGHT)
        self.fractal = cplxf.JuliaSet()

    def zoomIn(self):
        var_zoom = float(self.entry_zoom.get()) + 0.5
        self.strvar_zoom.set(str(var_zoom)) # no maximum zoom value
    def zoomOut(self):
        var_zoom = max(float(self.entry_zoom.get()) - 0.5, 0.5) # minimum zoom value: 0.5
        self.strvar_zoom.set(str(var_zoom))

    def moveRight(self):
        var_offsetX = float(self.entry_offsetX.get()) + 0.1 / float(self.entry_zoom.get())
        self.strvar_offsetX.set(str(round(var_offsetX, 4)))
    def moveLeft(self):
        var_offsetX = float(self.entry_offsetX.get()) - 0.1 / float(self.entry_zoom.get())
        self.strvar_offsetX.set(str(round(var_offsetX, 4)))
    def moveUp(self):
        var_offsetY = float(self.entry_offsetY.get()) + 0.1 / float(self.entry_zoom.get())
        self.strvar_offsetY.set(str(round(var_offsetY, 4)))
    def moveDown(self):
        var_offsetY = float(self.entry_offsetY.get()) - 0.1 / float(self.entry_zoom.get())
        self.strvar_offsetY.set(str(round(var_offsetY, 4)))
    
    def higherRes(self):
        var_next_res_index = min(self.const_resolutions.index(self.var_resolution) + 1, len(self.const_resolutions) - 1)
        self.var_resolution = self.const_resolutions[var_next_res_index]
        self.strvar_resolution.set(str(self.var_resolution[0]) + 'x' + str(self.var_resolution[1]))
    def lowerRes(self):
        var_next_res_index = max(self.const_resolutions.index(self.var_resolution) - 1, 0)
        self.var_resolution = self.const_resolutions[var_next_res_index]
        self.strvar_resolution.set(str(self.var_resolution[0]) + 'x' + str(self.var_resolution[1]))
    
    def apply(self):
        try:
            self.viewport.fractal = self.fractal
            if isinstance(self.fractal, cplxf.JuliaSet):
                self.viewport.fractal.c = complex(self.entry_c.get())
            self.viewport.fractal.max_iterations = int(self.entry_maxIt.get())
            self.viewport.resolution = self.var_resolution
            self.viewport.offset = (float(self.entry_offsetX.get()), float(self.entry_offsetY.get()))
            self.viewport.zoom = max(float(self.entry_zoom.get()), 0.5)
            self.viewport.colormap = self.combobox_color.get()
            self.plotViewport()
        except Exception as error:
            self.showError(error)

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
        fileName = (
            str(self.viewport.fractal) + '_' 
            + 'x' + str(self.viewport.zoom) + '_' 
            + str(self.viewport.resolution[0]) + 'x' + str(self.viewport.resolution[1])
            + '.png'
        )
        try:
            plt.imsave(fileName, self.image, cmap=self.viewport.colormap)
        except Exception as error:
            self.showError(error)
    
    def showError(self, error):
        tk.messagebox.showerror(
            title = 'Error',
            message = str(error)
        )