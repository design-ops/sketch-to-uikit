# Sketch to StylableUIKit

Generates code from Sketch to work with the [`StylableUIKit` Cocoapod](https://github.com/design-ops/stylable-uikit).

## Usage

### System Requirements

* Sketch App
* Docker

### Basic usage

1. First run `/bin/setup` 
	* (note: this can be run from anywhere on the filesystem)
	* This checks for dependencies and sets up Docker etc - follow any instructions to get dependencies setup.
2. To run all steps run `/bin/generate-design -s /path/to/file.sketch -a /path/to/xcode/project/folder/`
	* This will generate all of the necessary files and add (or update) them in the specified xcode project.

### Advanced usage

The `generate-design` script runs the individual sets aka `assets.sh`, `textstyles.sh`, `layerstyles.sh`, `general.sh`, `enums.sh`. Each of these scripts can be run independently.

#### Specify an alternative output directory

All scripts accept `-o /path/to/output/` and will generate files in that location

## Development

### PyCharm

When using PyCharm right click on the `src` folder and select `Mark Directory as > Sources Root`

### Running the tests

Run `bin/test` after you've set up the project, or alternatively run the tests on your machine with:

```bash
# In the folder that contains the src folder
pip install -r requirements.txt
export PYTHONPATH=$PYTHONPATH:./src
python -m unittest
```
