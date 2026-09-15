# hermes-plugin-poc

安全审计 PoC 插件(金丝雀,无功能)。

用途:验证 hosted hermes 沙箱内 `hermes plugins install <git-url>` 的任意代码
安装路径(Spark AI 2026-09-15 审计 H-11)。安装使用 `--no-enable`,插件不会被
加载;`plugin.py` 若被导入仅写入 /tmp 金丝雀标记,不读取任何秘密、不发起网络请求。

审计结束后删除。
