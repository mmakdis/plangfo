# plangfo

 plangfo is a module with some tools. It only has the blob languages detection thing right now tho :P

## Insallation
`pip3 install plangfo`

## Usage
Add `alias plangfo='python3 -m plangfo'` to your `.bashrc`

And just use it. Go to a directory, type `plangfo`

Here is a test repo:
![output](https://i.imgur.com/1lPnLTw.png)

Here is my output:

![plangfo_output](https://i.imgur.com/qXsL90M.png)

Something else:

![another_output](https://i.imgur.com/IaWab8G.png)

### How it works?

The percentages are calculated based on the bytes of code for each language as reported by the `get_bytes()` method.

### Arguments/specifying directories
To specify a directory, you need to specify an argument, and vice versa.

To do that, use `plangfo [option] [directory]`

| Arguments |                     |
| --------- | ------------------- |
| a         | --all-files         |
| b         | --bytes             |
| sb        | --sorted-bytes      |
| p         | --percentage        |
| sp        | --sorted-percentage |


# TODO:

- [x] `sb` | `--sorted-bytes`
- [ ] `.${file}` | It seems like the script doesn't detect hidden files. Will fix that soon.
- [ ] `--code-all` | How many lines of code in the whole directory.
- [ ] `--code-lang` | How many lines of code each language has.
- [ ] `--ignore` | Ignore some specific languages.
- [ ] Switch to C#.

# Languages

If you're wondering how I got that large data of languages. Then, no, of course I didn't make it myself.

I used `wget` to download [languages.yml](https://github.com/github/linguist/blob/master/lib/linguist/languages.yml)

`wget https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml`

Then, a Python script to generate a dictionary.

```python
import yaml
with open("languages.yml") as f:
    dataMap = yaml.safe_load(f)

file = open("data.py", "a+")
file.seek(0)
file.truncate()
file.write("languages = {\n")

for language in dataMap:
    try:
        file.write("\t\"" + language + "\"" + ": " + str(dataMap[language]["extensions"]) + ",\n")
    except KeyError:
        continue
file.write("\t}")
```

The result is, as expected, `data.py`.
