### GameZone

* *环境依赖*
```
  - master
    主机系统: centos7
    python版本: python3.9
    python包管理工具: pipenv
    
    - 安装pipenv: python -m pip install pipenv
    - 创建项目: mikdir ProjectName && cd ProjectName && pipenv --python 3.9
    - 激活虚拟环境: pipenv shell
    - 安装ansible: pipenv install ansible

    master和node节点免密登录
    master和node节点都创建一个gamecpp用户,使用gamecpp用户进行相关操作
  
  - node
    svn version 1.7.14
```


* *游戏区服操作示例*
```
  - 说明:
    新节点上进行开服需按照hosts文件中的格式进行添加
    每次开完服在record.txt文件中记录区服与node信息

  - 开服:
    修改hosts文件[opennode]选择节点机器进行开服
    ansible-playbook open.yml --extra-vars '{"zone_name": "test_syf", "zone_num": [1,2,3]}'
    zone_name: 区服名称, zone_num: 区服id列表

  - 区服更新: 程序及其配置更新
    ansible-playbook update.yml --extra-vars '{"zone_name": "test_syf", "zone_num": [1,2], "opt":"con"}'
    zone_name: 区服名称, zone_num: 区服id列表, opt: [bin|con] => [更新binfile|更新配置]

  - 区服操作: start, stop, check, reload; operate对应的值
    ansible-playbook operate.yml --extra-vars '{"zone_name": "test_syf", "zone_num": [1,6], "act": "start"}'
    zone_name: 区服名称, zone_num: 区服id列表, act: [start|stop|check|reload] => [启动|关闭|检查|重载]
```
