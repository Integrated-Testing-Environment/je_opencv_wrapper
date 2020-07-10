from Feature_Detection import Feature_Detection
from Template_Detection import Template_Detection
from Feature import Feature
from Object_Tracking import Object_Tracking
from IO import IO
from Video import Video
from Draw import Draw
from Event import Event
from Image_Processing import Image_Processing
from UI import UI
from Image_Operations import Image_Operations
from FPS import FPS

class Core():

    def __init__(self):
        try:
            self.Feature_Detection=Feature_Detection()
            self.Template_Detection=Template_Detection()
            self.Feature=Feature()
            self.Object_Tracking=Object_Tracking()
            self.IO=IO()
            self.Video=Video()
            self.Draw=Draw()
            self.Event=Event()
            self.Image_Processing=Image_Processing()
            self.UI=UI()
            self.Image_Operations=Image_Operations()
            self.FPS=FPS()
        except Exception as Errr:
            raise Errr