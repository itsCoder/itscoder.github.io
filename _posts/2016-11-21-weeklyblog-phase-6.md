---
author: someone
title: WeeklyBlog 第六期
featimg: weeklyblog_6.jpg
category: [WeeklyBlog]
---

北方的第一场雪已经降临，WeeklyBlog 也迎来了第六期，这期共有 10 篇文章，Android 为主。

##### C/C++

- [Linux 下用 Clion 编写及调用共享库的实践](https://zetaoyang.github.io/post/2016/11/05/linux-shared-object.html) ([@zetaoyang](https://github.com/zetaoyang))

  这篇文章带我们了解 Linux 下动态库和静态库的编写过程，为一直用 IDE 的司机们， 提供一个思路。作者还告诉我们 C 调用 C++ 库的方法。 最后作者给我们阐述 cmake 和 make 的区别。

##### Python

- [Python 描述符入门指北 \| Manjusaka](http://manjusaka.itscoder.com/2016/10/12/Something-about-Descriptor/) ([@写代码的香港记者](https://github.com/Zheaoli))

  Python 中的描述符可以说是新式类调用链中的根基，所有的方法，成员，变量调用时都将会有描述符的介入。同时我们可以利用描述符的特性来将我们的调用过程变得更为可控。这一点，我们可以在很多著名框架中找到这样的例子。本文通过 property 的源码实现，以及几个简单易懂的例子，讲解了 Python 中描述符的原理和使用。描述符能够在操作对象属性时进行 hook，实现各种黑魔法。


- [Atom\-Helper 小脚本](http://brucezz.itscoder.com/atom-helper-script) ([@brucezz](https://github.com/brucezz))

  都说程序员既要懒惰，又要保持好奇心。本文小天司机本着自己搜索插件和主题的需求出发，尝试写出一个解放自己的小插件，从分析问题，明确步骤层层递进，逻辑清晰地向我们展示了如何利用 Python 开发出一个脚本，虽然使用上与预期有点差距，不过作者在这个探索的过程中熟悉了许多陌生模块，期待着未来写出更多的自动化工具来为社区做出贡献。

##### 面向对象

- [面向对象六大原则和设计模式](https://itsmelo.github.io/2016/11/20/%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E5%85%AD%E5%A4%A7%E5%8E%9F%E5%88%99%E5%92%8C%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F/) ([@Melo](https://github.com/itsMelo))

  Melo 司机在本篇文章详细的描述了设计模式的入门：六大原则。文章通过文字叙述、介绍概念，然后辅以代码解释、帮助读者理解。面向对象的六大原则在开发过程中极为重要，他们给灵活、可扩展的软件系统提供了更细粒度的指导原则。而根本上如作者所说，六大原则简单概述起来就是：面向接口，单一职责，抽象，最小化。六大原则以及 23 中主流设计模式学习和理解起来不难，难的是如何运用在实际项目中，而达到这一点，想必要有足够的项目经验，足够的代码量。建议大家平时可以多看看优秀的开源项目的代码，一来知道一些功能是怎么实现的，二来学习优秀的架构是如何设计的，相信处处留心皆学问呀。

##### Android 

- [沉浸式适配个人总结 ](http://imxie.cc/2016/11/08/jike_Immersive_project/) ([@谢三弟](https://github.com/xcc3641))

  本文从实际项目出发，阐述了项目中 沉浸式/变色状态栏 的实现和一些需要注意的点。由于是从项目出发，本文的很多地方着重于解决项目中的问题，整体解决方案来看，由于状态栏样式的调整对布局和主题的选取侵入较多，读者需要根据自己的项目实际来学习。作者解决问题的思路和一些技巧都是不错的，同时在问题的考虑上也很周到。这是开发人员在平时的开发过程中需要学习和强化的点。

- [Android 单元测试-Mock及Mockito](http://hujiandong.com/2016/11/07/android-unit-test-mock/)  ([@JasonThink](https://github.com/jasonim))

  引入单元测试，带来的好处是显而易见的，首先可以直接帮我们寻找出 bug，并且在加入新的功能模块时，可以发现它是否影响并破坏了我们原有的功能。单元测试还可以强迫让我们的代码变得精炼短小，因为太过复杂的代码无法引入单元测试。单元测试还可以节省测试成本，不需要启动整个系统，就可以直接的，针对性的对任意模块进行测试。而且可以简单的模拟各种情况覆盖其各种分支。这是降低整体开发时间，提高软件质量的一种有效方法。

- [自定义选择复制功能的实现](http://jaeger.itscoder.com/android/2016/11/21/selectable-text-helper.html) ([@写代码的猴子](https://github.com/laobie))

  作者又为我们带来了一个便利的裤子，大家都知道 Android 开发中最让人头痛有两点，一是处理 Android 版本变化和向前兼容，二是国产百花齐放的流氓 rom。为了解决这些问题，作者完成了自定义选择复制功能，文章中按照发现问题，分析问题，并且提出解决方案的思路，逻辑清晰地搞定了需求，功能实现起来涉及的知识点很多，细节也需要去耐心处理，总之是一篇高质量的博客。

- [RxJava 学习笔记（部分示例代码及源码）](http://yongyu.itscoder.com/2016/11/15/rxjava_learning_note/)([@yongyu](https://github.com/yongyu0102))

  RxJava 在 Android 开发者中逐渐普及开来，即便你没有用过，相信你也听说过。RxJava最核心的两个东西是Observables（被观察者，事件源）和Subscribers（观察者）。本文非常详尽的为我们介绍了 Observable ，以及 RxJava 的原理和一些常规操作符的使用，配合着源码分析，做到了真正的知其所以然。本文篇幅较长，值得反复阅读和品味。期待下一部分的 RxJava 学习笔记。

- [使用贝塞尔曲线实现仿 QQ "一键下班"功能](http://hymane.itscoder.com/2016/11/13/hymane_20161113_qq_bubble_with_bezier/) ([@hymane](https://github.com/hymanme))

  作为 Android 开发者，动画和自定义控件是每个人必须啃下的知识，我们做出来的东西直接提供给用户使用，好与不好，是非常直观的。而动画有时恰恰就可以极大的提升用户感官上的体验。本文作者带我们走进了贝塞尔曲线的原理，以及“秀”了一波数学技巧，代码虽然不多，却不易理解，最终达到的效果非常不错。建议读者仔细阅读几次，相信就可以掌握，如果你正需要这个动画，那么你有福了。

- [Retrofit 2\.0 应用场景概述](https://shadowzwy.github.io/2016/11/17/Retrofit-2.0-%E5%BA%94%E7%94%A8%E5%9C%BA%E6%99%AF%E6%A6%82%E8%BF%B0.html) ([@shaDowZwy](https://github.com/shaDowZwy))

  如果说什么是今年 Android 最优秀的网络库，那 Retrofit 一定无出其右，通过 Retrofit 我们可以学习 okhttp 甚至配合 RxJava 来进一步展现它强大简洁高效的能力。本文通过 Retrofit 的应用场景，进行了灵活又高效的封装，带我们领略了 Retrofit 的便利和魅力。如果你还没用到 Retrofit ，那么动手实际操作试试，相信你会喜欢上它。

  ​