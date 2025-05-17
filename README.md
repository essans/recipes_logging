# recipes_logging
Collection of logging recipes


#logging.basicConfig(level=logging.DEBUG)


#### To watch the log file:

```bash
tail -f llama_agent.log | grep -- '- root -'
```

#### To filter the log file:
```bash
awk -F' - ' '$3 == "root"' llama_agent.log

grep ' - root - ' llama_agent.log
```
