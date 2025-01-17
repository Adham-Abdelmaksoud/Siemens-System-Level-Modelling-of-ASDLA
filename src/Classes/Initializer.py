import sys
from PySide6.QtWidgets import QCheckBox, QSpinBox, QDoubleSpinBox, QComboBox
from Classes.Children import Children
from Classes.Data_Submission import DataSubmission
from Classes.Filling import FillingQt
from Classes.Validator import Validator
from Classes.Layer_Node_Manager import LayerNodeManager
from utils.FileGenerator import FileGenerator
from Classes.Connections import Connections
from Classes.Controller import Controller
from Classes.Tensorboard import TensorView
from Classes.ResNet.resbuild import ResBuildWindow
from Classes.Transfer_Learning import DataOfTransfer
from Tests.Layer_Testing import LayerTesting
from Classes.Generated_Files_Viewer import GeneratedFilesViewer
from Classes.Parameters import Parameters
from Qt.Buttons import QTButtons
from Qt.Dialogue import LayerDialog

from utils.Cookiecutter import Cookiecutter

sys.path.append("./")


class Initializer(
    DataSubmission,
    FillingQt,
    Validator,
    LayerNodeManager,
    FileGenerator,
    Controller,
    Connections,
    TensorView,
    ResBuildWindow,
    DataOfTransfer,
    LayerTesting,
    GeneratedFilesViewer,
):
    def __init__(self) -> None:
        if self.debug:
            print("Initializer")
        self.Cookiecutter = Cookiecutter(
            self.SysPath.jinja_templates,
            self.debug
        )
        self.Children = Children(
            self.SysPath.res_build_ui_path,
            self.SysPath.GUI_path,
            self.loader
        )
        self.ui = self.Children.ui
        self.ResCreation = self.Children.ResCreation
        self.LayerDialog = LayerDialog()
        self.Qtbtn = QTButtons()
        Controller.__init__(self)
        LayerNodeManager.__init__(self)
        FillingQt.__init__(self)
        ResBuildWindow.__init__(self)
        DataOfTransfer.__init__(self)
        Connections.__init__(self)
        TensorView.__init__(self)
        DataSubmission.__init__(self)
        LayerTesting.__init__(self)
        GeneratedFilesViewer.__init__(self)
        self.Parameters = Parameters()

        self.ui.setWindowTitle("Application Specific Deep Learning Accelerator")

    def get_widget_data(self, widget):
        if isinstance(widget, QCheckBox):
            param_value = widget.isChecked()
        elif isinstance(widget, QSpinBox):
            param_value = widget.value()
        elif isinstance(widget, QDoubleSpinBox):
            param_value = widget.value()
        elif isinstance(widget, QComboBox):
            param_value = widget.currentData()
        else:
            param_value = widget.text().strip()
            try:
                param_value = eval(param_value)
            except:
                pass
        return param_value
