检查市是否连接上github
git remote -v
ssh -T git@github.com

克隆项目
git clone 项目地址

创建公钥
ssh-keygen -t rsa -C "396321556@qq.com"
将本地的公钥复制下来，粘贴到github的ssh处
再次检查 ssh -T git@github.com，提示成功

连接远程仓库
git remote add origin https://github.com/77dx/testcase_manager.git

提交代码到远程仓库
git push -u origin master

查看本地分支
git branch

查看远程分支
git branch -r

查看所有分支
git branch -a

切换远程分支
git checkout -b myRelease(new branch) origin/master

本地分支与远程不一致
需要重新拉取远程的代码和分支
git init
git remote add origin xxxx.git  //这里的xxxx是指的你项目的地址
git fetch origin xxx   //xxx为你远端新建的分支名字
git checkout -b 本地要创建的分支名字 origin/远端新创建的分支名字
git pull origin 远端分支    //这条命令就是从远端分支拉取自己的项目
git status   //查看当前修改未提交的内容
git add .     //添加操作，后面的点代表全部添加，也可以只添加修改的，但是点更方便
git commit -m"这里是提交的日志"      //提交到本地仓库
git push origin HEAD:远端分支名       // 提交到远端

从github拉取代码，取回 origin/master 分支，再与本地的 master 分支合并
git pull origin master


创建django app
django-admin.py startapp TestModel

数据库迁移
python manage.py migrate    # 创建表结构
python manage.py makemigrations    #让 Django 知道我们在我们的模型有一些变更

生成requirements.txt
pip freeze > requirements.txt
安装requirements.txt
pip install -r requirements.txt

集成前端vue
npm install -g vue-cli
切换npm源
npm install -g cnpm --registry=https://registry.npm.taobao.org
cnpm install

在项目根目录下，创建前端工程
vue-init webpack appfront

修改启动脚本会报错的问题
查出进程id,并杀掉进程
kill -9 $(ps -ef |grep python | grep -v grep | awk '{print $2}')