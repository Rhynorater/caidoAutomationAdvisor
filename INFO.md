write a python file which sends an api request to `https://gitingest.com/api/ingest` with teh following post body:
```
{
    "input_text": "caido/doc-developer/tree/main/src/reference",
    "token": "",
    "max_file_size": "1851",
    "pattern_type": "include",
    "pattern": "*.md"
}

``` and another one with this:
```
{
    "input_text": "caido/documentation/tree/main/src/reference",
    "token": "",
    "max_file_size": "1851",
    "pattern_type": "include",
    "pattern": "*.md"
}
```

Then, grab the `digest_url` from teh response and downlaod it, then merge the two.
