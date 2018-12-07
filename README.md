Python KCF acceleration with Intel GPU

## Requirements

 * Intel Media Driver - https://github.com/intel/media-driver.git
 * OpenCV with Intel_VA Enable 
 * Intel C-for-Media(MDF)  - https://01.org/c-for-media-development-package/downloads

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

可能需要安装的：
pip3 install matplotlib

sudo apt-get install python3-tk

pip3 install scikit-image

sudo apt install swig python3-dev

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


1.修改cmakelist相应opecv路径，要求opencv重新编译支持VA（opencv3.4版本 python3）

2.make后会在src下生产lib_kcftracker.so 手动删除此文件lib三个字母

3.直接运行kcf_test.py测试接口性能 此测试代码可看到对应接口函数


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

为方便python端转换对应的数据类型 本代码中kcftracker里面的几个cv::umat类型替换为cv::mat 类型转换在函数内实现

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

下载opencv-swig

make目录下的test可获取相应python调用的.so文件 可根据需要选择使用相应的数据类型 将所需.so和.py拷贝至src

我在kcf_submit/src下提供了另一种方法: 

swig -I/usr/local/include -c++ -python my_rect.i

g++ -shared -fpic my_rect_wrap.cxx $(pkg-config --cflags --libs python3) $(pkg-config --libs opencv) -o _my_rect.so


1. 选择用swig进行封装

2. 创建.i文件 
	例如本项目下的kcftracker.i：
	%module kcftracker	//名称
	%include "opencv.i"	//需要include的其他.i
	%{
	#include "tracker.h"	//直接在C++代码中原样写入
	#include "kcftracker.hpp"
	%}
	%include "tracker.h"
	%include "kcftracker.hpp"

	之后运行：
	swig -I/usr/local/include -c++ -python kcftracker.i

	本项目的rect数据类型也为自己实现的转换类型，自己写头文件，然后进行转换，可做参考：
	swig -I/usr/local/include -c++ -python my_rect.i
	g++ -shared -fpic my_rect_wrap.cxx $(pkg-config --cflags --libs python3) $(pkg-config --libs opencv) -o _my_rect.so
	最后可以在.py中实现import

	这里是所需的opencv-swig 可做参考：
	https://github.com/renatoGarcia/opencv-swig
	其中用到的mat数据类型就是引用这个生成的

3. 最后就是相应的CMakeLists编写，要将相应的依赖库都打包正确，项目中的CMakeLists可做参考，抛砖引玉啦。
	add_library(_kcftracker SHARED src/intelscalar.cpp src/SetupSurface.cpp src/fhog.cpp src/kcftracker.cpp src/main.cpp src/kcftracker_wrap.cxx)
	记得要加上生成的wrap文件，这个会生成lib_kcftracker.so 重命名 去掉前面的lib以供给python调用







