from threading import Thread, RLock
import time
import os
import pprint
import logging
import re
import time

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def get_words_count(shared_list, words, text, lock):
    # Scan text file and count words
    local_words = {word: 0 for word in words}

    with open(text, 'r') as f:
        for line in f:
            for word in words:
                local_words[word] += len(re.findall(word, line, re.IGNORECASE))

    # as a copy-paste accidental side-effect, we can see, that threads are executed in the same process :D
    logger.debug('Process %s: %s', os.getpid(), local_words)

    with lock:
        for word in words:
            shared_list[words.index(word)][word] += local_words[word]


if __name__ == '__main__':
    time_start = time.time()
    words = ['models', 'approaches', 'mechanisms']
    files = ['./text1.txt', './text2.txt', './text3.txt']

    lock = RLock()
    shared_list = list([dict({word : 0}) for word in words])

    threads = []

    for file in files:
        thread = Thread(target=get_words_count, args=(shared_list, words, file, lock))
        thread.start()
        threads.append(thread)

    [th.join() for th in threads]

    pprint.pprint(list(item.items() for item in shared_list))

    time_end = time.time()
    print(f"Time total: {time_end - time_start}")