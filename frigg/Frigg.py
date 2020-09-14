from core.frigg_builder import FriggBuilder
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--lang', type=str, default='en_US.utf8')
    parser.add_argument('--year', type=int, default=0)
    parser.add_argument('--month', type=int, default=0)
    return parser.parse_args()


def main():
    args = get_args()
    frigg_builder = FriggBuilder().with_lang(args.lang)
    if args.year != 0:
        frigg_builder = frigg_builder.with_year(args.year)
    if args.month != 0:
        frigg_builder = frigg_builder.with_month(args.month)

    frigg = frigg_builder.build()
    frigg.to_console()


if __name__ == '__main__':
    main()
