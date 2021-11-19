# oneOf-ex

This is an example to show that `jsonschema-rs` (`Python`) does not return nested errors when a field in `oneOf` is not matching the correct type.
However, `AJV` (`Javascript`) returns the nested errors.

##Requirements
`poetry`
`yarn`

##Run
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
