
import streamlit as st
from streamlit import experimental_user

from pretty_notification_box import notification_box

from os.path import exists
from os import mkdir

if not exists("data"):
    mkdir("data")
if not exists("data/package1.json"):
    open("data/package1.json", "w+").write("{'packages': {}}")
if not exists("data/package2.json"):
    open("data/package2.json", "w+").write("{'packages': {}}")
if not exists("data/package3.json"):
    open("data/package3.json", "w+").write("{'packages': {}}")
if not exists("data/extra_package1.json"):
    open("data/extra_package1.json", "w+").write("{'packages': {}}")
if not exists("data/extra_package2.json"):
    open("data/extra_package2.json", "w+").write("{'packages': {}}")
if not exists("data/files"):
    mkdir("data/files")
if not exists("data/files/package1"):
    mkdir("data/files/package1")
if not exists("data/files/package2"):
    mkdir("data/files/package2")
if not exists("data/files/package3"):
    mkdir("data/files/package3")
if not exists("data/files/extra_package1"):
    mkdir("data/files/extra_package1")
if not exists("data/files/extra_package2"):
    mkdir("data/files/extra_package2")

updata1 = """
🍧冰淇淋：\n
1.可以将查询到的列表进行排序 \n
2.包源2新增内置各种音乐 \n
3.无论的上传还是下载都会显示预览 \n
4.上传文件可以写上你的介绍 \n
"""

updata2 = """
🍪曲奇饼干:  \n
1.查询的列表的每项都会加上复制按钮  \n
2.修复错误，无法预览时  \n
3.加入可选参数
4.可设定自定义名称（旧版将文件名设为标识）  \n
"""

updata3 = """
🧁纸杯蛋糕  \n
1.增添扩展包源（扩展包源1，扩展包源2）
2.修复自定义名称下载错误文件名  \n
"""

st.set_page_config(
    page_title="资源共享库 🧁纸杯蛋糕",
    page_icon="🗃️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': updata1+updata2+updata3
    }
)

"""
# 🗃️资源共享库 

> 版本：🧁纸杯蛋糕

- 免费运行上传下载包裹
- 无需登录即可使用
- **老司机传输学习资料必备**

**注意：**
- ~~每次更新都会重置用户上传的文件~~ 每个版本会部署不同的分支页面，并且不会再去更改
"""

st.caption("有时候我们会需要去传输和查看一些个人隐私的文件，都可以来这里输入你的暗号和密码来查看和传输你需要的文件资源",
           help="偷偷告诉你：这是专为老司机定制哦")

st.caption(
    "你可以将这个项目地址分享出去，但是不要造成太大的流量，否则我们很有可能会被举报删除，如果可以，隔几天来看一下，以维持程序的运行，一旦七天没有任何流量，将会进入休眠模式")

"""

[🗃️老版本](https://packages.streamlit.app)
[🍧冰淇淋](https://packagesa.streamlit.app/)
[🍪曲奇饼干](https://packagesc.streamlit.app/)
[🧁纸杯蛋糕](https://packages-cupcake.streamlit.app/)

"""

with st.expander("更新日志", expanded=True):
    st.text(updata1)
    st.text(updata2)
    st.text(updata3)

"""
---

## 使用
"""

Content0 = 1
if "source" in st.experimental_get_query_params():
    Content0 = st.experimental_get_query_params()["source"][0]

PackageLIB = st.selectbox(
    "选择包源", ["包源1", "包源2", "包源3", "额外包源1", "额外包源2"],
    index=int(Content0) - 1 ,
    help="因为上传的文件有时难免会跟别人的文件重名，为了让你能够解决这个问题，配备不同的包源路径"
)

with st.expander("传输上传资源（别上传太多的文件，云最多提供1GB的存储空间）", True):
    Uploader = st.file_uploader("上传资源", help="现在暂时只能上传单个文件，请您见谅😺", accept_multiple_files=False)
    with st.container():
        File_Name2 = st.text_input("名称", "", placeholder="不填会自动设为文件名称")
        Description = st.text_input("介绍", "（上传者没有写任何介绍）", placeholder="老文件不会带有介绍")
        File_PassWord1 = st.text_input("密码", type="password", placeholder="如何没填写任何密码，视作无密码")
        Content4 = "false"
        if "get" in st.experimental_get_query_params():
            Content4 = st.experimental_get_query_params()["get"][0]
        OK = st.button("确认上传", use_container_width=True)

        if OK:
            from json import loads

            if PackageLIB == "包源1":
                Data1 = loads(open("data/package1.json", "r", encoding="utf-8").read())
                Name1 = "package1"
            if PackageLIB == "包源2":
                Data1 = loads(open("data/package2.json", "r", encoding="utf-8").read())
                Name1 = "package2"
            if PackageLIB == "包源3":
                Data1 = loads(open("data/package3.json", "r", encoding="utf-8").read())
                Name1 = "package3"
            if PackageLIB == "额外包源1":
                Data1 = loads(open("data/extra_package1.json", "r", encoding="utf-8").read())
                Name1 = "extra_package1"
            if PackageLIB == "额外包源2":
                Data1 = loads(open("data/extra_package2.json", "r", encoding="utf-8").read())
                Name1 = "extra_package2"

            if Uploader is not None:
                from os.path import exists
                if Uploader.name in Data1["packages"] or exists(f"data/files/{Name1}/{Uploader.name}"):
                    st.warning("文件库中已有此文件")
                else:
                    BytesData = Uploader.read()
                    st.divider()
                    st.caption(f"文件名：{Uploader.name}")
                    st.caption(f"文件大小：{Uploader.size}")
                    st.caption(f"文件类型：{Uploader.type}")

                    with open(f"data/files/{Name1}/{Uploader.name}", "wb+") as _File:
                        _File.write(BytesData)
                        _File.close()

                    _Data1 = Data1["packages"]
                    _Name2 = Uploader.name
                    if File_Name2 != "":
                        _Name2 = File_Name2
                    _Data1[_Name2] = {
                        "password": File_PassWord1,
                        "description": Description,
                        "name": Uploader.name,
                        "path": f"data/files/{Name1}/{Uploader.name}",
                    }

                    _Data2 = Data1
                    _Data2["packages"] = _Data1

                    from json import dumps

                    try:
                        Data1 = open(f"data/{Name1}.json", "w", encoding="utf-8") \
                            .write(dumps(_Data2, sort_keys=True, indent=4, separators=(',', ': ')))
                    except:
                        st.warning("上传失败！")
                    else:
                        st.success("上传成功！")

                        try:
                            Format = Uploader.type.split("/")[0]

                            if Format == "audio":
                                st.audio(BytesData, Uploader.type)
                            elif Format == "video":
                                st.video(BytesData, Uploader.type)
                            elif Format == "image":
                                st.image(BytesData)
                        except AttributeError:
                            st.warning("无法预览！")

with st.expander("查看读取资源", True):
    File_Name1, File_PassWord2 = st.columns(2)
    with File_Name1:
        Content1 = ""
        Content2 = ""
        Content3 = ""
        if "package" in st.experimental_get_query_params():
            Content1 = st.experimental_get_query_params()["package"][0]
        if "password" in st.experimental_get_query_params():
            Content2 = st.experimental_get_query_params()["password"][0]
        if "open" in st.experimental_get_query_params():
            Content3 = st.experimental_get_query_params()["open"][0]
        File_Name1_Input = st.text_input("资源名", Content1, placeholder="侧边栏可以查询到更多文件")
    with File_PassWord2:
        File_PassWord2_Input = st.text_input("资源密码", Content2, type="password",
                                             placeholder="如何文件无任何密码，将直接下载")
    with st.container():
        if st.button("取件", use_container_width=True):
            from json import loads

            if PackageLIB == "包源1":
                Data2 = loads(open("data/package1.json", "r", encoding="utf-8").read())
            if PackageLIB == "包源2":
                Data2 = loads(open("data/package2.json", "r", encoding="utf-8").read())
            if PackageLIB == "包源3":
                Data2 = loads(open("data/package3.json", "r", encoding="utf-8").read())
            if PackageLIB == "额外包源1":
                Data2 = loads(open("data/extra_package1.json", "r", encoding="utf-8").read())
            if PackageLIB == "额外包源2":
                Data2 = loads(open("data/extra_package2.json", "r", encoding="utf-8").read())

            try:
                if Data2["packages"][File_Name1_Input]["password"] == File_PassWord2_Input or \
                        Data2["packages"][File_Name1_Input]["password"] == "":
                    with st.container():
                        try:
                            Data3 = open(Data2["packages"][File_Name1_Input]["path"], "r", encoding="utf-8").read()
                        except UnicodeDecodeError:
                            Data3 = open(Data2["packages"][File_Name1_Input]["path"], "rb").read()
                        st.download_button("下载包裹文件", Data3, file_name=Data2["packages"][File_Name1_Input]["name"],
                                           help="点击下载会跳转到一个新网页，等待时间可能有点长",
                                           use_container_width=True)
                    st.success("成功取到你的包裹！（包裹无密码则直接获取）")

                    st.divider()

                    try:
                        from filetype import guess

                        Format2 = guess(Data2["packages"][File_Name1_Input]["path"]).mime.split("/")[0]
                        Format3 = guess(Data2["packages"][File_Name1_Input]["path"]).mime

                        st.caption(f"文件类型：{Format3}")

                        if Format2 == "audio":
                            st.audio(Data3, Format3)
                        elif Format2 == "video":
                            st.video(Data3, Format3)
                        elif Format2 == "image":
                            st.image(Data3, Format3)
                    except AttributeError:
                        st.warning("无法预览！")
                else:
                    st.warning("密码错误！")
            except KeyError as error:
                st.warning("找不到你的包裹！")

"""
## 其他
"""

with st.expander("源代码查看", ):
    st.caption("当然，我们是不会把`数据包`泄漏出去的")
    st.code(open("Home.py", "r", encoding="utf-8").read())

with st.sidebar:
    from streamlit_extras.colored_header import colored_header

    colored_header(
        label="如何使用❓",
        description="获取包裹：首先确认修改包裹所在的包源，然后找到`查看读取资源`这一栏，输入文件名称和密码，点击获取，即可出现下载按钮",
        color_name="red-70",
    )

    from json import loads

    if PackageLIB == "包源1":
        Name2 = "包源1"
        Data4 = loads(open("data/package1.json", "r", encoding="utf-8").read())
    if PackageLIB == "包源2":
        Name2 = "包源2"
        Data4 = loads(open("data/package2.json", "r", encoding="utf-8").read())
    if PackageLIB == "包源3":
        Name2 = "包源3"
        Data4 = loads(open("data/package3.json", "r", encoding="utf-8").read())
    if PackageLIB == "额外包源1":
        Name2 = "额外包源1"
        Data4 = loads(open("data/extra_package1.json", "r", encoding="utf-8").read())
    if PackageLIB == "额外包源2":
        Name2 = "额外包源2"
        Data4 = loads(open("data/extra_package2.json", "r", encoding="utf-8").read())

    with st.expander(f"查询到的所有包裹 {Name2}", True):
        _Data3 = Data4["packages"]
        for name in _Data3:
            st.divider()
            st.subheader(name)

            with st.container():
                if st.button(name, use_container_width=True):
                    st.experimental_set_query_params(package=name, source=Content0)
            try:
                st.text(Data4["packages"][name]["description"])
            except:
                pass

if 'admin_login' not in st.session_state:
    st.session_state['admin_login'] = 'false'

with st.expander("管理员设置"):
    Admin_Name, Admin_Password = st.columns(2)

    with Admin_Name:
        ADMIN_NAME = st.text_input("管理员名称")

    with Admin_Password:
        ADMIN_PWD = st.text_input("管理员密码", type="password")

    with st.container():
        if st.button("登录", use_container_width=True):
            if not st.session_state["admin_login"] == "true":
                if ADMIN_NAME == st.secrets["admin"]["name"] and ADMIN_PWD == st.secrets["admin"]["password"]:
                    st.session_state["admin_login"] = "true"
                    st.success("管理员账号登录成功！")
            else:
                st.warning("您已经登录了！")
        if st.button("注销", use_container_width=True):
            st.session_state["admin_login"] = "false"
            st.success("管理员账号注销成功！")

with st.expander("管理员选项"):
    if st.session_state["admin_login"] == "true":
        if st.button("获取所有包数据", use_container_width=True):
            st.json(loads(open("data/package1.json", "r", encoding="utf-8").read()), expanded=True)
            st.json(loads(open("data/package2.json", "r", encoding="utf-8").read()), expanded=True)
            st.json(loads(open("data/package3.json", "r", encoding="utf-8").read()), expanded=True)
            st.json(loads(open("data/extra_package1.json", "r", encoding="utf-8").read()), expanded=True)
            st.json(loads(open("data/extra_package1.json", "r", encoding="utf-8").read()), expanded=True)

        if st.button("生成数据树文件目录", use_container_width=True):
            from pathlib import Path

            tree_str = ''


            def generate_tree(pathname, n=0):
                global tree_str
                if pathname.is_file():
                    tree_str += '    |' * n + '-' * 4 + pathname.name + '\n'
                elif pathname.is_dir():
                    tree_str += '    |' * n + '-' * 4 + \
                                str(pathname.relative_to(pathname.parent)) + '\\' + '\n'
                    for cp in pathname.iterdir():
                        generate_tree(cp, n + 1)


            path = 'data'
            generate_tree(Path(path), 0)
            st.text_area("树状形目录", tree_str, height=550)
