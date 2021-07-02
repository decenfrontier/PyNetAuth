# python网络验证管理后台
![](https://img.shields.io/badge/Python-3.8-blue.svg)
![](https://img.shields.io/badge/PySide2-5.15.2-blue.svg)
![](https://img.shields.io/badge/MySQL-5.7-green.svg)


## 项目介绍
基于Pyside2框架开发的网络验证管理后台，实现接收并处理客户端发出的登录，注册，改密，充值等请求，客户端防破解, 并进行用户数据管理与分析。

### 项目结构  

项目内部包含 客户端 和 服务端 两个项目, 方便同时开发与调试

<img src=https://z3.ax1x.com/2021/07/02/Rcrnjx.png width=50%>  

MySQL数据库与服务器分离, 当服务器被CC攻击时, 可增加新的服务器, 让用户选择通过别的服务器访问

<img src=https://z3.ax1x.com/2021/07/02/Rc0JCn.png width=50%>

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
<img src=https://z3.ax1x.com/2021/07/02/R6EcFI.png width=50%>
- 数据库  
<img src=https://z3.ax1x.com/2021/06/23/RuxQDs.png width=50%>


#### 2 客户端
客户端demo用于配合服务端测试, 包括登录界面和软件主界面
<img src=https://z3.ax1x.com/2021/06/03/23QPAO.png width=50%>
