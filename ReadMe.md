
# 更新公告

0.4.0
- 添加 服务端处理充值类型消息
- 优化 表查询算法
- 添加 表更新算法


0.3.9
- 完善 充值按钮点击事件


0.3.8
- 添加 充值按钮点击事件
- 优化 为充值卡号标签添加超链接


0.3.7
- 修复 设置表格项文本不显示的问题
- 修复 再刷新卡密库时会追加显示


0.3.6
- 添加 按钮刷新卡密库点击事件
- 优化 表查询算法


0.3.5
- 添加 生成随机卡密函数
- 添加 按钮生成卡密点击事件


0.3.4
- 优化 客户端登录窗口圆角效果


0.3.3
- 新增 解绑按钮
- 修复 起始点应为QPoint类型
- 优化 界面


0.3.2
- 修复 登录成功不显示主界面


0.3.1
- 优化 获取外网IP方法
- 优化 新开一个线程去获取公网IP, 避免阻塞界面


0.3.0
- 修复 客户端登录窗口无法拖动
- 优化 使用添加窗口背景的第二种方法
- 优化 添加退出按钮
- 修复 退出按钮点击后由于接收线程还在运行导致无法退出


0.2.9
- 优化 添加窗口背景


0.2.8
- 修复 客户端窗口类改为QDialog


0.2.7
- 添加 客户端登录成功关闭登录窗口, 显示软件主界面
- 优化 窗口程序集统一移到项目根目录
- 修复 服务端向客户端发数据失败的问题


0.2.6
- 添加 服务端接收登录消息处理
- 添加 客户端接收登录响应处理


0.2.5
- 添加 客户端登录按钮点击事件编写


0.2.4
- 优化 对注册密码和qq进行非对称加密后再发送给服务器


0.2.3
- 添加 客户端对注册结果处理


0.2.2
- 添加 服务器返回注册结果给客户端


0.2.1
- 优化 机器码=主板序列号+硬盘序列号, 再把从12:移到前面, :12移到后面, 再倒序排列
- 修复 注册插入到数据库失败的bug


0.2.0
- 完善 服务器收到"注册"类型的消息时, 把注册信息插入到数据库
- 添加 表-插入函数


0.1.9
- 优化 机器码=主板序列号+硬盘序列号+bios序列号


0.1.8
- 优化 表查询时异常则回滚
- 完善 服务端接收数据
- 修复 客户端先转为字节型再发送数据


0.1.7
- 添加 客户端注册按钮点击事件


0.1.6
- 优化 客户端控件名
- 优化 客户端界面


0.1.5
- 测试 服务端 数据库查询 
- 添加 客户端 发送数据时异常处理
- 优化 两窗口设置不同初始位置


0.1.4
- 优化 服务端套接字, 游标, 连接对象改全局变量


0.1.3
- 优化 客户端端口号改全局变量


0.1.2
- 优化 服务端连接mysql添加异常处理
- 测试 服务端响应客户端
- 添加 客户端初始时时连接tcp, 并开启线程接收数据


0.1.1
- 添加 客户端点击登录按钮发送账号文本字节给服务端
- 优化 控件重命名


0.1.0
- 添加 客户端tcp初始化代码
- 添加 客户端初始化状态栏
- 修复 服务端, 客户端退出时异常


0.0.9
- 完善 服务端tcp初始化代码


0.0.8
- 优化 服务端记录到日志窗口前加上当前时间


0.0.7
- 添加 服务端tcp初始化代码
- 优化 把资源相关的放到res目录
- 添加 服务端-执行日志
- 添加 服务端-日志标签


0.0.6
- 添加 服务端mysql初始化代码


0.0.5
- 设置 客户端工具栏图标
- 优化 服务端工具栏图标


0.0.4
- 添加 客户端界面


0.0.3
- 添加 服务端界面-在线用户页
- 添加 服务端界面-卡密管理页


0.0.2
- 显示 服务端界面
- 添加 qrc资源文件
- 设置 服务端工具栏图标


0.0.1
- 添加 服务端界面全部用户页