<p align="center">
  <img src="assets/hero.svg" width="100%" alt="Roy Luo罗宇伦——从电路到代码，从声音到体验">
</p>

<h1 align="center">你好，我是罗宇伦Roy Luo</h1>

<p align="center">硬件与嵌入式开发者 · 端侧AI音频实践者 · Desk Park乐队吉他手</p>
<p align="center">关注消费电子与音频系统，把电路、算法和软件连接成可以实际使用的产品。</p>

<p align="center">
  <a href="https://roylyl.github.io/"><img src="https://img.shields.io/badge/Portfolio-roylyl.github.io-65E5C1?style=flat-square&amp;labelColor=14212D" alt="个人官网"></a>
  <a href="mailto:L3092105572@gmail.com"><img src="https://img.shields.io/badge/Contact-Email-7CB7FF?style=flat-square&amp;labelColor=14212D" alt="通过邮件联系我"></a>
  <a href="https://github.com/Roylyl?tab=followers"><img src="https://img.shields.io/github/followers/Roylyl?style=flat-square&amp;label=Followers&amp;color=65E5C1&amp;labelColor=14212D" alt="GitHub关注者"></a>
  <a href="https://github.com/Roylyl?tab=repositories"><img src="https://img.shields.io/github/stars/Roylyl?style=flat-square&amp;label=GitHub%20Stars&amp;color=7CB7FF&amp;labelColor=14212D" alt="GitHub项目获星"></a>
</p>

<p align="center">
  <a href="#about">关于我</a> · <a href="#hardware">硬件作品</a> · <a href="#opensource">开源项目</a> · <a href="#toolbox">技术工具</a> · <a href="#experience">实践经历</a> · <a href="#music">音乐</a> · <a href="#connect">联系</a>
</p>

<a id="about"></a>
## 关于我

我就读于湖南农业大学卓越工程师学院智能科学与技术专业，预计2028年毕业。目前在雷鸟创新担任AI音频算法实习生，围绕声音事件、环境场景和语音识别开展端侧模型接入与对照测试。

我喜欢从一个具体的使用问题出发：让不同品牌的耳机一起播放，让声音朝指定方向传播，让电脑接收CarPlay，也让音频模型能在设备上被方便地比较和使用。

| 正在投入的方向 | 我做的事情 |
| --- | --- |
| 硬件与嵌入式 | 从原理图、PCB、焊接到板级调试，搭建蓝牙与音频链路 |
| 端侧AI音频 | 接入声音事件、环境场景与ASR模型，处理前处理、推理与结果记录 |
| 多端产品体验 | 连接Android、iOS、Apple Watch、桌面端与网页中的设备交互 |
| 音乐与声音 | 在乐队演出、音色和编曲实践中理解音频设备的真实使用体验 |

<a id="hardware"></a>
## 硬件作品｜把想法做成设备

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="https://roylyl.github.io/soundshare.html"><img src="assets/soundshare.webp" height="180" alt="音享贴LENGHE SoundShare应用图标"></a>
      <h3>音享贴 · LENGHE SoundShare</h3>
      <p>跨生态多人蓝牙音频共享设备</p>
      <p>个人独立完成首版PCB、嵌入式音频链路和多端控制。连接音源与多个播放终端，支持独立音量、声道分配和同步校准。</p>
      <p><code>A2DP</code> <code>PCB</code> <code>Android/iOS</code> <code>Apple Watch</code></p>
      <p><a href="https://roylyl.github.io/soundshare.html">查看设计与项目演示 →</a></p>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="https://roylyl.github.io/ultrasonic.html"><img src="assets/ultrasonic.webp" height="180" alt="超声波定向扬声器概念图，非实物照片"></a>
      <h3>超声波定向扬声器</h3>
      <p>让声音朝指定方向传播</p>
      <p>作为项目负责人，搭建蓝牙PCM接收、实时缓存、40kHz超声调制、功率放大与换能器阵列组成的定向发声链路。</p>
      <p><code>ESP32</code> <code>PCM</code> <code>PWM</code> <code>KiCad</code></p>
      <p><a href="https://roylyl.github.io/ultrasonic.html">查看工程样机与项目介绍 →</a></p>
    </td>
  </tr>
</table>

<a id="opensource"></a>
## 开源项目｜连接设备，也连接体验

### CarPlay接收应用

把熟悉的CarPlay体验带到不同设备上。

| 项目 | 平台 | 用途 | 关注 |
| --- | --- | --- | --- |
| [WinPlay](https://github.com/Roylyl/WinPlay) | Windows | 无线CarPlay接收，支持本机热点与局域网连接 | [![WinPlay Stars](https://img.shields.io/github/stars/Roylyl/WinPlay?style=flat-square&label=Stars&color=65E5C1)](https://github.com/Roylyl/WinPlay/stargazers) |
| [MacPlay](https://github.com/Roylyl/MacPlay) | macOS | 原生CarPlay接收，支持USB或共用Wi-Fi连接 | [![MacPlay Stars](https://img.shields.io/github/stars/Roylyl/MacPlay?style=flat-square&label=Stars&color=65E5C1)](https://github.com/Roylyl/MacPlay/stargazers) |
| [LinuxPlay](https://github.com/Roylyl/LinuxPlay) | Linux | 在Linux设备上使用CarPlay | [![LinuxPlay Stars](https://img.shields.io/github/stars/Roylyl/LinuxPlay?style=flat-square&label=Stars&color=65E5C1)](https://github.com/Roylyl/LinuxPlay/stargazers) |
| [AndroidPlay](https://github.com/Roylyl/AndroidPlay) | Android | 面向手机与车机，支持系统热点、横屏全屏与多档帧率请求 | [![AndroidPlay Stars](https://img.shields.io/github/stars/Roylyl/AndroidPlay?style=flat-square&label=Stars&color=65E5C1)](https://github.com/Roylyl/AndroidPlay/stargazers) |

### 端侧音频与语音

<table>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/Roylyl/SoundTest">SoundTest ↗</a></h3>
      <p>面向iPhone、iPad与Apple Watch的声音事件和环境场景模型测试工具，统一录音、WAV导入、模型切换、批量推理与结果日志。</p>
      <p><code>声音事件</code> <code>环境场景</code> <code>端侧推理</code></p>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/Roylyl/ASRtest">ASRtest ↗</a></h3>
      <p>完全离线运行的语音识别模型测试平台，面向iPhone、iPad与Apple Watch，提供多模型接入与统一测试记录。</p>
      <p><code>离线ASR</code> <code>流式识别</code> <code>批量测试</code></p>
    </td>
  </tr>
</table>

### 工程工具与交互实验

| 项目 | 我想解决的问题 |
| --- | --- |
| [DeerWebTranslator](https://github.com/Roylyl/DeerWebTranslator) | 用自己的大模型API进行网页原位翻译，在译文、原文和双语阅读之间切换 |
| [READMEWriter](https://github.com/Roylyl/READMEWriter) | 把项目介绍、结构和文档检查整理成可复用的README写作技能 |
| [MacDuo](https://github.com/Roylyl/MacDuo) | 基于开源项目探索MacBook铰链角度、实时透视与空间深度交互 |
| [Astra-Music](https://github.com/Roylyl/Astra-Music) | 以《晚渡》为载体，探索FL Studio编曲与AI电脑操作，公开工程和MIDI |
| [Pet-Kun](https://github.com/Roylyl/Pet-Kun) / [Pet-Wei](https://github.com/Roylyl/Pet-Wei) | 为Codex桌面端制作带工作状态动画的自定义伙伴 |

<p align="right"><a href="https://github.com/Roylyl?tab=repositories">浏览全部仓库 →</a></p>

<a id="toolbox"></a>
## 技术工具｜围绕项目选择工具

<p>
  <a href="#toolbox"><img src="https://img.shields.io/badge/Embedded-ESP32%20%C2%B7%20ESP--IDF-65E5C1?style=flat-square&amp;labelColor=14212D" alt="嵌入式：ESP32与ESP-IDF"></a>
  <a href="#toolbox"><img src="https://img.shields.io/badge/Hardware-KiCad%20%C2%B7%20PCB-65E5C1?style=flat-square&amp;labelColor=14212D" alt="硬件：KiCad与PCB设计"></a>
  <a href="#toolbox"><img src="https://img.shields.io/badge/Audio-BLE%20%C2%B7%20A2DP-65E5C1?style=flat-square&amp;labelColor=14212D" alt="音频与控制：BLE与A2DP"></a>
</p>
<p>
  <a href="#toolbox"><img src="https://img.shields.io/badge/Code-Python-7CB7FF?style=flat-square&amp;labelColor=14212D" alt="Python"></a>
  <a href="#toolbox"><img src="https://img.shields.io/badge/Apple-Swift%20%C2%B7%20SwiftUI-7CB7FF?style=flat-square&amp;labelColor=14212D" alt="Swift与SwiftUI"></a>
  <a href="#toolbox"><img src="https://img.shields.io/badge/Android-Kotlin-7CB7FF?style=flat-square&amp;labelColor=14212D" alt="Kotlin"></a>
  <a href="#toolbox"><img src="https://img.shields.io/badge/Web-JavaScript-7CB7FF?style=flat-square&amp;labelColor=14212D" alt="JavaScript"></a>
</p>

| 领域 | 工具与实践 |
| --- | --- |
| 电路与板级开发 | KiCad、嘉立创EDA、原理图、PCB Layout、焊接与Bring-up |
| 嵌入式与音频链路 | ESP32、ESP-IDF、BLE、A2DP、PCM缓存与PWM调制 |
| 模型工程 | ONNX Runtime、TensorFlow Lite、sherpa-onnx、音频前处理与模型适配 |
| 多端开发 | Python、Swift/SwiftUI、Kotlin、JavaScript、Xcode、Android Studio |
| 工程协作 | Git/GitHub、日志分析、问题复现；结合Codex与Claude Code推进原型开发 |
| 音乐制作 | FL Studio、Logic Pro、电吉他、效果器、声卡与监听系统 |

<a id="experience"></a>
## 实践经历｜从使用场景走进工程细节

| 时间 | 经历 | 工作方向 |
| --- | --- | --- |
| 2026.09—至今 | 雷鸟创新 · AI音频算法实习生 | 端侧音频模型接入、批量推理、耗时统计与模型对照 |
| 2026.08—2026.09 | 湖南康通电子 · 硬件部实习生 | 智能陪伴机器人调研、设备与App交互、原型联动与硬件测试 |
| 2026.01—2026.02 | 深圳科创学院 · 市场调研实习 | 消费电子产品、竞品、应用场景与用户需求研究 |
| 2025.07—2025.08 | 长沙市印梦科技 · 设备调试与测试实习 | 超声波刀参数调试、性能测试与异常复现 |
| 2024.09—2028（预计） | 湖南农业大学 · 智能科学与技术本科 | 卓越工程师学院，嵌入式、硬件与AI应用实践 |

<a id="music"></a>
## 音乐｜另一种理解声音的方式

<p align="center">
  <a href="https://roylyl.github.io/#music"><img src="assets/music-stage.jpg" width="760" alt="Desk Park舞台演出照片"></a>
</p>

我是DP音乐工作室主理人、Desk Park乐队吉他手，也曾担任湖南农业大学校团委学生艺术团器乐队副队长，参与排练、演出组织和舞台调度。

从电吉他与效果器，到声卡、监听和DAW，音乐让我持续接触音频产品的实际使用场景。这些经验也影响着我对设备交互、声音体验和产品细节的判断。

[观看演出与音乐实践](https://roylyl.github.io/#music) · [查看Astra-Music编曲实验](https://github.com/Roylyl/Astra-Music)

<a id="connect"></a>
## 联系我

欢迎交流消费电子、嵌入式、音频系统和端侧AI，也欢迎相关实习机会与开源项目合作。

- 个人作品集：[roylyl.github.io](https://roylyl.github.io/)
- 邮箱：[L3092105572@gmail.com](mailto:L3092105572@gmail.com)
- Instagram：[@roylyl06](https://www.instagram.com/roylyl06/)
- 产品思考：[我怎样做产品与选择方向](https://roylyl.github.io/philosophy.html)

<p align="center"><sub>从一个使用问题出发，把想法做成可以体验的东西。</sub></p>
