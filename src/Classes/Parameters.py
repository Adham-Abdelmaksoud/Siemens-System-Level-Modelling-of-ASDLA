import json
import os
from PySide6.QtWidgets import QFileDialog
from Classes.Parameters_folder.Miscellaneous import Miscellaneous
from Classes.Parameters_folder.Optimizer import Optimizer
from Classes.Parameters_folder.LossFunction import LossFunction
from Classes.Parameters_folder.Scheduler import Scheduler
from Classes.Parameters_folder.Pretrained import Pretrained
import torchvision
from Classes.Parameters_folder.Layers_System.Layers_System import Layers_System
from torchvision import models

import copy
from Classes.Children import Children
from paths.SystemPaths import SystemPaths


class Parameters:
    def __init__(self) -> None:
        self.Children = Children()
        self.SysPath = SystemPaths()
        # optimizer
        self.Misc_params = Miscellaneous()

        self.Optim_params = Optimizer()
        # loss_func
        self.LossFunc_params = LossFunction()
        # scheduler
        self.Scheduler_params = Scheduler()
        # layers
        self.Layers_System = Layers_System()
        # pretrained
        self.Pretrained = Pretrained()
        self.layers = []
        self.connections()

    def connections(self):
        self.Children.qt_actionLoad.triggered.connect(self.load_configs)
        self.Children.qt_Create_transfer_Model_QPushButton.clicked.connect(
            lambda submit_func=self.save_json_transfer, Template="Transfer Model":
            submit_func(Template)
        )

    def create_architecture(self):
        self.Layers_System.Validate_func()
        self.architecture = {
            'layers': self.Layers_System.layers,
            'misc_params': self.Misc_params.miscellaneous,
            'optimizer': self.Optim_params.optimizer,
            'loss_func': self.LossFunc_params.loss_function,
            'scheduler': self.Scheduler_params.scheduler,
            'pretrained': self.Pretrained.pretrained
        }
        return self.architecture

    def load_configs(self):
        path_arch_json, _ = QFileDialog.getOpenFileName(
            None, "Load configuration file",  self.SysPath.jsondir, "JSON Files (*.json)"
        )
        if path_arch_json:
            with open(path_arch_json, "r") as json_file:
                temp = json.load(json_file)
                # misc
                self.Misc_params.load_from_config(temp)
                # optimizer
                self.Optim_params.load_from_config(temp)
                # loss_func
                self.LossFunc_params.load_from_config(temp)
                # scheduler
                self.Scheduler_params.load_from_config(temp)
                # layers
                self.Layers_System.load_from_config(temp)

    def save_json_transfer(self, Template=None):
        temp_arch = self.create_architecture()
        architecture = copy.deepcopy(temp_arch)
        print(architecture["misc_params"])
        path, _ = QFileDialog.getSaveFileName(
            None, "Save JSON file", self.SysPath.jsondir, "JSON Files (*.json)"
        )

        if Template == "Transfer Model":
            Height, Width = self.get_min_size(
                architecture["pretrained"]["value"])
            if Height > architecture["misc_params"]["height"]:
                architecture["misc_params"]["height"] = Height
            if Width > architecture["misc_params"]["width"]:
                architecture["misc_params"]["width"] = Width
            architecture["log_dir"] = self.SysPath.log_path
            m = models.__dict__[architecture["pretrained"]
                                ["value"]](weights='DEFAULT')
            (name, param) = list(m.named_parameters())[0]
            architecture["misc_params"]["channels"] = param.shape[1]

        print(architecture["misc_params"])
        if path:
            self.SysPath.jsondir = path
            with open(path, 'w') as f:
                f.write(json.dumps(architecture, indent=4))
            print("JSON file saved successfully.")

    def get_min_size(self, model_name):
        min_size = torchvision.models.get_model_weights(
            torchvision.models.__dict__[model_name]).DEFAULT.meta['min_size']
        return min_size
