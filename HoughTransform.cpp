#include <iostream>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc.hpp>

#pragma comment( lib, "opencv_world455d.lib" )

int main(int argc, const char* argv[])
{
    int hr = -1;

    try
    {
        cv::Mat src, edge, dst;
        std::vector<cv::Vec4i> lines;

        src = cv::imread("C:\\Users\\.~~png", cv::IMREAD_GRAYSCALE);

        cv::namedWindow("src", 1);
        imshow("src", src);

        cv::Canny(src, edge, 50, 200, 3);

        dst = cv::Mat::zeros(src.rows, src.cols, CV_8UC3);

        int fromTo[] = { 0, 2, 0, 1, 0, 0 };

        cv::mixChannels(&src, 1, &dst, 1, fromTo, 3);

        cv::HoughLinesP(
            edge,           
            lines, //ここに出力，配列として
            1,              
            CV_PI / 180.0,  
            80,             
            30,             
            10              
        );

        for (auto line : lines)
        {
            cv::line(dst, cv::Point(line[0], line[1]), cv::Point(line[2], line[3]), cv::Scalar(0, 0, 255), 1);
        }

        cv::namedWindow("dst", 1);
        cv::imshow("dst", dst);

        cv::waitKey(0);

        hr = 0;
    }

    catch (cv::Exception ex)
    {
        std::cout << ex.err << std::endl;
    }

    cv::destroyAllWindows();

    return hr;
}

//ref:http://maverickproj.web.fc2.com/OpenCV_45.html
