---
author: someone
title: WeeklyBlog 第二期
featimg: weeklyblog_2.jpg
category: [WeeklyBlog]
---

WeeklyBlog 项目第二期文章合集，本期流程更加规范，审阅时间延长，保证每篇文章都是高质量。

本期内容也较为丰富，有 Android 的基础知识、源码分析，也有解决实际开发中的问题的内容，还有一些独立开发者的内容，同时还有 Python 老司机的技术分享以及设计模式系列的开篇之作。

### 源码分析

- [HashMap 源码解析](http://allenwu.itscoder.com/hashmap-analyse)([@allenwu](http://allenwu.itscoder.com/)) 

  深入 HashMap 源码，讲解 JDK 1.7 和 JDK 1.8 HashMap 不同的实现，同时介绍了 hashCode() 方法的具体作用，以及涉及的相关数据结构的分析，一些关键点均给出了详细解释。

- [SparseArray 的使用及实现原理](http://extremej.itscoder.com/sparsearray_source_analyse/) ([@Joe](http://extremej.itscoder.com/))

  源码角度深入分析 SparseArray 的实现原理，并分析了其与 HashMap 相比较的优缺点，每个关键过程都配上具体的图来讲解原理，十分细致。其博客上的源码系列文章都很赞。


### Python

- [Flask Router 机制初探及 Python 装饰器复习](http://manjusaka.itscoder.com/2016/08/09/reading-the-fucking-flask-source-code-Part1/) ([@写代码的香港记者](https://github.com/Zheaoli))

  Python 老司机用 **Flask** 来作为阅读开源源码计划的开始，该系列的开篇之作，很适合用来巩固 **Python** 的中的很多细节。

### 设计模式

- [设计模式实践](http://brucezz.itscoder.com/design-pattern-practice-1) ([@brucezz](https://github.com/brucezz))

  设计模式实践系列的第一篇文章，以一个模拟实际的小场景来讲解设计模式，结合例子理解设计模式，将本来空洞的理论讲解的生动有趣。

### Android

- [View 的事件分发机制（Android 开发艺术探索读书笔记）](http://yongyu.itscoder.com/2016/08/28/view_touchEvent_dispatch/)([@yongyu0102](http://yongyu.itscoder.com/))

  本文先从文字描述上让读者了解到事件分发的概念，先有个感性认识，再结合源码进行事件分发机制的分析，对源码关键的地方均添加了详细的说明，帮助读者理解，让阅读源码变得不再那么可怕。


- [RecyclerView完美实现拖拽、滑动删除以及撤销删除](http://hymane.itscoder.com/2016/05/08/RecyclerView%E5%AE%8C%E7%BE%8E%E5%AE%9E%E7%8E%B0%E6%8B%96%E6%8B%BD%E3%80%81%E6%BB%91%E5%8A%A8%E5%88%A0%E9%99%A4%E4%BB%A5%E5%8F%8A%E6%92%A4%E9%94%80%E5%88%A0%E9%99%A4/) ([@hymane](https://github.com/Hymanme))

  本文司机从自己实际开发中出发，使用 ItemTouchHelper 工具类完美实现拖拽、滑动删除以及撤销删除等操作，整个过程都有详细的代码给出，并加以说明，对于有这方面需求的开发者来说值得一看。

- [从注册Google Play开发者到如何使用Google LVL验证服务](http://melodyxxx.com/2016/08/21/use_google_play_lvl/) ([@Melodyxxx](https://github.com/melodyxxx))

  本文司机 Melodyxxx 是一名大三的独立开发者，其开发的 Pure 天气在国内市场获得大量好评，最近上线 Google Play，从自己这次上架经历中总结了一篇完整详细的教程，从如何注册 Google Play 开发者到在项目中实现 LVL 验证均做了详细说明，很棒的经历！


- [框架源码 — 可能会有趣一点地简析学习 Retrofit](http://imxie.cc/2016/08/20/retrofit-source-learning/)  ([@谢三弟](http://imxie.cc/))

  谢三弟文辞幽默地从源码角度分析了 Retrofit 是如何将接口转换为网络请求，并分析出到底是哪里进行网络请求，源码中关键点都添加了详细的说明，对于使用 Retrofit 但是不知道其原理的开发者，本文是一篇不错的学习文章。

- [Android 中不得不谈的 setContentView](https://itsmelo.github.io/2016/08/19/Android%20%E4%B8%AD%E4%B8%8D%E5%BE%97%E4%B8%8D%E8%B0%88%E7%9A%84%20setContentView/) ([@Melo](https://itsmelo.github.io/))

  对于 Android 开发者而言，setContentView 再熟悉不过了，但是真的熟悉么？Melo 司机从 setContentView() 方法出发，步步深入，一点点挖掘到源码深处，同时以实际项目验证了探究的结果，并给出自己的分析。在这里还推荐下该站点其他的文章，都有着很高的质量。

- [BottomPopUpDialog 底部弹出框的实现](https://shadowzwy.github.io/BottomPopUpDialog%E5%BA%95%E9%83%A8%E5%BC%B9%E5%87%BA%E6%A1%86%E7%9A%84%E5%AE%9E%E7%8E%B0/) ([@shadow](https://github.com/shaDowZwy))

  本文从实际开发中遇到的问题出发，具体从底部弹出框实现的初期分析到实际开发中遇到的一些问题，以及其中的一些小细节，并抽成一个组件，提供必要的 api 来满足使用者的需求，后期可以考虑加上多样化的样式以及更多的自定义属性的支持。

- [热修复入门：Android 中的 ClassLoader](http://jaeger.itscoder.com/android/2016/08/27/android-classloader.html) ([@写代码的猴子](https://github.com/laobie))

  本文从比较常用的热修复基本原理——ClassLoader 方式入手，讲解了 Android 中 ClassLoader 机制，以及其与 JVM 中的 ClassLoader的差别，从源码分析了 Android 中几种 ClassLoader 的实现，并通过一个简单的实践示例验证前面提到的理论知识。

  ​

