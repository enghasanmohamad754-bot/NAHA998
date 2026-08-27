[app]
title = EngHasan998 Petro Library
package.name = petrolibrary
package.domain = com.enghasan998

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0
requirements = python3,kivy==2.3.0,kivymd==1.2.0,requests,urllib3,certifi,chardet,idna

orientation = portrait
fullscreen = 0

# صلاحيات الإنترنت والحفظ
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
