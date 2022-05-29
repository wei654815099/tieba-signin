# 百度贴吧自动签到脚本

## 环境变量配置

本脚本未做cookies获取操作，所以需要手动配置需要的cookie至环境变量

环境变量名为：tiebaCookies

配置示范如下：

```json
"env": {
    "tiebaCookies":"BDUSS=dDWWhoRXB0enZQTFEwclJMdFR0MXQ5UVJMQ2pGRTdHUjVhd2t5T3l2UVRjTHBpSVFBQUFBJCQAAAAAAAAAAAEAAAArUb80tPO087ray6cAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABPjkmIT45JicD; STOKEN=2fd87fe56d86a83f5f3f9df604bfecc8f06bd2dbc61755f33e7439242df40664;"
},
```

## 日志等级配置

如果你需要修改日志等级，查看更多程序的信息，需要在环境变量中配置tiebaLogLevel

配置示范如下：

```json
"env": {
    "tiebaCookies":"BDUSS=xUMk9sRm5-QUNCSFQ0eFd0YzNUVW5pSG5MSlZ5RER0dzUzNXVqSFEyNkFncnBpSVFBQUFBJCQAAAAAAAAAAAEAAAArUb80tPO087ray6cAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAID1kmKA9ZJiaG; STOKEN=f3baa843a9331bbe0c1102d2df80a4e56e942a98d121f17469d3b9d0eb8bcff7;",
    "tiebaLogLevel":"20"
},
```

tiebaLogLevel 的具体值意如下：

| 值   | 日志等级        |
| ---- | --------------- |
| 0    | NOTSET          |
| 10   | DEBUG           |
| 20   | INFO            |
| 30   | WARN、WARNING   |
| 40   | ERROR           |
| 50   | FATAL、CRITICAL |

## Docker镜像制作

修改目录下Dockerfile的tiebaCookies和tiebaLogLevel配置

然后执行下面操作：

```shell
docker build .
```

