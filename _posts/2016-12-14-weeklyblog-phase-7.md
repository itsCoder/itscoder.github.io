---
author: someone
title: WeeklyBlog 第七期
featimg: weeklyblog_7.jpg
category: [WeeklyBlog]
---

一晃 WeeklyBlog 项目进行快半年了，产出近 80 篇文章，很赞，继续前行。

### React Native

- [React Native 从零到一个小项目](http://janggwa.cn/2016/12/13/React%20Native%20%E4%BB%8E%E9%9B%B6%E5%88%B0%E4%B8%80%E4%B8%AA%E5%B0%8F%E9%A1%B9%E7%9B%AE/)([@JangGwa](https://github.com/JangGwa))

  React Native 是 Facebook 最近隆重推出的一款移动应用开发框架，学习成本很低，该司机以一个小项目着手向我们讲解了 RN 的入门到立项，再到完成。包括了 RN 环境搭建，基础讲解，以及一些常用控件的使用，最后贴上了自己的开源项目地址，想必可以给想或准备学习 RN 的小伙伴带来很大的指导意义。

### 插件

- [学习给 AS 和 IDEA 开发一个翻译插件](http://allenwu.itscoder.com/write-a-plugin-for-idea-and-as) ([@allenwu](https://github.com/wuchangfeng))

  我们一直在享用着各种编辑器插件给我们带来的便捷，而你是否想过自己动手去实现一个呢？或许在你需要的时候，你就可以利用这个技能为自己写个插件。而本文，将带你一步一步为 IDEA 和 AS 开发一款翻译插件，让你了解插件开发的全貌。

### Android

- [Android 项目框架--MVP 基础](https://github.com/itsCoder/weeklyblog/blob/master/phase_7/jasonthink_20161202_android_mvp_basic.md)  ([@Jasonim](https://github.com/Jasonim))

  Android 上 MVP 模式已经出现了一段时间，关于 MVP 的优点显而易见，解耦、内聚、各司其职，当然也有代码量增多项目笨重等弊端。本文通过一个小例子为我们清楚的描述了 MVP 的一些基础思想和写法，具体究竟要不要在自己的项目里使用 MVP，就看各自的具体情况了。


- [死磕 Fragment 的生命周期](https://itsmelo.github.io/2016/12/12/%E6%AD%BB%E7%A3%95%20Fragment%20%E7%9A%84%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F/) ([@melo](https://github.com/itsMelo))

  本篇文章作者通过一个争论引入本文的主题，带我们一步步告诉我们管理 Fragment 两种方式。ViewPager 的如何通过 Fragment 实现懒加载的。最后作者总结： 使用 Fragment 能体现 Android 组件化的思想，其带给开发者的便利远大于麻烦。虽然其生命周期复杂，栈又奇怪难管理，不过当正确的姿势使用 Fragment（不要嵌套 Fragment 使用）。


- [Activity 共享元素转场动画实践](http://extremej.itscoder.com/zoom-up-animation/) ([@Joe](http://extremej.itscoder.com/))

  阿风这期带来了一篇共享元素实践方面的文章，通过手动实现弥补了 API 不兼容低版本的问题。从需求引出，到思路描述，再到详细的代码实践，写得很充实。在文章的最后，还补充了几个踩到的坑，同时提出了解决方案，造福后人啊！


- [RecyclerView 入门其实很简单](http://hymane.itscoder.com/2016/12/03/hymane_20161204_how_to_controll_recyclerview/)([@hymane](https://github.com/hymanme))

  RecyclerView 是一个越用越优雅的控件，首先其规范了 ViewHolder 的写法，并且使用 LayoutManager 管理布局方向实现解耦，并且配合自带的动画和可以自定义的分割线，非常简单得就可以达到我们以前不太容易实现的效果。本文实现了一个多 Type 类型的 RecyclerView 带我们一览它的强大优雅，还提出一些实用的建议避免他人踩坑。RecyclerView 仍有许多可以探索的知识点，怎样高效优雅的使用 RecyclerView，值得琢磨。


- [JitPack 指南](http://imxie.itscoder.com/2016/12/04/how_to_upload_your_project_to_jitpack/)([@谢三弟](https://github.com/xcc3641))

  三弟的这篇教程简单明了的讲解了利用 JitPack 来更便捷的发布自己的代码库，顺序清楚，有图有步骤。


- [使用 SpannableString 格式化微博内容](http://imhanjie.com/2016/12/04/use_spannablestring_format_weibo/) ([@Melodyxxx](https://github.com/melodyxxx))

  本文结构清晰，作者从效果需求出发，逐步分析并给出代码，实现步骤也比较优雅，值得参考和学习。如果读者对所用的 API 不是非常了解，查阅资料之后就可以丰富自己的知识库了，也期待着作者能带来更多出色的教程。


- [Android 混淆工具--Proguard 实践](https://shadowzwy.github.io/2016/12/04/Android%E6%B7%B7%E6%B7%86%E5%B7%A5%E5%85%B7-Proguard%E5%AE%9E%E8%B7%B5.html) ([@shaDowZwy](https://github.com/shaDowZwy))

  由于 Java 是一种跨平台的解释型语言，Java 源代码编译成字节码存储于 Class 文件中。Java 字节码中包括了很多源代码信息，类似于变量名、方法名等等。而通过这些关键信息字节码文件很容易被反编译成 Java 源代码。
  本文作者在文章中向我们介绍了在 Android Studio 中 Proguard 起到了在 Java 平台中的混淆器的作用和在 Android Studio 中 Proguard 默认的配置信息，如何通过 Gradle 开启 Android Studio 中的混淆功能。在文章中后半部分介绍了自己的混淆的配置文件并且都有相关注释说明。这些对于未接触过这方面知识的读者是一个非常好的参考。

  另外在文章中作者也说道由于缩短变量、函数名以及丢失部分无用的信息， 在经过混淆之后的 apk 体积也有明显的缩小，这样对于节省网络流量以及节省下载时间都是非常有意义的。

- [Android 中使用 UIAutomator 执行自动化任务](http://brucezz.itscoder.com/use-uiautomator-in-android) ([@brucezz](https://github.com/brucezz))

  一个优秀的程序员，理应做到代码为我所用，而不是陷入无止境地机械化操作中。本文将向你介绍，作者是如何通过 adb 命令来完成测试过程中的机械化操作，从而释放你的双手。何不利用这段时间优雅品茗或者放空一下自己，释放你的灵魂呢！


- [Material Design 控件学习之 Toolbar](http://showzeng.itscoder.com/android/2016/12/01/material-design-widget-toolbar.html) ([@showzeng](https://github.com/showzeng))

  近来 Toolbar 绝对算是一个“明星”级别的 MD 控件了，与 ActionBar 相比较，Toolbar 的运用更加自由灵活，并且还可以与 DrawerLayout CoordinatorLayout 等控件配合使用，达到比较不错的效果。本文将 Toobar 的使用介绍的非常完善，也解答了一些 Toolbar 在使用过程中可能出现的问题，是一篇出色的控件简介文章。

