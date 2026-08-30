[app]

# ============================================================
# INFORMACIÓN DE LA APLICACIÓN
# ============================================================

title = Overlord

package.name = overlord

package.domain = org.aurora

source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt

source.exclude_dirs = .git,.github,.buildozer,bin,venv,__pycache__,tests

version = 0.1.0


# ============================================================
# DEPENDENCIAS PYTHON
# ============================================================

requirements = python3,kivy


# ============================================================
# CONFIGURACIÓN DE LA APLICACIÓN
# ============================================================

orientation = portrait

fullscreen = 0


# ============================================================
# ICONO Y PANTALLA DE INICIO
# ============================================================

# Si tienes estos archivos, puedes quitar el #:
#
# icon.filename = %(source.dir)s/data/icon.png
# presplash.filename = %(source.dir)s/data/presplash.png


# ============================================================
# ANDROID
# ============================================================

# API de Android
android.api = 35

# API mínima compatible
android.minapi = 24

# NDK
android.ndk = 25b

# API utilizada por el NDK
android.ndk_api = 24


# ============================================================
# ARQUITECTURA
# ============================================================

# Empezamos solamente con ARM64.
#
# Esto evita que el primer build tenga que compilar
# simultáneamente arm64-v8a + armeabi-v7a.

android.archs = arm64-v8a


# ============================================================
# APK DEBUG
# ============================================================

android.debug_artifact = apk


# ============================================================
# BACKUP DE ANDROID
# ============================================================

android.allow_backup = True


# ============================================================
# PERMISOS
# ============================================================

# Internet suele ser necesario para aplicaciones que
# utilizan conexiones de red.

android.permissions = android.permission.INTERNET


# ============================================================
# ANDROIDX
# ============================================================

# No activar AndroidX salvo que alguna dependencia Java
# de tu aplicación realmente lo necesite.


# ============================================================
# PYTHON-FOR-ANDROID
# ============================================================

# Bootstrap utilizado por Kivy.
p4a.bootstrap = sdl2

# Usar el proyecto oficial de python-for-android.
p4a.fork = kivy

# Dejamos que Buildozer seleccione una revisión compatible.
# No fijamos aquí un commit antiguo.


# ============================================================
# OPCIONES DE COMPILACIÓN
# ============================================================

# Copiar las librerías en lugar de generar libpymodules.so.
android.copy_libs = 1


# ============================================================
# ORIENTACIÓN
# ============================================================

android.manifest.orientation = portrait


# ============================================================
# BUILDODER
# ============================================================

[buildozer]

# 0 = solo errores
# 1 = información
# 2 = información detallada

log_level = 2

# Mostrar advertencia si Buildozer se ejecuta como root.
warn_on_root = 1


# ============================================================
# FIN
# ============================================================
