#include <iostream>
#include <vector>

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>

#include <Eigen/Geometry>
#include <boost/format.hpp>

#include <pcl/point_types.h>
#include <pcl/io/pcd_io.h>
#include <pcl/visualization/pcl_visualizer.h>
#include <pcl/visualization/cloud_viewer.h>

#include <pcl/io/io.h>

using namespace std;
int user_data;
    
void 
viewerOneOff (pcl::visualization::PCLVisualizer& viewer)
{
    viewer.setBackgroundColor (0, 0, 0);
    pcl::PointXYZ o;
    o.x = 1.0;
    o.y = 0;
    o.z = 0;
    viewer.addSphere (o, 0.25, "sphere", 0);
    
}
    
void 
viewerPsycho (pcl::visualization::PCLVisualizer& viewer)
{
    static unsigned count = 0;
    std::stringstream ss;
    ss << "Once per viewer loop: " << count++;
    viewer.removeShape ("text", 0);
    viewer.addText (ss.str(), 100, 100, "text", 0);
    
    //FIXME: possible race condition here:
    user_data++;
}

int main( int argc, char** argv )
{
    if (argc-1==0) {
        cout<<"Error path to pose.txt file."<<endl;
        return 0;
    }else {
        cout<<"Reading file :"<< argv[1] <<endl;
    }
    ifstream fin(argv[1]);
    if(!fin){
        cout<<"Reading Error!"<<endl;
    }else{
        cout<<"Reading Success!"<<endl;
        cout<<"Start converting!"<<endl;
    }
    vector<cv::Mat> colorImg, depthImg;
    vector<Eigen::Isometry3d, Eigen::aligned_allocator<Eigen::Isometry3d> > poses;

    for(int i=0;i<5;i++){
        boost::format fmt( "./%s/%d.%s" ); //图像文件格式
        colorImg.push_back( cv::imread( (fmt%"color"%(i+1)%"png").str() ));
        depthImg.push_back( cv::imread( (fmt%"depth"%(i+1)%"pgm").str(), -1 )); // 使用-1读取原始图像

        double data[7] = {0};
        for ( auto& d:data )
            fin>>d;
        Eigen::Quaterniond q(data[6],data[3],data[4],data[5]);
        Eigen::Isometry3d T(q);
        T.pretranslate(Eigen::Vector3d(data[0],data[1],data[2]));
        poses.push_back(T);
    }

    double cx = 325.5;
    double cy = 253.5;
    double fx = 518.0;
    double fy = 519.0;
    double depthScale = 1000.0;

    typedef pcl::PointXYZRGB PointT;
    typedef pcl::PointCloud<PointT> PointCloud;

    PointCloud::Ptr pointCloud( new PointCloud );

    for (unsigned int i=0; i<5; i++ ){
        cout<<"Conver image: "<<i<<endl;
        cv::Mat color = colorImg[i];
        cv::Mat depth = depthImg[i];
        Eigen::Isometry3d T = poses[i];

        for ( int v=0; v<color.rows; v++ ){
            for ( int u=0; u<color.cols; u++ ){
                unsigned int d = depth.ptr<unsigned short> ( v )[u]; // 深度值
                if ( d==0 ) continue; // 为0表示没有测量到
                Eigen::Vector3d point;
                point[2] = double(d)/depthScale;
                point[0] = (u-cx)*point[2]/fx;
                point[1] = (v-cy)*point[2]/fy;
                Eigen::Vector3d pointWorld = T*point;

                PointT p ;
                p.x = pointWorld[0];
                p.y = pointWorld[1];
                p.z = pointWorld[2];
                p.b = color.data[ v*color.step+u*color.channels() ];
                p.g = color.data[ v*color.step+u*color.channels()+1 ];
                p.r = color.data[ v*color.step+u*color.channels()+2 ];
                pointCloud->points.push_back( p );
            }
        }
    }
    pointCloud->is_dense = false;
    cout<<"There are "<<pointCloud->size()<<" points."<<endl;

    pcl::io::savePCDFileBinary("map.pcd", *pointCloud );

    
    pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud (new pcl::PointCloud<pcl::PointXYZRGB>);
    pcl::io::loadPCDFile ("map.pcd", *cloud);
    pcl::visualization::CloudViewer viewer ("Simple Cloud Viewer");
    viewer.showCloud(cloud);
    
    //use the following functions to get access to the underlying more advanced/powerful
    //PCLVisualizer
    
    //This will only get called once
    viewer.runOnVisualizationThreadOnce (viewerOneOff);
    
    //This will get called once per visualization iteration
    viewer.runOnVisualizationThread (viewerPsycho);
    while (!viewer.wasStopped ())
    {
    //you can also do cool processing here
    //FIXME: Note that this is running in a separate thread from viewerPsycho
    //and you should guard against race conditions yourself...
    user_data++;
    }



    cout << "End !~~" << endl;
    return 0;
}
