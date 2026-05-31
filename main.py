from src.pipeline import Pipeline

if __name__ == "__main__":
    pipeline = Pipeline("./inbox", "./mailbox", "./logs/processing.log", "./logs/stats.json")
    pipeline.run()