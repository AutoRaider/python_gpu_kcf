%module my_rect

%include <opencv.i>
%cv_instantiate_all_defaults

%{
    #include "my_rect.hpp"
%}

%include "my_rect.hpp"
