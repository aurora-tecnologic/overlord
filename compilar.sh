export ac_cv_func_sem_clockwait=no
export ac_cv_func_pthread_getname_np=no
export ac_cv_func_pthread_setname_np=no
export ac_cv_func_close_range=no
export ac_cv_func_fexecve=no
export ac_cv_func_getlogin_r=no
export ac_cv_func_preadv2=no
export ac_cv_func_pwritev2=no
export ac_cv_func_copy_file_range=no
export ac_cv_func_getloadavg=no
export ac_cv_func_getpwent=no
export ac_cv_func_setpwent=no
export ac_cv_func_endpwent=no

export PKG_CONFIG_PATH=""
export PKG_CONFIG_LIBDIR=""
export PKG_CONFIG="/data/data/com.termux/files/usr/bin/pkg-config"
export CFLAGS="-I/data/data/com.termux/files/usr/include"
export LDFLAGS="-L/data/data/com.termux/files/usr/lib"

buildozer -v android debug
