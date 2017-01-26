#coding=utf-8

oldFileName = raw_input('请输入要备份的文件名称:')
oldFile = open('./' + oldFileName,'r')

# 如果打开文件
if oldFile :
	
	# 提取文件的后缀
	fileTypeIndex = oldFileName.rfind('.')
	if fileTypeIndex > 0 :
		fileType = oldFileName[fileTypeIndex:]

	# 组织新文件的名字
	newFileName = oldFileName[:fileTypeIndex] + '[复件]' + fileType
	
	# 创建新的文件
	newFile = open(newFileName,'w')
	
	# 复制内容
	for lineContent in oldFile.readlines():
		newFile.write(lineContent)
	
	# 关闭文件
	oldFile.close()
	newFile.close()
	print "备份成功"
else:	
	print "打开文件失败"

