import os
p = "/data/data/com.termux/files/home/overlord/.buildozer/android/platform/python-for-android/pythonforandroid/recipes/libffi/__init__.py"
with open(p, "r") as f:
    c = f.read()

target = "shprint(sh.Command('./configure')"

patch = """
        os.system("find . -type f -name 'config*' -exec termux-fix-shebang {} \\\\; 2>/dev/null")
        os.system("find . -type f -name 'config*' -exec sed -i 's|/bin/sh|/data/data/com.termux/files/usr/bin/sh|g' {} \\\\; 2>/dev/null")
        os.system("find . -type f -name 'configure' -exec termux-fix-shebang {} \\\\; 2>/dev/null")
        os.system("find . -type f -name 'configure' -exec sed -i 's|/bin/sh|/data/data/com.termux/files/usr/bin/sh|g' {} \\\\; 2>/dev/null")
        shprint(sh.Command('./configure')"""

if "termux-fix-shebang" not in c:
    c = c.replace(target, patch)
    with open(p, "w") as f:
        f.write("import os\n" + c)
    print("[+] Receta de libffi purgada de /bin/sh con éxito.")
