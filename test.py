from restore_model import fileString_convert_vector
from subtree_to_vector import subtree_convert_vector

# file_path_name = "D:\\tbcnn_\\CVE-2018-4441.js"
# vector = fileString_convert_vector(file_path_name)
# print(vector)
#
# file_path_name = "D:\\datasetforTBCCD-master\\jsc-CVE\\CVE-2017-6980.js"
# vector_ = fileString_convert_vector(file_path_name)
# print(vector_)

file_path_name = "D:/cut_subtree/pool/ForStatement/CVE-2018-17463.md_1.js"
vector_ = subtree_convert_vector(file_path_name)
print(vector_)

# file_path_name = "D:/datasetforTBCCD-master/Graduate_experiment-master/1.js"
# vector_ = fileString_convert_vector(file_path_name)
# print(vector_)