# collafl
trying to implementing collafl.

Inorder to use this, we have to install llvm gold linker first. check [this](https://github.com/aflgo/oss-fuzz/blob/master/infra/base-images/base-clang/checkout_build_install_llvm.sh) out.

I modify llvm_mode/afl-llvm-pass.so.cc file to support computing hash described in [CollAFL: Path Sensitive Fuzzing](http://chao.100871.net/papers/oakland18.pdf) paper
