---
author: someone
title: WeeklyBlog 第八期
featimg: weeklyblog_8.jpg
category: [WeeklyBlog]
---

这是跨年的一期，新的一年新的开始，itsCoder 也会有新的计划，WeeklyBlog 项目还是会继续下去。

### Android

- [RxJava 线程切换源码的一些体会和思考](http://imxie.itscoder.com/2016/12/25/how_the_rxjava_thread_work/) ([@谢三弟](https://github.com/xcc3641))

  该司机先给读者出了一道关于线程操作符的考题，让读者自己先去思考，然后简洁明了的介绍了 RxJava 几个基础类/方法的作用，在此基础上，结合源码分析了线程切换的前因后果和线程变换的原理，最后给出了考题的答案，理论结合实战，分析的很棒，学习了，最后建议看此篇文章最好有一定的 RxJava 的使用或者理论基础，因为线程的变换原理主要是根据 RxJava 那几个关键类和方法，搞懂那几个类和方法，再学习此文章会轻松很多。

- [GearMachine Canvas 绘制漂亮的齿轮装置](http://refactor.cn/2016/12/26/GearMachine-Canvas%E7%BB%98%E5%88%B6%E6%BC%82%E4%BA%AE%E7%9A%84%E9%BD%BF%E8%BD%AE%E8%A3%85%E7%BD%AE/) ([@andyxialm](https://github.com/andyxialm))

  一篇实战性比较强的文章，实现了一加官网的一个炫酷的齿轮动画。在了解本篇文章之前需要对 View 的坐标系，Canvas(画布)，Paint(画笔)，Path(路径绘图) 有较好的理解和熟练的使用程度。在有了上述基础之后可以跟着源码实现中间两个齿轮的旋转效果，这样就很容易理解啦。个人感觉本篇动画难点还是各种坐标的计算和理解。文章最后还是比较贴心的说明了在自定义动画时候，涉及到数值的变化可以利用 ValueAnimator 来帮助解决。感觉这样一步一步引入解决的问题的思路好赞。
  最后，非常推荐大家看看本篇文章所对应的源码实现，作者的代码写的非常干净，非常赞。

- [Android View 动画和属性动画学习笔记](http://yongyu.itscoder.com/2016/12/25/animation_learning_note/)([@yongyu](https://github.com/yongyu0102))

  本文详细的介绍了帧动画、补间动画、和属性动画的使用场景，常用方法，以及可能踩到的一些坑。给出了在使用它们时，非常实用的建议。文章后半段分析了属性动画的源码，做到了知其所以然。在 Android 中动画本身就是一个比较难的技术，涉及了比较多的计算运算和数学知识。不过当真正去动手实践，总结经验时，也能去攻克它。

- [仿 google 相机点击聚焦效果](http://hymane.itscoder.com/2016/12/24/hymane_20161224_custom_camera_foucs_view/) ([@hymane](https://github.com/hymanme))

  本文行文规范整洁，思路清晰。模仿 Google 相机的聚焦效果也是非常得漂亮，本文从头到尾详细地介绍了如何分析解决一个动画效果的问题，不管是效果模仿学习或者是动画学习的开始，本文都是非常值得学习的文章。

- [Android 6.0 运行时权限简洁封装](https://itsmelo.github.io/2017/01/04/Android%206.0%E8%BF%90%E8%A1%8C%E6%97%B6%E6%9D%83%E9%99%90%E7%AE%80%E6%B4%81%E5%B0%81%E8%A3%85/) ([@Melo](https://itsmelo.github.io/))

  本文从实际问题出发，面对 6.0 动态权限申请问题，不得不手写很多重复的权限检查以及申请的代码，代码只要接触到“重复”就产生出“封装”。该司机为解决这一实际需求向我们展示了一个如何进行权限申请的封装，希望加以完善弄一个裤子出来。


- [RecyclerViewDivider: RecyclerView 分割线](https://github.com/laobie/RecyclerViewDivider) ([@写代码的猴子](https://github.com/laobie))

  基于官方的 `DividerItemDecoration` 修改，提供了更多的自定义选项，满足大部分需求场景，让 RecyclerView 分割线使用起来更加方便。


### Gradle

- [利用 Gradle 进行应用程序的编译打包](http://allenwu.itscoder.com/learn-gradle-in-android) ([@allenwu](https://github.com/wuchangfeng))

  文章开头简单描述了 Gradle 目录结构和 `build.gradle`，令读者有一个大概的认知，之后针对实际开发经常遇到的问题作出图文并茂的解决方案，作为翻查的笔记是十分不错的，如果读者有兴趣深入研究，也可以根据内容关键词 Google 检索学习，对于初学者是十分不错的。


### 设计模式

- [设计模式--单例模式](https://github.com/itsCoder/weeklyblog/blob/master/phase_8/jasonthink_20161225_design_pattern_singleton.md) ([@jasonim](https://github.com/jasonim))

  单例是应用最广的模式之一，单例必须保证只有一个实例的存在，许多时候整个系统只需要拥有一个全局对象，这样有利于我们协调系统整体的行为。作者在本篇文章中，详细介绍了四种常用单例模式的写法，并且分析了各自的优缺点，对于常用单例，但不熟悉为什么的同学是一个补习知识和提高的好文章。

### 设计

- [[译] 给予设计师灵感的 11 个顶尖网站](https://zetaoyang.github.io/post/2016/12/24/t-top-inspiration-websites-for-designers.html) ([@zetaoyang](https://github.com/zetaoyang))

  虽然不做设计，但是平时多看看，对提高审美还是有帮助的。很多时候喜欢国外的网站就是因为国外网站比较简洁，质量也比较高。

### 数据库

- [MySQL 基础之组提交](https://win-man.github.io/2016/12/07/win_man_20161224_mysql_binary_log_group_commit/)([@Win_Man](https://github.com/Win-Man))

  组提交是 MySQL 的基础概念之一，是可以说是 MySQL 分布式事物的根基。作者详细的介绍了这样一个特性被触发时，MySQL 所进行的工作。可以说是 MySQL 进阶必读之文。

  ​
