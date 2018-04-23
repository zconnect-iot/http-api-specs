import click

BLOCKS = (
    'paths',
    'schemas',
    'parameters',
    'responses',
    'other',
)

def block_start_name(block_name):
    return '### ZC2 builtin {}'.format(block_name)

def block_end_name(block_name):
    return '### end ZC2 builtin {}'.format(block_name)

def get_block_location(file, block_name):
    """ Returns a (start, end) tuple """
    return (
        file.index(block_start_name(block_name)),
        file.index(block_end_name(block_name))
    )

def update_block(file, base_specs, block_name):
    """ Uses array slices to splice in the block from ZC2 base specs """
    try:
        base_specs_block = get_block_location(base_specs, block_name)
    except ValueError:
        print("{} not found in base specs".format(block_name))
        return file

    try:
        specs_block = get_block_location(file, block_name)
    except ValueError:
        print("{} not found in specs".format(block_name))
        return file

    print("Replacing {} block".format(block_name))
    return file[:specs_block[0]] + \
                base_specs[base_specs_block[0]:base_specs_block[1]] + \
                file[specs_block[1]:]

@click.command()
@click.option('--spec', help="The file path of the specs to update")
@click.option('--base', default="./openapi.yaml", help="The base ZC2 specs to use")
def update_specs(spec, base):
    """ Updates the parts of the spec which are from ZC2.

    This will perform an in-place update of the API specs!
    """
    with open(base) as base_specs_fp:
        with open(spec) as file_fp:
            base_specs = base_specs_fp.read()
            file = file_fp.read()
            for block_name in BLOCKS:
                file = update_block(file, base_specs, block_name)

    with open(spec, 'w') as file_fp:
        file_fp.write(file)

if __name__ == "__main__":
    update_specs()