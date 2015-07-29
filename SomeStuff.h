#ifndef SOME_STUFF_H
#define SOME_STUFF_H

#ifdef _EXPORTING
   #define CLASS_DECLSPEC    __declspec(dllexport)
#else
   #define CLASS_DECLSPEC    __declspec(dllimport)
#endif

class CLASS_DECLSPEC SomeStuff
{
public:
    int someMethod();
};

#endif // SOME_STUFF_H
