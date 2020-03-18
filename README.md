# AzurLaneScripts

碧蓝航线的自动刷图脚本.

tips_1: 电脑需要安装python运行环境.
 
tips_2: 需要配合 安卓模拟器(推荐)/手机 使用.

tips_3: 这里仅讨论windows平台的使用.

tips_4: 默认读者已经有一定的动手能力.

tips_5: 脚本还在完善中, 配置运行方式都可能会(向着更简便的方式)改变.

## 使用方法

原理是通过ADB对手机屏幕截图, 对比模板图片判断当前游戏情况, 然后通过ADB模拟点击/拖拽等操作.

### 环境搭建

#### 安装python

前往 [miniconda](https://docs.conda.io/en/latest/miniconda.html) 下载 python 3.7 安装包并安装.

安装时注意配置运行环境(path).

    如何判断python安装成功?
    
    打开cmd, 执行 `python --version`, 如果正确显示python版本号则说明安装成功

#### 安装python依赖

需要用户手动安装cv2, 用来处理图像相关的工作.

    pip install opencv-python

#### 关于ADB和设备

本项目已经自带了adb.exe程序. 用户不必再手动下载.

许多安卓模拟器也会自带adb程序, 不过其自带的版本往往比较低, 一些功能残缺.

+ 如果发现在运行时提示找不到设备, 则可以将项目自带的ADB软件覆盖到模拟器中ADB响应的位置. 然后重启虚拟机.
+ 如果提示设备过多, 则可能虚拟机有多开的情况, 或者是虚拟机和手机同时连接了. 请断开多余设备.

### 运行

打开游戏, 进入游戏主界面. 然后运行脚本 `main.py`