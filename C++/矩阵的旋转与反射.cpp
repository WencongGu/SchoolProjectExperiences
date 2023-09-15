#include<iostream>
#include<conio.h>
#include<fstream>
using namespace std;
template<class T>
class CMatrix
{
	T** Mat;         //head pointer of the matrix
	int num;         //the amount of the row or column
	T** MatR;        //transfered
	T** MatRefl;     //reflected
public:
	CMatrix();       //constructor
	CMatrix(T** mat, int n);//constructor
	CMatrix(int n);  //constructor
	~CMatrix();      //destructor
	void Show(int k = 0);//print,k=0means the primary,
						 //k=1means the transfered,k=2means the reflected
	void R90();          //90degrees
	void R180();         //180degrees
	void R270();         //270degrees
	void reflectX(int k=0);     //reflect by X
	void reflectY(int k=0);     //reflect by Y
	void reflectP(int k = 0);   //reflect by POINT
	int lookfordata();   //look for a data
	int findbeforemoddata();//find before modifying
	int modifydata(int row, int column);// do modify
	double range();      //find the value of the determinan
	void inputfromfile();//datas come from the file
};
template<class T>
CMatrix<T>::CMatrix()
{
	int i,r, c;  ;
	num=5;
	Mat = new T * [num];
	MatR = new T * [num];
	MatRefl = new T * [num];
	for (i = 0; i < num; i++)
	{
		Mat[i] = new T;
		MatR[i] = new T;
		MatRefl[i] = new T;
	}
	    //为默认矩阵赋初值
	for (r = 0; r < 5; r++)
		for (c = 0; c < 5; c++)
		{
			Mat[r][c] = r * 5 + c + 1;
			MatR[r][c] = Mat[r][c];
			MatRefl[r][c] = Mat[r][c];//全体初始化，避免无值
		}
}//Use for supplying/creating the default matrix
template<class T>
CMatrix<T>::CMatrix(T** m, int n)
{
	int i,j;
	num = n;
	Mat = new T * [num];
	for (i = 0; i < num; i++)
	{
		Mat[i] = new T;
	}
	for(i=0;i<num;i++)
		for(j=0;j<num;j++)
		{
			Mat[i][j] = m[i][j];
		}

}                   //This part needs perfection.Didn't use it.//AFTER:Use for inputing from keyboard
template<class T>
CMatrix<T>::CMatrix(int n)
{
	int i;
	num = n;
	Mat = new T * [num];
	MatR = new T * [num];
	MatRefl = new T * [num];
	for (i = 0; i < num; i++)
	{
		Mat[i] = new T;
		MatR[i] = new T;
		MatRefl[i] = new T;
	}
	//Just distribute space without doing anything
}//Use for inputing from files
template<class T>
double CMatrix<T>::range()
{
	int  i, j,k;
	T** m;
	m = new T * [num];
	for (i = 0; i < num; i++)
	{
		m[i] = new T;
	}
	for (i = 0; i < num; i++)
		for (j = 0; j < num; j++)
			m[i][j] = Mat[i][j];
	double t;
	
	      for (k = 0; k < num; k++)
		  for (i = k + 1; i < num; i++)
		  for (j = k + 1; j < num; j++)
			  {
				  if(m[k][k]==0)
					 {for(int p=0;p<num;p++)
					        if(m[k][p]!=0&&m[k][k]==0)
						       for(int q=0;q<num;q++)
					                m[q][k]+=m[q][p];
							        
					        else if(m[k][k]!=0)       
					               break;
							else
								return 0;
					 t = m[i][k] / m[k][k];
		             m[i][j]+=-t * m[k][j];
				      }
			        
			      else
				    {t = m[i][k] / m[k][k];
		             m[i][j]+=-t * m[k][j];}
		  }
	double o = 1;
	for (i = 0; i < num; i++)
		o = o * m[i][i];
	delete []m;
	return o;
}         //got some trouble needed to be fixed......two days later still don't know......
template<class T>
CMatrix<T>::~CMatrix()
{
	delete []Mat;
	delete []MatR;
	delete []MatRefl;
}                 //destructor
template<class T>
void CMatrix<T>::R90()
{
	int r, c;
	for (r = 0; r < num; r++)
		for (c = 0; c < num; c++)
			MatR[num-1 - c][r] = Mat[r][c];//√
}
template<class T>
void CMatrix<T>::R180()
{
		int r, c;
		for (r = 0; r < num; r++)
			for (c = 0; c < num; c++)
				MatR[num -1- r][num-1 - c] = Mat[r][c];//√
}
template<class T>
void CMatrix<T>::R270()
{
		int r, c;
		for (r = 0; r < num; r++)
			for (c = 0; c < num; c++)
				MatR[c][num-1 - r] = Mat[r][c];//√
}
template<class T>
void CMatrix<T>::Show(int k)
{    //0-the primary,1-the rotation,2-the reflection.
	int r, c;
	int choice;
	choice = k;
	if (choice == 0)     //0-refers to the primary
	{
		cout << "  矩阵载入为：" << endl;
	    for (r = 0; r < num; r++)
		{
			for (c = 0; c < num; c++)
			{
				if (Mat[r][c] < 10)
					cout << " " << Mat[r][c] << " ";
				else
					cout << Mat[r][c] << " ";
			}
			cout << endl;
		}
	}
	if (choice == 1)     //1-refers to rotation
	{
		cout << "Array ROTATION:\n";
		for (r = 0; r < num; r++)
		{
			for (c = 0; c < num; c++)
			{
				if (MatR[r][c] < 10)
					cout << " " << MatR[r][c] << " ";
				else
					cout << MatR[r][c] << " ";
			}
			cout << endl;
		}
	}
	if (choice == 2)	 //2-refers to reflection
	{
		cout << "Array REFLECTION:\n";
		for (r = 0; r < num; r++)
		{
			for (c = 0; c < num; c++)
			{
				if (MatRefl[r][c] < 10)
					cout << " " << MatRefl[r][c] << " ";
				else
					cout << MatRefl[r][c] << " ";
			}
			cout << endl;
		}
	}
}
template<class T>
void CMatrix<T>::reflectX(int k)
{//k=1-reflect the primary,k=0-reflect the rotation.
	int r, c;
	if(k==1)//primary
	{ 
		for (r = 0; r < num; r++)
			for (c = 0; c < num; c++)
				MatRefl[r][c] = Mat[num-1 - r][c];
    }
	if (k == 0)//rotation
	{
		for (r = 0; r < num; r++)
			for (c = 0; c < num; c++)
				MatRefl[r][c] = MatR[num-1 - r][c];
	}
}
template<class T>
void CMatrix<T>::reflectY(int k)
{//k=1-reflect the primary,k=0-reflect the rotation.
	int r, c;
	if (k==1)//primary
	{
	for (r = 0; r < num; r++)
		for (c = 0; c < num; c++)
			MatRefl[r][c] = Mat[r][num-1 - c];
    }
	if (k == 0)//rotation
	{
		for (r = 0; r < num; r++)
			for (c = 0; c < num; c++)
				MatRefl[r][c] = MatR[ r][num-1-c];
	}
}
template<class T>
void CMatrix<T>::reflectP(int k)
{//k=1-reflect the primary,k=0-reflect the rotation.
	int r, c;
	if(k==1)//primary
	{for (r = 0; r < num; r++)
		for (c = 0; c <num; c++)
			MatRefl[r][c] = Mat[num-1 - r][num-1 - c];
	}
	if (k == 0)//rotation
	{
		for (r = 0; r < num; r++)
			for (c = 0; c < num; c++)
				MatRefl[r][c] = MatR[num-1 - r][num-1-c];
	}
}
template<class T>
int CMatrix<T>::lookfordata()
{
	int n=0;
	T k;
	cout << "INPUT the data you wanted (in primary matrix):  " << endl;
	cin >> k;
	for (int i = 0; i < num; i++)
		for (int j = 0; j < num; j++)
		{
			if (Mat[i][j] == k)
			{
				cout << "row= " << i + 1 << "\tcolumn= " << j + 1 << endl;
				n++;
			}
			else
				continue;
		}
	if (n!= 0)
	{
		cout << "TALTOLLY:  " << n << endl;
		cout << "The primary matrix has been found. Thanks.\n";
	}
	if (n == 0)
	{
		cout << "COULDNOT FIND IT. SORRY.\n";
	}
	return n;    //非0表示找到了所求数，为0时表示未找到
	
}
template<class T>
int CMatrix<T>::findbeforemoddata()
{
	int i,j, n = 0;
	T m, k;
	cout << "INPUT the data you're looking for  (in primary matrix):  \n";
	cin >> k;
	cout << "The system will look for them first,then modify directly." << endl;
	for ( i = 0; i < num; i++)
		for ( j = 0; j < num; j++)
		{
			if (Mat[i][j] == k)
			{
				cout << "row=  " << i + 1 << "column=  " << j + 1 << endl;
				n++;
			}
			else
				continue;
		}
	if (n != 0)
	{
		cout << "TALTOLLY:  " << n << endl;
		cout << "INPUT the data instead:\n";
	    cin >> m;
	    for ( i = 0; i < num; i++)
		  for ( j = 0; j < num; j++)
		  {
			if (Mat[i][j] == k)
			{
				Mat[i][j] = m;
			}
			else
				continue;
		  }
		cout << "Data in the primary matrix has been modified.  Thanks.\n";
		this->Show(0);
	}
	if(n==0)
	{
		cout << "There's no "<<k<<" in the matrix. \nNo need to bother change it.\n";
	}
	return n;    //非0表示找到了所求数，为0时表示未找到
}
template<class T>
int CMatrix<T>::modifydata(int r,int c)
{
	T k;
	cout << "INPUT the data you're taking instead:\n";
	cin >> k;
	Mat[r-1][c-1] = k;
	cout<<"Done.  Thanks.\n";
	this->Show(0);
	return 1;
}
template<class T>
void CMatrix<T>::inputfromfile()
{
	ifstream infile("a",ios_base::binary);
	if (!infile)
	{
		cout << "输入文件失败,请检查您的文件后重试！" << endl;
		exit(0);
	}
	int i, j;
	num = 5;
	for (i = 0; i < num; i++)
		for (j = 0; j < num; j++)
		{
		    infile >> Mat[i][j];
		}
	infile.close();
}

//菜单显示
void xuanzhuancaidan()     //旋转菜单
{
	cout << "\n当前界面为“旋转”，请选择角度：\n";
	cout << "        1） 90°" << endl;
	cout << "        2） 180°" << endl;
	cout << "        3） 270°" << endl;
	cout << "        4） 退出" << endl;
}
void fanshecaidan()       //反射菜单
{
	cout << "   正在准备进行反射操作，请选择反射轴  " << endl;
	cout << "        1） X轴" << endl;
	cout << "        2） Y轴" << endl;
	cout << "        3） 对角线" << endl;
	cout << "        4） 退出" << endl;
}
void qitacaozuo()        //其他操作
{
	cout << "\n当前界面为“其他操作”，请选择：\n";
	cout << "        1） 查找" << endl;
	cout << "        2） 替换" << endl;
	cout << "        3） 模" << endl;
	cout << "        4） 退出" << endl;
}
//菜单操作
//整型
CMatrix<int>* i;
void fucaidanint()          //副菜单
{
	int j,n,r, c,k;
	do
	{
	i->Show(0);
	cout << " 菜单" << endl;
	cout << "1. 旋转" << endl;
	cout << "2. 反射" << endl;
	cout << "3. 其他操作" << endl;
	cout << "4. 退出" << endl;
	cout << "    请选择:" << endl;
	cin >> j;
		if (j == 1)    //旋转
		{
			do
			{
				xuanzhuancaidan();//显示旋转菜单
				cin >> n;
				if (n == 1)
				{
					i->R90();
					i->Show(1);
				}
				if (n == 2)
				{
					(*i).R180();
					i->Show(1);
				}
				if (n == 3)
				{
					(*i).R270();
					i->Show(1);
				}
			} while (n != 4);//循环进入旋转角度选择界面，直到按4退出j=1的循环
			cout << "您选择“退出”，已返回上一级。\n";
		}
		if (j == 2)//反射
		{
			do
			{
				cout << "当前界面为“反射”。\n";
				cout << "请选择：\n  对原矩阵反射      （1）\n  对旋转后的矩阵反射（0）\n";
				cin >> k;
				if (k == 1)
				{
					cout << "您选择对原矩阵反射\n";
					fanshecaidan();
					cin >> n;
					if (n == 1)
					{
						cout<<"X轴反射"<<endl;
						(*i).reflectX(1);
						i->Show(2);
					}
					if (n == 2)
					{
						cout<<"Y轴反射"<<endl;
						(*i).reflectY(1);
						i->Show(2);
					}
					if (n == 3)
					{
						cout<<"对角线反射"<<endl;
						(*i).reflectP(1);
						i->Show(2);
					}
				}
				if(k==0)
				{
					cout <<"您选择对您上次旋转操作后得到的矩阵进行反射\n";
					fanshecaidan();
					cin >> n;
					if (n == 1)
					{
						cout<<"X轴反射"<<endl;
						(*i).reflectX(0);
						i->Show(2);
					}
					if (n == 2)
					{
						cout<<"Y轴反射"<<endl;
						(*i).reflectY(0);
						i->Show(2);
					}
					if (n == 3)
					{
						cout<<"对角线反射"<<endl;
						(*i).reflectP(0);
						i->Show(2);
					}
				}
			} while (n != 4); //循环进入反射轴选择界面，直到按4退出j = 2的循环
			cout << "您选择“退出”，已返回上一级。\n";
		}
		if (j == 3)//其他操作
		{
			do
			{
				qitacaozuo();
				cin >> n;
				if (n == 1)
				{
					(*i).lookfordata();
				}
				if (n == 2)
				{
					(*i).findbeforemoddata();
					cout << "INPUT the row and column you want:\n";
					cin >> r >> c;
					i->modifydata(r, c);
				}
				if (n == 3)
				{
					cout << "the det of the matrix is:   " << (*i).range() << endl;
				}
			} while (n != 4);
			cout << "您选择“退出”，已返回上一级。\n";//循环进入其他选择选择界面，直到按4退出j = 3的循环
		}
	} while (j != 4);//循环进入选择三个操作的界面，直到按4，因此可以多次操作求结果
	cout << "您选择“退出”，已返回上一级。\n";
}       //副菜单是精华，但也是出错最多的地方......
void zhucaidanint()
{   
	int m,n;
	cout << "此程序使用int型数据代替模板的T\n";
	do
	{
	cout << "   主菜单： \n";
	cout << "1. 从文件中输入矩阵" << endl;
	cout << "2. 从键盘输入矩阵" << endl;
	cout << "3. 使用默认的矩阵形式" << endl;
	cout << "4. 退出" << endl;
	cout << "请选择" << endl;
		cin >> m;
		if (m == 1)
		{
			cout << "您选择“从文件中输入矩阵”，请确保您的文件完整、可读。\n";
			i = new CMatrix<int>(5);
			i->inputfromfile();
			fucaidanint();
	    }
		if (m == 2)
		{    
			cout << "您选择“从键盘输入矩阵”，请输入：\n";
			cout << "请先键入矩阵维数：\t";
			cin >> n;
			cout<<endl;
			int  l, j;
	        int** m;
	        m = new int * [n];
	        for (l = 0;l < n; l++)
	           {
		         m[l] = new int;
	           }
			cout << "Please input your data:\n";
	for (l = 0; l < n; l++)
		for (j = 0; j < n; j++)
		{
			cout << "Mat [" << l + 1 << "][" << j + 1 << "]=\t";
			cin >> m[l][j];

		}
			i = new CMatrix<int> (m,n);
			fucaidanint();
			delete []m;
		}
		if (m == 3)
		{
			cout << "您已选择“使用默认的矩阵形式”，系统为您生成了一个5级矩阵:\n";
			i = new CMatrix<int>();
			fucaidanint();
		}
    } while (m != 4);//副菜单选择“退出”时进入此处的循环，从而实现多次操作，直到选择4退出程序
	    cout << "您选择“退出”，请按任意键继续。\n";
		delete i;
}
//浮点型
CMatrix<float>* f;
void fucaidanfloat()          //副菜单
{
	int j, n, r, c,k;
	do
	{
		f->Show(0);
		cout << " 菜单" << endl;
		cout << "1. 旋转" << endl;
		cout << "2. 反射" << endl;
		cout << "3. 其他操作" << endl;
		cout << "4. 退出" << endl; 
		cout << "请选择" << endl;
		cin >> j;
		if (j == 1)    //旋转
		{
			do
			{
				xuanzhuancaidan();//显示旋转菜单
				cin >> n;
				if (n == 1)
				{
					f->R90();
					f->Show(1);
				}
				if (n == 2)
				{
					(*f).R180();
					f->Show(1);
				}
				if (n == 3)
				{
					(*f).R270();
					f->Show(1);
				}
			} while (n != 4);//循环进入旋转角度选择界面，直到按4退出j=1的循环
			cout << "您选择“退出”，已返回上一级。\n";
		}
		if (j == 2)//反射
		{
			do
			{
				cout << "当前界面为“反射”。\n";
				cout << "请选择“对原矩阵反射（1）、对旋转后的矩阵反射（0）：\n";
				cin >> k;
				if (k == 1)
				{
					fanshecaidan();
					cin >> n;
					if (n == 1)
					{
						cout<<"X轴反射"<<endl;
						(*f).reflectX(1);
						f->Show(2);
					}
					if (n == 2)
					{
						cout<<"Y轴反射"<<endl;
						(*f).reflectY(1);
						f->Show(2);
					}
					if (n == 3)
					{
						cout<<"对角线反射"<<endl;
						(*f).reflectP(1);
						f->Show(2);
					}
				}
				if (k == 0)
				{
					fanshecaidan();
					cin >> n;
					if (n == 1)
					{
						cout<<"X轴反射"<<endl;
						(*f).reflectX(0);
						f->Show(2);
					}
					if (n == 2)
					{
						cout<<"Y轴反射"<<endl;
						(*f).reflectY(0);
						f->Show(2);
					}
					if (n == 3)
					{
						cout<<"对角线反射"<<endl;
						(*f).reflectP(0);
						f->Show(2);
					}
				}
			} while (n != 4); //循环进入反射轴选择界面，直到按4退出j = 2的循环
			cout << "您选择“退出”，已返回上一级。\n";
		}
		if (j == 3)//其他操作
		{
			do
			{
				qitacaozuo();
				cin >> n;
				if (n == 1)
				{
					(*f).lookfordata();
				}
				if (n == 2)
				{
					(*f).findbeforemoddata();
					cout << "INPUT the row and column you want:\n";
					cin >> r >> c;
					f->modifydata(r, c);
				}
				if (n == 3)
				{
					cout << "the det of the matrix is:   " << (*f).range() << endl;
				}
				} while (n != 4); 
			cout << "您选择“退出”，已返回上一级。\n";//循环进入其他选择选择界面，直到按4退出j = 3的循环
		}
	} while (j != 4);//循环进入选择三个操作的界面，直到按4，因此可以多次操作求结果
	cout << "您选择“退出”，已返回上一级。\n";
}       //副菜单是精华，但也是出错最多的地方......
void zhucaidanfloat()
{
	int m, n;
	cout<<"您当前在测试浮点型模板"<<endl;
	do
	{
	cout << "   主菜单： \n";
	cout << "1. 从文件中输入矩阵" << endl;
	cout << "2. 从键盘输入矩阵" << endl;
	cout << "3. 使用默认的矩阵形式" << endl;
	cout << "4. 退出" << endl;
	cout << "请选择" << endl;
	cin >> m;
		if (m == 1)
		{
			cout << "您选择“从文件中输入矩阵”，请确保您的文件完整、可读。\n";
			f = new CMatrix<float>(5);
			f->inputfromfile();
			fucaidanfloat();
		}
		if (m == 2)
		{
			cout << "您选择“从键盘输入矩阵”，请输入：\n";
			cout << "请先键入矩阵维数：\t";
			cin >> n;
			cout<<endl;
			int  i, j;
	        float** m;
	        m = new float * [n];
	        for (i = 0; i < n; i++)
	           {
		         m[i] = new float;
	           }
			cout << "Please input your data:\n";
	for (i = 0; i < n; i++)
		for (j = 0; j < n; j++)
		{
			cout << "DATA NO.[" << i + 1 << "][" << j + 1 << "]=\t";
			cin >> m[i][j];

		}
			f = new CMatrix<float> (m,n);
			fucaidanint();
			delete []m;
		}
		if (m == 3)
		{
			f = new CMatrix<float>();
			cout << "您已选择“使用默认的矩阵形式”，系统为您生成了一个5级矩阵:\n";
			f->Show(0);
			fucaidanfloat();
		}
	} while (m != 4);//副菜单选择“退出”时进入此处的循环，从而实现多次操作，直到选择4退出程序
	cout << "您选择“退出”，请按任意键继续。";
	delete f;
}


//测试函数
void floattest()
{
	cout << "请问您还需要验证float型数据下的类吗？\n";
	cout << "是（1）          否（2）\n";
	int a;
	cin >> a;
	if (a == 1)
	{
		zhucaidanfloat();
	}
	else
		exit(0);
}
void test()
{
	cout << "程序诊断中，请稍候......\n";
	CMatrix<int>* t;
	t=new CMatrix<int>();
	t->Show(0);
	cout << "det:"<<t->range()<< endl;
	cout << "创建对象正常" << endl;
	ifstream infile("a",ios_base::binary);
	if (!infile)
	{
		cout << "输入文件失败,请重试！" << endl;
	}
	int** m;
	int  i, j;
	int num = 5;
	m = new int * [num];
	for (i= 0; i < num; i++)
	{
		m[i] = new int;//构造5级矩阵
	}
	for (i = 0; i < num; i++)
		for (j = 0; j < num; j++)
		{
		    infile >> m[i][j];//输入流赋值给矩阵m
		}
	ofstream outfile("b",ios_base::binary);
	for (i = 0; i < num; i++)
		for (j = 0; j < num; j++)
		{
		    outfile<<m[i][j];//输入流矩阵写入文件
		}
	for (i = 0; i < num; i++)
		{
			for (j = 0; j < num; j++)
		        {
		          cout<<m[i][j]<<'\t';
		        }
	        cout<<endl;
	    }//输出输入流的矩阵
	if (infile)
	{
		cout << "输入流正常" << endl;
	}
	if (outfile)
	{
		cout << "输出流正常" << endl;
	}
    infile.close();
	outfile.close();
	cout << "测试完成。\n";
}

//主函数
int main()
{
	test();
	zhucaidanint();
	floattest();
	return 1;
}

//第九次修改，优化部分交互体验，修复部分bug。
//解决上次修改遗留问题。构造函数已经修复。程序功能完备。交互体验有上升空间，但是程序已经足够优秀了。基本排除了可能出现的bug
//第十次修改，精简主函数；优化程序，删除了部分无用变量，提高效率；修复bug。至此程序完成。