#include <iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>

#define THRESHOLD 0.7
#define FIND_TARGET_NUM 30

int main(int argc, char** argv) {
    // src::走査する画像
    // tmp::テンプレート用の画像
    cv::Mat src = cv::imread("C:\\Users\\oslab\\Documents\\laser_mean\\beehive\\2.5.png", 1);
    cv::Mat tmp = cv::imread("C:\\Users\\oslab\\Documents\\laser_mean\\beehive\\2.6.png", 1);
    cv::Mat result, dist;
    src.copyTo(dist);

    // template matching
    // src::入力
    // tmp::テンプレート
    // result:: 出力
    // cv::TM_CCOEFF_NORMED::比較手法の検討（正規化相関係数）
    cv::matchTemplate(src, tmp, result, cv::TM_CCOEFF_NORMED);

    //minMaxLoc で最小値・最大値を result から見つける
    double val;
    cv::Point loc;
    cv::minMaxLoc(result, NULL, &val, NULL, &loc);

    for (int i = 0; i<FIND_TARGET_NUM && fabs(val) > THRESHOLD; ++i) {

        //検出部分のマスク
        cv::rectangle(result, cv::Point(loc.x - tmp.cols / 2, loc.y - tmp.rows / 2), cv::Point(loc.x + tmp.cols / 2, loc.y + tmp.rows / 2), cv::Scalar(0), -1);
        //出力用画像への描画
        cv::rectangle(dist, cv::Point(loc.x, loc.y), cv::Point(loc.x + tmp.cols, loc.y + tmp.rows), cv::Scalar(0, 0, 255), 2);
        //再度最大値を持つ画素の検索
        cv::minMaxLoc(result, NULL, &val, NULL, &loc);
    }



    cv::imshow("canny", dist);
    cv::waitKey(0);
    //cv::imshow("Lap", img_l);

    //結果画像の出力
    cv::imwrite("../picture/output.png", dist);

    return 0;
}
