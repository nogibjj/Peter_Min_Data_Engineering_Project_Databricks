"""Handles CLI commands"""
import sys
import argparse
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import (
    general_query,
    create_record,
    update_record,
    delete_record,
    read_record,
)


def handle_arguments(args):
    """add action based on inital calls"""
    parser = argparse.ArgumentParser(description="ETL-Query Script")
    parser.add_argument(
        "action",
        choices=[
            "extract",
            "transform_load",
            "update_record",
            "delete_record",
            "create_record",
            "general_query",
            "read_record",
        ],
    )
    args = parser.parse_args(args[:1])
    print(args.action)
    if args.action == "update_record":
        parser.add_argument("record_id", type=int)
        parser.add_argument("major_code")
        parser.add_argument("major")
        parser.add_argument("major_category")
        parser.add_argument("grad_total", type=int)
        parser.add_argument("grad_sample_size", type=int)
        parser.add_argument("grad_employed", type=int)
        parser.add_argument("grad_full_time_year_round", type=int)
        parser.add_argument("grad_unemployed", type=int)
        parser.add_argument("grad_unemployment_rate", type=float)
        parser.add_argument("grad_median", type=int)
        parser.add_argument("grad_P25", type=int)
        parser.add_argument("grad_P75", type=int)
        parser.add_argument("nongrad_total", type=int)
        parser.add_argument("nongrad_employed", type=int)
        parser.add_argument("nongrad_full_time_year_round", type=int)
        parser.add_argument("nongrad_unemployed", type=int)
        parser.add_argument("nongrad_unemployment_rate", type=float)
        parser.add_argument("nongrad_median", type=int)
        parser.add_argument("nongrad_P25", type=int)
        parser.add_argument("nongrad_P75", type=int)
        parser.add_argument("grad_share", type=float)
        parser.add_argument("grad_premium", type=float)

    if args.action == "create_record":
        parser.add_argument("major_code")
        parser.add_argument("major")
        parser.add_argument("major_category")
        parser.add_argument("grad_total", type=int)
        parser.add_argument("grad_sample_size", type=int)
        parser.add_argument("grad_employed", type=int)
        parser.add_argument("grad_full_time_year_round", type=int)
        parser.add_argument("grad_unemployed", type=int)
        parser.add_argument("grad_unemployment_rate", type=float)
        parser.add_argument("grad_median", type=int)
        parser.add_argument("grad_P25", type=int)
        parser.add_argument("grad_P75", type=int)
        parser.add_argument("nongrad_total", type=int)
        parser.add_argument("nongrad_employed", type=int)
        parser.add_argument("nongrad_full_time_year_round", type=int)
        parser.add_argument("nongrad_unemployed", type=int)
        parser.add_argument("nongrad_unemployment_rate", type=float)
        parser.add_argument("nongrad_median", type=int)
        parser.add_argument("nongrad_P25", type=int)
        parser.add_argument("nongrad_P75", type=int)
        parser.add_argument("grad_share", type=float)
        parser.add_argument("grad_premium", type=float)

    if args.action == "general_query":
        parser.add_argument("query")

    if args.action == "delete_record":
        parser.add_argument("record_id", type=int)

    # parse again with ever
    return parser.parse_args(sys.argv[1:])


def main():
    """handles all the cli commands"""
    args = handle_arguments(sys.argv[1:])

    if args.action == "extract":
        print("Extracting data...")
        extract()
    elif args.action == "transform_load":
        print("Transforming data...")
        load()
    elif args.action == "update_record":
        update_record(
            args.record_id,
            args.major_code,
            args.major,
            args.major_category,
            args.grad_total,
            args.grad_sample_size,
            args.grad_employed,
            args.grad_full_time_year_round,
            args.grad_unemployed,
            args.grad_unemployment_rate,
            args.grad_median,
            args.grad_P25,
            args.grad_P75,
            args.nongrad_total,
            args.nongrad_employed,
            args.nongrad_full_time_year_round,
            args.nongrad_unemployed,
            args.nongrad_unemployment_rate,
            args.nongrad_median,
            args.nongrad_P25,
            args.nongrad_P75,
            args.grad_share,
            args.grad_premium,
        )
    elif args.action == "delete_record":
        delete_record(args.record_id)
    elif args.action == "create_record":
        create_record(
            args.major_code,
            args.major,
            args.major_category,
            args.grad_total,
            args.grad_sample_size,
            args.grad_employed,
            args.grad_full_time_year_round,
            args.grad_unemployed,
            args.grad_unemployment_rate,
            args.grad_median,
            args.grad_P25,
            args.grad_P75,
            args.nongrad_total,
            args.nongrad_employed,
            args.nongrad_full_time_year_round,
            args.nongrad_unemployed,
            args.nongrad_unemployment_rate,
            args.nongrad_median,
            args.nongrad_P25,
            args.nongrad_P75,
            args.grad_share,
            args.grad_premium,
        )
    elif args.action == "general_query":
        general_query(args.query)
    elif args.action == "read_record":
        data = read_record()
        print(data)
    else:
        print(f"Unknown action: {args.action}")


if __name__ == "__main__":
    main()
