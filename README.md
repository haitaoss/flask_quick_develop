# flask_quick_develop
这是一个基本的项目模板，直接拿过去就能写项目。修改mysql、redis的连接信息即可

# 项目目录的讲解
这是Flask Web项目的基本目录结构
    蓝图其实就是，蓝图范围内的文件（url路由），先放到一个地方。
    最终在app注册，蓝图的时候，直接将蓝图里面的信息注册到app中

flask_quick_develop是项目的家目录
    logs
        存放log日志文件的目录，可以再project_name/__init__.py文件中修改
    config.py
        项目的配置信息，开发只需要修改里面的mysql数据连接信息
        redis的连接信息
    manage.py
        是项目的启动文件，还可以通过这个文件可以对模型类执行迁移操作
    project_name 具体的项目信息
        static   项目静态文件的存放路径
                 当请求这个应用的地址中是以http://localhost/static开头的，flask就会根据路径去静态资源目录下面找资源
        tasks    这里是放celery程序的代码的
        utils    这是工具方法，
        libs     这是第三方标准库文件
      __init__.py
                有这个文件说明这个目录是python的包
                里面主要是
                    1.创建SQLAlchemy的实例对象。
                    2.创建redis链接对象。
                    3.给flask应用程序添加logger日志。
                    4.配置将session信息保存到redis中
                    5.开启csrf防护（应用wtf扩展包实现的，这个扩展包是将csrf_token保存到session中，验证的时候也是从session中取。和别的csrf校验方式不一样）
                    6.注册项目版本的蓝图（api_1_0）和提供静态文件的蓝图（web_html.py）
      constants.py 存放常量数据 
      web_html.py
                    提供静态资源文件，html。设置csrf_token到cookie中
      api_1_0
                这是项目的版本文件，里面就是模型类，试图文件（新建试图文件记得在，api_1_0/__init__.py文件中导入一下）
# 增加多模块项目

    修改了/project_name/api_1_0/__init__.py 文件，这里面可以写其子模块需要的相同的文件
    在/project_name/api_1_0/ 添加了order和user两个模块
    修改了/project_name/__init__.py 原来是注册api_1_0这个蓝图，现在是注册user和order模块的蓝图。
        注：蓝图是可以指定其静态文件和模板文件的查找路径的（我这里没有使用），但是查找顺序是从项目的静态文件目录和模板文件目录。
        找不到，再从模板的势力范围内查找。所以直接把静态资源文件都放在项目哪里
        **我们创建蓝图对象或者flask应用对象传递的__name__参数就是为了指定那个目录作为蓝图或者flask应用的跟目录
    
    测试蓝图的地址
    http://127.0.0.1:5000/api/v1.0/user/
    http://127.0.0.1:5000/api/v1.0/order/
    
    执行迁移文件生成模型类
    python manage.py db init 
    python manage.py db migrate
    python manage.py db upgrade
    
    遇到的问题
    可以去看看模型类的加载
    # 因为我们的order模块和user模块都导入了db导致一些问题，加上这个就没问题
    # sqlalchemy.exc.InvalidRequestError: Table 'ih_user_profile' is already defined for this MetaData instance. 
    # Specify 'extend_existing=True' to redefine options and columns on an existing Table object.
    
# 增加支付宝，接口的调用

    测试路径
    http://127.0.0.1:5000/支付宝.html
    
# 增加，图片上传的七牛云服务或者使用fastDFS存储服务器
    使用七牛
        只需要配置下文件，即可
        
    使用fastDFS需要安装一系列的程序
        测试路径
        http://127.0.0.1:5000/%E4%B8%8A%E4%BC%A0%E5%9B%BE%E7%89%87%E5%B9%B6%E6%98%BE%E7%A4%BA.html
        
# 图片验证码插件
    访问路径
    http://127.0.0.1:5000/api/v1.0/user/image_codes/
    
# 发送短信验证码
    访问路径
    http://127.0.0.1:5000/%E5%8F%91%E9%80%81%E7%9F%AD%E4%BF%A1%E9%AA%8C%E8%AF%81%E7%A0%81.html