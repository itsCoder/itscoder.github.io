---
author: someone
title: WeeklyBlog 第三期
featimg: weeklyblog_3.jpg
category: [WeeklyBlog]
---

由于一些原因第三期的文章姗姗来迟，这里表示抱歉。这期加入了新成员，也带来了新的文章。

### Python

- [Python 生成器和协程那点事儿](http://manjusaka.itscoder.com/2016/09/11/something-about-yield-in-python/) ([@写代码的香港记者](https://github.com/Zheaoli))

  本来想这周继续写写 Flask 那点破事儿的，但是想了想决定换换口味，来聊聊很不容易理解但是很重要的 Python 中的生成器和协程。
  
### Java

- [Java 注解 (Annotation) ](https://win-man.github.io/2016/09/06/Java%E6%B3%A8%E8%A7%A3(Annotation)%E7%AE%80%E5%8D%95%E4%BB%8B%E7%BB%8D/) ([@Win_Man](https://github.com/Win-Man))

  本文司机通过简单的案例讲解了 Java 中的注解知识点，思路清晰，可以帮助大家对注解有初步了解以及进行简单运用。

- [利用动态代理做点事儿](http://allenwu.itscoder.com/use-of-proxy)([@allenwu](http://allenwu.itscoder.com/))

  作者本篇文章主要分析了动态代理在 Java 中的实现及原理，以及在 Java 和 Android 中的应用，阅读本篇文章前应该对代理有一定的基础了解。作者从 Java 的基本实现入手讲解，通过 Demo 简单明了地讲解了动态代理的实现方式以及作用，然后深入的探究了代理类的调用原理。
  第二节中通过 Retrofit 的分析来阐明在 Android 中的应用这一部分很大的帮助我们理解了之前学习 Retrofit 源码时的一个疑惑。
  这篇文章个人感觉非常赞，没有过多的废话，思路清晰易于理解，但是一定要对代理有一定了解，并且对 Retrofit 有原理性的概念，否则读起来会比较懵逼。

### Android 

- [AsyncTask源码分析](http://imhanjie.com/2016/09/08/asynctask-analysis/) ([@Melodyxxx](https://github.com/melodyxxx))

  本文从源码角度分析了 AsyncTask 的运行原理，让开发者了解到自己平时重写的 `onPreExecute ()`、`doInBackground()` 方法具体是在那些地方具体调用的，整个分析过程顺着源码的执行步骤一步步深入，思路很清晰，读完发现 AsyncTask 确实是个很轻量级的处理异步任务的类。

- [对 SharedPreferences 再多一点了解](http://extremej.itscoder.com/shared_preferences_source/) ([@Joe](http://extremej.itscoder.com/))

  作者层层剖析，思路清晰，讲清楚了 SP 的 commit 和 apply 的区别原理。里面有诸多细节之处值得学习。
  比如：

  - commit 的同步提交是如何实现的？ apply 的异步又是如何实现的？
  - 如果 commit 和 apply 都使用了，会怎么个提交顺序？
  - 为什么会设计 “备份” 这个模型？

  答案都在文章里。

- [优雅地创建和销毁对象](http://janggwa.cn/2016/09/19/%E4%BC%98%E9%9B%85%E5%9C%B0%E5%88%9B%E5%BB%BA%E5%92%8C%E9%94%80%E6%AF%81%E5%AF%B9%E8%B1%A1/) ([@JangGwa](https://github.com/JangGwa))

  本文司机从如何优雅的创建和销毁对象入手。进而展开如何以及何时创建对象才会更加“优雅”。同时也讲述了如何适时的去销毁不需要的对象以及在对象销毁之前需要做的一些垃圾清理工作。总体上文章叙述与代码示例并行，让读者有兴趣阅读下去。如果读者更深层次掌握这一部分知识点，也会确保自己写出程序更加"优雅"和高效。

- [Gson 解析那些事](http://showzeng.itscoder.com/android/2016/09/11/Something-about-Gson-parsing.html) ([@showzeng](https://github.com/showzeng))

  本文从 JSON 的基础知识介绍起，然后引出 Google 公司发布的 Gson 开源项目，然后从开发者使用的角度一步步讲解了 Gson 库的使用过程，以及一些使用中遇到的概念和小细节。

- [码农必知之上传开源库到 jcenter by hymane](http://hymane.itscoder.com/2016/09/11/hymane_20160911__programmer_knows_push_library_to_jcenter/) ([@hymane](https://github.com/hymanme))

  本文司机从自己的经验出发，描述了如何将自己开发的组件或者项目上传到 Jcenter，开源给大家使用，整个流程清晰，关键步骤都配有代码和截图，十分详细。

- [View 的工作原理上 View 绘制流程梳理及 Measure 过程详解](http://yongyu.itscoder.com/2016/09/11/view_measure/) ([@yongyu](https://github.com/yongyu0102))

  本文从源码角度分析了  View 的三大流程 onMeasure()、onLayout() 和 onDraw()，对每个步骤的关键点结合源码进行了讲解， 并对 Measure 过程进行了详解。

- [热修复实现：ClassLoader 方式的实现](http://jaeger.itscoder.com/android/2016/09/20/nuva-source-code-analysis.html) ([@写代码的猴子](https://github.com/laobie))

  在之前的文章 热修复入门：Android 中的 ClassLoader 中，讲解了 Android 中的 ClassLoader 工作原理和通过 ClassLoader 实现热修复的可能性。本文结合 Nuva 项目，来讲讲基于 ClassLoader 方式如何具体实现热修复。

- [Android 初阶自定义 View 字符头像](http://imxie.itscoder.com/2016/09/14/let-s-practise-custom-view/) ([@谢三弟](https://github.com/xcc3641))

  三弟第一个开源的控件，需求不复杂，但是做成组件之后使用起来很方便，在文章中还讲解了 View 的绘制流程，结合本文的控件的实现，是一次很好的自定义控件的实践，也是开源的一小步。

- [RxLifecycle 使用与原理](http://brucezz.itscoder.com/usage-and-principle-of-rxlifecycle) ([@brucezz](https://github.com/brucezz))

  很好的一篇关于 RxLifecycle 的文章，条理很清晰，从如何使用到讲解其实现原理，很符合实际中学习一门技术时，先学会使用，后理解为什么这么用的过程。
