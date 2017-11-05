#!/bin/bash

articlefile='wiki-zh-article.txt'
articlefile_zht='wiki-zh-article-zht.txt'
txtfile='wiki-zh-words.txt'
model='wiki-zh-model'

if [ ! -f "$articlefile" ] && [ ! -f "$articlefile_zht" ]
then
	python3 unzipWiki.py
	echo '============================================================================='

	echo 'Wiki zip files unzipped & accumulated.'

	echo '============================================================================='
fi

if [ ! -f "$txtfile"  ]
then
	python3 splitWord.py
	echo '============================================================================='

	echo 'Wiki articles is segmented'

	echo '============================================================================='
fi

if [ ! -f "$model"  ]
then
	python3 trainWord2vec.py
	echo '============================================================================='

	echo 'Model built. You shall input "python3 test.py" to test the model'

	echo '============================================================================='
fi
