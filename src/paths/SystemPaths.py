import os


class SystemPaths:
    def __init__(self) -> None:
        print("System paths Class")
        # base directories
        self.basedir = os.path.dirname(__file__)
        self.publicdir = os.path.normpath(
            os.path.join(self.basedir, '../../public/'))
        self.srcdir = os.path.normpath(os.path.join(self.basedir, './../'))
        self.datadir = os.path.normpath(
            os.path.join(self.basedir, './../../data'))
        # log dir tensorboard
        self.Tensor_logs_dir = os.path.normpath(
            os.path.join(self.datadir, "./tensorboardlogs"))

        # GUI Paths and UI
        self.GUI_path = os.path.normpath(
            os.path.join(self.publicdir, "./GUI/mainwindow.ui"))
        self.main_ui_path = os.path.normpath(
            os.path.join(self.publicdir, "./GUI/mainwindow.ui"))
        self.res_build_ui_path = os.path.normpath(
            os.path.join(self.publicdir, "./GUI/resbuild.ui"))

        # Icons Paths
        self.delete_icon_path = os.path.normpath(
            os.path.join(self.publicdir, "./icons/delete.png"))
        self.up_icon_path = os.path.normpath(
            os.path.join(self.publicdir, "./icons/up.png"))
        self.down_icon_path = os.path.normpath(
            os.path.join(self.publicdir, "./icons/down.png"))

        # JSON paths
        self.ResJson = os.path.normpath(
            os.path.join(self.publicdir, "json_files/res.json"))
        self.arch_json_path = os.path.normpath(
            os.path.join(self.publicdir, "json_files/arch.json"))

        # Template paths
        self.jinja_templates = os.path.normpath(
            os.path.join(self.publicdir, "jinja_templates"))
        self.manual_cookie_jinja_template = os.path.normpath(
            os.path.join(self.publicdir, "jinja_templates/Manual"))
        self.transfer_template_dir = os.path.normpath(
            os.path.join(self.publicdir, "./Cookiecutter/Pretrained"))
        self.manual_template_dir = os.path.normpath(
            os.path.join(self.publicdir, "./Cookiecutter/Manual"))
        self.transfer_cookie_json = os.path.normpath(
            os.path.join(self.publicdir, "./Cookiecutter/Pretrained/cookiecutter.json"))
        self.manual_cookie_json = os.path.normpath(
            os.path.join(self.publicdir, "./Cookiecutter/Manual/cookiecutter.json"))
        # Dataset paths
        self.mnist_path = os.path.normpath(
            os.path.join(self.datadir, "./mnist"))
        # Log Path
        self.log_path = os.path.normpath(
            os.path.join(self.datadir, "./tensorboardlogs"))
        print(self.log_path)

        # to work on later
        self.css_path = 'ui/skin.qss'
        self.model_py_path = 'python_files/model.py'
        self.train_py_path = 'python_files/train.py'
        self.model_jinja_path = 'jinja_templates/model.py.jinja'
        self.train_jinja_path = 'jinja_templates/train.py.jinja'
