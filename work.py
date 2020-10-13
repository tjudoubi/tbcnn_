import os
import tensorflow as tf
import numpy as np
import network3
from sampleJS import get_tree
from sampleJS import getData_finetune_withoutlabel
from parameters import EPOCHS, LEARN_RATE
# 加载模型
sess = tf.Session()
saver = tf.train.import_meta_graph("./model_o/model.ckpt.meta")
saver.restore(sess, tf.train.latest_checkpoint("./model_o"))

# print("ModelV restored.")
# all_vars = tf.trainable_variables()
# list_v = []
# for v in all_vars:
#     list_v.append([v.name,v.eval(session=sess)])
#     print(v.name,v.eval(session=sess))


# 需要用到的参数，需要从池化层得到向量
graph = tf.get_default_graph()
# print(graph.as_graph_def().node)
conv_node1 = graph.get_tensor_by_name("network/conv_layer/conv_node/b_conv:0")

embedding = graph.get_tensor_by_name("Variable:0")
op = embedding.eval(session=sess)
print(conv_node1.eval(session=sess))
# print(embedding.eval(session=sess))
# nodes_node1 = graph.get_tensor_by_name("inputs/tree:0")
# children_node1 = graph.get_tensor_by_name("inputs/children:0")
# pool_out = graph.get_tensor_by_name("network/pooling/Max:0")