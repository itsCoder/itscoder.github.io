# coding=utf-8

import os
import re

FUCK_STR = ' '

PATTERN_PHASE_FILE = re.compile('\S+-weeklyblog-phase-(\d+)\.md')
PATTERN_POST = re.compile('-\s*\[(.+)\]\((https?://\S+)\)\s*\(\[@(.+)\]\((.+)\)\)')
PATTERN_CATEGORY = re.compile('#{5}\s*(.*?)\n')

BLOG_DIR = '_posts/'


def get_post(f, phase):
    phase_summary = ''
    with open(f, 'r') as md:
        content = md.readline().replace(FUCK_STR, " ")
        category = ''
        while content:
            if re.match(PATTERN_CATEGORY, content):
                category = re.match(PATTERN_CATEGORY, content).group(1)
            else:
                post = re.match(PATTERN_POST, content)
                if post:
                    # | 这是文章标题 | Android | 作者链接 |
                    phase_summary += '| %s | [%s](%s) | %s | [%s](%s) |\n' % (phase,
                                                                              post.group(1), post.group(2), category,
                                                                              post.group(3), post.group(4))
            content = md.readline().replace(FUCK_STR, " ")
    return phase_summary


if __name__ == '__main__':
    with open('README.md', 'w') as post_md:
        th = '| 期数 | 标题 | 类别 | 作者 |\n| :-----: | :---- | :-----: | :--: |\n'
        post_md.write(th)
        f_list = os.listdir(BLOG_DIR)
        f_list.reverse()
        for f_name in f_list:
            f = os.path.join(BLOG_DIR, f_name)
            if os.path.isfile(f):
                result = re.match(PATTERN_PHASE_FILE, f_name)
                if result:
                    phase_count = result.group(1)
                    post_md.write(get_post(f, phase_count))
