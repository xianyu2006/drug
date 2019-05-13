from scrapy import cmdline   #这两行代码的作用就是不用再在命令行里运行scrapy了，可以直接运行这行代码就直接运行整个scrapy项目了

cmdline.execute('scrapy crawl kl'.split())