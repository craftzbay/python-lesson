# Python

## PIP - python package manager

PIP нь пайтон программчлалын хэлний нэмэлт модуль болон сан удирдах хэрэгсэл юм.
PIP хувилбар шалгах `pip --version`

Нэмэлт сан суулгахдаа `pip install camelcase`

Суулгасан сан ашиглахдаа:
```import camelcase
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))
```

Суулгасан сан устгах `pip uninstall camelcase`

Сангуудын жагсаалт харах `pip list`
