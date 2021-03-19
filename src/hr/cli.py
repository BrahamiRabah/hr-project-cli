from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser(description="""
    to export a system's user information into formats that can be used 
    """)
    parser.add_argument("--path", help="the path to the export file")
    parser.add_argument("--format", '-f',
            help="how & where store the bucket",
            default='json',
            choices=['csv', 'json'],
            type=str.lower
            )

    return parser
def main():
    import sys
    from hr import user,export
    from hr import user as u
    
    args = create_parser().parse_args()
    user = u.fetch_user()

    if args.path:
        file = open(args.path, 'w', newline='')   
    else:
        file = sys.stdout

    if args.format == 'json':
        export.to_json_file(user, file)

    else:
        export.to_csv_file(user, file)



