import os

def tag_file(file_in_path, file_out_path, tag_token):
    '''
    Adds a tag to every line in a text file with a given token.

    Args:
        file_in_path (str): Path to the input text file.
        file_out_path (str): Path to the output text file.
        tag_token (str): Token to add to the beginning of each line.
    '''
    # Validate input arguments
    try:
        assert isinstance(file_in_path, str) and os.path.exists(file_in_path)
    except AssertionError:
        print(f'Invalid path to text file: {file_in_path}')
        return
    try:
        assert isinstance(file_out_path, str) and not os.path.exists(file_out_path)
    except AssertionError:
        print(f'Invalid output file path: {file_out_path} or file already exists.')
        return
    try:
        assert isinstance(tag_token, str)
    except AssertionError:
        print('Invalid tag token.')
        return

    print(f'Tagging lines in: {file_in_path}')
    print(f'Output file path: {file_out_path}')
    print(f'Tag token: {tag_token}')

    # Read the file and tag each line
    with open(file_in_path, 'r') as file_in:
        lines = file_in.readlines()

    tagged_lines = [f'{tag_token} {line.strip()}\n' for line in lines]

    # Write the tagged lines to the output file
    with open(file_out_path, 'w') as file_out:
        file_out.writelines(tagged_lines)

    print(f'Tagged lines written to: {file_out_path}')

def command_line_usage():
    import argparse

    parser = argparse.ArgumentParser(description='Tag each line in a text file with a given token.')
    parser.add_argument('file_in', type=str, help='Path to the input text file.')
    parser.add_argument('file_out', type=str, help='Path to the output text file.')
    parser.add_argument('tag_token', type=str, help='Token to add to the beginning of each line.')

    args = parser.parse_args()

    tag_file(args.file_in, args.file_out, args.tag_token)

if __name__ == '__main__':
    command_line_usage()