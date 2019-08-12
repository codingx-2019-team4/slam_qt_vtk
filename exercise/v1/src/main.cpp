#include <cstdio>

#include <opencv2/opencv.hpp>
#include <opencv2/imgproc/imgproc.hpp>

#include <Eigen/Geometry>

#include <boost/format.hpp>

#include <pcl-1.9/pcl/point_types.h>

using namespace cv;

int main(int argc, char **argv) {
    Mat img = imread("../img/dog.jpg",1);

    while(true){

        imshow("Display window", img);     

        if(cvWaitKey(10)==27){                      

            break;

        }

    }

    return 0;

}
