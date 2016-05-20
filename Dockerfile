FROM slave4.wizeye.com.cn:5000/ubuntu-python
COPY memory.py /home/memory.py
CMD python /home/memory.py