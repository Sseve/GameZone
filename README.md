### GameZone

* *环境依赖*
```
  - master
    ansible 2.7
    master和node节点免密登录
    master和node节点都创建一个gamecpp用户,使用gamecpp用户进行相关操作
  
  - node
    svn version 1.7.14
```


* *游戏区服操作示例*
```
  - 说明:
    新节点上进行开服需按照hosts文件中的格式进行添加

  - 开服:
    修改hosts文件[opennode]选择节点机器进行开服
    ansible-playbook open.yml --extra-vars "zone=num"
    num指定具体的区服id

  - 区服更新: 程序及其配置更新
    ansible-playbook update.yml

  - 区服操作: start, stop, check, reload; operate对应的值
    ansible-playbook operate.yml --extra-vars "operate='start'"
```
