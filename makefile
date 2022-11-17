process:
	python3 ./scripts/process_words.py

reprocess:
	python3 ./scripts/reprocess_words.py

word:
	python3 ./scripts/get_word.py

word_start_with:
	python3 ./scripts/get_word_start_with.py

words:
	python3 ./scripts/get_words.py

rename:
	python3 ./scripts/rename_words.py

lock:
	pigar

stop_words:
	python3 ./scripts/stop_words.py
