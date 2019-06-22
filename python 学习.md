### 今日份Python学习心得 ###
#### os模块 ####

```
a = 'E:\\new file\\abc.txt'

os.path.basename(a)

basename的意思就是最后一个反斜杠后面的内容。

```

```
os.path.dirname(a)

dirname的意思就是最后一个反斜杠前面的内容。
```

```
b = 'E:\\new file\\new'

os.path.basename(b)

os.path.dirname(b)

注意basename可以为文件夹，也可以是文件名。
```

```
os.path.split(a)

用split就可以把最后反斜杠的前后给分开来。
```

```
(os.path.basename(a), os.path.dirname(a))

(os.path.dirname(a), os.path.basename(a))

我们可以用数组来把他们括起来。
```

```
[os.path.dirname(a), os.path.basename(a)]

当然列表也是可以容纳这些数据的。

```

```
a = 'E:\\new file\\abc.txt'

a.split()

单纯地用分割，只会按照空格来分割。
```

```
a = 'E:\\new file\\abc.txt'

a.split(os.path.sep)

但是用sep就可以准确地对这些路径进行分割。
```

os.walk模块重点学习
root, dirs, files in os.walk(file_dir):	
print(root) #当前目录路径名
print(dirs) #当前路径下所有目录文件名
print(files) #当前路径下所有非目录子文件

>一个迭代器，他会实现将指定文件夹下所有的文件都遍历，然后给出所有的文件名

### 将路径保存到文件 ###
```
# -*- coding: utf-8 -*-   
  
import os  
  
def file_name(file_dir):
	filelistlog = file_dir + "\\filelistlog.txt" 
	postfix = set(['gif', 'jpg', 'jpeg', 'png', 'bmp', 'swf'])   
	for root, dirs, files in os.walk(file_dir):	
		print(root) #当前目录路径名
		
		print(dirs) #当前路径下所有目录文件名
		print(files) #当前路径下所有非目录子文件

		for in_file, con_file in enumerate(files):
			relative_dir = root.split(os.path.sep)[-1] + '/' + con_file
			print(relative_dir)
			if con_file.split('.')[-1] in postfix:
				with open(filelistlog, 'a+') as fo: 
					fo.writelines(relative_dir) 
					fo.write('\n')

if __name__ == '__main__':
	dirpath = os.getcwd() # 指定根目录
	file_name(dirpath)
```

### django中文件打开,并添加大数据库 ###


```
category = Category.objects.last()
tag = Tag.objects.first()
med = Media.objects.all()
with open('filelistlog.txt', 'r') as f:
	for all_url in f.readlines():
		url = all_url.strip('\n')
		media = Media()
		media.title = '1'
		media.type_in_media = med[3].type_in_media
		media.media_file = con
		media.created = med[3].created
		media.update = med[3].update
		media.category = med[3].category
		media.save()
		media.tag.add(tag)
```

