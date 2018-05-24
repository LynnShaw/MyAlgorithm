#include <stdio.h>

class Singleton {
public:
    static Singleton *getInstance();

private:
    Singleton();

    Singleton(const Singleton &);

    Singleton &operator=(const Singleton&);

    static Singleton* instance;
};

Singleton::Singleton() {

}
Singleton::Singleton(const Singleton &) {

}
Singleton& Singleton::operator=(const Singleton &) {

}

// 静态成员属于类作用域，但不属于类对象，它的生命周期和普通的静态变量一样，
// 程序运行时进行分配内存和初始化，程序结束时则被释放。
// 所以**不能在类的构造函数中进行初始化。**
Singleton* Singleton::instance=new Singleton();
Singleton* Singleton::getInstance() {
    return instance;
}

int main(){
    Singleton* singleton1 = Singleton::getInstance();
    Singleton* singleton2 = Singleton::getInstance();

    if (singleton1 == singleton2)
        fprintf(stderr,"singleton1 = singleton2\n");

    return 0;
}