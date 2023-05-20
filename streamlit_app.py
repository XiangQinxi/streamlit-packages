import markdown
import streamlit as st

st.set_page_config(
    page_title="资源共享库",
    page_icon="🗃️",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': "QQ：`137977353` E-Mail：`XiangQinxi@outlook.com`"
    }
)

"""
# 🗃️资源共享库

- 免费运行上传下载包裹
- 无需登录即可使用
- **老司机传输学习资料必备**
"""

st.caption("有时候我们会需要去传输和查看一些个人隐私的文件，都可以来这里输入你的暗号和密码来查看和传输你需要的文件资源", help="偷偷告诉你：这是专为老司机定制哦")

st.caption("你可以将这个项目地址分享出去，但是不要造成太大的流量，否则我们很有可能会被举报删除，如果可以，隔几天来看一下，以维持程序的运行，一旦七天没有任何流量，将会进入休眠模式")

"""
---
"""

"此项目开始于2023/4/30 🥳"


"""
---
"""

lib = st.selectbox("选择包源", ["包源1", "包源2", "包源3"], help="因为在上传和读取时都会让文件处于被打开状态，而其他的人就会打不开，所以分配了不同的包源")


with st.expander("传输上传资源（别上传太多的文件，云最多提供1GB的存储空间）", True):
    s = st.file_uploader("上传资源", help="现在暂时只能上传单个文件，请您见谅😺", accept_multiple_files=True)
    with st.container():
        pwd1 = st.text_input("密码", type="password")
        if st.button("确认上传", use_container_width=True):
            from io import StringIO
            from json import loads

            if lib == "包源1":
                data = loads(open("data/package1.json", "r", encoding="utf-8").read())
            if lib == "包源2":
                data = loads(open("data/package2.json", "r", encoding="utf-8").read())
            if lib == "包源3":
                data = loads(open("data/package3.json", "r", encoding="utf-8").read())

            for uploaded_file in s:
                bytes_data = uploaded_file.read()
                st.divider()
                st.caption(f"文件名：{uploaded_file.name}")
                st.caption(f"文件大小：{uploaded_file.size}")
                st.caption(f"文件类型：{uploaded_file.type}")

                _data = data["packages"]
                _data[uploaded_file.name] = {
                    "password": pwd1,
                    "content": bytes_data
                }

                _data2 = data
                _data2["packages"] = _data

                from json import dumps

                _data2

                if lib == "包源1":
                    data = open("data/package1.json", "wb", encoding="utf-8").write(dumps(_data2))
                if lib == "包源2":
                    data = open("data/package2.json", "wb", encoding="utf-8").write(dumps(_data2))
                if lib == "包源3":
                    data = open("data/package3.json", "wb", encoding="utf-8").write(dumps(_data2))

with st.expander("查看读取资源", True):
    n, pwd = st.columns(2)
    with n:
        nt = st.text_input("资源名", "demo-pack.txt")
    with pwd:
        pwdt = st.text_input("资源密码", "123456789", type="password")
    with st.container():
        if st.button("取件", use_container_width=True):
            from json import loads
            if lib == "包源1":
                data = loads(open("data/package1.json", "r", encoding="utf-8").read())
            if lib == "包源2":
                data = loads(open("data/package2.json", "r", encoding="utf-8").read())
            if lib == "包源3":
                data = loads(open("data/package3.json", "r", encoding="utf-8").read())

            try:
                if data["packages"][nt]["password"] == pwdt:
                    with st.container():
                        try:
                            data2 = open(data["packages"][nt]["path"], "r", encoding="utf-8").read()
                        except UnicodeDecodeError:
                            data2 = open(data["packages"][nt]["path"], "rb").read()
                        st.download_button("下载包裹文件", data2, file_name=nt, help="点击下载会跳转到一个新网页，等待时间可能有点长", use_container_width=True)
                    st.success("成功取到你的包裹！")
                else:
                    st.error("密码错误")
            except KeyError as error:
                st.error("找不到你的包裹！")


with st.expander("源代码查看", ):
    st.caption("当然，我们是不会把`数据包`泄漏出去的")
    {
        "packages": {
            "demo-pack.txt": {
                "password": "123456789",
                "path": "data/files/demo-pack.txt"
            }
        }
    }
    {
        ".streamlit": {
            "config.toml": {
                "theme": {
                    "primaryColor": "#99ebff",
                    "backgroundColor": "#000000",
                    "secondaryBackgroundColor": "#040404",
                    "textColor": "#ffffff",
                    "font": "monospace"
                },
                "server": {
                    "port": 8651
                },
                "browser": {
                    "gatherUsageStats": False
                },
                "logger": {
                    "level": "info"
                }
            }
        },
        "data": {
            "package1.json": {},
            "package2.json": {},
            "package3.json": {}
        },
        "pages": {
            "_.py": None
        },
        "requirements.exe": ["streamlit", "streamlit-extras"],
        "主页": {}
    }
    st.code(open("Home.py", "r", encoding="utf-8").read())


with st.sidebar:
    from streamlit_extras.colored_header import colored_header

    colored_header(
        label="如何使用❓",
        description="获取包裹：首先确认修改包裹所在的包源，然后找到`查看读取资源`这一栏，输入文件名称和密码，点击获取，即可出现下载按钮",
        color_name="red-70",
    )

