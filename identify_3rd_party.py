# quick script to identify libraries with active logging

for name in logging.root.manager.loggerDict:
    print(name)

#tune behavior
logging.getLogger("llama_index").setLevel(logging.ERROR)
