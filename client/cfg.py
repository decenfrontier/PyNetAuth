import copy

from client import mf

# 基配置类
class CfgBase():
    def __init__(self):
        self.cfg_dict = {}

    def set(self, key: str, val: str):
        self.cfg_dict[key] = val

    def get(self, key: str):
        return self.cfg_dict.get(key)

    def __setattr__(self, key, val):
        if val is not None:
            self.__dict__[key] = val

# 登录配置类
class CfgLogin(CfgBase):
    def __init__(self):
        super().__init__()
        self.cfg_dict = copy.deepcopy(default_login_dict)

    def controls_to_file(self):
        ui = mf.wnd_login
        # ---------------------- 控件 -> 实例属性 ---------------------
        self.edt_login_account = ui.edt_login_account.text()
        self.edt_login_pwd = ui.edt_login_pwd.text()
        self.chk_login_remember = ui.chk_login_remember.isChecked()
        # ---------------------- 实例属性 -> 配置文件 ---------------------
        self.set("edt_login_account", self.edt_login_account)
        self.set("edt_login_pwd", self.edt_login_pwd)
        self.set("chk_login_remember", self.chk_login_remember)
        mf.py_to_json(self.cfg_dict, mf.PATH_LOGIN_JSON)

    def file_to_controls(self):
        cfg_dict = mf.json_to_py(mf.PATH_LOGIN_JSON)
        if cfg_dict:
            self.cfg_dict.update(cfg_dict)
        ui = mf.wnd_login
        # ------------------------ 配置文件 -> 实例属性 -------------------------
        self.edt_login_account = self.get("edt_login_account")
        self.edt_login_pwd = self.get("edt_login_pwd")
        self.chk_login_remember = self.get("chk_login_remember")
        # ------------------------ 实例属性 -> 控件 -------------------------
        ui.edt_login_account.setText(self.edt_login_account)
        ui.edt_login_pwd.setText(self.edt_login_pwd)
        ui.chk_login_remember.setChecked(self.chk_login_remember)

default_login_dict = {
    "edt_login_account": "111111",
    "edt_login_pwd": "222222",
    "chk_login_remember": True,
}

cfg_login = CfgLogin()