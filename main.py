from src.logger import set_up_logger
from src.load import load_restaurant_data

logger = set_up_logger()

def main() -> None:

    logger.info(
        "Starting restaurant analytics pipeline."
    )

    load_restaurant_data()

    logger.info(
        "Pipeline completed successfully."
    )


if __name__ == "__main__":
    main()