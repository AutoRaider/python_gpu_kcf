#include <opencv2/core.hpp>
#include <iostream>

inline
cv::Rect CVrect(float x, float y, float width, float height)
{
    cv::Rect roi;
    roi.x = x; roi.y = y; roi.width = width; roi.height = height;
    return roi;
}

