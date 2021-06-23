# pyside2开发的网络验证管理后台-桌面端
![](https://img.shields.io/badge/Python-3.8-blue.svg)
![](https://img.shields.io/badge/PySide2-5.15.2-blue.svg)
![](https://img.shields.io/badge/MySQL-5.7-green.svg)


## 项目介绍
基于Pyside2框架开发的网络验证管理后台，实现接收并处理客户端发出的登录，注册，改密，充值等请求，客户端防破解, 并进行用户数据管理与分析。

### 项目结构  
<img src=https://z3.ax1x.com/2021/06/04/2JtJo9.png width=50%>

#### 1 服务端
- 项目管理  
<img src=https://z3.ax1x.com/2021/06/03/2152TI.png width=50%>
- 用户管理  
<img src=https://z3.ax1x.com/2021/06/04/2JtFsS.png width=50%>
- 卡密管理  
<img src=https://z3.ax1x.com/2021/06/03/21OXNQ.png width=50%>
- 每日流水  
<img src=https://z3.ax1x.com/2021/06/03/23SfN8.png width=50%>
- IP与日志  
<img src=https://z3.ax1x.com/2021/06/03/23SfN8.png width=50%>


#### 2 客户端
客户端demo用于配合服务端测试  
<img src=https://z3.ax1x.com/2021/06/03/23QPAO.png width=50%>



## 近期更新公告

3.2.6
- 添加 小时卡


3.2.5
- 优化 处理项目时, 若存在版本号返回真, 否则返回结果假


3.2.4
- 优化 新用户月卡注册送2天, 推荐人送2天, 老用户续费月卡送 2+累计充值月数 天


3.2.3
- 删除 发卡网址
- 添加 设置注册赠送时间和推荐人赠送时间
- 修复 注册时没把卡号设置已使用时间


3.2.2
- 限制 每日最大解绑次数为4次


3.2.1
- 优化 用户充值时上锁
- 修复 用户首次登录后返回给新用户的到期时间错误


3.2.0
- 新增 注册推荐人机制
- 优化 注册不再检测机器码


3.1.9
- 优化 解绑不再判断在线状态
- 优化 心跳时若正常则更新机器码


3.1.8
- 优化 冻结的账号下次解冻时, 重新设置到期时间


3.1.7
- 新增 顶号登录(登录时不再判断在线状态)

...