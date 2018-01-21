# work_or_not
code part for project work_or_not(with Inception V3, tensorflow)

gen_test_img.py通过不同类的视频素材生成训练所需的图片，在python2下运行正常。

首先克隆tensorflow源码到该工程目录文件夹下，注意版本分支。

建立data文件夹，下面包含所要进行分类的实例图片。路径实例如下：

root_path
  data
     class1
      instances1
      instances2
      ...
     class2
      instance1
      instance2
      ...
     ...
 在工程目录下在开启cmd，运行command.txt内的第一条命令，默认参数已给出，可根据不同需求修改。
 
 生成模型后，
 
 restore.py脚本简单测试。
 
 camera.py脚本打开摄像头，实时采样，给出反馈，并积累更多素材进行进一步训练。
