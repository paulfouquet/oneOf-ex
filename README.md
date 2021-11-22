# oneOf-ex

This is an example to show that `jsonschema-rs` (`Python`) does not return nested errors when a field in `oneOf` is not matching the correct type.
However, `AJV` (`Javascript`) returns the nested errors.

## Requirements
`poetry`
`yarn`

## Run
`jsonschema-rs` (`Python`)

```bash
poetry install
poetry shell
python main.py
```

`AJV` (`Javascript`)

```bash
yarn
yarn index
```

## Output
```bash
/oneOf-ex$ yarn index
Error for single schema:  /properties/id   must be string
Error for dual schema:  /properties/id   must be string
Error for dual schema:  /category   must be equal to constant
Error for dual schema:     must match exactly one schema in oneOf
/oneOf-ex$ python main.py 
Error for single schema:  1234 is not of type "string"
Error for dual schema:  {"category":"CatA","properties":{"id":1234}} is not valid under any of the given schemas
```
