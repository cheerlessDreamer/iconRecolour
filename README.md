# iconRecolour
A small program that takes SVG files, then exports PNG files in various sizes and colours found in a list. Useful for exporting multiple versions of icons that conform to a particular design or branding system.

### Usage

You can supply an additional 'Colour to Replace' argument using a hex colour format, such as:

-$ python3 iconGenerator.py #BADA55

### Installation

Coming soon.

### Current Todos and Known Problems
- [ ] Should automatically add a `#` if one is not supplied in the 'Colour to Replace' argument 
- [ ] Only works when SVG matches a specific colour. Should be made to be colour-agnostic
- [ ] Currently finds and replaces only the first hex colour found in an SVG file. Script should notify user if more than one colour is found
