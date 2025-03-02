minecraft_commands=[
    "kill",
    "gamerule",
    "op",
    "deop",
    "whitelist",
    "ban",
    "unban",
    "msg",
    "near",
    "whois",
    "seen",
    "sudo",
    "give",
    "time",
    "tp",
    "weather",
    "stop"
]






minecraft_commands_help={
    "kill":"杀死玩家,用法:/kill <玩家名>/n如：/kill 迷你世界",
    "gamerule":"游戏规则,用法:/gamerule <规则名> <规则值>\n如：/gamerule keepInventory true",
    "op":"操作员,用法:/op <玩家名>\n如：/op Notch",
    "deop":"取消操作员,用法:/deop <玩家名>\n如：/deop Notch",
    "whitelist":"白名单管理,用法:/whitelist <add/remove> <玩家名>\n如：/whitelist add Notch\n/whitelist remove Notch",
    "ban":"封禁玩家,用法:/ban <玩家名> <原因>\n如：/ban Notch 玩家恶意破坏服务器",
    "unban":"解封玩家,用法:/unban <玩家名>\n如：/unban Notch",
    "msg":"发送私聊消息,用法:/msg <玩家名> <消息内容>\n如：/msg Notch 你好，欢迎来到服务器！",
    "near":"附近玩家,用法:/near <玩家名>\n如：/near Notch",
    "whois":"查询玩家信息,用法:/whois <玩家名>\n如：/whois Notch",
    "seen":"查询玩家上次在线时间,用法:/seen <玩家名>\n如：/seen Notch",
    "sudo":"以玩家身份执行命令,用法:/sudo <玩家名> <命令>\n如：/sudo Notch /kill",
    "give":"给玩家物品,用法:/give <玩家名> <物品ID> <数量>\n如：/give Notch minecraft:dirt 64",
    "time":"设置服务器时间,用法:/time <方法> <时间>\n如：/time set 1000",
    "tp":"传送玩家,用法:/tp <玩家名>\n如：/tp Notch",
    "weather":"设置天气,用法:/weather <天气>\n如：/weather clear",
    "stop":"停止服务器,用法:/stop\n如：/stop"
}