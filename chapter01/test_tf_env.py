# -*- coding: utf-8 -*-
# @Time    : 2021/9/6 9:34
# @Author  : 王天赐
# @Email   : 15565946702@163.com
# @File    : test_tf_env.py
# @Software: PyCharm

import tensorflow as tf

print('GPU:', tf.test.is_gpu_available())
