from PySide6.QtWidgets import (
    QVBoxLayout,
    QLabel,
    QDialog,
    QDialogButtonBox,
    QHBoxLayout,
    QLineEdit,
    QSpinBox,
    QComboBox,
    QCheckBox,
)
import inspect

import types
from typing import Generic, TypeVar, Union


class LayerDialog():

    def create_dialogue_controller(self, torch_funcs, func_name, params_names, params_value_widgets, allParamsColumn_QVBoxLayout):

        for param in torch_funcs[func_name]:
            try:
                if bool in param["type"].__args__:
                    paramValue_QWidget = QCheckBox()
                    paramValue_QWidget.setChecked(param['defaultvalue'])
                elif int in param["type"].__args__:
                    paramValue_QWidget = QSpinBox(minimum=1, maximum=1000)
                    paramValue_QWidget.setValue(0)
                else:
                    paramValue_QWidget = QLineEdit()
                    if (
                        param['defaultvalue'] != inspect._empty
                        and
                        param['defaultvalue'] != None
                    ):
                        paramValue_QWidget.setText(str(param['defaultvalue']))
            except:
                if bool == param["type"]:
                    paramValue_QWidget = QCheckBox()
                    paramValue_QWidget.setChecked(param['defaultvalue'])
                elif int == param["type"]:
                    paramValue_QWidget = QSpinBox(minimum=1, maximum=1000)
                    paramValue_QWidget.setValue(0)
                else:
                    paramValue_QWidget = QLineEdit()
                    if (
                        param['defaultvalue'] != inspect._empty
                        and
                        param['defaultvalue'] != None
                    ):
                        paramValue_QWidget.setText(str(param['defaultvalue']))

            params_names.append(param['name'])
            params_value_widgets.append(paramValue_QWidget)

            paramRow_QHBoxLayout = QHBoxLayout()
            paramRow_QHBoxLayout.addWidget(QLabel(f'{param["name"]}'))
            paramRow_QHBoxLayout.addWidget(paramValue_QWidget)
            allParamsColumn_QVBoxLayout.addLayout(paramRow_QHBoxLayout)