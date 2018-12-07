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








