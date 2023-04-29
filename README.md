# AutoDoc-GPT

调用gpt-api自动生成框架源码的代码文档。

好处:

1. 节省时间,避免繁琐的手工文档和教程编写过程。AI可以自动分析代码,生成文档和教程。

2. 规范和统一的格式。AI可以根据预设的模板和格式自动生成文档,保证风格的一致性。

3. 实时更新。每次代码修改后,AI都可以自动重新生成最新版本的文档和教程。

4. 覆盖更加全面。AI可以通过代码分析,自动生成项目各个方方面面、各类对象的文档,覆盖率更高。

   

使用场景:

1. 开源项目的readme文档和wiki教程生成。可以节省社区贡献者大量时间。
2. 企业内部项目的规范文档和新人培训教程产出。提高文档和培训教材的一致性和及时更新
3. 以文档或教程为主要产出的作者。可以大大减轻文档和课程制作的工作量,专注于内容优化。
4. 前端UI组件/工具库的文档网站生成。这类项目文档量比较大,适合使用AI自动生成。
5. 接口/SDK的使用文档自动化生成。通过代码可以清晰解析出各个接口的使用方式,适合AI自动生成文档。
6. 以上都是代码自动文档生成的比较适用的场景。虽然目前AI的代码分析和理解能力还不及人工,但在一定范围内,利用好AI的自动化能力,还是可以在大幅度节省人工劳动时间的同时,保证较高的文档和教程质量。

## Getting Started

### Installing

Clone this repository to your local machine:

```bash
git clone https://github.com/awekrx/AutoDoc-ChatGPT.git
```

Then install the required packages:

```bash
pip install -r requirements.txt
```

## Supported programming languages

- [X] <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="20" /> Python
- [X] <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" height="20" /> JavaScript
- [X] <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" height="20" /> TypeScript
- [ ] <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg" height="20" /> Go
- [ ] <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/csharp/csharp-original.svg" height="20" /> C#
- [ ] <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg" height="20" /> C++
- [ ] <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/php/php-original.svg" height="20" /> PHP
- [ ] <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/ruby/ruby-original.svg" height="20" /> Ruby
- [ ] <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-plain.svg" height="20" /> Rust
- [ ] <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg" height="20" /> Java
- [ ] <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kotlin/kotlin-original.svg" height="20" /> Kotlin

And others...

## 快速使用方式

1. 下载一键部署包：

2. 解压部署包

3. 修改config.ini

   - 将openai的api_key复制过来。

   - 如果想要稳定调用，不需要翻墙，可以使用阿里云的函数计算来实现一个代理。

     - 第一步：点击下方链接，进入“管理控制台”，开通函数计算FC

       https://t.aliyun.com/U/nb5Ka1

       ![图片](https://mmbiz.qpic.cn/mmbiz_png/R3InYSAIZkEiacOvvlMTVYVduic8Vme9t5hbiczp65Mib6dnQCuL3aWicVDpJ1LiaNiaDckGrkq5ZdJuZcuDicvrhURQMw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

       第二步：访问应用中心的openai-proxy

       http://www.devsapp.cn/details.html?name=openai-proxy

       第三步：点击“一键部署”按钮

       ![图片](https://mmbiz.qpic.cn/mmbiz_png/R3InYSAIZkEiacOvvlMTVYVduic8Vme9t599LxZLEGI8cNPibImtZlbibica212XEiagJXJ9byVFTdNobvL5ID0mUrCQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)img

       第四步：点击“创建并部署默认环境”

       ![图片](https://mmbiz.qpic.cn/mmbiz_png/R3InYSAIZkEiacOvvlMTVYVduic8Vme9t5nEeo6ribriaECTQLrgpsYgp7I7BGbibIicFBZ0sR5uuMtehlyZJ13ORUgg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

       接下来就是等着阿里云的精彩表演：

       ![图片](https://mmbiz.qpic.cn/mmbiz_png/R3InYSAIZkEiacOvvlMTVYVduic8Vme9t5blQJ07WItAb3tfbZ3SMlanL80rW4UAVKn7qxM5a0XIpSj2u3I5Yib4A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

       完成部署之后，可以看到如下图的操作列中，有“访问域名”链接，点击后就可以获取到用来代理的域名了。

       ![图片](https://mmbiz.qpic.cn/mmbiz_png/R3InYSAIZkEiacOvvlMTVYVduic8Vme9t5oxSKlDnhleMibV3pkh2gJja7bUcufhZNAK9ViaBtkiaibDoPOibAVP5gC6Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

       最后将域名地址复制到config.ini的proxy处

4. 调用目录下的start.bat文件

5. 输入需要解析的代码文件地址或者目录地址

6. 打开outputs文件获取生成的md文档



### 自行安装

1. 安装python环境

2. 安装库

   ```
   pip install -r requirements.txt
   ```

3. 修改config.ini。过程同上
4. 双击运行start.bat。过程同上



老陈资料分享和AI交流扣群：1103483108

