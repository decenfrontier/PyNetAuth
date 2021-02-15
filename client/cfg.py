import copy

from client import mf

class BaseCfg():
    def __init__(self, plan_name: str):
        self.plan_name = plan_name
        self.plan_dict = {}

    def set(self, key: str, val: str):
        self.plan_dict[key] = val

    def get(self, key: str):
        return self.plan_dict.get(key)

    def __setattr__(self, key, val):
        if val is not None:
            self.__dict__[key] = val


# 登录配置类
class CfgLogin(BaseCfg):
    def __init__(self, plan_name: str):
        super().__init__(plan_name)
        self.plan_dict = copy.deepcopy(default_login_dict)

    def controls_to_file(self):
        ui = mf.wnd_login
        # ---------------------- 控件 -> 实例属性 ---------------------
        # ---------------------- 实例属性 -> 配置文件 ---------------------
        # 执行列表
        self.lst_exec = [ui.lst_exec.item(i).text() for i in range(ui.lst_exec.count())]
        self.set("lst_exec", self.lst_exec)
        # 战斗
        self.cmb_skill_round1 = ui.cmb_skill_round1.currentText()
        self.cmb_obj_round1 = ui.cmb_obj_round1.currentText()
        self.cmb_skill_round2 = ui.cmb_skill_round2.currentText()
        self.cmb_obj_round2 = ui.cmb_obj_round2.currentText()
        self.cmb_policy_bb = ui.cmb_policy_bb.currentText()
        self.chk_fuyu = ui.chk_fuyu.isChecked()
        self.chk_tm_anqi = ui.chk_tm_anqi.isChecked()
        self.chk_df_lahuan = ui.chk_df_lahuan.isChecked()
        self.chk_zhao_huan = ui.chk_zhao_huan.isChecked()
        self.chk_save_people = ui.chk_save_people.isChecked()
        self.set("cmb_skill_round1", self.cmb_skill_round1)
        self.set("cmb_obj_round1", self.cmb_obj_round1)
        self.set("cmb_skill_round2", self.cmb_skill_round2)
        self.set("cmb_obj_round2", self.cmb_obj_round2)
        self.set("cmb_policy_bb", self.cmb_policy_bb)
        self.set("chk_fuyu", self.chk_fuyu)
        self.set("chk_tm_anqi", self.chk_tm_anqi)
        self.set("chk_df_lahuan", self.chk_df_lahuan)
        self.set("chk_zhao_huan", self.chk_zhao_huan)
        self.set("chk_save_people", self.chk_save_people)

        json_plan_dict[self.plan_name] = self.plan_dict
        mf.py_to_json(json_plan_dict, mf.PATH_PLAN_JSON)


    def file_to_attr(self):
        cfg_plan_dict = mf.json_to_py(mf.PATH_PLAN_JSON)
        d = cfg_plan_dict.get(self.plan_name)
        if isinstance(d, dict):
            self.plan_dict.update(d)
        # ------------------------ 配置文件 -> 实例属性 -------------------------
        # 执行列表
        self.lst_exec = self.get("lst_exec")  # "师门任务-剧情任务"
        # 战斗
        self.cmb_skill_round1 = self.get("cmb_skill_round1")
        self.cmb_obj_round1 = self.get("cmb_obj_round1")
        self.cmb_skill_round2 = self.get("cmb_skill_round2")
        self.cmb_obj_round2 = self.get("cmb_obj_round2")
        self.cmb_policy_bb = self.get("cmb_policy_bb")
        self.chk_fuyu = self.get("chk_fuyu")
        self.chk_tm_anqi = self.get("chk_tm_anqi")
        self.chk_df_lahuan = self.get("chk_df_lahuan")
        self.chk_zhao_huan = self.get("chk_zhao_huan")
        self.chk_save_people = self.get("chk_save_people")

    def attr_to_controls(self):
        ui = mf.main_wnd
        # ------------------------ 实例属性 -> 控件 -------------------------
        # 执行列表
        ui.lst_exec.clear()
        ui.lst_exec.addItems(self.lst_exec)
        # 战斗
        ui.cmb_skill_round1.setCurrentText(self.cmb_skill_round1)
        ui.cmb_obj_round1.setCurrentText(self.cmb_obj_round1)
        ui.cmb_skill_round2.setCurrentText(self.cmb_skill_round2)
        ui.cmb_obj_round2.setCurrentText(self.cmb_obj_round2)
        ui.cmb_policy_bb.setCurrentText(self.cmb_policy_bb)
        ui.chk_fuyu.setChecked(self.chk_fuyu)
        ui.chk_tm_anqi.setChecked(self.chk_tm_anqi)
        ui.chk_df_lahuan.setChecked(self.chk_df_lahuan)
        ui.chk_zhao_huan.setChecked(self.chk_zhao_huan)
        ui.chk_save_people.setChecked(self.chk_save_people)



default_login_dict = {
    "edt_login_account": "111111",
    "edt_login_pwd": "222222",
    "chk_login_remember": True,
}

