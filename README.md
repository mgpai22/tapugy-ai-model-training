# Setup

```
git clone https://github.com/mgpai22/tapugy-ai-model-training.git
```

```
cd tapugy-ai-model-training
```

```
docker-compose up -d --build
```
check logs with
```
docker-compose logs -f
```
- open the outputted link
- notebook site should open
- make a new ipynb file
- paste all the code of `gpu_test.py` into the first block and run to see if gpu access is there
  - If an empty list prints that indicates a lack of gpu access
- paste all the code of `main.py` into the second block and run
