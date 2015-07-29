#include <node.h>
#include <nan.h>

#include "SomeStuff.h"

NAN_METHOD(Foo)
{
    NanScope();

    SomeStuff s;

    NanReturnValue(s.someMethod());
}

void InitAll(v8::Handle<v8::Object> exports)
{
    exports->Set(NanNew<v8::String>("foo"),
                 NanNew<v8::FunctionTemplate>(Foo)->GetFunction());
}

NODE_MODULE(module1, InitAll)
