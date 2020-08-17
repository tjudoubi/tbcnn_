from restore_model import fileString_convert_vector

file_path_name = "D:\\tbcnn_\\CVE-2018-4441.js"
vector = fileString_convert_vector(file_path_name)
print(vector)

file_path_name = "D:\\datasetforTBCCD-master\\jsc-CVE\\CVE-2017-6980.js"
vector_ = fileString_convert_vector(file_path_name)
print(vector)